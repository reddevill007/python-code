f = open('another.txt', 'w')
f.write("I am appending ")
f.close() # when we open in w  mode it eraces all the appended character
# but when we run in append mode we can write again and again just by ruuning the program