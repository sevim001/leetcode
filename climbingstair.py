#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Returns no. of ways to
# reach sth stair


def countWays(s):
 return fib(s + 1)

# Driver program
s = 5
print (countWays(s))