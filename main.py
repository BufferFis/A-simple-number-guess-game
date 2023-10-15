import random
x,y=list(map(int, input('Enter lower and upper bound with a space: ').split()))
t=random.randint(x,y)
z=int(input('In how many guesses will u like to guess the number? '))
count=0
while z!=0:
    k=int(input('guess: '))
    if k>t:
        z-=1
        count+=1
        print(F'Your guess was too high, you have {z} tries remaining')
    elif k<t:
        z-=1
        count+=1
        print(F'Your guess was too low, you have {z} tries remaining')
    elif k==t:
        print(f'Yes u are correct the number was {t}, U found it in {count} amount of tries')
        break
    elif z==1:
        print('Last try make it count')
    

        
