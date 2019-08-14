import math    #importing math library for sine,cosine etc. functions

#below function takes user choice and angle in degrees as input
def calculate(choice,angle):

    rad=math.radians(angle)    #conversion of angle from degree to radians

    if(choice=="s"):           #if user choice is 's' for sine then the function 
        sin=math.sin(rad)      #  calculates value of sine for the angle
        return "sine",sin      #  and returns user choice and the value

    elif(choice=="c"):         #when choice is 'c' for cosine
        cos=math.cos(rad)
        return "cosine",cos 

    elif(choice=="t"):         #when choice is "t" for tangent
        tan=math.tan(rad)
        return "tangent",tan
        



print("Enter your choice(s-sine,c-cosine,t-tangent) : ")  
choice = input()                                        #asking for user choice
print("Enter angle in degrees : ")
angle = float(input())                                  #input for angle


#storing the values returned by the function in variables
user_choice,value=calculate(choice,angle)       

#finally printing the output
print("User choice is : "+user_choice)
print(user_choice+"(",str(angle)+") = "+str(value))
