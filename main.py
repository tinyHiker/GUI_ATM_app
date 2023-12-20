from tkinter import *
import os
from PIL import ImageTk, Image

#Main Screen
master = Tk()
master.title("Banking App")


def login_session():
    all_accounts= os.listdir()
    login_name = temp_login_name.get()
    login_password= temp_login_password.get()
    
    for name in all_accounts:
        if login_name == name:
            with open(name, 'r') as file:
                file_data = file.read()
                file_data = file_data.split('\n')
                password= file_data[1]
                
                #Account Dashboard
                if login_password == password:
                    login_screen.destroy()
                    account_dashboard = Toplevel(master)
                    account_dashboard.title('Dashboard')
                    
                    #Labels
                    Label(account_dashboard, text = "Account Dashboard", font=('Calibri', 12)).grid(row=0, sticky = N, pady =10) # TIMESTAMP: 32:37 VID 2
                else:
                    login_notif.config(fg='red', text='Invalid password')
                    
                return 
        
    login_notif.config(fg='red', text='Invalid username')
    
            
            
            
            
    

def login():
    
    global temp_login_name, temp_login_password, login_notif, login_screen
    
    
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title("Login")
    
    #Labels
    Label(login_screen, text = "Login to your account", font = ('Calibri', 12)).grid(row=0, sticky=N, pady = 10 )
    Label(login_screen, text = "Username", font = ('Calibri', 12)).grid(row=1, sticky=W, pady=10)
    Label(login_screen, text = "Password", font = ('Calibri', 12)).grid(row=2, sticky=W, pady=10)
    login_notif = Label(login_screen, text= '',  font = ('Calibri', 12))
    login_notif.grid(row=4, sticky = N)
    
    #Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_password, show='*').grid(row=2, column=1, padx=5)
    
    #Button
    Button(login_screen, text="Login", command = login_session, width=15, font = ('Calibri', 12)).grid(row=3, sticky=W, pady=5, padx=5)

def finish_reg():
    print('done')
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    print(all_accounts)
    
    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg= 'red', text = 'All fields required')
        return 
    
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exists")
            return
        else:
            with open(name, 'w') as new_file:
                new_file.write(name + '\n')
                new_file.write(password + '\n')
                new_file.write(age + '\n')
                new_file.write(gender+ '\n')
                new_file.write('0')
                new_file.close()
                notif.config(fg = 'green', text = "Account created succesfully")
    
def register():
    
    # Vars
    global temp_name, temp_age, temp_gender, temp_password, notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    
    register_screen = Toplevel(master)
    register_screen.title('Register')
    
    #Labels
    Label(master = register_screen, text = "Please enter your details below to register", font = ('Calibri', 12)).grid(row = 0, sticky = N, pady= 10)
    Label(master = register_screen, text = "Name", font = ('Calibri', 12)).grid(row =1, sticky = W)
    Label(master = register_screen, text = "Age", font = ('Calibri', 12)).grid(row =2, sticky = W)
    Label(master = register_screen, text = "Gender", font = ('Calibri', 12)).grid(row =3, sticky = W)
    Label(master = register_screen, text = "Password", font = ('Calibri', 12)).grid(row =4, sticky = W)
    notif = Label(master = register_screen, text='', font = ('Calibri', 12))
    notif.grid(row = 6, sticky = N, pady =10)
    
    #Entires 
    Entry(register_screen, textvariable= temp_name).grid(row=1, column = 0 )
    Entry(register_screen, textvariable= temp_age).grid(row=2, column = 0 )
    Entry(register_screen, textvariable= temp_gender).grid(row=3, column = 0 )
    Entry(register_screen, textvariable= temp_password, show = "*").grid(row=4, column = 0 )
    
    Button(register_screen, text = "Register", command = finish_reg, font = ("Calibri", 12)).grid(row=5, sticky = N, pady=10)
    
#Image import 
img = Image.open('secure.jpg')
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text = "Custom Baking Beta", font = ('Calibri', 14)).grid(row=0, sticky = N, pady = 10)
Label(master, text = "the most secure bank you've probably used", font = ('Calibri', 12)).grid(row=1, sticky = N)
Label(master, image = img).grid(row=2, sticky = N, pady=15)

#Buttons
Button(master, text = "Register", font = ('Calibri', 12), width = 20, command = register).grid(row=3, sticky =N)
Button(master, text = "Login", font = ('Calibri', 12), width = 20, command = login).grid(row=4, sticky =N, pady= 10)



master.mainloop()