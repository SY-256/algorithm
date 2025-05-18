import random
from typing import List


# 座標を保持するクラス
class Coord:
    def __init__(self, y: int = 0, x: int = 0):
        self.y = y
        self.x = x


# 定数の定義
H = 3  # 迷路の高さ
W = 4  # 迷路の幅
END_TURN = 4  # ゲーム終了ターン
INF = 1e10  # 大きなスコア

# 行動選択用の乱数生成器を初期化
mt_for_action = random.Random(0)


class MazeState:
    # 右、左、下、上への移動方向
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def __init__(self, seed=None):
        self.points = [
            [0 for _ in range(W)] for _ in range(H)
        ]  # 床のポイント（0で初期化）
        self.turn = 0  # 現在のターン
        self.character = Coord()  # キャラクターの位置
        self.game_score = 0  # ゲーム上で実際に獲得したスコア
        self.evaluated_score = 0  # 探索上で評価したスコア

        if seed is not None:
            # 盤面構築用の乱数生成器を初期化
            mt_for_construct = random.Random(seed)

            # キャラクター一の初期化
            self.character.y = mt_for_construct.randint(0, H - 1)
            self.character.x = mt_for_construct.randint(0, W - 1)

            # 床のポイントを初期化
            for y in range(H):
                for x in range(W):
                    if y == self.character.y and x == self.character.x:
                        continue
                    self.points[y][x] = mt_for_construct.randint(0, 9)

    # ゲーム終了判定
    def isDone(self) -> bool:
        return self.turn == END_TURN

    # 探索用の盤面評価をする
    def evaluateSocre(self) -> None:
        # ゲームスコアをそのまま盤面の評価とする
        self.evaluated_score = self.game_score

    # 指定したactionでゲームを1ターン進める
    def advance(self, action: int) -> None:
        self.character.x += self.dx[action]
        self.character.y += self.dy[action]

        point = self.points[self.character.y][self.character.x]
        if point > 0:
            self.game_score += point
            self.points[self.character.y][self.character.x] = 0

        self.turn += 1

    # 現在の状況でプレーヤーが可能な行動をすべて取得する
    def legalActions(self) -> List[int]:
        actions = []
        for action in range(4):
            ty = self.character.y + self.dy[action]
            tx = self.character.x + self.dx[action]
            if 0 <= ty < H and 0 <= tx < W:
                actions.append(action)
        return actions

    # 現在のゲーム状況を文字列にする
    def toString(self) -> str:
        result = []
        result.append(f"turn:\t{self.turn}")
        result.append(f"score:\t{self.game_score}")

        for h in range(H):
            row = ""
            for w in range(W):
                if self.character.y == h and self.character.x == w:
                    row += "@"
                elif self.points[h][w] > 0:
                    row += str(self.points[h][w])
                else:
                    row += "."
            result.append(row)

        return "\n".join(result)


# ランダムに行動を決定する
def randomAction(state: MazeState) -> int:
    legal_action = state.legalActions()
    return legal_action[mt_for_action.randint(0, len(legal_action) - 1)]


# 貪欲法で行動する
def greedyAction(state: MazeState) -> int:
    legal_action = state.legalActions()
    best_score = -INF  # 小さな値でベストスコアを初期化
    best_action = -1  # ありえない行動で初期化

    for action in legal_action:
        now_state = MazeState()
        # 現在の状態をコピー
        now_state.points = [row[:] for row in state.points]
        now_state.turn = state.turn  # 全選択肢検証するが、ターンは進ませない
        now_state.character = Coord(state.character.y, state.character.x)
        now_state.game_score = state.game_score

        now_state.advance(action)
        now_state.evaluateSocre()

        if now_state.evaluated_score > best_score:
            best_score = now_state.evaluated_score
            best_action = action

    return best_action


# シードを指定してゲーム状況を表示しながらAIにプレイ
def playGame(seed: int) -> None:
    state = MazeState(seed)
    print(state.toString())

    while not state.isDone():
        state.advance(greedyAction(state))
        print(state.toString())


# ゲームをgame_number回プレイして平均スコアを表示する
def testAiScore(game_number: int) -> None:
    mt_for_construct = random.Random(0)
    score_mean = 0

    for i in range(game_number):
        # 新しいゲーム状態を作成
        state = MazeState(mt_for_construct.randint(0, 100000))

        while not state.isDone():
            state.advance(greedyAction(state))

        score = state.game_score
        score_mean += score

    score_mean /= game_number
    print(f"Socre:\t{score_mean}")


if __name__ == "__main__":
    # ゲームを繰り返す回数
    testAiScore(100)
