#print hello world with difference  way
from time import sleep

x = "Hello World"
a ="qwertyuiopasdfghjklzxcvbnm1234567890,./[]\;''{ !@#$%^&*}|<>?:QWERTYUIOPASDFGHJKLZXCVBNM" 

for i in range(len(x)):
    for y in range(len(a)):
        if x[i] == a[y]:
            print(x[:i]+a[y])
            break
        print(x[:i]+a[y])
        sleep(0.05)
        




