n = int(input())
a = list(map(int, input().split()))

alice = []
bob = []

for i, v in enumerate(sorted(a, reverse=True)):
    i += 1
    alice.append(v) if i % 2 != 0 else bob.append(v)
print(sum(alice) - sum(bob))