def greet(name):
    print(f"Hello {name}.")
#greet("Harshi")

def nums(a,b):
    return a+b,a-b
#result = nums(1,2)
#print(result)

def square(num):
    return num*num
#result = square(5)
#print(result)

def is_even(num):
    if(num % 2 == 0):
        return True
    else:
        return False
#print(is_even(3))

def average(nums):
    return sum(nums)/len(nums)
print(average([1,2,3]))
