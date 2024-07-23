name=input("Please,enter your name:" )
print("hello",name )

message="""
select an option from following:
click1 ---> check balance
click2 ----> deposite
click3 ----> withdraw"""
print(message)
task=int(input("please select on of the options:"))
available_amount=5000
if task>=1 and task<=3:
    if task==1:
        print("your available balance is:",available_amount)
    elif task==2:
        deposite_amount= int(input("enter the amount you want to deposite:"))
        if deposite_amount>=500:
            available_amount= available_amount + deposite_amount
            print("u have successfully deposited the amount")
            print("now your available balance is:", available_amount)

        else:
            print("please enter amount greater than 500")

    elif task==3:
        withdraw_amount=int(input("enter the amount you want to withdraw:"))

        if withdraw_amount > available_amount:
            print(""" Uh-Oh!
        It seems you do not have this much amount in your account . 
        Please enter a valid amount""")
        else:
            available_amount= available_amount - withdraw_amount
            print("Your available balance after withdrawing is:",available_amount)

