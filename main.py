import customtkinter
from customtkinter import *
import os
import time
from input_exceptions import FieldException
from user import User
customtkinter.set_appearance_mode("dark")
import pyfiglet 


def register():
    #Registration variables
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    #Registration Screen
    register_screen = CTkToplevel(master)
    register_screen.geometry('500x500')
    register_screen.title('Register')
    
    #Prompt
    register_prompt = CTkLabel(master = register_screen, text = "Please enter your details below to register:", font = ('Georgia', 17))
    register_prompt.place(x= 70, y=90)

    #Name Field
    name_label = CTkLabel(master = register_screen, text = "Username: ", font = ('Georgia', 15))
    name_label.place(x= 76, y= 135)
    CTkEntry(register_screen, textvariable= temp_name).place(x= 155, y= 135)
    
    #Age Field
    age_label = CTkLabel(master = register_screen, text = "Age: ", font = ('Georgia', 15))
    age_label.place(x= 108, y= 175)
    CTkEntry(register_screen, textvariable= temp_age).place(x= 155, y= 175)
   
    #Gender Field
    gender_label = CTkLabel(master = register_screen, text = "Gender: ", font = ('Georgia', 15))
    gender_label.place(x= 95, y= 215)
    CTkEntry(register_screen, textvariable= temp_gender).place(x= 155, y= 215)
    
    #Password Field
    password_label = CTkLabel(master = register_screen, text = "Pin: ", font = ('Georgia', 15))
    password_label.place(x= 108, y= 255)
    CTkEntry(register_screen, textvariable= temp_password, show = "*").place(x= 155, y= 255)
    
    #Sucess/Error Message Area
    notif = CTkLabel(master = register_screen, text='', font = ('Georgia', 16))
    notif.place(x = 155, y = 375)
    
    try:
        CTkButton(register_screen, text = "Register", command = lambda: finish_reg(temp_name, temp_age, temp_gender, temp_password, notif, register_screen), font = ("Georgia", 14)).place(x=155, y= 325)
    except FieldException as fe:
        notif.configure(text_color="red", text= fe.message)
        
        
def check_reg_input(name, age, gender, password):
    all_accounts = os.listdir()
    
    if name == "" or age == "" or gender == "" or password == "":
        raise FieldException('All fields required')
        
    
    for name_check in all_accounts:
        if name == name_check:
            raise FieldException('Account already exists')


def write_register_data(name, age, gender, password):
    with open(name, 'w') as new_file:
        new_file.write(name + '\n')
        new_file.write(password + '\n')
        new_file.write(age + '\n')
        new_file.write(gender+ '\n')
        new_file.write('0')
        new_file.close()
        
    
    
def finish_reg(temp_name, temp_age, temp_gender, temp_password, notif, register_screen):
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    
    
    check_reg_input(name, age, gender, password)
    
    write_register_data(name, age, gender, password)
    notif.configure(text_color = 'green', text = "Account created succesfully\nGo to the login page")
                
                
                
                
def login():
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    
    #Login Screen
    login_screen = CTkToplevel(master)
    login_screen.geometry('500x500')
    login_screen.title("Login")
    
    
    #Labels
    login_prompt = CTkLabel(master = login_screen, text = "Please enter your credentials below to login", font = ('Georgia', 17))
    login_prompt.place(x= 70, y=110)
    
    
    username_label = CTkLabel(master = login_screen, text = "Username: ", font = ('Georgia', 15))
    CTkEntry(login_screen, textvariable= temp_login_name).place(x= 185, y= 155)
    username_label.place(x= 100, y= 155)
    
    user_password_label = CTkLabel(master = login_screen, text = "Pin: ", font = ('Georgia', 15))
    CTkEntry(login_screen, textvariable= temp_login_password).place(x= 185, y= 195)
    user_password_label.place(x= 108, y= 195)
    
   
    login_notif = CTkLabel(master = login_screen, text='', font = ('Georgia', 16))
    login_notif.place(x = 155, y = 340)
    

    try: 
        CTkButton(login_screen, text = "Login", command = lambda: login_session(temp_login_name, temp_login_password, login_notif, login_screen), font = ("Georgia", 14)).place(x=155, y= 265)
    except FieldException as fe:
        login_notif.configure(text_color="red", text=fe.message)
    
    
    
def check_login_existence(login_name):
    all_accounts = os.listdir()
    for name in all_accounts:
        if login_name == name:
            return True
    raise FieldException('Account does not not exist')



def check_password(login_name, login_password):
    with open(login_name, 'r') as file:
                file_data = file.read()
                file_data = file_data.split('\n')
                password = file_data[1]
                
    if login_password == password:
        return True
    raise FieldException('The password is incorrent')
    
    
def login_session(temp_login_name, temp_login_password, login_notif, login_screen):
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    
    exists = check_login_existence(login_name)
    
    if exists: 
        password_check = check_password(login_name, login_password)
        
    
    if password_check:
        login_screen.destroy()
        user = User(login_name)
        account_dashboard = CTkToplevel(master)
        create_dashboard(account_dashboard, user)
        
        
        

def create_dashboard(account_dashboard, user):
    account_dashboard.title('Dashboard')
    account_dashboard.geometry('500x500')
        
    CTkLabel(account_dashboard, text = "Account Dashboard", font=('Georgia', 22)).place(x= 153, y= 30)
    CTkLabel(account_dashboard, text = "Welcome " + user.name, font=('Georgia', 14)).place(x= 200, y= 75)
                    
    #Buttons
    CTkButton(account_dashboard, text = "Personal Details", font = ('Georgia', 16), width = 40, height = 30, command = lambda: personal_details(user)).place(x= 185, y= 160)
    CTkButton(account_dashboard, text = "Deposit", font = ('Georgia', 16), width = 40, height = 30, command = lambda: deposit(user)).place(x= 215,y = 250)
    CTkButton(account_dashboard, text = "Withdraw", font = ('Georgia', 16), width = 40, height = 30, command = lambda: withdraw(user)).place(x= 207, y= 350)
    
                      
    
    
def personal_details(user):
    #Personal Details Screen
    personal_details_screen = CTkToplevel(master)
    personal_details_screen.geometry('500x500')
    
    personal_details_screen.title('Personal Details')
    
    #Labels
    CTkLabel(personal_details_screen, text = "Personal Details" , font = ('Georgia', 24)).place(x= 170, y= 50)
    CTkLabel(personal_details_screen, text = "Name: " + user.name, font = ('Georgia', 16)).place(x= 200, y= 140)
    CTkLabel(personal_details_screen, text = "Age: " + str(user.age), font = ('Georgia', 16)).place(x=200, y= 210)
    CTkLabel(personal_details_screen, text = "Gender: " + user.gender, font = ('Georgia', 16)).place(x=200, y= 280)
    CTkLabel(personal_details_screen, text = "Balance: $" + str(user.balance), font = ('Georgia', 16)).place(x=200, y= 350)



def check_deposit_withdraw_input(amount):
    if amount.get() == "":
        raise FieldException('Amount required')
    if float(amount.get()) < 0:
        raise FieldException('Negative of zero currency is not accepted')



def finish_deposit(amount, deposit_notif, current_balance_label, user):
    
    check_deposit_withdraw_input(amount)
    updated_balance = user.update_balance(float(amount.get()))
    current_balance_label.configure(text="Current Balance" + str(updated_balance), text_color = "green")
    



    
    
def deposit(user):
    #Vars 
    #global amount 
    #global deposit_notif
    #global current_balance_label
    
    amount = StringVar()
    
    #Deposit Screen
    deposit_screen = CTkToplevel(master)
    deposit_screen.title('Deposit')
    deposit_screen.geometry('500x500')
    '''
    account_dashboard.title('Dashboard')
    account_dashboard.geometry('500x500')
        
    CTkLabel(account_dashboard, text = "Account Dashboard", font=('Georgia', 22)).place(x= 153, y= 30)
    CTkLabel(account_dashboard, text = "Welcome " + user.name, font=('Georgia', 14)).place(x= 200, y= 75)
                    
    #Buttons
    CTkButton(account_dashboard, text = "Personal Details", font = ('Georgia', 16), width = 40, height = 30, command = lambda: personal_details(user)).place(x= 185, y= 160)
    CTkButton(account_dashboard, text = "Deposit", font = ('Georgia', 16), width = 40, height = 30, command = lambda: deposit(user)).place(x= 215,y = 250)
    CTkButton(account_dashboard, text = "Withdraw", font = ('Georgia', 16), width = 40, height = 30, command = lambda: withdraw(user)).place(x= 207, y= 350)'''
    
    #Label
    CTkLabel(deposit_screen, text = "Deposit", font = ('Georgia', 23)).place(x = 100, y = 100)
    current_balance_label = CTkLabel(deposit_screen, text = "Current Balance: $" + str(user.balance), font = ('Georgia', 15))
    current_balance_label.place(x = 80, y= 160)
    
    CTkLabel(deposit_screen, text = "Amount: ", font = ('Georgia', 15)).place(x= 80, y = 200 )
    
    #Entry
    CTkEntry(deposit_screen, textvariable = amount).place(x = 120, y= 200)
    
    deposit_notif = CTkLabel(deposit_screen, text = "", font = ('Calibri', 12))
    deposit_notif.place(x= 140, y= 300)
    
    #Button
    try:
        CTkButton(deposit_screen, text ="Finish", font = ('Calibri', 12), command = lambda: finish_deposit(amount, deposit_notif, current_balance_label, user)).place(x= 140, y= 330)
    except FieldException as fe:
        deposit_notif.configure(text_color="red", text= fe.message)
        
        
    

def check_overdraft(withdraw_amount, user):
    if float(withdraw_amount.get()) > user.balance:
        raise FieldException('Insufficient balance')
        
    

def finish_withdraw(withdraw_amount, withdraw_notif, current_balance_label, user):
    check_deposit_withdraw_input(withdraw_amount)
    check_overdraft(withdraw_amount, user)
    updated_balance = user.withdraw(float(withdraw_amount.get()))
    current_balance_label.configure(text="Current Balance" + str(updated_balance), text_color = "green")
    withdraw_notif.configure(text = "Balance Updated", text_color = "green")
    
    

    
    
    
def withdraw(user):
    withdraw_amount = StringVar()
    
    #DEPOSIT_SCREEN DESIGN
    
    withdraw_screen = CTkToplevel(master)
    withdraw_screen.title('Withdraw')
    
    #Label
    CTkLabel(withdraw_screen, text = "Withdraw", font = ('Calibri', 12)).grid(row=0, sticky = N , pady = 10)
    current_balance_label = CTkLabel(withdraw_screen, text = "Current Balance: $" + str(user.balance), font = ('Calibri', 12))
    current_balance_label.grid(row=1, sticky = W)
    
    CTkLabel(withdraw_screen, text = "Amount: ", font = ('Calibri', 12)).grid(row=2, sticky = W)
    withdraw_notif = CTkLabel(withdraw_screen, font = ('Calibri', 12))
    withdraw_notif.grid(row=4, sticky = N, pady= 5)
    
    #Entry
    
    CTkEntry(withdraw_screen, textvariable = withdraw_amount ).grid(row=2, column = 1)
  
    #Button
    try:
        CTkButton(withdraw_screen, text ="Finish", font = ('Calibri', 12), command = lambda: finish_withdraw(withdraw_amount, withdraw_notif, current_balance_label, user)).grid(row=3, sticky = W, pady = 5)
    except FieldException as fe:
        withdraw_notif.configure(text_color = "red", text = fe.message)
        
    

master = CTk()
master.title("Banking ATM")
master.geometry('500x500')


#Labels
CTkLabel(master, text = "Custom Banking ATM", font = ('Georgia', 35)).place(x=110, y=100)
CTkLabel(master, text = "The most secure ATM you've ever used (NOT)", font = ('Georgia', 15)).place(x=110, y=150)


#Buttons
CTkButton(master, text = "Register", font = ('Georgia', 18), width = 120, height = 40, command = register).place(x=185, y=220)
CTkButton(master, text = "Login", font = ('Calibri', 18), width = 120, height= 40, command = login).place(x=185,y=300)


ascii_art = pyfiglet.figlet_format("This is a simple ATM for Tkinter Practice")
print(ascii_art)
print("""The ATM allows for registration and login\nOnce a user is logged in, they can:
      
      > 1. View their personal details
      
      > 2. Withdraw cash
      
      > 3. Deposit cash
      """)



master.mainloop()