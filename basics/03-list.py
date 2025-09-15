# list 
my_list=[1,2,3,4,5]
print(my_list)

# append - add single item
add_item=6
my_list.append(add_item)
print(my_list)

# extend - add another list , set , tuple 
add_list=[7,8,9,10]
my_list.extend(add_list)
print(my_list)

# insert - add item at specific index
my_list.insert(3,"a")
print(my_list)

# remove - remove specific item
my_list.remove("a")
print(my_list)

# pop - remove last item and return the value
value = my_list.pop()
print(my_list)
print(value)

# pop - remove item and return the value by passing specific index
value = my_list.pop(2)
print(my_list)
print(value)


# count - no of times appearance in given list
add_item=6
my_list.append(add_item)
no_of_times = my_list.count(6)
print("no of times repeat",no_of_times) 

# clear - remove all items
my_list.clear()
print(my_list)

# sorting
random_list = [2,6,0,3,5,4,9,8,1,7]
random_list.sort()
print(random_list)

# reverse
random_list.reverse()
print(random_list)

original_list = [1,2,3,4]
copied_list = original_list.copy()
print(f"original list {original_list}")
print(f"copied list {copied_list}")
