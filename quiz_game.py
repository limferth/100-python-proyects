print("welcome to my computer quiz!!")

playing = input("Do you want to play ?")
print(playing)

if playing.lower() != "yes":
    quit()


print("okey! let's plat :)")
score = 0
# 1no
answer =  input("what does CPU stand for?  ")
if answer.lower() == "central porcessing unit":
    print("correct")
    score += 1
else:
    print("incorret!")
# DOS
answer =  input("what is your GPU stand fo?  ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorret!")
# TRRES
answer =  input("whatd does RAM stand for?  ")
if answer.lower() == "Random acces memory":
    print("correct")
    score += 1
else:
    print("incorret!")

# CUATRO
answer =  input("whats does PSU stand for   ")
if answer.lower() == "power ssuply":
    print("correct")
    score += 1
else:
    print("incorret!")


print("you got " + str(score) + " question corect")
print("you got " + str((score/ 4) * 100) + "%")