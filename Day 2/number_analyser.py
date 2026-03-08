nums = []
for i in range(10):
    num = int(input(f"Enter your {i+1} number: "))
    nums.append(num)

largest = max(nums)
smallest = min(nums)
average = sum(nums)/ len(nums)

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Average: {average}")
print("Numbers greater than average: ")
for num in nums:
    if(num > average):
        print(num)