# EPIC MADLIBS PROJECT STARTS HERE!!!!!
import random
def madlibs1():
    print(madlibs1)
def madlibs2():
    print(madlibs2)
def madlibs3():
    print(madlibs3)

input1 = input("a single word: ")
input2 = input("a long string of words: ")
input3 = input("a tv show: ")
input4 = input("a ending clause: ")

madlibs1 = (f"Hello everyone my name is {input1} and i am here to introduce myself! I like doing fun things like normal people.\
              i enjoy long walks on the beach and {input2}! My favourite show is {input3}, i know i'm a little bit quirky <3 \
               it was nice meeting you all and {input4}")

madlibs2 = (f"{input1} is a dumb man and i {input2} every single day!, i concentrate on {input3} but i'm bored now so {input4}")

madlibs3 = (f"i put my bet on {input1}, kid's a loose canon but he {input2} every single god damn day. I'll take him over {input3} any day. \
              if you gentlemen excuse me now, i have to {input4}")

madlibs = [madlibs1, madlibs3, madlibs3]
main = random.choice(madlibs)
print(main)
    