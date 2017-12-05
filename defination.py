from enum import Enum, auto

from typing import Dict, Union


class FUNCTIONAL(Enum):
    alcohol = auto()
    aldehyde = auto()
    ketone = auto()
    cabonyl = auto()
    caboxylic_acid = auto()
    amine = auto()
    amide = auto()
    ether = auto()
    ester = auto()
    benzene = auto()
    thiol = auto()


class BASE_FUNCTIONAL(Enum):
    alkane = auto()
    alkene = auto()
    alkyne = auto()


'''class PREFIX(Enum):
    meth = 1
    eth = 2
    prop = 3
    but = 4
    pent = 5
    hex = 6
    hept = 7
    oct = 8
    non = 9
    dec = 10

    unknown = -1'''

prefix_table = {'meth' : 1, 'eth' : 2, 'prop' : 3, 'but' : 4,
                'pent' : 5, 'hex' : 6, 'hept' : 7, 'oct' : 8,
                'non'  : 9, 'dec' : 10}

base_suffix_table = {'an' : BASE_FUNCTIONAL.alkane , 'en' : BASE_FUNCTIONAL.alkene, 'yn' : BASE_FUNCTIONAL.alkyne}

suffix_table = {'ol'  : FUNCTIONAL.alcohol, 'al' : FUNCTIONAL.aldehyde, 'one' : FUNCTIONAL.ketone}

suffix_structor = {FUNCTIONAL.alcohol : 'OH-{}',
                   FUNCTIONAL.aldehyde :   'O\n'
                                           '‖\n'
                                           '{}\n'
                                           '|\n'
                                           'H',
                   FUNCTIONAL.ketone :  'O\n'
                                        '‖\n'
                                        '{}',
                   }
