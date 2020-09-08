'''
Knapsack Problem
Now that you saw the dynamic programming solution for the knapsack problem, it's time to implement it. 
Assume you are given two things:

The items, each having its associated weight (kg) and value ( $ ).
A knapsack that can hold a maximum weight of knapsack_max_weight (kg).
Use dynamic programming to implement the function knapsack_max_value() 
to return the maximum total value of items that can be accommodated into the given knapsack.

Note - The items variable is the type Item, which is a named tuple.

'''

# helper code
import collections
# an item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])

'''
The Naive Approach - Based on Recursion:
The idea is, for each given item, 
if the item-weight is less than the remaining capacity (kg) of the knapsack, 
then calculate the value ( $ ) of the knapsack if we:

Do not put the item in the knapsack - 
Value ( $ ) of the knapsack will be the output of the knapsack_recursive() function, 
with the same remaining capacity, and check for the next item down the list.

Put the item in the knapsack - 
Value ( $ ) of the knapsack will be the sum of the current value of the item 
and output of the knapsack_recursive() function, with updated remaining capacity, 
and check for the next item down the list.
Return the maximum of either of the above two values. 
In knapsack_recursive() function, begin with developing the solution for the base case 
i.e., smallest subproblem.

Note - Below is the implementation of this naive approach with recursion, 
that has an exponential time complexity as  𝑂(2𝑛), where  𝑛  is the number of given items, 
becuase we are evaluating both the two options (put/not put) for each given item.
'''

# Naive approach based on recursion
def knapsack_max_value(knapsack_max_weight, items):
    lastIndex = len(items) - 1
    return knapsack_recursive(knapsack_max_weight, items, lastIndex)

def knapsack_recursive(capacity, items, lastIndex):
    # base case
    if capacity <= 0 or lastIndex < 0:
        return 0

    # put hte item in the knapsack
    valueA = 0
    if items[lastIndex].weight <= capacity:
        valueA = items[lastIndex].value \
        + knapsack_recursive(capacity - items[lastIndex].weight, items, lastIndex - 1)

    # do not put the item in the knapsack
    valueB = knapsack_recursive(capacity, items, lastIndex - 1)

    # pick the maximum of the two results
    result = max(valueA, valueB)

    return result

'''
The Approach - Dynamic Programming
Store and reuse the intermediate results in a lookup table. 
This step is called memoization. 
Start with initializing a lookup table (a list), 
where the index represents the remaining capacity (kg) of the knapsack, 
and the element represents the maximum value ( $ ) that it can hold.

For a given item, if the item-weight is less than the remaining capacity (kg) of the knapsack, 
then we have two options:

Do not pick the item - 
In this case, the value ( $ ) of knapsack with the remaining capacity would not change. 
It can be represented as lookup_table[capacity].

Pick the item - 
In this case, the value ( $ ) and capacity (kg) of the knapsack would be updated. 
The value ( $ ) of the knapsack will be equal to 
value ( $ ) of the current object + value ( $ ) in the lookup table at [capacity - item.weight] position. It can be represented as lookup_table[capacity - item.weight] + item.value.
Update the lookup table, lookup_table[capacity], with the maximum of either of the above two values.

Note - This approach with dynamic programming will have a time complexity 
as  𝑂(2𝑛𝐶)≡𝑂(𝑛𝐶) , where  𝑛  is the number of given items and  
𝐶  is the max capacity (kg) of the knapsack.
'''

# Dynamic Programming solution
# get the maximum total value ($) of items that can be accomodated into the given knapsack.
def knapsack_max_value(knapsack_max_weight, items):

    # initialize a lookup table to store the maximum value ($)
    lookup_table = [0] * (knapsack_max_weight + 1)

    # iterate down the given list
    for item in items:

        # the capacity represents amount of remaining capacity (kg) of knapsack at a given moment.
        for capacity in reversed(range(knapsack_max_weight + 1)): # no out of range error
            if item.weight <= capacity:
                lookup_table[capacity] = \
                max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]

# Test - Let's test your function
tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == knapsack_max_value(**test['input'])
