bool = True
def func1():
    print("True")
def func2():
    print("False")
def _if(bool, func1, func2):
    if bool == True:
        return func1()
    else:
        return func2()