def Services(): 
    import os
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")
    os.system("tput setaf 10")
    name = "\"  \t\t\t\t          LINUX TERMINAL USER INTERFACE\""
    os.system("echo {0} | figlet -f wideterm -d ./fonts/".format(name))
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")

    os.system("tput setaf 11")
    print("\n\t\t\t\t..........................SERVICES MENU.............................")
    os.system("tput setaf 6")
    
    print("""
    \n\t\t\t\t1.Show all services          \t\t\t\t2.Start Service
    \n\t\t\t\t3.Show Status of the Service \t\t\t\t4.Restart Service
    \n\t\t\t\t5.Enable Service             \t\t\t\t6.Disable Service
    \n\t\t\t\t7.Reload Service             \t\t\t\t8.Stop Service
    \n""")
    
    os.system("tput setaf 7")
    print("\t\t\t\t\tEnter 0 to terminate \t Enter -1 return to main menu\n")
    os.system("tput setaf 2")
    choice = int(input("Select the Option : "))
    os.system("tput setaf 7")
    
    if(choice==0):
        exit()
    elif(choice==1):
        os.system("systemctl -a")
    elif(choice==2):
        name = str(input("\nEnter Service Name: "))
        os.system("systemctl start {}".format(name))
    elif(choice==3):
        name = str(input("\nEnter Service Name: "))
        os.system("systemctl status {}".format(name))
    elif(choice==4):
        name = str(input("\nEnter Service Name: "))
        os.system("systemctl restart {}".format(name))
    elif(choice==5):
        name = str(input("\nEnter Service Name: "))
        os.system("systemctl enable {}".format(name))
    elif(choice==6):
        name = str(input("\nEnter Service Name: "))
        os.system("systemctl disable {}".format(name))
    elif(choice==7):
        name = str(input("\nEnter Service Name: "))
        os.system("systemctl reload {}".format(name))
    elif(choice==8):
        name = str(input("\nEnter Service Name: "))
        os.system("systemctl stop {}".format(name))
    elif(choice==-1):
        os.system("clear")
        import main
        main.main()
    else:
        print("You Entered Wrong Choice ...")
    os.system("tput setaf 11")
    c=input("\nPress Enter: The Screen will be cleared")
    os.system("clear")


while True:
   Services()
