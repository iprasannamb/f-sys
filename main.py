from filesystem import FileSystem

fs = FileSystem()

while(1):
 
    print("\n 1. Create File\n 2. Write File\n 3. Read File\n 4. Show Inode \n 5.Exit");
    opt=int(input("Enter you choice :"))
    match(opt):
        case 1:
            fname=input("Enter file name :")
            fs.create_file(fname)
            
        case 2:
            fcontent=input("Enter the content to store :")
            fs.write_file(f"{fname}",f"{fcontent}")
            
        case 3:
            print(fs.read_file(fname))
            
        case 4:
            fs.show_inode(fname)
            
        case 5:
            exit(0);
