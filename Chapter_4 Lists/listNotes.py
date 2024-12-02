# A common Python technique is to use 

# range(len(someList)) 
# with a for loop to iterate over the indexes of a list. 

# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for i in range(len(supplies)):
#    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# Index 0 in supplies is: pens
# Index 1 in supplies is: staplers
# Index 2 in supplies is: flamethrowers
# Index 3 in supplies is: binders


# enumerate() will return two values: the index of the item in the list, and the item in the list itself.

# random.choice() function will return a randomly selected item from the list.
# random.shuffle() function will reorder the items in a list.
# index() method that can be passed a value, and if that value exists in the list, the index of the value is returned.
# append() and insert() will add to a list

# del and remove() removes from a list
# The del statement is good to use when you know the index of the value you want to remove from the list. 
# The remove() method is useful when you know the value you want to remove from the list.
# sort(), spam.sort(reverse=True) reverses list

# The tuple data type is almost identical to the list data type, except in two ways. 
# First, tuples are typed with parentheses, ( and ), instead of square brackets, [ and ].
# TUPLES ARE IMMUTABLE, USE THEM WHEN YOU WANT UNCHANGING GROUP OF VARS 

#List and tups can be changed into one another:
# tuple([list])
# list(('cat', 'dog', 'fish'))
# id('Howdy') # The returned number will be different on your machine.
# 44491136

# copy.copy / copy.deepcopy makes copies of mutable types like dicts or lists I guess? the deep one gets lists within lists