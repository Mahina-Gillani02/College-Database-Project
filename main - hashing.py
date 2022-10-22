from tkinter import *
from tkinter import ttk
import sqlite3

database_connection = sqlite3.connect("chemist.db")
database_cursor = database_connection.cursor()

global_username = ""
global_role = ""

def login():
    login_window = Tk()
    login_window.title("Medinet")
    login_window.configure(bg="#439817") 

    title_label = Label(login_window, text="Login",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)

    username_label = Label(login_window,bg="#439817",fg="white",font=("Cambria", 14), text="Username:")
    username_label.grid(row=1, column=0)
    username_entry = Entry(login_window)
    username_entry.grid(row=1, column=1)
    
    password_label = Label(login_window,bg="#439817",fg="white",font=("Cambria", 14), text="Password:")
    password_label.grid(row=2, column=0)
    password_entry = Entry(login_window,show="*")
    password_entry.grid(row=2, column=1)

    enter_button = Button(login_window,text="Enter",width="10",height="1",bg="#398214",fg="white",font=("Cambria", 14),command = lambda:login_submit(username_entry.get(),password_entry.get(),login_window))
    enter_button.grid(row=3, column=0, padx=5, pady=5)

    login_window.mainloop()

def login_submit(username,password,login_window):
    global global_username
    global global_role

    full_list = ""
    ascii_password = [ord(c) for c in password]
    password_list = [str(item) for item in ascii_password]
    for item in password_list:
        full_list += item
    hashed_password = int(full_list)%4409

    database_cursor.execute("SELECT * FROM Employees WHERE Username = '%s' AND HashedPassword = '%s'" % (username,hashed_password))
    matchingUsers = database_cursor.fetchall()

    if len(matchingUsers) == 0:
        notification("Username and/or password incorrect")
    else:
        global_username = username
        global_role = matchingUsers[0][8]
        login_window.destroy()
        main_menu()
        
def main_menu():

    global global_role
    
    main_window = Tk()
    main_window.title("Medinet")
    main_window.configure(bg="#439817")

    title_label = Label(main_window, text="Main Menu",bg="#439817",fg="white", font=("Cambria", 30))
    title_label.grid(row=0, column=0, columnspan = 5)

    employees_label = Label(main_window, text="Employees",bg="#439817",fg="white", font=("Cambria", 15))
    employees_label.grid(row=1, column=0)

    patients_label = Label(main_window, text="Patients",bg="#439817",fg="white", font=("Cambria", 15))
    patients_label.grid(row=1, column=1)

    prescriptions_label = Label(main_window, text="Prescriptions",bg="#439817",fg="white", font=("Cambria", 15))
    prescriptions_label.grid(row=1, column=2)

    stock_label = Label(main_window, text="Stock",bg="#439817",fg="white", font=("Cambria", 15))
    stock_label.grid(row=1, column=3)

    personal_label = Label(main_window, text="Personal",bg="#439817",fg="white", font=("Cambria", 15))
    personal_label.grid(row=1, column=4)

    view_employees_button = Button(main_window,text="View Employees",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),view_employees()])
    view_employees_button.grid(row=2, column=0, padx=5, pady=5)

    view_patients_button = Button(main_window,text="View Patients",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),view_patients()])
    view_patients_button.grid(row=2, column=1, padx=5, pady=5)

    view_stock_button = Button(main_window,text="View Stock",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),view_stock()])
    view_stock_button.grid(row=2, column=3, padx=5, pady=5)

    view_deliveries_button = Button(main_window,text="View Deliveries",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),view_deliveries()])
    view_deliveries_button.grid(row=2, column=2, padx=5, pady=5)

    add_employee_button = Button(main_window,text="Add Employee",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),add_employee()])
    add_employee_button.grid(row=3, column=0, padx=5, pady=5)

    delete_employee_button = Button(main_window,text="Delete Employee",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),delete_employee()])
    delete_employee_button.grid(row=5, column=0, padx=5, pady=5)
    
    quit_button = Button(main_window,text="Quit",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = main_window.destroy)
    quit_button.grid(row=5, column=4, padx=5, pady=5)

    add_patient_button = Button(main_window,text="Add Patient",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),add_patient()])
    add_patient_button.grid(row=3, column=1, padx=5, pady=5)

    delete_patient_button = Button(main_window,text="Delete Patient",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),delete_patient()])
    delete_patient_button.grid(row=5, column=1, padx=5, pady=5)

    update_patient_button = Button(main_window,text="Update Patient",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),update_patient()])
    update_patient_button.grid(row=4, column=1, padx=5, pady=5)

    update_stock_button = Button(main_window,text="Update Stock",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),update_stock()])
    update_stock_button.grid(row=3, column=3, padx=5, pady=5)

    view_my_information_button = Button(main_window,text="View My Information",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),view_my_information()])
    view_my_information_button.grid(row=2, column=4, padx=5, pady=5)

    create_prescription_button = Button(main_window,text="Create Prescription",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),create_prescription()])
    create_prescription_button.grid(row=3, column=2, padx=5, pady=5)

    update_password_button = Button(main_window,text="Update Password",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),update_password()])
    update_password_button.grid(row=3, column=4, padx=5, pady=5)

    delete_prescription_button = Button(main_window,text="Delete Prescription",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),delete_prescription()])
    delete_prescription_button.grid(row=4, column=2, padx=5, pady=5)

    update_employee_button = Button(main_window,text="Update Employee",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),update_employee()])
    update_employee_button.grid(row=4, column=0, padx=5, pady=5)
    
    if global_role == "Employee":

        add_employee_button = Button(main_window,text="Add Employee",state="disabled",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),add_employee()])
        add_employee_button.grid(row=3, column=0, padx=5, pady=5)

        view_employees_button = Button(main_window,text="View Employees",state="disabled",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),view_employees()])
        view_employees_button.grid(row=2, column=0, padx=5, pady=5)

        delete_employee_button = Button(main_window,text="Delete Employee",state="disabled",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),delete_employee()])
        delete_employee_button.grid(row=5, column=0, padx=5, pady=5)

        update_employee_button = Button(main_window,text="Update Employee",state="disabled",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[main_window.destroy(),update_employee()])
        update_employee_button.grid(row=4, column=0, padx=5, pady=5)
        
    main_window.mainloop()

def update_password():
    update_password_window = Tk()
    update_password_window.title("Medinet")
    update_password_window.configure(bg="#439817")

    update_password_title_label = Label(update_password_window,bg="#439817",fg="white", text="Update Password", font=("Cambria", 20))
    update_password_title_label.grid(row=0, column=0, columnspan = 2)

    old_password_title_label = Label(update_password_window,bg="#439817",fg="white",font=("Cambria", 14), text="Old Password")
    old_password_title_label.grid(row=1, column=0)
    old_password_entry = Entry(update_password_window)
    old_password_entry.grid(row=1, column=1)

    new_password_title_label = Label(update_password_window,bg="#439817",fg="white",font=("Cambria", 14), text="New Password")
    new_password_title_label.grid(row=2, column=0)
    new_password_entry = Entry(update_password_window)
    new_password_entry.grid(row=2, column=1)

    confirm_new_password_title_label = Label(update_password_window,bg="#439817",fg="white",font=("Cambria", 14), text="Confirm New Password")
    confirm_new_password_title_label.grid(row=3, column=0)
    confirm_new_password_entry = Entry(update_password_window)
    confirm_new_password_entry.grid(row=3, column=1)

    update_button = Button(update_password_window,text="Update",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:update_password_submit(old_password_entry.get(),
                                                                                                                                                   new_password_entry.get(),
                                                                                                                                                   confirm_new_password_entry.get(),
                                                                                                                                                   update_password_window))
    update_button.grid(row=4, column=0, padx=5, pady=5)

    close_button = Button(update_password_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[update_password_window.destroy(),main_menu()])
    close_button.grid(row=4, column=1, padx=5, pady=5)

    update_password_window.mainloop()

def update_password_submit(old_password_entry,new_password_entry,confirm_new_password_entry,update_password_window):
    global global_username

    if new_password_entry != confirm_new_password_entry:
        notification("New passwords don't match")
    else:
        with database_connection:
            database_cursor.execute("SELECT Password From Employees WHERE Username = '%s'" % (global_username))
            same_users_list = database_cursor.fetchall()
            same_users = same_users_list[0][0]
        if same_users != old_password_entry:
            notification("Old password doesn't match")
        else:
            full_list = ""
            ascii_password = [ord(c) for c in confirm_new_password_entry]
            password_list = [str(item) for item in ascii_password]
            for item in password_list:
                full_list += item
            hashed_password = int(full_list)%4409

            with database_connection:
                database_cursor.execute("UPDATE Employees SET Password = '%s', HashedPassword = %s WHERE Username = '%s'" % (confirm_new_password_entry,hashed_password,global_username))
                database_connection.commit()
                notification("Password updated")
                update_password_window.destroy()
                main_menu()
                
def view_employees():
    employee_window = Tk()
    employee_window.title("Medinet")
    employee_window.configure(bg="#439817")
    
    with database_connection:
        database_cursor.execute("SELECT * FROM Employees")
        employees_list = database_cursor.fetchall()

    view_employees_title_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 20), text="View Employees")
    view_employees_title_label.grid(row=0, column=0, columnspan=7)

    employee_ID_title_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="EmployeeID")
    employee_ID_title_label.grid(row=1, column=0)
    
    first_name_title_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="First Name")
    first_name_title_label.grid(row=1, column=1)

    surname_title_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Surname")
    surname_title_label.grid(row=1, column=2)

    date_of_birth_title_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Date of Birth")
    date_of_birth_title_label.grid(row=1, column=3)

    address_title_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Address")
    address_title_label.grid(row=1, column=4)

    postcode_title_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Postcode")
    postcode_title_label.grid(row=1, column=5)

    role_title_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Role")
    role_title_label.grid(row=1, column=6)

    for index, employee_member in enumerate(employees_list):        

        employee_ID_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[0])
        employee_ID_label.grid(row=index+2, column=0)

        first_name_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[1])
        first_name_label.grid(row=index+2, column=1)

        surname_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[2])
        surname_label.grid(row=index+2, column=2)

        date_of_birth_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[3])
        date_of_birth_label.grid(row=index+2, column=3)

        address_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[4])
        address_label.grid(row=index+2, column=4)

        postcode_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[5])
        postcode_label.grid(row=index+2, column=5)

        role_label = Label(employee_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[8])
        role_label.grid(row=index+2, column=6)

    close_button = Button(employee_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[employee_window.destroy(),main_menu()])
    close_button.grid(row=len(employees_list)+2, column=5, columnspan = 2, padx=5, pady=5)

    employee_window.mainloop()
    
def view_patients():
    patient_window = Tk()
    patient_window.title("Medinet")
    patient_window.configure(bg="#439817")
    
    with database_connection:
        database_cursor.execute("SELECT * FROM Patients")
        patient_list = database_cursor.fetchall()

    view_patients_title_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 20), text="View Patients")
    view_patients_title_label.grid(row=0, column=0, columnspan=6)

    patient_ID_title_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="PatientID")
    patient_ID_title_label.grid(row=1, column=0)

    first_name_title_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="First Name")
    first_name_title_label.grid(row=1, column=1)

    surname_title_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Surname")
    surname_title_label.grid(row=1, column=2)

    date_of_birth_title_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Date of Birth")
    date_of_birth_title_label.grid(row=1, column=3)

    address_title_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Address")
    address_title_label.grid(row=1, column=4)

    postcode_title_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Postcode")
    postcode_title_label.grid(row=1, column=5)

    for index, patient_member in enumerate(patient_list):        

        patient_ID_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 12), text=patient_member[0])
        patient_ID_label.grid(row=index+2, column=0)

        first_name_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 12), text=patient_member[1])
        first_name_label.grid(row=index+2, column=1)

        surname_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 12), text=patient_member[2])
        surname_label.grid(row=index+2, column=2)

        date_of_birth_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 12), text=patient_member[3])
        date_of_birth_label.grid(row=index+2, column=3)

        address_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 12), text=patient_member[4])
        address_label.grid(row=index+2, column=4)

        postcode_label = Label(patient_window,bg="#439817",fg="white",font=("Cambria", 12), text=patient_member[5])
        postcode_label.grid(row=index+2, column=5)

    close_button = Button(patient_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[patient_window.destroy(),main_menu()])
    close_button.grid(row=len(patient_list)+2, column=5, columnspan = 1, padx=5, pady=5)

    patient_window.mainloop()
    
def add_patient():
    add_patient_window = Tk()
    add_patient_window.title("Medinet")
    add_patient_window.configure(bg="#439817")

    title_label = Label(add_patient_window, text="Add Patient",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)
    
    first_name_label = Label(add_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="First Name")
    first_name_label.grid(row=1, column=0)
    first_name_entry = Entry(add_patient_window)
    first_name_entry.grid(row=1, column=1)

    surname_label = Label(add_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Surname")
    surname_label.grid(row=2, column=0)
    surname_entry = Entry(add_patient_window)
    surname_entry.grid(row=2, column=1)

    date_of_birth_label = Label(add_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Date of Birth")
    date_of_birth_label.grid(row=3, column=0)
    date_of_birth_entry = Entry(add_patient_window)
    date_of_birth_entry.grid(row=3, column=1)

    address_label = Label(add_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Address")
    address_label.grid(row=4, column=0)
    address_entry = Entry(add_patient_window)
    address_entry.grid(row=4, column=1)

    postcode_label = Label(add_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Postcode")
    postcode_label.grid(row=5, column=0)
    postcode_entry = Entry(add_patient_window)
    postcode_entry.grid(row=5, column=1)
    
    submit_button = Button(add_patient_window,text="Submit",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:add_patient_submit(first_name_entry.get(),
                                                                                                                                             surname_entry.get(),
                                                                                                                                             date_of_birth_entry.get(),
                                                                                                                                             address_entry.get(),
                                                                                                                                             postcode_entry.get(),
                                                                                                                                             add_patient_window))
    submit_button.grid(row=6, column=0, padx=5, pady=5)
    
    close_button = Button(add_patient_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[add_patient_window.destroy(),main_menu()])
    close_button.grid(row=6, column=1, padx=5, pady=5)

    add_patient_window.mainloop()

def add_patient_submit(first_name,surname,date_of_birth,address,postcode,add_patient_window):

    if first_name == "":
        notification("Please enter your first name")
    elif surname == "":
        notification("Please enter your surname")
    elif date_of_birth == "":
        notification("Please enter your date of birth")
    elif address == "":
        notification("Please enter your address")
    elif postcode == "":
        notification("Please enter your postcode")
    else:
        with database_connection:
            sqlStatement = "INSERT INTO Patients (PatientFirstName,PatientSurname,PatientDateOfBirth,PatientAddress,PatientPostcode) VALUES ('%s','%s','%s','%s','%s')" % (first_name,
                                                                                                                                                                           surname,
                                                                                                                                                                           date_of_birth,
                                                                                                                                                                           address,
                                                                                                                                                                           postcode)
            database_cursor.execute(sqlStatement)
            database_connection.commit()
            notification("Patient added to the database")
            add_patient_window.destroy()
            main_menu()

def delete_patient():
    delete_patient_window = Tk()
    delete_patient_window.title("Medinet")
    delete_patient_window.configure(bg="#439817")

    title_label = Label(delete_patient_window, text="Delete Patient",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)

    with database_connection:
        database_cursor.execute("SELECT * FROM Patients")
        matching_patients = database_cursor.fetchall()

    patient_ids = []
    patient_options = []

    for patient in matching_patients:
        patient_ids.append(patient[0])
        patient_options.append(patient[1])

    patient_combobox = ttk.Combobox(delete_patient_window,values=patient_options)
    patient_combobox.grid(row=1,column=1)

    picking_patient_label = Label(delete_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick a patient")
    picking_patient_label.grid(row=1,column=0)

    delete_button = Button(delete_patient_window,text="Delete",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:delete_patient_submit(patient_combobox.current(),patient_ids,delete_patient_window))
    delete_button.grid(row=2, column=0, padx=5, pady=5)

    close_button = Button(delete_patient_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[delete_patient_window.destroy(),main_menu()])
    close_button.grid(row=2, column=1, padx=5, pady=5)

    delete_patient_window.mainloop()

def delete_patient_submit(combobox_position,patient_ids,delete_patient_window):

        deleting_patient = patient_ids[combobox_position]

        with database_connection:
            database_cursor.execute("DELETE FROM Patients WHERE PatientID = '%s'" % (deleting_patient))
            notification("Patient deleted")
            database_connection.commit()
            delete_patient_window.destroy()
            main_menu()
            
def update_patient():
    update_patient_window = Tk()
    update_patient_window.title("Medinet")
    update_patient_window.configure(bg="#439817")
    
    title_label = Label(update_patient_window, text="Update Patient",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)

    with database_connection:
        database_cursor.execute("SELECT * FROM Patients")
        matching_patients = database_cursor.fetchall()

    patient_ids = []
    patient_options = []

    for patient in matching_patients:
        patient_ids.append(patient[0])
        patient_options.append(patient[1])

    patient_combobox = ttk.Combobox(update_patient_window,values=patient_options)
    patient_combobox.grid(row=1,column=1)

    picking_patient_label = Label(update_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick a patient")
    picking_patient_label.grid(row=1,column=0)

    first_name_label = Label(update_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="First Name")
    first_name_label.grid(row=2, column=0)
    first_name_entry = Entry(update_patient_window)
    first_name_entry.grid(row=2, column=1)

    surname_label = Label(update_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Surname")
    surname_label.grid(row=3, column=0)
    surname_entry = Entry(update_patient_window)
    surname_entry.grid(row=3, column=1)

    date_of_birth_label = Label(update_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Date of Birth")
    date_of_birth_label.grid(row=4, column=0)
    date_of_birth_entry = Entry(update_patient_window)
    date_of_birth_entry.grid(row=4, column=1)

    address_label = Label(update_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Address")
    address_label.grid(row=5, column=0)
    address_text = Text(update_patient_window,height=3,width=15,wrap=WORD)
    address_text.grid(row=5, column=1)

    postcode_label = Label(update_patient_window,bg="#439817",fg="white",font=("Cambria", 14), text="Postcode")
    postcode_label.grid(row=6, column=0)
    postcode_entry = Entry(update_patient_window)
    postcode_entry.grid(row=6, column=1)

    patient_combobox.bind("<<ComboboxSelected>>", lambda event, arg=(patient_combobox,patient_ids,first_name_entry,surname_entry,date_of_birth_entry,address_text,postcode_entry): edit_patient_combobox_change(event, arg))    

    update_button = Button(update_patient_window,text="Update",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:update_patient_submit(patient_combobox.current(),
                                                                                                                                                   patient_ids,
                                                                                                                                                   first_name_entry.get(),
                                                                                                                                                   surname_entry.get(),
                                                                                                                                                   date_of_birth_entry.get(),
                                                                                                                                                   address_text.get(),
                                                                                                                                                   postcode_entry.get(),
                                                                                                                                                   update_patient_window))
    update_button.grid(row=7, column=0, padx=5, pady=5)

    close_button = Button(update_patient_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[update_patient_window.destroy(),main_menu()])
    close_button.grid(row=7, column=1, padx=5, pady=5)

    update_patient_window.mainloop()

def edit_patient_combobox_change(event, arg):
    patient_combobox = arg[0]
    patient_ids = arg[1]
    first_name_entry = arg[2]
    surname_entry = arg[3]
    date_of_birth_entry = arg[4]
    address_text = arg[5]
    postcode_entry = arg[6]

    first_name_entry.delete(0,END)
    surname_entry.delete(0,END)
    date_of_birth_entry.delete(0,END)
    address_text.delete('1.0',END)
    postcode_entry.delete(0,END)
    
    selected_row = patient_combobox.current()
    selected_id = patient_ids[selected_row]

    with database_connection:
        database_cursor.execute("SELECT * FROM Patients WHERE PatientID = '%s'" % selected_id)
        matching_patient = database_cursor.fetchall()
        
    first_name_entry.insert(0,matching_patient[0][1])
    surname_entry.insert(0,matching_patient[0][2])
    date_of_birth_entry.insert(0,matching_patient[0][3])
    address_text.insert('1.0',matching_patient[0][4])
    postcode_entry.insert(0,matching_patient[0][5])
    
def update_patient_submit(combobox_position,patient_ids,first_name,surname,date_of_birth,address,postcode,update_patient_window):
     
    selected_patient = patient_ids[combobox_position]

    with database_connection:
        database_cursor.execute("UPDATE Patients SET PatientFirstName = '%s',PatientSurname = '%s', PatientDateOfBirth = '%s', PatientAddress = '%s', PatientPostcode = '%s' WHERE PatientID = %s" % (first_name,surname,date_of_birth,address,postcode,selected_patient))
        database_connection.commit()
        notification("Patient updated")
        update_patient_window.destroy()
        main_menu()

def view_stock():
    medicine_window = Tk()
    medicine_window.title("Medinet")
    medicine_window.configure(bg="#439817")

    with database_connection:
        database_cursor.execute("SELECT * FROM Medicine")
        medicine_list = database_cursor.fetchall()

    view_stock_title_label = Label(medicine_window,bg="#439817",fg="white",font=("Cambria", 20), text="View Stock")
    view_stock_title_label.grid(row=0, column=0, columnspan=3)

    medicine_ID_title_label = Label(medicine_window,bg="#439817",fg="white",font=("Cambria", 14), text="MedicineID")
    medicine_ID_title_label.grid(row=1, column=0)

    medicine_name_title_label = Label(medicine_window,bg="#439817",fg="white",font=("Cambria", 14), text="Medicine Name")
    medicine_name_title_label.grid(row=1, column=1)

    boxes_title_label = Label(medicine_window,bg="#439817",fg="white",font=("Cambria", 14), text="Boxes")
    boxes_title_label.grid(row=1, column=2)

    for index, medicine_item in enumerate(medicine_list):        

        medicine_ID_label = Label(medicine_window,bg="#439817",fg="white",font=("Cambria", 12), text=medicine_item[0])
        medicine_ID_label.grid(row=index+2, column=0)

        medicine_name_label = Label(medicine_window,bg="#439817",fg="white",font=("Cambria", 12), text=medicine_item[1])
        medicine_name_label.grid(row=index+2, column=1)

        boxes_label = Label(medicine_window,bg="#439817",fg="white",font=("Cambria", 12), text=medicine_item[2])
        boxes_label.grid(row=index+2, column=2)
        
    close_button = Button(medicine_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[medicine_window.destroy(),main_menu()])
    close_button.grid(row=len(medicine_list)+2, column=0, columnspan = 2, padx=5, pady=5)

    medicine_window.mainloop()

def add_employee():
    add_employee_window = Tk()
    add_employee_window.title("Medinet")
    add_employee_window.configure(bg="#439817")

    title_label = Label(add_employee_window, text="Add Employee",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)
    
    first_name_label = Label(add_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="First Name")
    first_name_label.grid(row=1, column=0)
    first_name_entry = Entry(add_employee_window)
    first_name_entry.grid(row=1, column=1)

    surname_label = Label(add_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Surname")
    surname_label.grid(row=2, column=0)
    surname_entry = Entry(add_employee_window)
    surname_entry.grid(row=2, column=1)

    date_of_birth_label = Label(add_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Date of Birth")
    date_of_birth_label.grid(row=3, column=0)
    date_of_birth_entry = Entry(add_employee_window)
    date_of_birth_entry.grid(row=3, column=1)

    address_label = Label(add_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Address")
    address_label.grid(row=4, column=0)
    address_entry = Entry(add_employee_window)
    address_entry.grid(row=4, column=1)

    postcode_label = Label(add_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Postcode")
    postcode_label.grid(row=5, column=0)
    postcode_entry = Entry(add_employee_window)
    postcode_entry.grid(row=5, column=1)

    username_label = Label(add_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Username")
    username_label.grid(row=6, column=0)
    username_entry = Entry(add_employee_window)
    username_entry.grid(row=6, column=1)

    password_label = Label(add_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Password")
    password_label.grid(row=7, column=0)
    password_entry = Entry(add_employee_window, show="*")
    password_entry.grid(row=7, column=1)
    
    role_label = Label(add_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Role")
    role_label.grid(row=8, column=0)
    role_variable = StringVar()
    role_variable.set("Pick a role")
    role_options = ["Employee","Manager"]
    role_menu = OptionMenu(add_employee_window,role_variable,*role_options)
    role_menu.grid(row=8, column=1)
    
    submit_button = Button(add_employee_window,text="Submit",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:add_employee_submit(first_name_entry.get(),
                                                                                                                                             surname_entry.get(),
                                                                                                                                             date_of_birth_entry.get(),
                                                                                                                                             address_entry.get(),
                                                                                                                                             postcode_entry.get(),
                                                                                                                                             username_entry.get(),
                                                                                                                                             password_entry.get(),
                                                                                                                                             role_variable.get(),
                                                                                                                                             add_employee_window))
    submit_button.grid(row=9, column=0, padx=5, pady=5)
    
    close_button = Button(add_employee_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[add_employee_window.destroy(),main_menu()])
    close_button.grid(row=9, column=1, padx=5, pady=5)

    add_employee_window.mainloop()

def add_employee_submit(first_name,surname,date_of_birth,address,postcode,username,password,role,add_employee_window):

    if first_name == "":
        notification("Please enter your first name")
    elif surname == "":
        notification("Please enter your surname")
    elif date_of_birth == "":
        notification("Please enter your date of birth")
    elif address == "":
        notification("Please enter your address")
    elif postcode == "":
        notification("Please enter your postcode")
    elif username == "":
        notification("Please enter your username")
    elif password == "":
        notification("Please enter your password")
    elif role == "":
        notification("Please pick your role")
    else:############################
        full_list = ""
        ascii_password = [ord(c) for c in password]
        password_list = [str(item) for item in ascii_password]
        for item in password_list:
            full_list += item
        hashed_password = int(full_list)%4409
        with database_connection:
            sqlStatement = "INSERT INTO Employees (FirstName,Surname,DateOfBirth,Address,Postcode,Username,Password,Role,HashedPassword) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',%s)" % (first_name,
                                                                                                                                                                               surname,
                                                                                                                                                                               date_of_birth,
                                                                                                                                                                               address,
                                                                                                                                                                               postcode,
                                                                                                                                                                               username,
                                                                                                                                                                               password,
                                                                                                                                                                               role,
                                                                                                                                                                               hashed_password)
            database_cursor.execute(sqlStatement)
            database_connection.commit()
            notification("Employee added to the database")
            add_employee_window.destroy()
            main_menu()

def delete_employee():
    delete_employee_window = Tk()
    delete_employee_window.title("Medinet")
    delete_employee_window.configure(bg="#439817")

    title_label = Label(delete_employee_window, text="Delete Employee",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)

    with database_connection:
        database_cursor.execute("SELECT * FROM Employees")
        matching_employees = database_cursor.fetchall()

    employee_ids = []
    employee_options = []

    for employee in matching_employees:
        employee_ids.append(employee[0])
        employee_options.append(employee[1])

    employee_combobox = ttk.Combobox(delete_employee_window,values=employee_options)
    employee_combobox.grid(row=1,column=1)

    picking_employee_label = Label(delete_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick an employee")
    picking_employee_label.grid(row=1,column=0)

    delete_button = Button(delete_employee_window,text="Delete",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:delete_employee_submit(employee_combobox.current(),employee_ids,delete_employee_window))
    delete_button.grid(row=2, column=0, padx=5, pady=5)

    close_button = Button(delete_employee_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[delete_employee_window.destroy(),main_menu()])
    close_button.grid(row=2, column=1, padx=5, pady=5)

    delete_employee_window.mainloop()

def delete_employee_submit(combobox_position,employee_ids,delete_employee_window):

        deleting_employee = employee_ids[combobox_position]

        with database_connection:
            database_cursor.execute("DELETE FROM Employees WHERE EmployeeID = '%s'" % (deleting_employee))
            notification("Employee deleted")
            database_connection.commit()
            delete_employee_window.destroy()
            main_menu()
           
def update_employee():
    update_employee_window = Tk()
    update_employee_window.title("Medinet")
    update_employee_window.configure(bg="#439817")
    
    title_label = Label(update_employee_window, text="Update Employee",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)

    with database_connection:
        database_cursor.execute("SELECT * FROM Employees")
        matching_employees = database_cursor.fetchall()

    employee_ids = []
    employee_options = []

    for employee in matching_employees:
        employee_ids.append(employee[0])
        employee_options.append(employee[1])

    employee_combobox = ttk.Combobox(update_employee_window,values=employee_options)
    employee_combobox.grid(row=1,column=1)

    picking_employee_label = Label(update_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick an employee")
    picking_employee_label.grid(row=1,column=0)

    first_name_label = Label(update_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="First Name")
    first_name_label.grid(row=2, column=0)
    first_name_entry = Entry(update_employee_window)
    first_name_entry.grid(row=2, column=1)

    surname_label = Label(update_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Surname")
    surname_label.grid(row=3, column=0)
    surname_entry = Entry(update_employee_window)
    surname_entry.grid(row=3, column=1)

    date_of_birth_label = Label(update_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Date of Birth")
    date_of_birth_label.grid(row=4, column=0)
    date_of_birth_entry = Entry(update_employee_window)
    date_of_birth_entry.grid(row=4, column=1)

    address_label = Label(update_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Address")
    address_label.grid(row=5, column=0)
    address_text = Text(update_employee_window,height=3,width=15,wrap=WORD)
    address_text.grid(row=5, column=1)

    postcode_label = Label(update_employee_window,bg="#439817",fg="white",font=("Cambria", 14), text="Postcode")
    postcode_label.grid(row=6, column=0)
    postcode_entry = Entry(update_employee_window)
    postcode_entry.grid(row=6, column=1)

    employee_combobox.bind("<<ComboboxSelected>>", lambda event, arg=(employee_combobox,employee_ids,first_name_entry,surname_entry,date_of_birth_entry,address_text,postcode_entry): edit_employee_combobox_change(event, arg))    

    update_button = Button(update_employee_window,text="Update",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:update_employee_submit(employee_combobox.current(),
                                                                                                                                                   employee_ids,
                                                                                                                                                   first_name_entry.get(),
                                                                                                                                                   surname_entry.get(),
                                                                                                                                                   date_of_birth_entry.get(),
                                                                                                                                                   address_text.get(),
                                                                                                                                                   postcode_entry.get(),
                                                                                                                                                   update_employee_window))
    update_button.grid(row=7, column=0, padx=5, pady=5)

    close_button = Button(update_employee_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[update_employee_window.destroy(),main_menu()])
    close_button.grid(row=7, column=1, padx=5, pady=5)

    update_employee_window.mainloop()

def edit_employee_combobox_change(event, arg):

    employee_combobox = arg[0]
    employee_ids = arg[1]
    first_name_entry = arg[2]
    surname_entry = arg[3]
    date_of_birth_entry = arg[4]
    address_text = arg[5]
    postcode_entry = arg[6]

    first_name_entry.delete(0,END)
    surname_entry.delete(0,END)
    date_of_birth_entry.delete(0,END)
    address_text.delete('1.0',END)
    postcode_entry.delete(0,END)
    
    selected_row = employee_combobox.current()
    selected_id = employee_ids[selected_row]
    
    with database_connection:
        database_cursor.execute("SELECT * FROM Employees WHERE EmployeeID = '%s'" % selected_id)
        matching_employee = database_cursor.fetchall()
    
    first_name_entry.insert(0,matching_employee[0][1])
    surname_entry.insert(0,matching_employee[0][2])
    date_of_birth_entry.insert(0,matching_employee[0][3])
    address_text.insert('1.0',matching_employee[0][4])
    postcode_entry.insert(0,matching_employee[0][5])
    
def update_employee_submit(combobox_position,employee_ids,first_name,surname,date_of_birth,address,postcode,update_employee_window):
     
    selected_employee = employee_ids[combobox_position]

    with database_connection:
        database_cursor.execute("UPDATE Employees SET FirstName = '%s',Surname = '%s', DateOfBirth = '%s', Address = '%s', Postcode = '%s' WHERE EmployeeID = %s" % (first_name,surname,date_of_birth,address,postcode,selected_employee))
        database_connection.commit()
        notification("Employee updated")
        update_employee_window.destroy()
        main_menu()

def create_prescription():
    create_prescription_window = Tk()
    create_prescription_window.title("Medinet")
    create_prescription_window.configure(bg="#439817")

    title_label = Label(create_prescription_window, text="Create Prescription",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)
    
    with database_connection:
        database_cursor.execute("SELECT * FROM Patients")
        matching_patients = database_cursor.fetchall()

    patient_ids = []
    patient_options = []

    for patient in matching_patients:
        patient_name = patient[1] + " " + patient[2]
        patient_ids.append(patient[0])
        patient_options.append(patient_name)
    
    patient_combobox = ttk.Combobox(create_prescription_window,values=patient_options)
    patient_combobox.grid(row=1,column=1)

    picking_patient_label = Label(create_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick a patient")
    picking_patient_label.grid(row=1,column=0)

    with database_connection:
        database_cursor.execute("SELECT * FROM Medicine")
        medicine_list = database_cursor.fetchall()

    medicine_ids = []
    medicine_options = []

    for medicine in medicine_list:
        medicine_ids.append(medicine[0])
        medicine_options.append(medicine[1])

    medicine_combobox = ttk.Combobox(create_prescription_window,value=medicine_options)    
    medicine_combobox.grid(row=2,column=1)

    picking_medicine_label = Label(create_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick a medicine")
    picking_medicine_label.grid(row=2,column=0)
    
    medicine_quantity_label = Label(create_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Quantity")
    medicine_quantity_label.grid(row=3,column=0)
    medicine_quantity_entry = Entry(create_prescription_window)
    medicine_quantity_entry.grid(row=3,column=1)

    medicine_combobox2 = ttk.Combobox(create_prescription_window,value=medicine_options)
    medicine_combobox2.grid(row=4,column=1)

    picking_medicine_label2 = Label(create_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick a medicine")
    picking_medicine_label2.grid(row=4,column=0)
    
    medicine_quantity2_label = Label(create_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Quantity")
    medicine_quantity2_label.grid(row=5,column=0)
    medicine_quantity2_entry = Entry(create_prescription_window)
    medicine_quantity2_entry.grid(row=5,column=1)

    medicine_combobox3 = ttk.Combobox(create_prescription_window,value=medicine_options)
    medicine_combobox3.grid(row=6,column=1)

    picking_medicine_label3 = Label(create_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick a medicine")
    picking_medicine_label3.grid(row=6,column=0)

    medicine_quantity3_label = Label(create_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Quantity")
    medicine_quantity3_label.grid(row=7,column=0)
    medicine_quantity3_entry = Entry(create_prescription_window)
    medicine_quantity3_entry.grid(row=7,column=1)

    delivery_requested_label = Label(create_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Delivery Required?")
    delivery_requested_label.grid(row=8,column=0)
    deivery_requested_var = IntVar()
    delivery_checkbox = Checkbutton(create_prescription_window, variable=deivery_requested_var,bg="#439817")
    delivery_checkbox.grid(row=8,column=1)

    delivery_date_label = Label(create_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Delivery Date")
    delivery_date_label.grid(row=9,column=0)
    delivery_date_entry = Entry(create_prescription_window)
    delivery_date_entry.grid(row=9,column=1)

    submit_button = Button(create_prescription_window,text="Create Prescription",width="15",height="1",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:create_prescription_submit(medicine_quantity_entry.get(),
                                                                                                                                                                        medicine_quantity2_entry.get(),
                                                                                                                                                                        medicine_quantity3_entry.get(),
                                                                                                                                                                        patient_combobox.current(),
                                                                                                                                                                        medicine_combobox.current(),
                                                                                                                                                                        medicine_combobox2.current(),
                                                                                                                                                                        medicine_combobox3.current(),
                                                                                                                                                                        deivery_requested_var.get(),
                                                                                                                                                                        delivery_date_entry.get(),
                                                                                                                                                                        patient_ids,
                                                                                                                                                                        medicine_ids,
                                                                                                                                                                        create_prescription_window))
    submit_button.grid(row=10, column=0, padx=5, pady=5)
    
    cancel_button = Button(create_prescription_window,text="Cancel",width="10",height="1",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[create_prescription_window.destroy(),main_menu()])
    cancel_button.grid(row=10, column=1, padx=5, pady=5)

    create_prescription_window.mainloop()

def create_prescription_submit(medicine_quantity_entry,
                               medicine_quantity2_entry,
                               medicine_quantity3_entry,
                               patient_combobox_position,
                               combobox_position,
                               combobox_position2,
                               combobox_position3,
                               delivery_requested_var,
                               delivery_date_entry,
                               patient_ids,
                               medicine_ids,
                               create_prescription_window):
    if delivery_date_entry == "":
        notification("Please enter the delivery date")
    else:
        print(delivery_requested_var)

        print(patient_ids[patient_combobox_position])

        PatientID = patient_ids[patient_combobox_position]

        if delivery_requested_var == 1:
            delivery_requested = "y"
        else:
            delivery_requested = "n"
            
        with database_connection:
            sqlStatement = "INSERT INTO Prescriptions (PatientID,DeliveryRequested,DeliveryDate,Delivered) VALUES ('%s','%s','%s','n')" % (PatientID,delivery_requested,delivery_date_entry)
            database_cursor.execute(sqlStatement)
            database_connection.commit()

        with database_connection:
            sqlStatement = "SELECT MAX(PrescriptionID) FROM Prescriptions"
            database_cursor.execute(sqlStatement)
            max_ID_row = database_cursor.fetchone()
            max_ID = max_ID_row[0]

        if (medicine_quantity_entry != "") and (combobox_position != -1):
            MedicineID = medicine_ids[combobox_position]
            with database_connection:
                sqlStatement = "INSERT INTO PrescriptionItems (PrescriptionID,MedicineID,Boxes) VALUES ('%s','%s','%s')" % (max_ID,MedicineID,medicine_quantity_entry)
                database_cursor.execute(sqlStatement)
                database_connection.commit()
                
        if (medicine_quantity2_entry != "") and (combobox_position2 != -1):
            MedicineID2 = medicine_ids[combobox_position]
            with database_connection:
                sqlStatement = "INSERT INTO PrescriptionItems (PrescriptionID,MedicineID,Boxes) VALUES ('%s','%s','%s')" % (max_ID,MedicineID2,medicine_quantity2_entry)
                database_cursor.execute(sqlStatement)
                database_connection.commit()
                
        if (medicine_quantity3_entry != "") and (combobox_position3 != -1):
            MedicineID3 = medicine_ids[combobox_position]
            with database_connection:
                sqlStatement = "INSERT INTO PrescriptionItems (PrescriptionID,MedicineID,Boxes) VALUES ('%s','%s','%s')" % (max_ID,MedicineID3,medicine_quantity3_entry)
                database_cursor.execute(sqlStatement)
                database_connection.commit()

        notification("Prescription added to the database")
        create_prescription_window.destroy()
        main_menu()

def delete_prescription():
        delete_prescription_window = Tk()
        delete_prescription_window.title("Medinet")
        delete_prescription_window.configure(bg="#439817")

        title_label = Label(delete_prescription_window, text="Delete Prescription",bg="#439817",fg="white", font=("Cambria", 20))
        title_label.grid(row=0, column=0, columnspan = 2)
    
        with database_connection:
            database_cursor.execute("SELECT PrescriptionID, Patients.PatientID, PatientFirstName, PatientSurname FROM Prescriptions, Patients WHERE Prescriptions.PatientID = Patients.PatientID")
            matching_prescriptions = database_cursor.fetchall()

        prescription_names = []

        for prescription in matching_prescriptions:
            
            presciption_full_name = prescription[0],prescription[2],prescription[3]
            prescription_names.append(presciption_full_name)

        prescription_combobox = ttk.Combobox(delete_prescription_window,values=prescription_names)
        prescription_combobox.grid(row=1,column=1)

        picking_prescription_label = Label(delete_prescription_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick a prescription")
        picking_prescription_label.grid(row=1,column=0)

        delete_button = Button(delete_prescription_window,text="Delete",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:delete_prescription_submit(prescription_combobox.get(),delete_prescription_window))
        delete_button.grid(row=2, column=0, padx=5, pady=5)

        close_button = Button(delete_prescription_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[delete_prescription_window.destroy(),main_menu()])
        close_button.grid(row=2, column=1, padx=5, pady=5)

        delete_prescription_window.mainloop()

def delete_prescription_submit(combobox_value,delete_prescription_window):

    print(combobox_value)
    combobox_data_list = combobox_value.split()
    prescription_id = combobox_data_list[0]
    print(prescription_id)
    
    with database_connection:
        database_cursor.execute("DELETE FROM Prescriptions WHERE PrescriptionID = '%s'" % (prescription_id))
        
        database_cursor.execute("DELETE FROM PrescriptionItems WHERE PrescriptionID = '%s'" % (prescription_id))
        notification("Prescription deleted")
        database_connection.commit()
        delete_prescription_window.destroy()
        main_menu()
        
def view_my_information():
    view_my_information_window = Tk()
    view_my_information_window.title("Medinet")
    view_my_information_window.configure(bg="#439817")

    title_label = Label(view_my_information_window, text="View My Information",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 7)

    global global_username

    with database_connection:
            database_cursor.execute("SELECT * FROM Employees WHERE Username = '%s'" % (global_username))
            employees_list = database_cursor.fetchall()
            
    employee_ID_title_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 14), text="EmployeeID")
    employee_ID_title_label.grid(row=1, column=0)
    
    first_name_title_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 14), text="First Name")
    first_name_title_label.grid(row=1, column=1)

    surname_title_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 14), text="Surname")
    surname_title_label.grid(row=1, column=2)

    date_of_birth_title_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 14), text="Date of Birth")
    date_of_birth_title_label.grid(row=1, column=3)

    address_title_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 14), text="Address")
    address_title_label.grid(row=1, column=4)

    postcode_title_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 14), text="Postcode")
    postcode_title_label.grid(row=1, column=5)

    role_title_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 14), text="Role")
    role_title_label.grid(row=1, column=6)

    for index, employee_member in enumerate(employees_list):        

        employee_ID_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[0])
        employee_ID_label.grid(row=2, column=0)

        first_name_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[1])
        first_name_label.grid(row=2, column=1)

        surname_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[2])
        surname_label.grid(row=2, column=2)

        date_of_birth_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[3])
        date_of_birth_label.grid(row=2, column=3)

        address_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[4])
        address_label.grid(row=2, column=4)

        postcode_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[5])
        postcode_label.grid(row=2, column=5)

        role_label = Label(view_my_information_window,bg="#439817",fg="white",font=("Cambria", 12), text=employee_member[8])
        role_label.grid(row=2, column=6)

    close_button = Button(view_my_information_window,text="Close",width="20",height="2",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:[view_my_information_window.destroy(),main_menu()])
    close_button.grid(row=3, column=0, columnspan = 2, padx=5, pady=5)

    view_my_information_window.mainloop()

def update_stock():
    update_stock_window = Tk()
    update_stock_window.title("Medinet")
    update_stock_window.configure(bg="#439817")

    title_label = Label(update_stock_window, text="Update Stock",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)

    picking_medicine_label = Label(update_stock_window,bg="#439817",fg="white",font=("Cambria", 14), text="Pick a medicine")
    picking_medicine_label.grid(row=2,column=0)
    
    with database_connection:
        database_cursor.execute("SELECT * FROM Medicine")
        medicine_list = database_cursor.fetchall()

    medicine_ids = []
    medicine_options = []

    for medicine in medicine_list:
        medicine_ids.append(medicine[0])
        medicine_options.append(medicine[1])

    medicine_combobox = ttk.Combobox(update_stock_window,value=medicine_options)    
    medicine_combobox.grid(row=2,column=1)

    quantity_label = Label(update_stock_window,bg="#439817",fg="white",font=("Cambria", 14), text="Quantity")
    quantity_label.grid(row=3,column=0)
    quantity_entry = Entry(update_stock_window)
    quantity_entry.grid(row=3, column=1)

    medicine_combobox.bind("<<ComboboxSelected>>", lambda event, arg=(medicine_combobox,medicine_ids,quantity_entry): edit_medicine_combobox_change(event, arg))

    update_button = Button(update_stock_window,text="Update",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:update_stock_submit(medicine_combobox.current(),
                                                                                                                                                   medicine_ids,
                                                                                                                                                   quantity_entry.get(),
                                                                                                                                                   update_stock_window))
    update_button.grid(row=4, column=0, padx=5, pady=5)

    close_button = Button(update_stock_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[update_stock_window.destroy(),main_menu()])
    close_button.grid(row=4, column=1, columnspan = 2, padx=5, pady=5)

    update_stock_window.mainloop()
    
def edit_medicine_combobox_change(event, arg):

    medicine_combobox = arg[0]
    medicine_ids = arg[1]
    quantity_entry = arg[2]
    quantity_entry.delete(0,END)

    selected_row = medicine_combobox.current()
    selected_id = medicine_ids[selected_row]
    
    with database_connection:
        database_cursor.execute("SELECT * FROM Medicine WHERE MedicineID = '%s'" % selected_id)
        matching_medicine = database_cursor.fetchall()
    
    quantity_entry.insert(0,matching_medicine[0][2])

def update_stock_submit(combobox_position,medicine_ids,quantity,update_stock_window):

    selected_medicine = medicine_ids[combobox_position]

    with database_connection:
        database_cursor.execute("UPDATE Medicine SET Boxes = %s WHERE MedicineID = %s" % (quantity,selected_medicine))
        database_connection.commit()
        notification("Medicine updated")
        update_stock_window.destroy()
        main_menu()
        
def view_deliveries():
    view_deliveries_window = Tk()
    view_deliveries_window.title("Medinet")
    view_deliveries_window.configure(bg="#439817")

    title_label = Label(view_deliveries_window, text="View Deliveries",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 2)

    delivery_date_entry = Entry(view_deliveries_window)
    delivery_date_entry.grid(row=1, column=0)

    search_button = Button(view_deliveries_window,text="Search",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:view_deliveries_search(delivery_date_entry.get()))
    search_button.grid(row=1, column=1, padx=5, pady=5)

    close_button = Button(view_deliveries_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[view_deliveries_window.destroy(),main_menu()])
    close_button.grid(row=4, column=1, columnspan = 2, padx=5, pady=5)

    view_deliveries_window.mainloop()

def view_deliveries_search(delivery_date):
    if delivery_date == "":
        notification("Please enter a delivery date")
    else:
        with database_connection:
            database_cursor.execute("SELECT PatientFirstName, PatientSurname, PatientAddress, PrescriptionItems.Boxes, MedicineName FROM Prescriptions, PrescriptionItems, Patients, Medicine WHERE DeliveryDate = '%s' AND Prescriptions.PatientID = Patients.PatientID AND Prescriptions.PrescriptionID = PrescriptionItems.PrescriptionID AND PrescriptionItems.MedicineID = Medicine.MedicineID" % (delivery_date))
            matching_prescriptions = database_cursor.fetchall()
            if len(matching_prescriptions) == 0:
                notification("No delivery found")
            else:
                view_deliveries_list(matching_prescriptions)

def view_deliveries_list(matching_prescriptions):
    view_deliveries_list_window = Tk()
    view_deliveries_list_window.title("Medinet")
    view_deliveries_list_window.configure(bg="#439817")

    title_label = Label(view_deliveries_list_window, text="View Deliveries",bg="#439817",fg="white", font=("Cambria", 20))
    title_label.grid(row=0, column=0, columnspan = 5)

    first_name_title_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 14), text="First Name")
    first_name_title_label.grid(row=1, column=0)

    surname_title_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 14), text="Surname")
    surname_title_label.grid(row=1, column=1)

    address_title_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 14), text="Address")
    address_title_label.grid(row=1, column=2)

    medicine_title_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 14), text="Medicine")
    medicine_title_label.grid(row=1, column=3)

    boxes_title_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 14), text="Boxes")
    boxes_title_label.grid(row=1, column=4)

    for index, delivery in enumerate(matching_prescriptions):        

        first_name_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 12), text=delivery[0])
        first_name_label.grid(row=index+2, column=0)

        surname_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 12), text=delivery[1])
        surname_label.grid(row=index+2, column=1)

        address_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 12), text=delivery[2])
        address_label.grid(row=index+2, column=2)

        medicine_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 12), text=delivery[4])
        medicine_label.grid(row=index+2, column=3)

        boxes_label = Label(view_deliveries_list_window,bg="#439817",fg="white",font=("Cambria", 12), text=delivery[3])
        boxes_label.grid(row=index+2, column=4)
    
    close_button = Button(view_deliveries_list_window,text="Close",width="20",height="2",font=("Cambria", 14),bg="#398214",fg="white",command = lambda:[view_deliveries_list_window.destroy()])
    close_button.grid(row=len(matching_prescriptions)+2, column=3, columnspan = 2, padx=5, pady=5)

def notification(message):
    notification_window = Tk()
    notification_window.title("Medinet")
    notification_window.configure(bg="#439817")
    notification_label = Label(notification_window, text=message,bg="#439817",fg="white",font=("Cambria", 12))
    notification_label.grid(row=0, column=0)
    ok_button = Button(notification_window,text="OK",width="10",height="1",font=("Cambria", 12),bg="#398214",fg="white",command = lambda:notification_window.destroy())
    ok_button.grid(row=2, column=0, padx=5, pady=5)
    
login()
