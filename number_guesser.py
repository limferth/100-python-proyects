import random

top_of_range = input("type a number")



if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range < 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("please type a number next time")
    quit()

number_random = random.randrange(0, top_of_range)
guesses = 0

print(number_random)

while True:
    guesses =+ 1
    user_guess = input("make a gues: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else: 
        print("please type a number next time. ")
        continue
    print("after continue ")
    if user_guess == number_random:
        print("you got it!!")
        break
    
    elif user_guess > number_random:
        print("yor were above the number: ")
    else:
        print("you were below the number!")
        
print("you got it in ", + str(guesses) + "guesses")