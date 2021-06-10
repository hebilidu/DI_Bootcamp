from time import perf_counter
from termcolor import colored
from random import randint, sample
from collections import defaultdict

def timer(func):
    """use as a decorator to get any function run time duration"""
    def wrapper(*args, **kwargs):
        start = perf_counter()
        payload = func(*args, **kwargs)
        end = perf_counter()
        print(colored(f"Elapsed time for {func.__name__}: {end - start: 0.6f} seconds", 'red'))
        return payload
    return wrapper

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        
        a = merge_sort(a)
        b = merge_sort(b)
        c = []
        
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1
        c += a[i:]
        c += b[j:]
        return c

@timer
def longest_sequence1(nums: list) -> int:
    """return length of longest consecutive elements sequence"""
    # <your code here>
    # Algorithm 1: sort list and scan result for longest consecutive sequence
    # Step 1: sort list with the built-in sort() function
    nums.sort() # O(n*log(n))
    # Step 2: find longest consecutive sequence
    longest = []
    candidate = []
    for n in nums: # O(n)
        if candidate == [] or candidate[-1] == n - 1:
            candidate.append(n)
        elif candidate[-1] != n:
            # consecutive sequence is broken: check if candidate is longest then reset candidate to start new sequence
            if len(candidate) > len(longest):
                longest = candidate.copy()
            candidate = [n]
    # print('nums', nums)
    # print('longest', longest)
    return len(longest)

@timer
def longest_sequence2(nums: list) -> int:
    """return length of longest consecutive elements sequence"""
    # <your code here>
    # Algorithm 2: Using dictionaries (defaultdict returns specified default value for non-existing keys)
    if len(nums) == 0:
        return 0
    d = set(nums)
    ans = 1
    nb = defaultdict(int)
    for i in nums: # O(n) !!!
        cur = 1            
        if i in nb:
            cur = nb[i]
        else:
            while i + 1 in d:
                nb[i] = cur # memoization
                i += 1
                cur += 1            
        ans = max(ans, cur)
    return ans

def main():
    # input_list = [6, 4, 100, 5, 200, 2, 3]
    # input_list = [6, 4, 100, 5, 200, 2, 3, 4]
    input_list = [randint(-5000,5000) for _ in range(5000)]

    # print('input_list', input_list)
    print('longest_sequence1', longest_sequence1(input_list))
    print('longest_sequence2', longest_sequence2(input_list))

if __name__ == "__main__":
    main()