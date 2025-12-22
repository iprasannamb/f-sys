class Inode:
    def __init__(self):
        self.size = 0
        self.direct = []
        self.indirect = None
