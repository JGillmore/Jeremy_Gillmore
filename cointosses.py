import random
heads = 0
tails = 0
for num in range(1,5001):
    string = "Attempt #" + str(num) + ": Throwing a coin... It's a "
    if random.random() >= .5:
        string += "head"
        heads += 1
    else:
        string += "tail"
        tails += 1
    string += "! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
    print string
print "Ending the program, thank you!"
