from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

common_counts = Counter(S[0])

for s in S[1:]:
    current_count = Counter(s)
    for char in list(common_counts):
        if char not in current_count:
            common_counts[char] = 0  # Counterは辞書としてkeyでvalueにアクセスできる！
        else:
            common_counts[char] = min(common_counts[char], current_count[char])
result = ""
for char in sorted(common_counts):
    result += char * common_counts[char]
print(result)
