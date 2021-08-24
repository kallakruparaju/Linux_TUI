def BasicCommands(): 
    import os
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")
    os.system("tput setaf 10")
    name = "\"  \t\t\t\t          LINUX TERMINAL USER INTERFACE\""
    os.system("echo {0} | figlet -f wideterm -d ./fonts/".format(name))
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")

    os.system("tput setaf 11")
    print("\n\t\t\t\t..........................BASIC COMMANDS MENU.............................")
    os.system("tput setaf 6")
    
    print("""
    \n\t\t\t\t\t1.Show Date                  \t\t\t2.Show Cal
    \n\t\t\t\t\t3.Show manual of the command \t\t\t4.Show Free Memory
    \n\t\t\t\t\t5.Show Network card          \t\t\t6.Show mounted disks
    \n\t\t\t\t\t7.Show uptime                \t\t\t8.Check user
    \n""")
    
    os.system("tput setaf 7")
    print("\t\t\t\t\tEnter 0 to terminate \t Enter -1 return to main menu\n")
    os.system("tput setaf 2")
    choice = int(input("Select the Option : "))
    os.system("tput setaf 7")
    if(choice==0):
        exit()
    elif(choice==1):
        print()
        os.system("date")
    elif(choice==2):
        print()
        os.system("cal")
    elif(choice==3):    
        cmd = str(input("\nEnter the command: "))
        os.system("man {}".format(cmd))
    elif(choice==4):
        print()
        os.system("free -m")
    elif(choice==5):
        print()
        os.system("ifconfig")
    elif(choice==6):
        print()
        os.system("df -h")
    elif(choice==7):
        print()
        os.system("uptime")
    elif(choice==8):
        print()
        os.system("whoami")
    elif(choice== -1):
        os.system("clear")
        import main
        main.main()
    else:
        print("You Entered Wrong Choice ...")
    os.system("tput setaf 11")
    c=input("\nPress Enter: The Screen will be cleared")
    os.system("clear")
    
while True:
    BasicCommands()
