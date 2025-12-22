from conts import TOTAL_BLOCKS

class Disk:
    def __init__(self):
        self.blocks = [""] * TOTAL_BLOCKS
        self.free_blocks = set(range(TOTAL_BLOCKS))

    def allocate_block(self):
        if not self.free_blocks:
            raise Exception("Disk full")
        block = self.free_blocks.pop()
        return block

    def write_block(self, block, data):
        self.blocks[block] = data

    def read_block(self, block):
        return self.blocks[block]
