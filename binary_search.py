# naive search: scan entire list and ask if its equal to target 
# if yes, return index
# if no, then return -1

def naive_search(l, target):
    # example l = [ 1, 3, 5, 7, 9, 13, 16, 19, 24, 29, 36]
    # if target is 16
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer
# we will leverage the fact that our list is SORTED

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)- 1
    if high < low:
        return -1
    # example l = [ 1, 3, 5, 7, 9, 13, 12, 16, 19, 24, 29, 36, 70]
    # still using 16 as target
    midpoint = (len(l)) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1 )
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)
      
if __name__ == '__main__':
    l = [ 1, 3, 5, 7, 9, 13, 12, 16, 19, 24, 29, 36, 70]
    target = 16
    print(naive_search(l, target))
    print(binary_search(l, target))