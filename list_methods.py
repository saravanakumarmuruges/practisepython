sample_list = [1,2,3,4,5]

sample_list.append(6) #to add value at last of the list

print(sample_list)
###################################################################################
app_list=[7,8,9,10]

sample_list.extend((app_list)) #to merge one  list with another

print(sample_list)
###################################################################################
sample_list.insert(1,'Two') #to insert given value in given index

print(sample_list)
###################################################################################
sample_list.remove('Two') #to remove first occurance of given value
print(sample_list)
###################################################################################
sample_list.pop()
print(sample_list) #to rwemove last item in the list
###################################################################################
print(sample_list.count(5)) #to print no.of occurance of value in the given list
###################################################################################
sample_list.sort() #to sort list in assending order
print(sample_list)
sample_list.sort(reverse=True) #To sort list in the desending order
print(sample_list)
sample_list.reverse() #To reverse the list from curent order, without any assending or desending operations
print(sample_list)
###################################################################################
new_list = sample_list.copy() #to make copy of list into another variable
print(new_list)
print(sample_list.index(7)) #To get inxex of given value in an list, Will give value error if its not avaiable
###################################################################################
del sample_list[2] #To remove value in given index location
print(sample_list)
del sample_list[4:6] #to remove values in the given index range
print(sample_list)
###################################################################################
sample_list.clear() #To remove all values in the list
print(sample_list)