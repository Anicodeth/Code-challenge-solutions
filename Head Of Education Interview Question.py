"""
A train line going through a city has two routes, the regular route and the express route. Both routes go through the same n + 1 stops labeled from 0 to n. Initially, you start on the regular route at stop 0.
You are given two 1-indexed integer arrays regular and express, both of length n. regular[i] describes the cost it takes to go from stop i - 1 to stop i using the regular route, and express[i] describes the cost it takes to go from stop i - 1 to stop i using the express route.


You are also given an integer expressCost which represents the cost to transfer from the regular route to the express route.
Note that:
There is no cost to transfer from the express route back to the regular route.
You pay expressCost every time you transfer from the regular route to the express route.
There is no extra cost to stay on the express route.
Return a 1-indexed array costs of length n, where costs[i] is the minimum cost to reach stop i from stop 0.
Note that a stop can be counted as reached from either route.


Example 1:
Image: https://assets.leetcode.com/uploads/2022/07/25/ex1drawio.png
Input: regular = [1,6,9,5], express = [5,2,3,10], expressCost = 8
Output: [1,7,14,19]
Explanation: The diagram above shows how to reach stop 4 from stop 0 with minimum cost.
- Take the regular route from stop 0 to stop 1, costing 1.
- Take the express route from stop 1 to stop 2, costing 8 + 2 = 10.
- Take the express route from stop 2 to stop 3, costing 3.
- Take the regular route from stop 3 to stop 4, costing 5.
The total cost is 1 + 10 + 3 + 5 = 19.
Note that a different route could be taken to reach the other stops with minimum cost.
"""

def minCost(regPrice, expressPrice, index, resCost, n):
    
    if index >= n:
        return
    
    #generation of all possiblites which are four
    routeOne = regPrice + regular[index]
    routeTwo = expressPrice + express[index] + 0
    routeEThree = expressPrice + express[index]
    routeEFour = regularPrice + regular[index] + expressCost
    
    
    resCost[index] = min(routeOne, routeTwo, routeThree, routeFour)
    
    minCost(min(routeOne, routeTwo) , min(routeEOne, routeETwo), index + 1, resCost, n) 
    

    return
    


