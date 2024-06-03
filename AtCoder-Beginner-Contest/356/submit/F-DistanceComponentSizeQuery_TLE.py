import bisect

Q, K = map(int, input().split())
S = []

results = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        idx = bisect.bisect_left(S, x)
        S.pop(idx) if idx < len(S) and S[idx] == x else bisect.insort_left(S, x)
    elif query[0] == 2:
        x = query[1]
        low,high = bisect.bisect_left(S, x - K), bisect.bisect_right(S, x + K)
        visited = set()
        stack = [x]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                low_idx,high_idx = bisect.bisect_left(S, node - K), bisect.bisect_right(S, node + K)
                for idx in range(low_idx, high_idx):
                    if S[idx] not in visited:
                        stack.append(S[idx])

        results.append(len(visited))

for result in results:
    print(result)

