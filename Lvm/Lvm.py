def Lvm(): 
    import os
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")
    os.system("tput setaf 10")
    name = "\"  \t\t\t\t          LINUX TERMINAL USER INTERFACE\""
    os.system("echo {0} | figlet -f wideterm -d ./fonts/".format(name))
    os.system("tput setaf 10")
    print("***************************************************************************************************************************************")

    os.system("tput setaf 11")
    print("\n\t\t\t\t..........................LVM MENU.............................")
    os.system("tput setaf 6")
    
    print("""
    \n\t\t\t\t1.Display Harddisks          \t\t\t\t2.Create Physical Volume
    \n\t\t\t\t3.Display Physical Volume    \t\t\t\t4.Create Volume Group
    \n\t\t\t\t5.Display Volume Group       \t\t\t\t6.Create Logic Volume
    \n\t\t\t\t7.Display Logic Volume       \t\t\t\t8.Format Logic Volume
    \n\t\t\t\t9.Extend Volume              \t\t\t\t10.Resize Volume
    \n""")
    
    os.system("tput setaf 7")
    print("\t\t\t\t\tEnter 0 to terminate \t Enter -1 return to main menu\n")
    os.system("tput setaf 2")
    choice = int(input("Select the Option : "))
    os.system("tput setaf 7")
    
    if(choice==0):
        exit()
    elif(choice==1):
        os.system("fdisk -l")
    elif(choice==2):
        device=input("Enter device name : ")
        os.system("pvcreate {}".format(device))
    elif(choice==3):
        device=input("Enter device name : ")
        os.system("pvdisplay {}".format(device))
    elif(choice==4):
        volumegroup=input("Enter volume group name : ")	
        devices=input("Enter device names : ")
        os.system("vgcreate {} {}".format(volumegroup,devices))
    elif(choice==5):
        volumegroup=input("Enter volume group name : ")
        os.system("vgdisplay {}".format(volumegroup))
    elif(choice==6):
        volumegroup=input("Enter volume group name : ")
        logicvolume=input("Enter logic volume name : ")
        size=int(input("Enter size : "))
        os.system("lvcreate --size {}G --name {} {}".format(size,logicvolume,volumegroup))
    elif(choice==7):
        volumegroup=input("Enter volume group name : ")
        logicvolume=input("Enter logic volume name : ")
        os.system("lvdisplay {}/{}".format(volumegroup,logicvolume))
    elif(choice==8):
        volumegroup=input("Enter volume group name : ")
        logicvolume=input("Enter logic volume name : ")
        os.system("mkfs.ext4 /dev/{}/{}".format(volumegroup,logicvolume))
    elif(choice==9):
        size=input("Enter size : ")
        volumegroup=input("Enter volume group name : ")
        logicvolume=input("Enter logic volume name : ")
        os.system("lvextend --size +{}G /dev/{}/{}".format(size,volumegroup,logicvolume))
    elif(choice==10):
        volumegroup=input("Enter volume group name : ")
        logicvolume=input("Enter logic volume name : ")
        os.system("resize2fs /dev/{}/{}".format(volumegroup,logicvolume))
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
   Lvm()
