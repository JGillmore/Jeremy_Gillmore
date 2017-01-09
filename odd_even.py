for num in range(1,1000):
    string = "The number is "+ str(num) + ".  This is an "
    if num % 2 != 0:
        string += "odd number."
    else:
        string += "even number."
    print string
