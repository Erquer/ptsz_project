class Task:
    # duration
    p = 0
    # readyTime
    r = 0
    # deadline
    d = 0
    # wage
    w = 0

    def __init__(self, p, r, d, w):
        self.p = int(p)
        self.r = int(r)
        self.d = int(d)
        self.w = int(w)

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.p, self.r, self.d, self.w)