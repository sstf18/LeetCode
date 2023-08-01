def test_2_wei_bag_problem1():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    dp = [[0] * (bagweight + 1) for _ in range(len(weight))]

    # init
    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]

    #find the len of weight, how many staff
    for i in range(1, len(weight)):    # train staff
        for j in range(bagweight + 1):   # train backpack 
            if j < weight[i]:
                # cannot put in bag
                dp[i][j] = dp[i - 1][j]
            else: 
                # put in bag
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

    print(dp[len(weight) - 1](bagweight))


test_2_wei_bag_problem1()