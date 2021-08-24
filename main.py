def main():
    import os
    os.system("clear")
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")
    os.system("tput setaf 10")
    name = "\"  \t\t\t\t          LINUX TERMINAL USER INTERFACE\""
    os.system("echo {0} | figlet -f wideterm -d ./fonts/".format(name))
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")

    os.system("tput setaf 11")
    print("\n\t\t\t\t..........................MAIN MENU..........................")
    os.system("tput setaf 6")
    print("""
    \n\t\t\t\t\t1.Basic Linux commands
    \n\t\t\t\t\t2.Services
    \n""")
    os.system("tput setaf 7")
    print("\n\t\t\t\t\tEnter 0 to terminate \n")
    os.system("tput setaf 2")
    choice = int(input("Select the Option : "))
    os.system("tput setaf 7")
    if(choice==0):
        exit()
    elif(choice==1):
        os.system("clear")
        from BasicCommands import BasicCommands
        BasicCommands.BasicCommands()
    elif(choice==2):
        os.system("clear")
        from Services import Services
        Services.Services()
    else : 
        print("Enter the correct option..")
if __name__ == "__main__":
    main()
