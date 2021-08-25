def Webserver(): 
    import os
    from subprocess import getstatusoutput
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")
    os.system("tput setaf 10")
    name = "\"  \t\t\t\t          LINUX TERMINAL USER INTERFACE\""
    os.system("echo {0} | figlet -f wideterm -d ./fonts/".format(name))
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")

    os.system("tput setaf 11")
    print("\n\t\t\t\t..........................WEBSERVER MENU.............................")
    os.system("tput setaf 6")
    
    print("""
    \n\t\t\t\t1.Check httpd installed or not  \t\t\t\t2.Install HTTPD
    \n\t\t\t\t3.Httpd Service Status          \t\t\t\t4.Start httpd Service 
    \n\t\t\t\t5.Stop httpd service            \t\t\t\t6.restart httpd Service 
    \n\t\t\t\t7.Enable httpd service          \t\t\t\t8.Disable httpd Service
    \n""")
    
    os.system("tput setaf 7")
    print("\t\t\t\t\tEnter 0 to terminate \t Enter -1 return to main menu\n")
    os.system("tput setaf 2")
    choice = int(input("Select the Option : "))
    os.system("tput setaf 7")
    
    if(choice==0):
        exit()
    elif(choice==1):
        package=getstatusoutput("rpm -q httpd")
        if package[0] == 0:
            print("Package httpd is already Installed\tPackage is - {}".format(package[1]))
        else:
            print("Package httpd is not installed")
    elif(choice==2):
        package=getstatusoutput("rpm -q httpd")
        if package[0] == 0:
            print("Package httpd is already Installed\tPackage is - {}".format(package[1]))
        else:
             print("wait httpd package is installing")     
             package=getstatusoutput("yum install httpd -y >> /dev/null")
    elif(choice==3):
        os.system("sudo systemctl status httpd")
    elif(choice==4):
        os.system("sudo systemctl start httpd")
    elif(choice==5):
         os.system("sudo systemctl stop httpd")
    elif(choice==6):
         os.system("sudo systemctl restart httpd")
    elif(choice==7):
         os.system("sudo systemctl enable httpd")
    elif(choice==8):
         os.system("sudo systemctl disable httpd")
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
   Webserver()
