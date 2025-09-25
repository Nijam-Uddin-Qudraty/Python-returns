def function(a,c,b=2): # function with default parameter should be mentiond at the last
    print(a,b,c)
function(1,3)

def func(a,*args,**kwargs): # *args will use values every values except a's value
    # ** kwargs will recieve values with keyowrds
    # here args and kwargs are optional
    print(a)
    for i in args:
        print(i)
    for i in kwargs:
        print(kwargs)

func(1, b=3)
# func(1,2,3,4)
# func(2,4,5,6,c=2)

def required_keword(*,a,b): #have to give a * to make keys required, have to pass these after a arges
    print(a,b)

required_keword(a=12,b=39)
# single named parameters those are passed after args are required keyword value
def req(*args, a,):
    print(a)
    for i in args:
        print(i)
req(a=3)

# we can also use unpack directly
def unpack_list(a,b,c):
    print(a,b,c)

unpack_list(*[1,2,3])

def unpack_dict(a,b,c):
    print(a,b,c)
dic={"a":"nijam","b":10,"c":"b"}
unpack_dict(**dic)

## immutable items shouldn't pass to a funciton, cz they uses their address 
