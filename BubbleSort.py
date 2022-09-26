# BUBBLE SORTING

# Ascending sorting
ascending_array = [4,8,6,2,0,1,7,59,2,778,66,999,1,422]

# In bubble sorting we need to compare between each two elements in an array

# array length
n = len(ascending_array)

for _ in range(n-1):

    for index in range(n-1):
        # if our current element is greater than the next element swap, else pass
        if ascending_array[index] >= ascending_array[index + 1]:
            tmp = ascending_array[index]
            ascending_array[index] = ascending_array[index + 1]
            ascending_array[index + 1] = tmp

# printing the result
print(ascending_array)

#------------------------------------------------------------------------------------------

# Descending sorting
descending_array = [4,8,6,2,0,1,7,59,2,778,66,999,1,422]

# In bubble sorting we need to compare between each two elements in an array

# array length
n = len(descending_array)

for _ in range(n-1):

    for index in range(n-1):
        # if our current element is smaller than the next element swap, else pass
        if descending_array[index] <= descending_array[index + 1]:
            tmp = descending_array[index]
            descending_array[index] = descending_array[index + 1]
            descending_array[index + 1] = tmp

# printing the result
print(descending_array)




