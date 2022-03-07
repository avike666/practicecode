def function1():
    print("hello world!")
    print("avike")


print("print this line") #our first output
#print(result3)

#this is going to produce an error since it needs to execute function3(y) before
#it can produce the desired output as required by the conditions expressed in the defiend function


#functions in python gets executed sequentially.

def function2(x):
    return 3*x
result2 = function2(3)

function1() #we call function1() #output on second line
function2(3) #output does not print out function2 only function1
#it performs function2(x)

def function3(y):
    return y * 10
    return function3(y)

result3 = function3(5)
function3(5) #even tho we call this function and the function includes print
               #it's not displaying the output
print(result3)
print(result2)
