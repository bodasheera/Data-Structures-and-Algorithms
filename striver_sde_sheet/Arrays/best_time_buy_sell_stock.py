""" PROBLEM STATEMENT: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the 
future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
    1 <= prices.length <= 10**5
    0 <= prices[i] <= 10**4


Approach 1 : 2 loops . time complexity O(n**2), space complexity O(1) 

Approach 2: 
1. min_price = 10**5 , profit = 0
2. traverse loop
3. find min element of min and prices[i]
4. find max of profit and prices[i] - min_price

Time Complexity O(n)
Space Complexity O(1)

"""


from typing import List

class BruteForce:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0 , len(prices)):
            for j in range(i , len(prices)):
                if(prices[j] - prices[i] > profit):
                    profit = prices[j] - prices[i]
          
        return profit


class BruteForce:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = (10**4) + 1
        profit = 0
        for i in range(len(prices)):
           min_price = min(min_price,prices[i])
           profit = max(profit, prices[i] - min_price)

        return profit

