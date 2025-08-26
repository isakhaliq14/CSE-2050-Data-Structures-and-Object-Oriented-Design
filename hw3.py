import random
import time

def generate_lists(size):
    list1 = random.sample(range(size*2), size)
    list2 = random.sample(range(size*2), size)

    return list1, list2

def find_common(list1, list2):
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count += 1
    return count

def find_common_efficient(list1, list2):
    big_list = list1 + list2  
    set1 = set(big_list)
    unique = len(set1)
    common = (len(list1) + len(list2)) - unique
    return common

def measure_time():
    different_sizes = [10, 100, 1000, 10000, 20000]
    print("List Size    find_common Time (s)    find_common_efficient Time (s) \n -----------  ----------------------  -----------------------------")
    for size in different_sizes:
        list1, list2 = generate_lists(size)
        
        start1 = time.time()
        find_common(list1, list2)
        common_time = time.time() - start1
        
        start2 = time.time()
        find_common_efficient(list1, list2)
        efficient_time = time.time() - start2
        
        print(f'{size} {common_time} {efficient_time}')


if __name__ == "__main__":
    measure_time()