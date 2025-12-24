def show_inode(self, filename):
        inode = self.inodes[self.directory[filename]]
        print("\n--- Inode Structure ---")
        print(f"Inode No     : {inode.inode_no}")
        print(f"Size         : {inode.size} bytes")
        print(f"Created At  : {inode.created_at}")
        print(f"Direct Ptrs : {inode.direct}")
        print(f"Indirect Ptr: {inode.indirect}")
