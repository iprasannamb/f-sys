from conts import TOTAL_BLOCKS

class Disk:
    def __init__(self):
        self.blocks = [None] * TOTAL_BLOCKS
        self.free_blocks = list(range(TOTAL_BLOCKS))

    def allocate_block(self, data=None):
        if not self.free_blocks:
            raise Exception("Disk Full")
        block = self.free_blocks.pop(0)
        self.blocks[block] = data
        return block

    def read_block(self, block_no):
        return self.blocks[block_no]

    def write_block(self, block_no, data):
        self.blocks[block_no] = data
