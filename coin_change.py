'''
Coin Change
You are given coins of different denominations and a total amount of money. Write a function to compute the fewest coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

As an example:

Input: coins = [1, 2, 3], amount = 6
Output: 2
Explanation: The output is 2 because we can use 2 coins with value 3. That is, 6 = 3 + 3. We could also use 3 coins with value 2 (that is, 6 = 2 + 2 + 2), but this would use more coins—and the problem specifies we should use the smallest number of coins possible.
There's test code below that you can use to check your solution. And at the bottom of the notebook, you'll find two different possible solutions.
'''
# assume F(amount) is the minimum number of coins needed to make a change from coins
# [c0, c1, c2...cn-1]
# then we know that F(amount) = min(F(amount-c0), F(amount-c1), F(amount-c2)...F(amount-cn-1)) + 1

# base case:
    # when amount == 0: F(amount) = 0
    # when amount < 0: F(amount) = floaot('inf')
# This should return one value: the fewest coins needed to make up the given amount
# that we have already calculated so that we do not have to do the calculation again.
# create a memeo that will storing the fewest coins with given amount
# that we have already calculated so taht we do not have to do the
# calculation again.

def coin_change(coins, amount):

    memo = {}
    
    def return_change(remaining):
        # base_case
        if remaining < 0: return float('inf')
        if remaining == 0: return 0

        # check if we have already calculated
        if remaining not in memo:
            # if not previously calculated, calculate it  by calling return_change with
            # the remaining amount
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)
        return memo[remaining]
    
    res = return_change(amount)

    # return -1 when no change found
    return -1 if res == float('inf') else res

def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)
arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)
arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)

# we initiate F[amount] to be float('inf') and F[0] = 0
# let F[amount] to be the minimum number of coins needed to get change for the amount.
# F[amount + coin] = min(F(amount + coin), F(amount) + 1) if F[amount] is reachable.
# F[amount + coin]
def coin_change1(coins, amount):
    # initiate the list with length amount + 1 and prefill with float('inf')
    res = [float('inf')] * (amount + 1)

    # when amount = 0, 0 number of coins will be needed for the change
    res[0] = 0

    i = 0
    while i < amount:
        if res[i] != float('inf'):
            for coin in coins:
                if i <= amount - coin:
                    res[i + coin] = min(res[i] + 1, res[i + coin])
        i += 1

    if res[amount] == float('inf'):
        return -1
    return res[amount]

def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change1(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)