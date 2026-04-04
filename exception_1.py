try:
    num=int(input("enter a number:"))
    num=int(input("enter another number :"))
    result=num1/num2

except ZeroDivisionError:
         print("you can not divided by zero")
except ValueError:
         print("please enter a valid number !")
else:
    print("division successful result is :",result)

finally:
     print("this block always run")
