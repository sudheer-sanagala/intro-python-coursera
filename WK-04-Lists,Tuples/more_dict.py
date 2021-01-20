# A dictionary is not ordered, so we can’t use positions to access elements; instead, we have to use the key-value pair.
# It is changeable, which allows us to update dictionary elements.
# No duplicate allowed.

dictionary_1 = {
    "brand":"BMW",
    "model": "Model 3",
    "year": 2000}

print(dictionary_1)

# keys of dict
print(f'Print dict keys -',(dictionary_1.keys()))

# values of dict
print(f'Print dict value -',(dictionary_1.values()))

# keys and values of dict
print(f'Print dict keys -',(dictionary_1.items()))


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''
def add_two(nums, target):
    result = []

    for i in range(len(nums)):
        # Add element to next element
        for j in range(i+1,len(nums)):
            print("Element in list -",j)
            if nums[i]+nums[j] == target:
                result.append(i)
                result.append(j)
    print(result)
    return result

nums = [2,7,11,15]
target = 9
add_two(nums,target)
'''

def two_sum (nums,target):  
    dictionary = {}
    for index,value in enumerate(nums):      
        diff = target - value
        if diff in dictionary:
            return [index, dictionary[diff]]
        else:
            dictionary[value] = index   
    print(f"Dict -",(dictionary))
    return dictionary

# test case 
nums = [2,7,11,15]
target = 9
two_sum(nums,target)


# https://towardsdatascience.com/master-python-dictionary-for-beginners-in-2021-1cdbaa17ec45




def add(num):
    result = 0

    for i in range(0,num+1):
        #print(f"value {i}")
        result= result+i
        print(f"In loop {i}, with sum {result}")

    print(result)
    return result

add(5)