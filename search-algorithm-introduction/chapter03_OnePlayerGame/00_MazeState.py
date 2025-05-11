import random


# 座標を保持するクラス
class Coord:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# 定数の定義
H = 3  # 迷路の高さ
W = 3  # 迷路の幅
END_TRUN = 4  # ゲームの終了ターン

# 行動選択用の乱数生成器を初期化
random.seed(0)


# 一人ゲームの例
# 1ターンに上下左右四方向のいずれかに1マス進む
# 床にあるポイントを踏むと自身のスコアになり、床のポイントが消える
# END_TURNの時点のスコアを高くすることが目的
class MazeState:
    # 右、左、下、上への移動方向
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def __init__(self, seed=None):
        self.character = Coord()
        self.game_score = 0  # ゲーム上で実際に得たスコア
        self.turn = 0  # 現在のターン
        self.points = [
            [0 for _ in range(W)] for _ in range(H)
        ]  # 床のポイントを1~9で表現（二次元配列）

        if seed is not None:
            # 盤面構築用の乱数生成器を初期化
            random.seed(seed)
            self.character.y = random.randint(0, H - 1)
            self.character.x = random.randint(0, W - 1)

            for y in range(H):
                for x in range(W):
                    if y == self.character.y and x == self.character.x:
                        continue
                    self.points[y][x] = random.randint(0, 9)

    # ゲームの終了判定
    def isDone(self):
        return self.turn == END_TRUN

    # 指定したactionでゲームを1ターン進める
    def advance(self, action):
        self.character.x += self.dx[action]
        self.character.y += self.dy[action]
        point = self.points[self.character.y][self.character.x]
        if point > 0:
            self.game_score += point
            self.points[self.character.y][self.character.x] = 0
        self.turn += 1

    # 現在の状況でプレイヤーが可能な行動をすべて取得する
    def legalActions(self):
        actions = []
        for action in range(4):  # 移動できるのは四方向だから
            ty = self.character.y + self.dy[action]
            tx = self.character.x + self.dx[action]
            if 0 <= ty < H and 0 <= tx < W:
                actions.append(action)
        return actions

    # 現在のゲーム状況を文字列にする
    def toString(self):
        s = f"turn:\t{self.turn}\n"
        s += f"score:\t{self.game_score}\n"
        for h in range(H):
            for w in range(W):
                if (
                    self.character.y == h and self.character.x == w
                ):  # キャラクターの位置
                    s += "@"
                elif self.points[h][w] > 0:  # 取得できる数値盤面
                    s += str(self.points[h][w])
                else:
                    s += "."  # 取得済みの盤面(0の値が入っている場所)
            s += "\n"
        return s


# Stateという別名を定義
State = MazeState


# ランダムに行動を決定
def randomAction(state):
    legal_actions = state.legalActions()
    return legal_actions[
        random.randint(0, len(legal_actions) - 1)
    ]  # 取れる選択の中からランダムで1つ選択して返す


# シードを指定してゲーム状況を表示しながらAIにプレーさせる
def playGame(seed):
    state = State(seed)
    print(state.toString())
    while not state.isDone():
        state.advance(randomAction(state))
        print(state.toString())


if __name__ == "__main__":
    playGame(42)  # 盤面初期化のシード
