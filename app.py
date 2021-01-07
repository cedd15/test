def myfunc(x):
    return lambda a: a * x

mydoubler = myfunc(2) #variable "mydoubler" is used to name the lambda
#the value of this variable is the function which should have an argument and that is 2


print(mydoubler(5)) #we are now calling lambda with another argument