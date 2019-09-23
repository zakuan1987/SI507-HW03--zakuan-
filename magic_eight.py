def Homework_3():
    print("What is your question")

Homework_3()

def check_input(response):
    correct_response = False
    while correct_response == False:
        # print(response)
        if response == "quit":
            exit()
        if '?' not in response:
            print('Every questions ends with a question mark!')
            response = input(name + ", what is your question for the Magic 8 Ball?")
        else:
            correct_response = True
            return response

name = input("Enter your name:")

# add loop
while True:
    response = input(name + ", what is your question for the Magic 8 Ball?")
    if response == "quit":
        break
    response = check_input(response)
