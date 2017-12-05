from typing import Optional
from defination import BASE_FUNCTIONAL, FUNCTIONAL, suffix_structor

class Organic :

    def __init__(self, size : int, group : BASE_FUNCTIONAL, functional : FUNCTIONAL, pos : Optional[int] = 1):
        self.size = size
        self.group = group
        self.functional = functional
        self.pos = pos

    def set_pos(self, pos):
        self.pos = pos

    def print_out(self):

        F = suffix_structor.get(self.functional, '{}')

        R = "-".join( ['C'] * self.size)

        out = F.format(R)

        print(out)


    def __str__(self):
        return "{}  {}  {} {}".format(self.size , self.group , self.functional, self.pos)