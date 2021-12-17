# a=input("ENTER YOUR NAME\n")
# b=input("ENTER THE DATE\n")
# print("'''Dear ",a,"\nyou are selected!\n",b,"'''")
letter='''Dear <|NAME|>,
Greetings from abc coading house.I am happy to mtell you about your selection
You are selected!
have a great day....
Date: <|DATE|>'''
a=input("ENTER YOUR NAME\n")
b=input("ENTER THE DATE\n")
letter = letter.replace("<|NAME|>",a)
letter = letter.replace("<|DATE|>",b)
print(letter)