# Class Example

import tkinter as tk
#from PIL import Image, ImageTk
import dbFunctions as db

def getFormInformation(connObj):
    firstName = ent_FirstName.get()
    lastName = ent_LastName.get()
    phoneNumber = ent_PhoneNumber.get()

    ent_FirstName.delete(0,tk.END)
    ent_LastName.delete(0,tk.END)
    ent_PhoneNumber.delete(0,tk.END)

    # result = '{} {}\n{}'.format(firstName, lastName, phoneNumber)

    # lbl_Result = tk.Label(text=result, master=root)
    # lbl_Result.grid(row=4, sticky='n', columnspan=2, padx=5, pady=5)

    if firstName != '':
        userInfo = lastName, firstName, phoneNumber

        db.addUser(connObj, userInfo)

        users = db.getAllUsers(connObj)

        result = ''

        for user in users:
            result += '{} {} {}\n'.format(user[2], user[1], user[3])
        
        lbl_Result = tk.Label(text=result, master=root) 
        lbl_Result.grid(row=4, sticky='n', columnspan=2, padx=5, pady=5)

# Start of Program

dbFilePath = "users.db"
connObj = db.setupTable(dbFilePath)

if connObj is not None:
    db.createTable(connObj)
else:
    print("Error: DB connection unable to be established.")

root  = tk.Tk()

root.geometry("{}x{}".format(250,250))

root.title('Example Form')

# Image Handling
# path = 'flower.jpg'
# scalingFactor = .4
# loadImg = Image.open(path)
# width, height = loadImg.size
# loadImg = loadImg.resize( ( int(width * scalingFactor), int(height * scalingFactor) ), Image.ANTIALIAS)
# img = ImageTk.PhotoImage(loadImg)
# lbl_Image = tk.Label(master=root, image=img)


lbl_FirstName = tk.Label(text="First Name", master=root)
ent_FirstName = tk.Entry(master=root)

lbl_LastName = tk.Label(text="Last Name", master=root)
ent_LastName = tk.Entry(master=root)

lbl_PhoneNumber = tk.Label(text="Phone Number", master=root)
ent_PhoneNumber = tk.Entry(master=root)

btn_Submit = tk.Button(text="Submit", relief=tk.RAISED, command= lambda: getFormInformation(connObj))

lbl_FirstName.grid(row=0, column=0, sticky='w', padx=5, pady=5)
ent_FirstName.grid(row=0, column=1, sticky='w', padx=5, pady=5)

lbl_LastName.grid(row=1, column=0, sticky='w', padx=5, pady=5)
ent_LastName.grid(row=1, column=1, sticky='w', padx=5, pady=5)

lbl_PhoneNumber.grid(row=2, column=0, sticky='w', padx=5, pady=5)
ent_PhoneNumber.grid(row=2, column=1, sticky='w', padx=5, pady=5)

btn_Submit.grid(row=3, sticky='n', columnspan=2, padx=5, pady=5)

# lbl_Image.grid(row=5, columnspan=2, padx=5, pady=5)

root.mainloop()