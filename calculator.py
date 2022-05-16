print("Enter The Operation To Be Performed:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Square of a Number")
print("6.Cube of a Number")

symbol=input("Enter your choice: ",)

if symbol=="1":
    a=input("Enter the First Number: ",)
    b=input("Enter the Second Number: ",)
    result=int(a)+int(b)
    print("The Sum is: ",result)
elif symbol=="2":
    a=input("Enter the First Number: ",)
    b=input("Enter the Second Number: ",)
    result=int(a)-int(b)
    print("The Difference is: ",result)
elif symbol=="3":
    a=input("Enter the First Number: ",)
    b=input("Enter the Second Number: ",)
    result=int(a)*int(b)
    print("The Product is: ",result)
elif symbol=="4":
    a=input("Enter the Dividend: ",)
    b=input("Enter the Divisor: ",)
    if b=="0":
        print("Divided By Zero Error!!!")
    else:
        quotient=int(a)/int(b)
        remainder=int(a)%int(b)
        print("The Quotient is: ",int(quotient))
        print("The Remainder is: ",remainder)
elif symbol=="5":
    a=input("Enter the Number: ",)
    result=int(a)*int(a)
    print("The Square of Given Number is: ",result)
elif symbol=="6":
    a=input("Enter the Number: ",)
    result=int(a)*int(a)*int(a)
    print("The Cube of Given Number is: ",result)
else:
    print("<-----Please Enter the correct Operation!!!----->")
