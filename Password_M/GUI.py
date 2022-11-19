
import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import backend as backend


#*******************************PAWNED API CHECK***********************


#****************************PASSWORD GENERATOR****************************

def generate_password():
    #function of generating password
    letters=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]

    numbers=['1','2','3','4','5','6','7','8','9','0']
    symbols=['@','#','$','*','?','|','%','+','=','_']

  
    password_letters=[ choice(letters) for _ in range(randint(8,10))]
     
    password_numbers=[choice(numbers) for _ in range(randint(2,4))] 
   
    password_symbols=[choice(symbols) for _ in range(randint(2,4))]
    password_list= password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password="".join(password_list)

    new_password_entry.insert(0,password)
    pyperclip.copy(password)

#**********************************FIND PASSWORD************************************

def find_password():
    
    website= website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data= json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
        
    else:
        if website in data:
            password= data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    
    
#**********************************SAVE************************************

def save():
    #Function save the password and the website name of the Json File
    website= website_entry.get()    
    new_password= new_password_entry.get()
    
    new_data={
        website:{
            
            "Password": new_password
        }
    }
    is_ok = messagebox.askokcancel(title=website, message=f"These are details enter:\nWebsite: {website}\n Password: {new_password}\n Is it ok to save?")
    
    if len(website)==0 or len(new_password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    
    elif is_ok:
        try:
            with open("data.json", "r") as data_file:
                data=json.load(data_file)
    
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:  
            data.update(new_data)       
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
           
        finally:   
            website_entry.delete(0,END)
            new_password_entry.delete(0,END)
            
    
        
#------------------------------------GUI------------------------------------
#Creating UserInterface window
window= Tk()
window.title("Password Manager")
window.config(padx=150, pady=150,background="#B1DDC6")

#Creating containers for the image
canvas = Canvas(height=300, width=300,background="#B1DDC6", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150,150,image=logo_img)
canvas.grid(row=0, column=1)

#--------------------------------Label---------------------------
#Creating the label on the interface
password_label = Label(text="Password",background="#B1DDC6",highlightthickness=0)
new_password_label= Label(text="New Password",background="#B1DDC6",highlightthickness=0)
website_label= Label(text="Website",background="#B1DDC6",highlightthickness=0)

website_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)
new_password_label.grid(row=3, column=0)


#-----------------------------Entry---------------------------
#Creating the different entry
website_entry= Entry(width=35,highlightthickness=0)
password_entry= Entry(width=35,highlightthickness=0)
new_password_entry= Entry(width=35,highlightthickness=0)

website_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)
new_password_entry.grid(row=3, column= 1)

#--------------------Button----------------------

#Creating the different Button

search_button = Button(text="Search", width=21,highlightthickness=0 ,command=find_password)
generate_password = Button(text="Generate Password",highlightthickness=0 ,width=21,command=generate_password)
password_check_button= Button(text="Password Check", width=21,highlightthickness=0,command=lambda:backend.main(password_entry.get()))
add_button = Button(text="Add",width=36 ,highlightthickness=0,command=save)


search_button.grid(row=1, column=2)
generate_password.grid(row=3, column=2)
add_button.grid(row=4, column=1,columnspan=2)
password_check_button.grid(row=2, column=2)





window.mainloop()
