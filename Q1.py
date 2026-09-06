n = int(input("Enter the number of elements (N): "))

numbers = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    numbers.append(num)

if n > 0:
    largest = numbers[0]
    smallest = numbers[0]
    total_sum = 0
    even_count = 0
    odd_count = 0
    reversed_list = []

    
    for num in numbers:
        
        if num > largest:
            largest = num
            
        if num < smallest:
            smallest = num
    
        total_sum += num
        
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    for i in range(n - 1, -1, -1):
        reversed_list.append(numbers[i])

    print(f"\n1. The largest element: {largest}")
    print(f"2. The smallest element: {smallest}")
    print(f"3. The sum of all elements: {total_sum}")
    print(f"4. The number of even elements: {even_count}")
    print(f"5. The number of odd elements: {odd_count}")
    print(f"6. The list in reverse order: {reversed_list}")
else:
    print("The list is empty.")
