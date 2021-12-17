def game():
    return 655

score = game()
with open("hiscore.txt") as f:
    hiscore=f.read()

if hiscore=="":
    with open("hiscore.txt","w") as f:
        f.write(str(score))

elif hiscore<score:
    with open("hiscore.txt","w") as f:
        f.write(str(score))
