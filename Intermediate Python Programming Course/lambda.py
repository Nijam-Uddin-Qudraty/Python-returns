# labda is anonymous short function

add = lambda x:x+5
print(add(10))

lt = [(1,3),(6,9),(3,6)]

# by default sort functions uses the 1st item of the inner items to sort data
# so by if we want to sort data in different way we have to use key arugment
lt_sort = sorted(lt)
lt_reverse_sort = sorted(lt, reverse=True)
print(lt_sort,"\n",lt_reverse_sort)

# key argument takes function as it value
# so we can use lambda function for sort func expression here

lt_sort = sorted(lt, key= lambda x: x[1])
nums = [1,4,6,9]
mult = map(lambda x:x*10,nums)
print(list(mult))

div_3 = filter(lambda x: x%3==0,nums)
print(list(div_3))