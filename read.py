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
