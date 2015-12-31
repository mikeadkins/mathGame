import random

count = 0

while count < 5:
    number_a = random.randint(0,5)
    number_b = random.randint(0,5)
    state = True
    
    while state:
        print number_a, "X" , number_b
        guess = int(raw_input("Enter answer:"))
        if guess == number_a * number_b:
            print "Great Job!"
            state = False
        else:
            print "Sorry try again."
            
    else:
        count = count + 1
           
else:
    print "Congratulations. Give this code to Dad: 9876 "
