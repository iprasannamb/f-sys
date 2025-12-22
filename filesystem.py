from disk import Disk
from Inode import Inode
from conts import BLOCK_SIZE, MAX_DIRECT_BLOCKS

class FileSystem:
    def __init__(self):
        self.disk = Disk()
        self.inodes = []
        self.directory = {}

    def create_file(self, filename):
        inode = Inode()
        self.inodes.append(inode)
        self.directory[filename] = len(self.inodes) - 1

    def write_file(self, filename, data):
        inode = self.inodes[self.directory[filename]]
        inode.size = len(data)
        chunks = [data[i:i+BLOCK_SIZE] for i in range(0, len(data), BLOCK_SIZE)]

        for chunk in chunks[:MAX_DIRECT_BLOCKS]:
            block = self.disk.allocate_block()
            self.disk.write_block(block, chunk)
            inode.direct.append(block)

        if len(chunks) > MAX_DIRECT_BLOCKS:
            inode.indirect = self.disk.allocate_block()
            indirect = []
            for chunk in chunks[MAX_DIRECT_BLOCKS:]:
                block = self.disk.allocate_block()
                self.disk.write_block(block, chunk)
                indirect.append(block)
            self.disk.write_block(inode.indirect, indirect)

    def read_file(self, filename):
        inode = self.inodes[self.directory[filename]]
        data = ""
        for block in inode.direct:
            data += self.disk.read_block(block)

        if inode.indirect is not None:
            for block in self.disk.read_block(inode.indirect):
                data += self.disk.read_block(block)

        return data
