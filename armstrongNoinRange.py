def armstrong_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]

start, end = map(int, input("Enter range (start end): ").split())
print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers_in_range(start, end)}")
