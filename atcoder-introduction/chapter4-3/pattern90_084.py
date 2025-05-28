N = int(input())
S = str(input())
"""
（考えたこと） 
↓2パターンで全探索する
①両端が違う記号
⇒スタートの記号と切り替わるタイミング以降、カウント
⇒2重ループなるので回避必要
⇒増減で切り替わる問題の考え方使えるかも！
⇒同じ記号が続く数もカウントして、切り替わるタイミングで加算！
"""
ans = 0
for i in range(N - 1):
    flag = False
    for j in range(i + 1, N):
        if S[i] != S[j]:
            ans += 1
            flag = True
        elif flag:
            ans += 1
print(ans)
