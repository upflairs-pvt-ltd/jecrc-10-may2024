name = input("Plz enter your name : ")
print("Welcome ,", name,'\n')
starting_message = """
plz choose your task :
Type --> 1 for check balance
Type --> 2 for deposit amout
Type --> 3 for withdrawl amout
"""
print(starting_message)
task = int(input("plz enter your task : "))
current_available_balance = 5000

if task >=1 and task<=3:

    if task == 1:
        ## code to be check balance
        print("Your available balance is : ",current_available_balance)  
    elif task == 2:
        # code to be deposit
        deposit_amount = int(input("Plz enter your deposit amount : ")) 
        if deposit_amount > 500:
            current_available_balance += deposit_amount
            print("you have successfully deposit your amount : ",deposit_amount)
            print("Your available balance is : ",current_available_balance)  

        else:
            print("Plz deposit more than 500 Rupees")




    else:
        # withdrawl
        withdrawl_amount = int(input("plz eneter withdrawl amount :"))  
        if withdrawl_amount < current_available_balance:
            current_available_balance -= withdrawl_amount
            print("you have successfully withdrawl amount is : ",withdrawl_amount)
            print("Your available balance is : ",current_available_balance)  

        else:
            print("you have no sufficient amount !")

        
else:
    print("choose valid task, in btwn 1 to 3")






