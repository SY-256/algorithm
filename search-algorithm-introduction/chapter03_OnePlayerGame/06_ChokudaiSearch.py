import time
import random
import heapq
from typing import List


class Coord:
    """座標を保持するクラス"""

    def __init__(self, y: int = 0, x: int = 0):
        self.y = y
        self.x = x


class TimeKeeper:
    """時間を管理するクラス"""

    def __init__(self, time_threshold: int):
        """時間制限をミリ秒単位で指定してインスタンスを作る"""
        self.start_time = time.time()
        self.time_threshold = time_threshold / 1000.0  # 秒に変換

    def is_time_over(self) -> bool:
        """インスタンス生成した時間から指定した時間制限を超過したかを判定する"""
        return time.time() - self.start_time >= self.time_threshold


# 定数定義
INF = 1e10
H = 3  # 迷路の高さ
W = 4  # 迷路の幅
END_TURN = 4  # ゲーム終了ターン


class MazeState:
    """迷路ゲームの状態を表すクラス"""

    # 右、左、下、上への移動方向
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def __init__(self, seed: int = None):
        self.points = [[0 for _ in range(W)] for _ in range(H)]
        self.turn = 0
        self.character = Coord()
        self.game_score = 0
        self.evaluated_score = 0
        self.first_action = -1

        if seed is not None:
            self._initialize_with_seed(seed)

    def _initialize_with_seed(self, seed: int):
        """シードを使って迷路を初期化"""
        rng = random.Random(seed)
        self.character.y = rng.randint(0, H - 1)
        self.character.x = rng.randint(0, W - 1)

        for y in range(H):
            for x in range(W):
                if y == self.character.y and x == self.character.x:
                    continue
                self.points[y][x] = rng.randint(0, 9)

    def is_done(self) -> bool:
        """ゲームの終了判定"""
        return self.turn == END_TURN

    def evaluate_score(self):
        """探索用の盤面評価をする"""
        self.evaluated_score = self.game_score

    def advance(self, action: int):
        """指定したactionでゲームを1ターン進める"""
        self.character.x += self.dx[action]
        self.character.y += self.dy[action]

        point = self.points[self.character.y][self.character.x]
        if point > 0:
            self.game_score += point
            self.points[self.character.y][self.character.x] = 0

        self.turn += 1

    def legal_actions(self) -> List[int]:
        """現在の状況でプレーヤーが可能な行動をすべて取得する"""
        actions = []
        for action in range(4):
            ty = self.character.y + self.dy[action]
            tx = self.character.x + self.dx[action]
            if 0 <= ty < H and 0 <= tx < W:
                actions.append(action)
        return actions

    def copy(self):
        """状態のコピーを作成"""
        new_state = MazeState()
        new_state.points = [row[:] for row in self.points]
        new_state.turn = self.turn
        new_state.character = Coord(self.character.y, self.character.x)
        new_state.game_score = self.game_score
        new_state.evaluated_score = self.evaluated_score
        new_state.first_action = self.first_action
        return new_state

    def to_string(self) -> str:
        """現在のゲーム状況を文字列にする"""
        result = f"turn:\t{self.turn}\n"
        result += f"score:\t{self.game_score}\n"

        for h in range(H):
            for w in range(W):
                if self.character.y == h and self.character.x == w:
                    result += "@"
                elif self.points[h][w] > 0:
                    result += str(self.points[h][w])
                else:
                    result += "."
            result += "\n"

        return result

    def __lt__(self, other):
        """ヒープ用の比較関数（評価スコアが高いほうが優先）"""
        # Pythonのheapqは最小ヒープなので、比較を逆にする
        return self.evaluated_score > other.evaluated_score


def chokudai_search_action(
    state: MazeState, beam_width: int, beam_depth: int, beam_number: int
) -> int:
    """chokudaiサーチで行動を決定する"""
    # 各深さごとのビーム（優先度付きキュー）を初期化
    beam = [[] for _ in range(beam_depth + 1)]

    # 初期状態をビーム[0]に追加
    heapq.heappush(beam[0], state)

    # beam_number回ビームサーチを実行
    for cnt in range(beam_number):
        for t in range(beam_depth):
            now_beam = beam[t]
            next_beam = beam[t + 1]

            # 現在の深さからbeam_width個の状態を取り出して展開
            for i in range(beam_width):
                if not now_beam:
                    break

                now_state = heapq.heappop(now_beam)

                if now_state.is_done():
                    break

                legal_actions = now_state.legal_actions()
                for action in legal_actions:
                    next_state = now_state.copy()
                    next_state.advance(action)
                    next_state.evaluate_score()

                    # ルートノードで最初の行動を記録
                    if t == 0:
                        next_state.first_action = action

                    heapq.heappush(next_beam, next_state)

    # 最も深い層から順に最良の状態を探す
    for t in range(beam_depth, -1, -1):
        if beam[t]:
            best_state = max(beam[t], key=lambda x: x.evaluated_score)
            return best_state.first_action

    return -1


def test_ai_score(game_number: int):
    """ゲームをgame_number回プレイして平均スコアを表示する"""
    rng = random.Random(0)
    score_mean = 0

    for i in range(game_number):
        seed = rng.randint(0, 2**31 - 1)
        state = MazeState(seed)

        while not state.is_done():
            action = chokudai_search_action(
                state,
                beam_width=1,  # ビーム幅
                beam_depth=END_TURN,  # ビームの深さ
                beam_number=2,  # ビームを打つ回数
            )
            state.advance(action)

        score_mean += state.game_score

    score_mean = score_mean / game_number
    print(f"score:\t{score_mean}")


def main():
    test_ai_score(100)


if __name__ == "__main__":
    main()
