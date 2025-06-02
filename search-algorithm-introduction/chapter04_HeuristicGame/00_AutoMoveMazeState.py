import random
import copy
from typing import Callable

# 定数定義
H = 5  # 迷路の高さ
W = 5  # 迷路の幅
END_TURN = 5  # ゲームの終了ターン
CHARACTER_N = 3  # キャラクター数

INF = 1e10


class Coord:
    """座標を保持するクラス"""

    def __init__(self, y: int = 0, x: int = 0):
        self.y = y
        self.x = x


class AutoMoveMazeState:
    """
    自動一人ゲームの例
    キャラクターは1マス先の最もポイントの高い床に自動で移動する。
    合法手の中でスコアが同値のものがある場合、右、左、下、上の順で行動が優先される。
    1ターンに上下左右四方向のいずれかに壁のない場所に1マスずつ進む。
    床にあるポイントを踏むと自身のスコアとなり、床のポイントが消える。
    END_TURNの時点のスコアを高くすることを目的とし、
    ゲームに介入できる要素として、初期状態でのキャラクターをどこに配置するかを選択できる。
    どのようにキャラクターを配置すると最終スコアが高くなるかを考えるゲーム。
    """

    # 方向ベクトル（右、左、下、上）
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def __init__(self, seed: int):
        """h*wの迷路を生成する"""
        self.turn = 0
        self.game_score = 0
        self.evaluated_score = 0

        # 床のポイントを1~9で表現する
        self.points = [[0 for _ in range(W)] for _ in range(H)]

        # CHARACTER_N体のキャラクター
        self.characters = [Coord() for _ in range(CHARACTER_N)]

        # シードを設定してポイントを生成
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
                if point > best_point:
                    best_point = point
                    best_action_index = action

        character.y += self.dy[best_action_index]
        character.x += self.dx[best_action_index]

    def advance(self):
        """ゲームを1ターン進める"""
        # 全キャラクターを移動
        for character_id in range(CHARACTER_N):
            self.move_player(character_id)

        # ポイントを取得してスコアに加算
        for character in self.characters:
            point = self.points[character.y][character.x]
            self.game_score += point
            self.points[character.y][character.x] = 0

        self.turn += 1

    def is_done(self) -> bool:
        """ゲームの終了判定"""
        return self.turn == END_TURN

    def to_string(self) -> str:
        """現在のゲーム状況を文字列にする"""
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

    def get_score(self, is_print: bool = False) -> int:
        """スコア計算をする"""
        # 状態をコピー
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


def random_action(state: AutoMoveMazeState) -> AutoMoveMazeState:
    """ランダムにキャラクターを配置する戦略"""
    now_state = copy.deepcopy(state)

    for character_id in range(CHARACTER_N):
        y = random.randint(0, H - 1)
        x = random.randint(0, W - 1)
        now_state.set_character(character_id, y, x)

    return now_state


def play_game(
    ai_name: str,
    ai_function: Callable[[AutoMoveMazeState], AutoMoveMazeState],
    seed: int,
):
    """ゲームを1回プレイしてゲイム状況を表示する"""
    state = AutoMoveMazeState(seed)
    state = ai_function(state)

    print(state.to_string())
    score = state.get_score(True)
    print(f"Score of {ai_name}: {score}")


def main():
    # ランダムアクション戦略でプレイ
    random.seed(0)  # アクション用のシードを設定
    play_game("randomAction", random_action, 0)


if __name__ == "__main__":
    main()
