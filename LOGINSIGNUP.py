import json

user1=input("Do you wants to do login or signup:")

def signup():
    
    detalis={}
    
    details1={}
    
    detalis_list=[]

    first_name=input("enter your first_name >>___")

    last_name=input("enter your last_name   >>___")
    
    password=input("enter your new password >>___")
    
    capitel_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    number="0123456789"

    special_charecter="@#₹&!*$%¢€£©®"
    
    if len(password)>=8:

        veriable1=0

        veriable2=0

        veriable3=0
        
        for i in range(len(password)):

            if password[i] in capitel_letter:

                veriable1+=1

            elif password[i] in number:

                veriable2+=1

            elif password[i] in special_charecter:

                veriable3+=1
        
        if   veriable1>=1 and veriable2>=1 and veriable3>=1:

            confirm_password=input("enter your confirm password >>___")

            if password==confirm_password:

                detalis["Firstname"]=first_name

                detalis["Lastname"]=last_name
                
                detalis["Password"]=password
                
                with open("all_information.json","a+") as file:

                    json.dump(detalis,file,indent=4)

                    detalis_list.append(detalis)

                    details1["users"]=detalis

                    print(f"Congratulation {first_name}  your sing up is Successfull ")
                
            else:
                print("Passwords do not match")
        else:
            print("The password should contain at least one special character and one number")
    else:
        print("please enter 8 digit password")

def login():
    
    my_file=open("all_information.json","r")  
    
    file_read=my_file.read()

    user_name = input("enter user name >>____")

    password=input("enter your password >>____")

    if user_name in file_read:

        if password in file_read:
            print("your login is successfull")
            
        else:
            print("please enter your correct passwors")
            
    else:
        print("You need to sign up first. Your password is incorrect")

        signup()

def login_signup():

    if user1=="signup":
        signup()

    else:
        login()

login_signup()   