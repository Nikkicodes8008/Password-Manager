import random
import string
import json
import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox
from pathlib import Path

listbox_data={}
def GRP():
    var_upper = tk.BooleanVar()
    var_lower = tk.BooleanVar()
    var_special = tk.BooleanVar()
    var_numbers = tk.BooleanVar()

    new_window=Toplevel(window)
    new_window.title("Generate Random Password")
    new_window.geometry("600x300")
    
    frame1=tk.Frame(new_window)
    frame1.pack(pady=10)

    desc=tk.Label(frame1,text="Platform")
    desc.pack(side=tk.LEFT)

    dese=tk.Entry(frame1,width=30)
    dese.pack(side=tk.RIGHT,padx=10)

    frame2=tk.Frame(new_window)
    frame2.pack(pady=10)

    usr=tk.Label(frame2,text="Username")
    usr.pack(side=tk.LEFT)
    
    usre=tk.Entry(frame2,width=30)
    usre.pack(side=tk.RIGHT,padx=10)
    
    frame3=tk.Frame(new_window)
    frame3.pack(pady=10)

    len=tk.Label(frame3,text="Length of Password")
    len.pack(side=tk.LEFT)
    
    lene=tk.Entry(frame3,width=30)
    lene.pack(side=tk.RIGHT,padx=10)


    frame4=tk.Frame(new_window)
    frame4.pack(expand=True,fill=tk.X)

    cb_upper = tk.Checkbutton(frame4, text="Include uppercase letters", variable=var_upper)
    cb_upper.pack(side=tk.LEFT)

    cb_lower = tk.Checkbutton(frame4, text="Include lowercase letters", variable=var_lower)
    cb_lower.pack(side=tk.LEFT)

    cb_special = tk.Checkbutton(frame4, text="Include special characters", variable=var_special)
    cb_special.pack(side=tk.LEFT)

    cb_numbers = tk.Checkbutton(frame4, text="Include digits", variable=var_numbers)
    cb_numbers.pack(side=tk.LEFT)


    generate=tk.Button(new_window,text="Generate Password",command=lambda: password_generator(usre.get(), dese.get(), lene.get(),
                                                     passwe,var_lower.get(),var_numbers.get(),var_special.get(),var_upper.get()))
    generate.pack(pady=10)

    frame5=tk.Frame(new_window)
    frame5.pack(pady=10)

    passw=tk.Label(frame5,text="Password: ")
    passw.pack(pady=10,side=tk.LEFT)

    passwe=tk.Label(frame5,text="")
    passwe.pack(side=tk.LEFT,padx=10)

def password_generator(usre,dese,lene,passwe,var_lower,var_numbers,var_special,var_upper):
    if dese:
        description=dese.strip()
    else:
        messagebox.showerror("Error","Enter a Platform in Platform field")
        return
    
    if usre:
        username=usre.strip()
    else:
        messagebox.showerror("Error","Enter a username in username field")
        return
    try:
        length=int(lene.strip())
    except ValueError:
        messagebox.showerror("Error","Enter a number in length field")
        return

    if length < 4:
        messagebox.showwarning("Warning","Password length too small")
        return
    
    pool=""
    LOWER_CASE=string.ascii_lowercase
    UPPER_CASE=string.ascii_uppercase
    SPECIAL_CHAR=string.punctuation
    DIGITS=string.digits
    password=[]
    len_pass=0
    if var_lower:
        password.append(random.choice(LOWER_CASE))
        len_pass+=1
        pool+=LOWER_CASE     
    if var_upper:
        password.append(random.choice(UPPER_CASE))
        len_pass+=1
        pool+=UPPER_CASE
    if var_special:
        password.append(random.choice(SPECIAL_CHAR))
        len_pass+=1
        pool+=SPECIAL_CHAR
    if var_numbers:
        password.append(random.choice(DIGITS))
        len_pass+=1
        pool+=DIGITS
    if pool=="":
        messagebox.showwarning("Warning you did not select any characters")
        return

    for _ in range (length-len_pass):
        password.append(random.choice(pool))
 
    random.shuffle(password)
 
    str_password="".join(password)

    usr_pass={username:str_password}

    data[description]=usr_pass
    with file_path.open("w") as f:
        json.dump(data,f,indent=4)

    passwe.config(text=str_password)

def VSP():
    new_window=Toplevel(window)
    new_window.title("Stored Passwords")
    msg=tk.Listbox(new_window,width=100)
    msg.pack(pady=10,expand=True,fill=tk.BOTH)
    output=""
    for description, creds in data.items():
        for username, password in creds.items():
            item_text=f"Platform: {description}    |   Username: {username}    |   Password: {password}"
            msg.insert(tk.END, f"Platform: {description}    |   Username: {username}    |   Password: {password}")
            listbox_data[item_text]=description

    del_cred=tk.Button(new_window,text="Delete Credential",command=lambda:DCL(msg))
    del_cred.pack(pady=10)

def SEC():
    new_window=Toplevel(window)
    new_window.title("Save Existing Credentials")
    new_window.geometry("600x300")

    frame1=tk.Frame(new_window)
    frame1.pack(pady=10)

    desc=tk.Label(frame1,text="Platform")
    desc.pack(side=tk.LEFT)

    dese=tk.Entry(frame1,width=30)
    dese.pack(side=tk.RIGHT,padx=10)

    frame2=tk.Frame(new_window)
    frame2.pack(pady=10)

    usr=tk.Label(frame2,text="Username")
    usr.pack(side=tk.LEFT)
    
    usre=tk.Entry(frame2,width=30)
    usre.pack(side=tk.RIGHT,padx=10)
    
    frame3=tk.Frame(new_window)
    frame3.pack(pady=10)

    passl=tk.Label(frame3,text="Password")
    passl.pack(side=tk.LEFT)
    
    passe=tk.Entry(frame3,width=30)
    passe.pack(side=tk.RIGHT,padx=10)

    save=tk.Button(new_window,text="Save",command=lambda:save_existing_credentials(usre.get(),dese.get(),passe.get(),new_window))
    save.pack(pady=10)
    
def save_existing_credentials(usre,dese,passe,new_window):
    description=dese.strip()
    username=usre.strip()
    password=passe.strip()

    if description and username and password:
        usr_pass={username:password}
        data[description]=usr_pass
        try:
            with file_path.open("w") as f:
                json.dump(data,f,indent=4)
            messagebox.showinfo("Success","Credentials Saved Successfully")
            new_window.destroy()
        except Exception as e:
            messagebox.showerror("Failure",f"Unable to save credentials \nError {e}")
    else:
        messagebox.showerror("Warning","Please enter all 3 fields before submitting")
        return   
def DCL(msg):
    try:
        ind=msg.curselection()[0]
        selected_text = msg.get(ind)
        description = listbox_data[selected_text]
        del data[description]
        msg.delete(ind)
        with file_path.open("w") as f:
            json.dump(data,f,indent=4)
    except Exception as e:
        messagebox.showerror("Error",f"You got an Error:{e}")

def DAP():
    data.clear()
    try:
        with file_path.open("w") as f:
            json.dump(data,f,indent=4)
        messagebox.showinfo("Success", "All the saved credentials have been successfully deleted")
    except Exception as e:
        messagebox.showerror("Failure",f"Error occured {e}")

window=tk.Tk()
window.title("Nikhil's Password Manager")
window.geometry("400x300")

data={}
file_path = Path(__file__).parent /"passwords.json"

try:
    with file_path.open("r") as f:
        data=json.load(f)
except:
    messagebox.showwarning("Error","Unable to load Passwords.json file")

Header=tk.Label(window,text="Nikhil's Password Manager",font=("arial",18))
Header.pack(pady=10)

frame=tk.Frame(window)
frame.pack(pady=10,expand=True,fill=tk.BOTH)

GenRanPass=tk.Button(frame,text="Generate Random Password",command=GRP)
GenRanPass.pack(pady=10,expand=True,fill=tk.BOTH)

ViewStoredpass=tk.Button(frame,text="View Stored Passwords",command=VSP)
ViewStoredpass.pack(pady=10,expand=True,fill=tk.BOTH)

SaveExiistPasss=tk.Button(window,text="Save Existing Credentials",command=SEC)
SaveExiistPasss.pack(pady=10,expand=True,fill=tk.BOTH)

Del_all_pass=tk.Button(window,text="Delete all saved credentials",command=DAP)
Del_all_pass.pack(pady=10,expand=True,fill=tk.BOTH)

window.mainloop()