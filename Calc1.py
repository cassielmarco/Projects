def chek (num):
    while True:
        try: 
            num = float(num)
            return num
        except ValueError:
            num = input(" ERR Enter A number again: ")
    
def chekop (num1,num2):
    while True:
        opp = input("Enter the operation you want to perform (+, -, *, /): ")
        if opp == "+":
            res = num1 + num2 
            return res
        elif opp == "-":
            res = num1 - num2
            return res 
        elif opp == "*":
            res = num1 * num2
            return res
        elif opp == "/":
            if num2 == 0:
                print("change op")
            else:
                res = num1 / num2
                return res
        else: 
            print("cant do this bro")

while True:

    num1 = input("Enter numm1: ") 
    num1 = chek(num1)
    num2 = input("Enter num2: ")
    num2 = chek(num2)
    ress = chekop(num1,num2)
    print(ress)
    location = "C:\Users\moham\OneDrive\Desktop\Projects\Calc1history.txt"
    with  open(location, "a") as file : 
        text = file.write(str(ress)+"\n")
    with open(location, "r") as file :
        text = file.read()
    hchoice = input("do you want to see ur history yes or no: ")
    if hchoice == "yes":
        print(text) 
    elif hchoice == "no":
        print("ok")
     
    choice = input("do you want another calculation? yes/no: ")
    if choice == "no":
        break
    elif choice == "yes":
        print("ok")