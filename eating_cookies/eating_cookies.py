'''
Input: an integer
Returns: an integer
'''
# With the cache, every n value now is only computed once
def eating_cookies(n, cache={}):
    # Your code here
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2,cache) + eating_cookies(n-3, cache)
        return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50

    print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to each {num_cookies} cookies")


#Notes
    # formula to calculate combinations
    # nCr = n! / r! * (n - r)!
    # need to code a factorial
    # def factorial(n): 
    #     if n == 0: 
    #         return 1
    #     return n * factorial(n-1) 
    # r = how many cookies are eaten at a time, in the range of 1 - 3

    # def factorial(num): 
    #     if num == 0: 
    #         return 1
    #     return num * factorial(num - 1) 



    # def eating_cookies(n):
    #     # Your code here
    #     if n < 0:
    #         return 0
    #     if n < 2:
    #         r = n
    #         return 1
    #     elif n == 2:
    #         return 2
    #     elif n >= 3:
    #         r = 3
    #         return factorial(n) / factorial((n - r))

    # this doesn't quite work because there are duplicates in how to eat cookies. ie you can eat 2 then 1 or you can eat 1 then 2.

    # the cookie monster is going to eat one cookie at a time, there is on one way he can do this

    # the cookie monster is going to eat cookies 2 at a time, if n is odd there will be a remainder of 1 which he can eat at the beginning, end or in between any two cookies. 2+ outcomes, else there is only one way to eat them.
    # 
    # the cookie moster is going to eat 3 cookies at once,
    # if n % 3 = 0 then there is one way he can do it.
    # if n % 3 = 1 then there is 2+ ways he can do it, same as the 2 cookie method
    # if n % 3 = 2 then there is the new issue of how he eats the remain two, together or separate
    # if he eats them together then