# sort the list into value order
# initiate comparison variable as first variable
# check if comparison variable is same as following list element
# comparison variable reassigned to next variable in list

lst = [1, 5, 3, 1]
#idx   0  1  2  3

# def find_dup(lst):
#     sorted_lst = sorted(lst)
#     idx = 0
#     while idx < len(sorted_lst) - 2:
#         comparison_num = sorted_lst[idx + 1]
#         if sorted_lst[idx] == comparison_num:
#             return sorted_lst[idx]
#         idx += 1

# def find_dup(lst):
#     duplicate = [element for element in lst if lst.count(element) == 2]
#     return duplicate[0]

# def find_dup(lst):
#     seen = set()
    
#     for element in lst:
#         if element in seen:
#             return element
        
#         seen.add(element)

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                  7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True