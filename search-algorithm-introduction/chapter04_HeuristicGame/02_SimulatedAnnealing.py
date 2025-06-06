import random
import math
import copy

# 定数
H = 5  # 迷路の高さ
W = 5  # 迷路の幅
END_TURN = 5  # ゲーム終了ターン
CHARACTER_N = 3  # キャラクターの数
INF = 1e10

# グローバル乱数生成器
random.seed(0)


class Coord:
    """座標を保持するクラス"""

    def __init__(self, y: int = 0, x: int = 0):
        self.y = y
        self.x = x


class AutoMoveMazeState:
    """自動一人ゲームの状態を管理するクラス"""

    # 移動方向（右、左、下、上）の順
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def __init__(self, seed: int):
        self.turn = 0
        self.game_score = 0
        self.evaluated_score = 0
        self.points = [[0 for _ in range(W)] for _ in range(H)]
        self.characters = [Coord() for _ in range(CHARACTER_N)]

        # 迷路の初期化
        random.seed(seed)
        for y in range(H):
            for x in range(W):
                self.points[y][x] = random.randint(1, 9)

    def set_character(self, character_id: int, y: int, x: int):
        """指定位置に指定キャラクターを配置する"""
        self.characters[character_id].y = y
        self.characters[character_id].x = x

    def move_player(self, character_id: int):
        """指定キャラクターを移動させる"""
        character = self.characters[character_id]
        best_point = -INF
        best_action_index = 0

        for action in range(4):
            ty = character.y + self.dy[action]
            tx = character.x + self.dx[action]
            if 0 <= ty < H and 0 <= tx < W:
                point = self.points[ty][tx]
                if best_point < point:
                    best_point = point
                    best_action_index = action

        character.y += self.dy[best_action_index]
        character.x += self.dx[best_action_index]

    def advance(self):
        """ゲームを1ターン進める"""
        # キャラクターを移動
        for character_id in range(CHARACTER_N):
            self.move_player(character_id)

        # ポイント獲得
        for character in self.characters:
            point = self.points[character.y][character.x]
            self.game_score += point
            self.points[character.y][character.x] = 0

        self.turn += 1

    def is_done(self):
        """ゲームの終了判定"""
        return self.turn == END_TURN

    def to_string(self):
        """現在のゲームの状況を文字列にする"""
        result = f"turn:\t{self.turn}\n"
        result += f"score:\t{self.game_score}\n"

        for h in range(H):
            for w in range(W):
                is_written = False

                # キャラクターがいるかチェック
                for character in self.characters:
                    if character.y == h and character.x == w:
                        result += "@"
                        is_written = True
                        break

                if not is_written:
                    if self.points[h][w] > 0:
                        result += str(self.points[h][w])
                    else:
                        result += "."
            result += "\n"

        return result

    def get_score(self, is_print: bool = False):
        """スコア計算をする"""
        tmp_state = copy.deepcopy(self)

        # キャラクターの位置にあるポイントを消す
        for character in tmp_state.characters:
            tmp_state.points[character.y][character.x] = 0

        # 終了するまでキャラクターの移動を繰り返す
        while not tmp_state.is_done():
            tmp_state.advance()
            if is_print:
                print(tmp_state.to_string())

        return tmp_state.game_score

    def init(self):
        """初期化する（キャラクターの位置をランダムに配置）"""
        for character in self.characters:
            character.y = random.randint(0, H - 1)
            character.x = random.randint(0, W - 1)

    def transition(self):
        """状態遷移する（1つのキャラクターをランダムな位置に移動）"""
        character = self.characters[random.randint(0, CHARACTER_N - 1)]
        character.y = random.randint(0, H - 1)
        character.x = random.randint(0, W - 1)


def hill_climb(state, number):
    """山登り法"""
    now_state = copy.deepcopy(state)
    now_state.init()
    best_score = now_state.get_score()

    for i in range(number):
        next_state = copy.deepcopy(now_state)
        next_state.transition()
        next_score = next_state.get_score()

        if next_score > best_score:
            best_score = next_score
            now_state = next_state

    return now_state


def simulated_annealing(state, number, start_temp, end_temp):
    """焼きなまし法"""
    now_state = copy.deepcopy(state)
    now_state.init()
    best_score = now_state.get_score()
    now_score = best_score
    best_state = copy.deepcopy(now_state)

    for i in range(number):
        next_state = copy.deepcopy(now_state)
        next_state.transition()
        next_score = next_state.get_score()

        temp = start_temp + (end_temp - start_temp) * (i / number)
        probability = math.exp((next_score - now_score) / temp)
        is_force_next = probability > random.random()

        if next_score > now_score or is_force_next:
            now_score = next_score
            now_state = next_state

        if next_score > best_score:
            best_score = next_score
            best_state = copy.deepcopy(next_state)

    return best_state


def test_ai_score(ai_name, ai_function, game_number):
    """ゲームをgame_number回プレイして平均スコアを表示する"""
    random.seed(0)
    score_mean = 0

    for i in range(game_number):
        state = AutoMoveMazeState(random.randint(0, 1000000))
        state = ai_function(state)
        score = state.get_score(False)
        score_mean += score

    score_mean /= game_number
    print(f"Socre of {ai_name}:\t{score_mean}")


def main():
    simulate_number = 1000
    game_number = 1000

    # AIアルゴリズムのリスト
    ais = [
        ("hillClimb", lambda state: hill_climb(state, simulate_number)),
        (
            "simulatedAnnealing",
            lambda state: simulated_annealing(state, simulate_number, 500, 10),
        ),
    ]

    for ai_name, ai_function in ais:
        test_ai_score(ai_name, ai_function, game_number)


if __name__ == "__main__":
    main()
