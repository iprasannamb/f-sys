from filesystem import FileSystem

fs = FileSystem()

while(1):
    print("\n 1. Create File\n 2. Write File\n 3. Read File\n 4. Show Inode\n5.Exit");
    opt=int(input("Enter you choice :"))
    match(opt):
        case 1:
            name=input("Enter file name :")
            fs.create_file("file1.txt")
            
        case 2:
            fs.write_file("file1.txt","This is an inode based file system demo")
            
        case 3:
            print(fs.read_file("file1.txt"))
            
        case 4:
            fs.show_inode("file1.txt")
            
        case 5:
            exit(0);
