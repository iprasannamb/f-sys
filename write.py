from conts import BLOCK_SIZE,DIRECT_POINTERS

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
