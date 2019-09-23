def Homework_3():
    print("What is your question")

Homework_3()

import random

ans1 = "It is certain"
ans2 = "It is decidedly so"
ans3 = "Without a doubt"
ans4 = "Yes - definitely"
ans5 = "You may rely on it"
ans6 = "As I see it, yes"
ans7 = "Most likely"
ans8 = "Outlook good"
ans9 = "Yes"
ans10 = "Signs point to yes"
ans11 = "Reply hazy, try again"
ans12 = "Ask again later"
ans13 = "Better not tell you now"
ans14 = "Cannot predict now"
ans15 = "Concentrate and ask again"
ans16 = "Don't count on it"
ans17 = "My reply is no"
ans18 = "My sources say no"
ans19 = "Outlook not so good"
ans20 = "Very doubtful"

choice = random.randint(1,20)

if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer = ans5
elif choice == 6:
    answer = ans6
elif choice == 7:
    answer = ans7
elif choice == 8:
    answer = ans8
elif choice == 9:
    answer = ans9
elif choice == 10:
    answer = ans10
elif choice == 11:
    answer = ans11
elif choice == 12:
    answer = ans12
elif choice == 13:
    answer = ans13
elif choice == 14:
    answer = ans14
elif choice == 15:
    answer = ans15
elif choice == 16:
    answer = ans16
elif choice == 17:
    answer = ans17
elif choice == 18:
    answer = ans18
elif choice == 19:
    answer = ans19
else:
    answer = ans20

print("*************************")
print("Magic 8 Ball:",answer)
