def Files(): 
    import os
    import subprocess
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")
    os.system("tput setaf 10")
    name = "\"  \t\t\t\t          LINUX TERMINAL USER INTERFACE\""
    os.system("echo {0} | figlet -f wideterm -d ./fonts/".format(name))
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")

    os.system("tput setaf 11")
    print("\n\t\t\t\t..........................FILES MENU.............................")
    os.system("tput setaf 6")
    
    print("""
    \n\t\t\t\t1.Show all Files                 \t\t2.Check file exists or not
    \n\t\t\t\t3.Create Empty file              \t\t4.Create Folder
    \n\t\t\t\t5.Read data in the file          \t\t6.Add data in the file
    \n\t\t\t\t7.Copy file to another folder    \t\t8.Move file to another folder
    \n\t\t\t\t9.Remove file                    \t\t10.Remove Folder
    \n\t\t\t\t11.Store output of the command   \t\t12.Copy data from one file to another
    \n""")
    
    os.system("tput setaf 7")
    print("\t\t\t\t\tEnter 0 to terminate \t Enter -1 return to main menu\n")
    os.system("tput setaf 2")
    choice = int(input("Select the Option : "))
    os.system("tput setaf 7")
    
    if(choice==0):
        exit()
    elif(choice==1):
        os.system("ls -alh")
    elif(choice==2):
        filename = str(input("\nEnter File Name: "))
        test=subprocess.getoutput("ls {}".format(filename))
        exitcode=subprocess.getoutput("echo $?")
        if(exitcode==0):
           print("\nFile Existed")
        else:
           print("\nFile not Existed")
    elif(choice==3):
        filename = str(input("\nEnter File Name:: "))
        os.system("touch {}".format(filename))
    elif(choice==4):
        foldername = str(input("\nEnter Folder Name: "))
        test=subprocess.getoutput("mkdir {}".format(foldername))
        exitcode=subprocess.getoutput("echo $?")
        if(exitcode==0):
           print("folder created successfully")
        else:
           print("folder already existed")
    elif(choice==5):
        filename = str(input("\nEnter File Name: "))
        os.system("cat {}".format(filename))
    elif(choice==6):
        print("""\n1.To add data in the file (Note: if file exists old data overwrite)
                 \n2.Append the data in the file
                 \n""")
        os.system("tput setaf 2")
        option = int(input("Select the Option : "))
        filename = str(input("\nEnter File Name: "))
        if(option==1):
              os.system("cat > {}".format(filename))
        elif(option==2):
              os.system("cat >> {}".format(filename))
        else:
              print("Please select correct option")
    elif(choice==7):
        filename = str(input("\nEnter file Name: "))
        foldername = str(input("\nEnter Folder Name: "))
        subprocess.getoutput("cp {} {}".format(filename,foldername))
        exitcode=subprocess.getoutput("echo $?")
        if(exitcode==0):
           print("file copied successfully")
    elif(choice==8):
        filename = str(input("\nEnter file Name: "))
        foldername = str(input("\nEnter Folder Name: "))
        subprocess.getoutput("mv {} {}".format(filename,foldername))
        exitcode=subprocess.getoutput("echo $?")
        if(exitcode==0):
           print("file moved successfully")
    elif(choice==9):
        filename = str(input("\nEnter file Name: "))
        os.system("rm {}".format(filename))
    elif(choice==10):
        foldername = str(input("\nEnter Folder Name: "))
        os.system("rm -rf {}".format(foldername))
    elif(choice==11):
        cmd = str(input("\nEnter the command: "))
        filename = str(input("\nEnter file Name: "))
        os.system("{} > {}".format(cmd,filename))
    elif(choice==12):
        filename1 = str(input("\nEnter file Name from where to: "))
        filename1 = str(input("\nEnter file Name to copy the copied data: "))
        os.system("cat < {} > {} ".format(filename1,filename2))
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
   Files()
