import sys

N, K = map(int, sys.stdin.readline().split())
xs = sorted(list(map(int, sys.stdin.readline().split())))

S_1, S_2 = [0], [0]
for x in xs:
    S_1.append(S_1[-1] + x)
    S_2.append(S_2[-1] + x * x)

def cost(k, j):
    d = (S_1[j] - S_1[k]) * 1.0
    return S_2[j] - S_2[k] - d * d / (j - k)

dp = [[float('inf') for _ in range(N+1)] for _ in range(K+1)]
dp[0][0] = 0
for i in range(1, K+1):
    stack = [(1, N, 0, N)]
    while stack:
        l, r, alpha_l, alpha_r = stack.pop()
        if l > r: continue
        mid = (r + l)//2
        alpha = alpha_l

        # compute the dp value in the middle
        for k in range(alpha_l, min(mid, alpha_r + 1)):
            here = dp[i - 1][k] + cost(k, mid)
            if here < dp[i][mid]:
                dp[i][mid], alpha = here, k

        # conquer
        stack.append((l, mid-1, alpha_l, alpha))
        stack.append((mid+1, r, alpha, alpha_r))

print(dp[K][N])
