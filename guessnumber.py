import random
list=[]
def hints(num):
    h=0
    for i in range(2,int(num)):
        if num%i==0:
            list.append(i)
            h+=1
    if h==0:
        print("Prime number")
        
flag=True
while flag:
    num=input('Type a number for upper bound: ')
    if num.isdigit():
        print("Let's play")
        num=int(num)
        flag=False
    else:
        print("Invalid input! Try Again!")
secret=random.randrange(1,num)
guess=None
count=1
i=1
hints(secret)
len=len(list)
while guess!=secret:
    guess=input('Please Enter a number between 1 and '+str(num)+' :')
    if guess.isdigit():
        guess=int(guess)
    if guess==secret:
        print("Your guess is correct!")
    else:
        if guess>secret:
            print('Your guess is greater than secret key!')
        elif guess<secret:
            print('Your guess is smaller than secret key!')
        if i<=len:
            print('HINT'+str(i)+': Secret key is divisible by',list[i-1])
            i+=1
        else:
            print('Please Try Again!')
        count+=1
print("It took you",count,'chances')