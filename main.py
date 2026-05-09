def knapsack(weights, values, capacity):
    """0/1 Knapsack — DP yondashuvi."""
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(capacity+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i-1][w-weights[i-1]] + values[i-1])

    # Qaysi narsalar tanlandi?
    chosen, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen.append(i-1)
            w -= weights[i-1]

    return dp[n][capacity], chosen[::-1]

if __name__ == "__main__":
    weights  = [2, 3, 4, 5]
    values   = [3, 4, 5, 6]
    capacity = 8

    max_val, items = knapsack(weights, values, capacity)
    print(f"Maksimal qiymat: {max_val}")
    print(f"Tanlangan narsalar (indeks): {items}")
    print(f"Og'irliklari: {[weights[i] for i in items]}")
    print(f"Qiymatlari  : {[values[i]  for i in items]}")
