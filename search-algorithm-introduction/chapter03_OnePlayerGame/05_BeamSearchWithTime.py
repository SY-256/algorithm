import random
import time
import heapq
from copy import deepcopy


class Coord:
    """座標を保持するクラス"""

    def __init__(self, y=0, x=0):
        self.y = y
        self.x = x


class TimeKeeper:
    """時間を管理するクラス"""

    def __init__(self, time_threshold):
        """時間制限をミリ秒単位で指定してインスタンスを生成"""
        self.start_time = time.time()
        self.time_threshold = time_threshold / 1000.0  # ミリ秒を秒に変換

    def is_time_over(self):
        """インスタンス生成時から指定した時間制限を超過したか判定"""
        elapsed_time = time.time() - self.start_time
        return elapsed_time >= self.time_threshold


class MazeState:
    """迷路ゲームの状態を管理するクラス"""

    # 定数
    H = 30  # 迷路の高さ
    W = 30  # 迷路の幅
    END_TURN = 100  # ゲーム終了ターン

    # 移動方向（右、左、下、上）
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def __init__(self, seed=None):
        self.points = [[0 for _ in range(self.W)] for _ in range(self.H)]
        self.turn = 0
        self.character = Coord()
        self.game_score = 0
        self.evaluated_score = 0
        self.first_action = -1

        if seed is not None:
            self._initialize_maze(seed)

    def _initialize_maze(self, seed: int):
        """h*wの迷路を作成"""
        random.seed(seed)

        # キャラクターの初期位置をランダムに設定
        self.character.y = random.randint(0, self.H - 1)
        self.character.x = random.randint(0, self.W - 1)

        # ポイント配置
        for y in range(self.H):
            for x in range(self.W):
                if y == self.character.y and x == self.character.x:
                    continue
                self.points[y][x] = random.randint(0, 9)

    def is_done(self):
        """ゲーム終了判定"""
        return self.turn == self.END_TURN

    def evaluate_score(self):
        """探索用の盤面評価"""
        self.evaluated_score = self.game_score

    def advance(self, action):
        """指定したactionでゲームを1ターン進める"""
        self.character.x += self.dx[action]
        self.character.y += self.dy[action]

        point = self.points[self.character.y][self.character.x]
        if point > 0:
            self.game_score += point
            self.points[self.character.y][self.character.y] = 0

        self.turn += 1

    def legal_actions(self):
        """現状の状況でプレーヤーが可能な行動をすべて取得"""
        actions = []
        for action in range(4):
            ty = self.character.y + self.dy[action]
            tx = self.character.x + self.dx[action]
            if 0 <= ty < self.H and 0 <= tx < self.W:
                actions.append(action)
        return actions

    def to_string(self):
        """現在のゲーム状況を文字列にする"""
        result = f"turn:\t{self.turn}\n"
        result += f"score:\t{self.game_score}\n"

        for h in range(self.H):
            for w in range(self.W):
                if self.character.y == h and self.character.x == w:
                    result += "@"
                elif self.points[h][w] > 0:
                    result += str(self.points[h][w])
                else:
                    result += "."
            result += "\n"

        return result

    def copy(self):
        """状態のディープコピー"""
        new_state = MazeState()
        new_state.points = [row[:] for row in self.points]  # 2次元リストの深いコピー
        new_state.turn = self.turn
        new_state.character = Coord(self.character.y, self.character.x)
        new_state.game_score = self.game_score
        new_state.evaluated_score = self.evaluated_score
        new_state.first_action = self.first_action

        return new_state

    def __lt__(self, other):
        """heapqでの比較用（評価用スコアの大小逆転）"""
        return self.evaluated_score > other.evaluated_score


def beam_search_action_with_time_threshold(state, beam_width, time_threshold):
    """ビーム幅と制限時間(ms)を指定してビームサーチで行動を決定"""
    time_keeper = TimeKeeper(time_threshold)

    # 優先度キューを使用して（heapqは最小ヒープなので、__lt__で逆転）
    now_beam = [state]
    best_state = state

    t = 0
    while True:
        next_beam = []

        for i in range(min(beam_width, len(now_beam))):
            if time_keeper.is_time_over():
                return best_state.first_action

            if not now_beam:
                break

            # heapqから最大評価スコアの状態を取得
            now_state = heapq.heappop(now_beam)
            legal_actions = now_state.legal_actions()

            for action in legal_actions:
                next_state = now_state.copy()
                next_state.advance(action)
                next_state.evaluate_score()

                if t == 0:
                    next_state.first_action = action

                heapq.heappush(next_beam, next_state)

        # 次のビームを上位beam_width個に絞込み
        if len(next_beam) > beam_width:
            # 評価スコア上位beam_width個を選択
            next_beam = heapq.nlargest(
                beam_width, next_beam, key=lambda x: x.evaluated_score
            )
            # heapqに再構築
            heapq.heapify(next_beam)

        now_beam = next_beam
        if now_beam:
            best_state = max(
                now_beam, key=lambda x: x.evaluated_score
            )  # 最大スコアを取得

        if best_state.is_done():
            break

        t += 1

    return best_state.first_action


def test_ai_score(game_number):
    """ゲームをgame_number回プレイして平均スコアを表示"""
    random.seed(0)
    score_sum = 0

    for i in range(game_number):
        seed = random.randint(0, 2**31 - 1)
        state = MazeState(seed)

        while not state.is_done():
            action = beam_search_action_with_time_threshold(
                state,
                beam_width=5,
                time_threshold=10,  # 制限時間1ms
            )
            state.advance(action)

        score_sum += state.game_score

    score_mean = score_sum / game_number
    print(f"Score:\t{score_mean}")


def main():
    test_ai_score(100)


if __name__ == "__main__":
    main()
