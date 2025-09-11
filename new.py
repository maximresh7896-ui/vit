import random
points={"player":0, "comp":0}
def check_odd(number):
    if number%2==0:
        return False
    else:
        return True
while True:
    a=random.randint(0, 120)
    if check_odd(a):
        continue
    b=random.randint(0, 120)
    if check_odd(b):
        continue
    op=random.choice(["+","-"])
    if op=="+":
        answer=a+b
        user=int(input(f"{a}+{b}="))
    else:
        answer = a-b
        user = int(input(f"{a}-{b}="))
    if answer==user:
        print("congradulation you correctly do the question")
        points["player"]+=1
    else:
        print("the answer is wrong")
        points["comp"]+=1
    print(f'Score: {points["player"]}:{points["comp"]}')