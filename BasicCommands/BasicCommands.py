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
    \n\t\t\t\t\t1.Show Date
    \n\t\t\t\t\t2.Show Cal
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
