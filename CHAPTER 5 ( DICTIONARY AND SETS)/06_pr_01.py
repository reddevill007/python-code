hindidictionary={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item",
    "Kitab":"Book"
}
print("Options are ",hindidictionary.keys())
a = input("Enter the Hindi word\n")
print("The meaning of your word is: ",hindidictionary.get(a))