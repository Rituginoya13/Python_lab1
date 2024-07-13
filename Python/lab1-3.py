name=str(input("Enter your name: "))
year=str(input("Enter your Standrard/Year: "))
mark1=int(input("Enter marks of Sub1: "))
mark2=int(input("Enter marks of Sub2: "))
mark3=int(input("Enter marks of Sub3: "))
mark4=int(input("Enter marks of Sub4: "))
mark5=int(input("Enter marks of Sub5: "))
sum=mark1+mark2+mark3+mark4+mark5
avg=sum/5

if(avg>=100):
    print("Please enter valid marks")
elif(avg>90 and avg<=99):
    print("A+ Grade")    
elif(avg>70 and avg<=89):
    print("A Grade")   
elif(avg>60 and avg<=69):
    print("B Grade")   
elif(avg>50 and avg<=59):
    print("C Grade")   
elif(avg>33 and avg<=49):
    print("D Grade")   
else:
    print("Faii")