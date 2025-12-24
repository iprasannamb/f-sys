from filesystem import FileSystem

fs = FileSystem()

fs.create_file("file1.txt")
fs.write_file("file1.txt", "This is an inode based file system demo")
print(fs.read_file("file1.txt"))

fs.show_inode("file1.txt")
