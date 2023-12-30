# need to add timer for each question and showcase wrong questions and their right solution
import random
import time
# constansts
Operators=['+','-','*','%','/']
Min=3
Max=12
Totalq=10


def generate_prob():
        leftnum=random.randint(Min,Max)
        rightnum=random.randint(Min,Max)
        Operator=random.choice(Operators)
        # string because same data type operand so operation can be performed
        exp=str(leftnum)+' '+Operator+' '+str(rightnum)
        answer = eval(exp)
        return exp,answer

ans=0
wrong=0

print("Welcome to the math game!")
print("PRESS TO ANYTHING TO START")
input("")
print("-----------------")
start_time=time.time()
for i in range(Totalq):
    exp,answer=generate_prob() 
    guess=input('Problem #'+str(i+1)+' :'+ exp +'=')
  
   # gives 10 sec for each question

    # for x in range(my_time, 0, -1):
    #     seconds = x % 60
    
    #     print(f"{{seconds:02}")
    #     time.sleep(10)

    #     print("TIME'S UP!")
    while True:
        if guess == str(answer):
            ans+=1
            break
                
#we are converting ans to str and not guess to int bcoz if user enter invalid int it will crash the program
stop_time=time.time()
totaltime=stop_time-start_time
print('total wrong answers',wrong) 
print('Correct Answers',ans)
print('well done! ,u finished in',round(totaltime),'seconds')
mistake=input("do u want to see the mistakes ??,if so type yes :")
# print("Wrong Answered Questions and their answer")
# if mistake.lower()=='yes':
#     print(mistakes1)
#     print(" ")
#     print(mistakes2)
# print("-----------------")


