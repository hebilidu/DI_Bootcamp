from time import perf_counter
from termcolor import colored

def timer(func):
    """use as a decorator to get any function run time duration"""
    def wrapper(*args, **kwargs):
        start = perf_counter()
        payload = func(*args, **kwargs)
        end = perf_counter()
        print(colored(f"Elapsed time for {func.__name__}: {end - start: 0.6f} seconds", 'red'))
        return payload
    return wrapper

@timer
def subsetsum(numbers: list, target: int) -> bool:
    # <your code here>
    # Algorithm 1: Pre-calculate all combinations of two added items into a dictionary
    # Step 1: build dictionary of all possible sums
    # print(numbers)
    sums = {} # O(1)
    sublist = numbers.copy() # O(n) 
    sublist.reverse() # O(n)
    # print(sublist)
    for a in numbers: # O(n^2)
        sublist.pop() # O(1)
        # print(sublist)
        for b in sublist:  # O(n)
            s = a + b # O
            if s in sums:
                sums[s].append((a,b)) # O(1)
            else:
                sums[s] = [(a,b)] # O(1)
    # Step 2: look for target
    # print(sums)
    # print(target, type(target))
    if target in sums: # O(1)
        return sums[target] # O(1)
    else:
        return False

@timer
def subsetsum2(numbers: list, target: int) -> bool:
    # <your code here>
    # Algorithm 2: Loop through dictionaries (which are hashtables) rather than lists
    # Step 1: build dictionary of all possible sums
    sums = {} # O(1)
    nums = dict(zip(numbers, numbers)) # O(n) ?
    sublist = nums.copy() # O(n)
    # print(nums)
    for a in nums: # O(n)
        sublist.pop(a) # O(1)
        # print(sublist)
        for b in sublist:  # O(n)
            s = a + b # O(1)
            if s in sums:
                sums[s].append((a,b)) # O(1)
            else:
                sums[s] = [(a,b)] # O(1)
    # Step 2: look for target
    # print(sums)
    # print(target, type(target))
    if target in sums: # O(1)
        return sums[target] # O(1)
    else:
        return False

def main():
    nums = [12, -7, 20, 1, 4, -10, -1]
    # nums = [i for i in range(-10, 500)]
    print("\n=========\nAlgorithm #1\n=========")
    print('subsetsum(nums, 1):', subsetsum(nums, 1), '\n')
    print('subsetsum(nums, 2):', subsetsum(nums, 2), '\n')
    print('subsetsum(nums, 3):', subsetsum(nums, 3), '\n')
    print('subsetsum(nums, 4):', subsetsum(nums, 4), '\n')
    print("\n=========\nAlgorithm #2 : with hash tables\n=========")
    print('subsetsum2(nums, 1):', subsetsum2(nums, 1), '\n')
    print('subsetsum2(nums, 2):', subsetsum2(nums, 2), '\n')
    print('subsetsum2(nums, 3):', subsetsum2(nums, 3), '\n')
    print('subsetsum2(nums, 4):', subsetsum2(nums, 4), '\n')

if __name__ == "__main__":
    main()