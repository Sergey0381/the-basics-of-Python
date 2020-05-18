#Task  1

n_1 = int(input('Enter number :'))
n_2 = int(input('Enter number :'))
def my_f(n_1 ,n_2):
    try:
        return n_1 / n_2
    except ZeroDivisionError:
        print('division by zero')
        return
print(my_f(n_1,n_2))
