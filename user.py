class User:
    def __init__(self, name):
        
        with open(name, 'r') as file:
            file_data = file.read()
            user_details  = file_data.split('\n')
            
        self.name = user_details[0]
        self.age = int(user_details[2])
        self.gender = user_details[3]
        self.balance = float(user_details[4])
    
    def update_balance(self, deposit):
        self.balance += deposit 
        
        with open(self.name, "r+") as file:
            file_data = file.read()
            details = file_data.split('\n')
            current_balance = details[4]
            updated_balance = str(self.balance)
            file_data = file_data.replace(current_balance, updated_balance)
            file.seek(0)
            file.truncate(0)
            file.write(file_data)
            file.close()
            
        return self.balance
            
    def withdraw(self, amount):
        self.balance -= amount
        
        with open(self.name, "r+") as file:
            file_data = file.read()
            details = file_data.split('\n')
            current_balance = details[4]
            updated_balance = str(self.balance)
            file_data = file_data.replace(current_balance, updated_balance)
            file.seek(0)
            file.truncate(0)
            file.write(file_data)
            file.close()
            
        return self.balance
        
        
    
        
        
        
        