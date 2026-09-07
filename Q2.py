def process_list(numbers):
    N = []
    numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    copiedlist = numbers.copy()
    copiedlist = [num for num in copiedlist if num >= 0]
   


