comment=input("Enter the text: ")

if "make a lot of money" in comment:
    spam=True

elif "buy now" in comment:
    spam=True

elif "click this" in comment:
    spam=True

elif "subscribe now" in comment:
    spam=True

else:
    spam=False

if spam:
    print("The text is spam")
else:
    print("The text is not spam")

