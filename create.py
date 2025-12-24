from Inode import Inode

def create_file(self, filename):
        inode = Inode(self.next_inode)
        self.inodes[self.next_inode] = inode
        self.directory[filename] = self.next_inode
        self.next_inode += 1
        print(f"File '{filename}' created (inode {inode.inode_no})")


