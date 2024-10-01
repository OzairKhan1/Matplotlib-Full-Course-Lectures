"""                                     Zip Function
The zip function is used for parallel iteration. It means we have to pass iterator to it

**********  The output returns by zip function is object type. we have to convert it to list
1) This Function returns a tuple of elements on the same index from all the lists
2) The length of output list depends on the length of shortest list by default.
We can change this behaviour by using zip_longest() from itertools
3) The number of elements per tuple depends on the number of iterator passed
4) by passing a single list returns list of that tuple
5) by passing none will returns an empty list


"""

# point 1 and 3 is convered:: 2 list passed so length of individual will be 2.
a = [1,2,3,4]
b = [6,7,8,9]
zipped = zip(a,b)
print('Zip Object',zipped) # this will be a zip object. we can convet it to list, set or dict. but list prefers
zipped_list = list(zipped)
print('Zip list: ',zipped_list)


#Example 2:: by passing lists of different lengths.

c = [1,2,3,4,5,6,7,8,9,10]
d = [6,7,8,9,10]
zipp = list(zip(c,d))
print(f"The length of shortest will be taken:", zipp," lenth is ",len(zipp))

#Example 3: By passing
#using zip_longest from  itertools
from itertools import  zip_longest
zip_longst = list(zip_longest(c,d))
print(f"With zip longest the result will be changed to: {zip_longst}")

#Example 4: passing a single element list

e = [1000]
print(f"single element list: {list(zip(e))}") # Returns a list of tuple b/c we convet zip to list
#to access that single element
print(f"Acees elements from list of tuple",list(zip(e))[0][0])

#Example 5:: Returns an empty tuple

print("Returns an empty list",list(zip([])))

# Use this We can do the nested loop job using single loop with zip
# In this example we want to Multiply e

