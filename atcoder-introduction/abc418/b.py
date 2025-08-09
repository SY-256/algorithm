S = input()

ans = 0
for i in range(len(S) - 1):
    if S[i] == "t":
        for j in range(i + 1, len(S)):
            if S[j] == "t":
                t = S[i : j + 1]
                if len(t) >= 3:
                    x = t.count("t")
                    ans = max(ans, ((x - 2) / (len(t) - 2)))

print(f"{ans:.17f}")
