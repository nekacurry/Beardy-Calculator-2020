print("How Many Bearded Dragons will Fit in Your Home?")
#Bearded dragons are dope, who wouldn't want to know?

SQft = input("What is the square footage of your living space?: ")
SQft = int(SQft)
#The SQft input is reassigned to an integer in order to be calculated

furniture = input("What is the estimated percentage of furniture in your living space?: ")
furniture = int(furniture)
#The furniture input is reassigned to an integer in order to be calculated

fSQft = (furniture / 100 * SQft) 
#We need to convert the percentage of furniture into square feet for further calculation

lSQft = (SQft - fSQft)
#The square footage of the home minus the square footage of furniture leaves behind the open square footage in which to fill with beardies

message = f"You can fit {lSQft / 2} Bearded Dragons inside your home!"
#The open square footage is then divided by 2sqft, which is the average size of a bearded dragon tank

print(message)
#Congrats! Fill your home with lizards!