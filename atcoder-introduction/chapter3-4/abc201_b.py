N = int(input())

input_dict = {}
for i in range(N):
    S, T = input().split()
    input_dict[S] = int(T)
print(sorted(input_dict.items(), key=lambda x:x[1], reverse=True)[1][0])