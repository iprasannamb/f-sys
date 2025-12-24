import time
from conts import DIRECT_POINTERS

class Inode:
    def __init__(self, inode_no):
        self.inode_no = inode_no
        self.size = 0
        self.created_at = time.ctime()

        self.direct = [-1] * DIRECT_POINTERS
        self.indirect = -1
