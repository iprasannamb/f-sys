from filesystem import FileSystem

fs = FileSystem()

fs.create_file("demo.txt")
fs.write_file("demo.txt", "inode based file system in python")
print(fs.read_file("demo.txt"))
