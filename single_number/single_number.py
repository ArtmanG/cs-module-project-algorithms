'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
        # O(n^2) runtime 
        # is this the best we can do? 
        # how do we get rid of one of the for loops? 
        # when looping through the elements, let's count how many times they occur 
        # can we use list.count(number) and check if the count == 1
        # brute force solution: two nested loops 
            # loop through every element in the list 

        # is there a data structure that would help us? 
        # a dict helps us by allowing us to check for duplicate values 
        # sets are also an option
        # as we loop, save the fact that we saw this value, if we see it again, then we remove them 
        # dictionaries 

        # as far as space complexity is concerned, worst case would 
        # if we have half of the elements in the set before we start
        # removing any of them: O((1/2) * n) space complexity 

        # Space complexity: measures how memory-usage scales
        # Any data structures that are passed into a function don't count towards space complexity space complexity only cares about any additional data structures that are initialized during an algorithm's execution. 
    # loop through it twice, once adding all the numbers too the set, 2nd pass removing all the duplicates

    s = set()
    for x in arr:
        # loop through every element in the list 
        if x in s:
            # removes the element if it is already in there.
            s.remove(x) 
        else:
            # adds the element in arr to the set
            s.add(x)

    # we should only have one element in our set 
    return list(s)[0]




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")