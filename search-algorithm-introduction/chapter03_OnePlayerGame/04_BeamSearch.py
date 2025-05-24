import random
import heapq
from dataclasses import dataclass
from typing import List, Tuple


# 座標を保持するクラス
@dataclass
class Coord:
    y: int = 0
    x: int = 0


# ゲームの定数
H = 3  # 迷路の高さ
W = 4  # 迷路の幅
END_TRUN = 4  # ゲームの終了ターン
INF = 1e10  # ありえない位大きなスコア


# 迷路ゲームの状態クラス
class MazeSate:
    # 右、左、下、上への移動方向
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def __init__(self, seed=None):
        self.character = Coord()
        self.points = [[0 for _ in range(W)] for _ in range(H)]
        self.turn = 0
        self.game_score = 0
        self.evaluated_score = 0
        self.first_action = -1

        # シードが与えられた場合は迷路を生成
        if seed is not None:
            random.seed(seed)
            self.character.y = random.randint(0, H - 1)
            self.character.x = random.randint(0, W - 1)

            for y in range(H):
                for x in range(W):
                    if y == self.character.y and x == self.character.x:
                        continue
                    self.points[y][x] = random.randint(0, 9)

    # ゲームの終了判定
    def is_done(self) -> bool:
        return self.turn == END_TRUN

    # 探索用の盤面評価
    def evaluate_score(self):
        self.evaluate_score = (
            self.game_score
        )  # 簡単のために、ゲームスコアをそのまま盤面評価とする

    # 指定したactionでゲームを1ターン進める
    def advance(self, action: int):
        self.character.x += self.dx[action]
        self.character.y += self.dy[action]

        point = self.points[self.character.y][self.character.x]
        if point > 0:
            self.game_score += point
            self.points[self.character.y][self.character.x] = 0

        self.turn += 1

    # 現在の状況でプレー可能な行動をすべて取得する
    def legal_actions(self) -> List[int]:
        actions = []
        for action in range(4):
            ty = self.character.y + self.dy[action]
            tx = self.character.x + self.dx[action]
            if 0 <= ty < H and 0 <= tx < W:
                actions.append(action)
        return actions

    # 現在のゲーム状況を文字列にする
    def to_string(self) -> str:
        result = f"turn:\t{self.turn}"
        result += f"score:\t{self.game_score}"

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

    # 優先度キューでの比較のためのメソッド
    # [<]を使うときに呼び出される特殊メソッド
    def __lt__(self, other):
        return (
            self.evaluate_score > other.evaluated_score
        )  # 降順にするため大きいほうが優先


# ビーム幅と深さを指定してビームサーチで行動を決定する
def beam_search_action(state: MazeSate, beam_width: int, beam_depth: int) -> int:
    # 優先度キューを使用してビームを管理（Pythonのheapqは最小値を取り出すので、MazeStateの__lt__で調節）
    now_beam = []
    best_state = None

    # 初期状態をビームに追加
    heapq.heappush(now_beam, state)

    for t in range(beam_depth):
        next_beam = []

        # 現在のビームから上位beam_width個の状態を展開
        for i in range(beam_width):
            if not now_beam:
                break

            now_state = heapq.heappop(now_beam)
            legal_actions = now_state.legal_actions()

            for action in legal_actions:
                # 状態を複製して行動を実行
                next_state = MazeSate()
                next_state.character = Coord(
                    now_state.character.y, now_state.character.x
                )
                next_state.points = [
                    row[:] for row in now_state.points
                ]  # 2次元配列の深いコピー
                next_state.turn = now_state.turn
                next_state.game_score = now_state.game_score
                next_state.evaluated_score = now_state.evaluated_score
                next_state.first_action = now_state.first_action

                next_state.advance(action)
                next_state.evaluate_score()

                if t == 0:
                    next_state.first_action = action

                heapq.heappush(next_beam, next_state)

        # 次のターンのビームを現在のターンのビームに設定
        now_beam = next_beam

        # ビームが空でなければ最良の状態を更新
        if now_beam:
            best_state = now_beam[0]  # heapq[0]は最小の要素(__lt__で最大に変換)

            if best_state.is_done():
                break

    return best_state.first_action


# ゲームをgame_number回プレイして平均スコアを表示
# NOTE: 正しくないと思うので1ゲームだけ実行して盤面と共に確認する
def test_ai_score(game_number: int):
    random.seed(0)
    score_mean = 0

    for i in range(game_number):
        state = MazeSate(random.randint(0, 10000))

        while not state.is_done():
            # ビーム幅2、深さEND_TURNでビームサーチ実行
            action = beam_search_action(state, beam_width=2, beam_depth=END_TRUN)
            state.advance(action)

        score = state.game_score
        score_mean += score

    score_mean /= game_number
    print(f"Score: \t{score_mean}")


if __name__ == "__main__":
    test_ai_score(game_number=100)
