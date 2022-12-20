def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    try:
        while start <= end:
            print("Step", steps, ": ", str(list[start:end+1]))

            steps += 1
            middle = (start + end) // 2

            if element == list[middle]:
                return middle
            if element < list[middle]:
                end = middle - 1
            else:
                start = middle + 1
        return -1
    except IndexError:
        print("Value not in list!")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
target = 14

binary_search(my_list, target)
