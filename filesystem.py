from disk import Disk
from Inode import Inode
from conts import BLOCK_SIZE, DIRECT_POINTERS

class FileSystem:
    def __init__(self):
        self.disk = Disk()
        self.inodes = {}
        self.directory = {}
        self.next_inode = 0

    def create_file(self, filename):
        inode = Inode(self.next_inode)
        self.inodes[self.next_inode] = inode
        self.directory[filename] = self.next_inode
        self.next_inode += 1
        print(f"File '{filename}' created (inode {inode.inode_no})")
        
    def write_file(self, filename, data):
        inode = self.inodes[self.directory[filename]]

        chunks = [data[i:i+BLOCK_SIZE] for i in range(0, len(data), BLOCK_SIZE)]

        for i, chunk in enumerate(chunks):
            block = self.disk.allocate_block(chunk)

            if i < DIRECT_POINTERS:
                inode.direct[i] = block
            else:
                if inode.indirect == -1:
                    inode.indirect = self.disk.allocate_block([])
                self.disk.read_block(inode.indirect).append(block)

        inode.size = len(data)

    def read_file(self, filename):
        inode = self.inodes[self.directory[filename]]
        content = ""

        for block in inode.direct:
            if block != -1:
                content += self.disk.read_block(block)

        if inode.indirect != -1:
            for block in self.disk.read_block(inode.indirect):
                content += self.disk.read_block(block)

        return content

    def show_inode(self, filename):
        inode = self.inodes[self.directory[filename]]
        print("\n--- Inode Structure ---")
        print(f"Inode No     : {inode.inode_no}")
        print(f"Size         : {inode.size} bytes")
        print(f"Created At  : {inode.created_at}")
        print(f"Direct Ptrs : {inode.direct}")
        print(f"Indirect Ptr: {inode.indirect}")
   
