import customtkinter
from customtkinter import *
import os
import time

customtkinter.set_appearance_mode("dark")

def register():
    
    # Vars
    global temp_name, temp_age, temp_gender, temp_password, notif, register_screen
    
    
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    
    register_screen = CTkToplevel(master)
    register_screen.geometry('500x500')
    register_screen.title('Register')
    
    #Labels
    register_prompt = CTkLabel(master = register_screen, text = "Please enter your details below to register:", font = ('Georgia', 17))
    register_prompt.place(x= 70, y=90)
    
    
    name_label = CTkLabel(master = register_screen, text = "Name: ", font = ('Georgia', 15))
    name_label.place(x= 100, y= 135)
    
    age_label = CTkLabel(master = register_screen, text = "Age: ", font = ('Georgia', 15))
    age_label.place(x= 108, y= 175)
    
   
    gender_label = CTkLabel(master = register_screen, text = "Gender: ", font = ('Georgia', 15))
    gender_label.place(x= 95, y= 215)
    
    password_label = CTkLabel(master = register_screen, text = "Password: ", font = ('Georgia', 15))
    password_label.place(x= 83, y= 255)
    
    notif = CTkLabel(master = register_screen, text='', font = ('Georgia', 16))
    notif.place(x = 155, y = 375)
    
    #Entries
    CTkEntry(register_screen, textvariable= temp_name).place(x= 155, y= 135)
    CTkEntry(register_screen, textvariable= temp_age).place(x= 155, y= 175)
    CTkEntry(register_screen, textvariable= temp_gender).place(x= 155, y= 215)
    CTkEntry(register_screen, textvariable= temp_password, show = "*").place(x= 155, y= 255)
    CTkButton(register_screen, text = "Register", command = finish_reg, font = ("Georgia", 14)).place(x=155, y= 325)
    
    
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    print(all_accounts)
    
    if name == "" or age == "" or gender == "" or password == "":
        notif.configure(text_color= 'red', text = 'All fields required')
        return 
    
    for name_check in all_accounts:
        if name == name_check:
            notif.configure(text_color="red", text="Account already exists")
            return
        else:
            with open(name, 'w') as new_file:
                new_file.write(name + '\n')
                new_file.write(password + '\n')
                new_file.write(age + '\n')
                new_file.write(gender+ '\n')
                new_file.write('0')
                new_file.close()
                notif.configure(text_color = 'green', text = "Account created succesfully\nGo to the login page")
                
                
    
    
def login():
    
    global temp_login_name, temp_login_password, login_notif, login_screen
    
    
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    
    #Login Screen
    login_screen = CTkToplevel(master)
    login_screen.geometry('500x500')
    login_screen.title("Login")
    #####################################
    
    #Labels
    login_prompt = CTkLabel(master = login_screen, text = "Please enter your credentials below to login", font = ('Georgia', 17))
    login_prompt.place(x= 70, y=110)
    
    
    username_label = CTkLabel(master = login_screen, text = "Username: ", font = ('Georgia', 15))
    username_label.place(x= 100, y= 155)
    
    user_password_label = CTkLabel(master = login_screen, text = "Password: ", font = ('Georgia', 15))
    user_password_label.place(x= 108, y= 195)
    
   
    login_notif = CTkLabel(master = login_screen, text='', font = ('Georgia', 16))
    login_notif.place(x = 155, y = 340)
    
    
    #Entries
    CTkEntry(login_screen, textvariable= temp_login_name).place(x= 185, y= 155)
    CTkEntry(login_screen, textvariable= temp_login_password).place(x= 185, y= 195)
    
    CTkButton(login_screen, text = "Login", command = login_session, font = ("Georgia", 14)).place(x=155, y= 265)
    
    
    
def login_session():
    global login_name
    all_accounts= os.listdir()
    login_name = temp_login_name.get()
    login_password= temp_login_password.get()
    
    for name in all_accounts:
        if login_name == name:
            with open(name, 'r') as file:
                file_data = file.read()
                file_data = file_data.split('\n')
                password = file_data[1]
                
                #Account Dashboard
                if login_password == password:
                    login_screen.destroy()
                    account_dashboard = CTkToplevel(master)
                    account_dashboard.title('Dashboard')
                    account_dashboard.geometry('500x500')
                    
                    #Labels
                    CTkLabel(account_dashboard, text = "Account Dashboard", font=('Georgia', 22)).place(x= 153, y= 30)
                    CTkLabel(account_dashboard, text = "Welcome " + name, font=('Georgia', 14)).place(x= 200, y= 75)
                    
                    
                    #Buttons
                    CTkButton(account_dashboard, text = "Personal Details", font = ('Georgia', 16), width = 40, height = 30, command = personal_details).place(x= 185, y= 160)
                    CTkButton(account_dashboard, text = "Deposit", font = ('Georgia', 16), width = 40, height = 30, command = deposit).place(x= 215,y = 250)
                    CTkButton(account_dashboard, text = "Withdraw", font = ('Georgia', 16), width = 40, height = 30, command = withdraw).place(x= 207, y= 350)
                    
                    return 
                else:
                    login_notif.configure(text_color = "red", text='Invalid password')
                    
                return 
        
    login_notif.configure(text_color = "red", text='Invalid username')
    
def personal_details():
    print("personal details")
    
    #Vars
    file = open(login_name, 'r')
    file_data = file.read()
    user_details  = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]
    
    #Personal Details Screen
    personal_details_screen = CTkToplevel(master)
    personal_details_screen.geometry('500x500')
    
    personal_details_screen.title('Personal Details')
    
    #Labels
    CTkLabel(personal_details_screen, text = "Personal Details" , font = ('Georgia', 24)).place(x= 170, y= 50)
    CTkLabel(personal_details_screen, text = "Name: " + details_name, font = ('Georgia', 16)).place(x= 200, y= 140)
    CTkLabel(personal_details_screen, text = "Age: " + details_age, font = ('Georgia', 16)).place(x=200, y= 210)
    CTkLabel(personal_details_screen, text = "Gender: " + details_gender, font = ('Georgia', 16)).place(x=200, y= 280)
    CTkLabel(personal_details_screen, text = "Balance: $" + details_balance, font = ('Georgia', 16)).place(x=200, y= 350)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text = 'Amount is required!', fg = 'red')
        return 
    if float(amount.get()) <= 0:
        deposit_notif.config(text = "Negative currency is not accepted", fg = "red")
        return 
    
    file = open(login_name, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    current_balance_label.configure(text="Current Balance" + str(updated_balance), text_color = "green")
    deposit_notif.configure(text = "Balance Updated", text_color = "green")

    
    
def deposit():
    #Vars 
    global amount 
    global deposit_notif
    global current_balance_label
    
    amount = StringVar()
    
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    
    #Deposit Screen
    
    deposit_screen = CTkToplevel(master)
    deposit_screen.title('Deposit')
    
    #Label
    CTkLabel(deposit_screen, text = "Deposit", font = ('Calibri', 12)).grid(row=0, sticky = N , pady = 10)
    current_balance_label = CTkLabel(deposit_screen, text = "Current Balance: $" + details_balance, font = ('Calibri', 12))
    current_balance_label.grid(row=1, sticky = W)
    
    CTkLabel(deposit_screen, text = "Amount: ", font = ('Calibri', 12)).grid(row=2, sticky = W)
    deposit_notif = CTkLabel(deposit_screen, font = ('Calibri', 12))
    deposit_notif.grid(row=4, sticky = N, pady= 5)
    
    #Entry
    CTkEntry(deposit_screen, textvariable = amount ).grid(row=2, column = 1)
    
    #Button
    CTkButton(deposit_screen, text ="Finish", font = ('Calibri', 12), command = finish_deposit).grid(row=3, sticky = W, pady = 5)
    

def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text = 'Amount is required!', fg = 'red')
        return 
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text = "Negative currency is not accepted", fg = "red")
        return 
    
    file = open(login_name, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    
    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text = "Insuffiecient Funds!", fg= "red")
        return 
        
        
    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    current_balance_label.configure(text="Current Balance" + str(updated_balance), text_color = "green")
    withdraw_notif.configure(text = "Balance Updated", text_color = "green")
    
    
    
def withdraw():
    global withdraw_amount 
    global withdraw_notif
    global current_balance_label
    
    withdraw_amount = StringVar()
    
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    
    #Deposit Screen
    
    withdraw_screen = CTkToplevel(master)
    withdraw_screen.title('Withdraw')
    
    #Label
    CTkLabel(withdraw_screen, text = "Withdraw", font = ('Calibri', 12)).grid(row=0, sticky = N , pady = 10)
    current_balance_label = CTkLabel(withdraw_screen, text = "Current Balance: $" + details_balance, font = ('Calibri', 12))
    current_balance_label.grid(row=1, sticky = W)
    
    CTkLabel(withdraw_screen, text = "Amount: ", font = ('Calibri', 12)).grid(row=2, sticky = W)
    withdraw_notif = CTkLabel(withdraw_screen, font = ('Calibri', 12))
    withdraw_notif.grid(row=4, sticky = N, pady= 5)
    
    #Entry
    CTkEntry(withdraw_screen, textvariable = withdraw_amount ).grid(row=2, column = 1)
    
    #Button
    CTkButton(withdraw_screen, text ="Finish", font = ('Calibri', 12), command = finish_withdraw).grid(row=3, sticky = W, pady = 5)
    

master = CTk()
master.title("Banking App")
master.geometry('500x500')


#Labels
CTkLabel(master, text = "Custom Baking Beta", font = ('Georgia', 35)).place(x=110, y=100)
CTkLabel(master, text = "The most secure bank you've ever used (NOT)", font = ('Georgia', 15)).place(x=110, y=150)


#Buttons
CTkButton(master, text = "Register", font = ('Georgia', 18), width = 120, height = 40, command = register).place(x=185, y=220)
CTkButton(master, text = "Login", font = ('Calibri', 18), width = 120, height= 40, command = login).place(x=185,y=300)



master.mainloop()