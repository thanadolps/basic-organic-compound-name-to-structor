from Organic import Organic
from defination import *
from typing import List, Union, Tuple

def token(name : str) -> List[str]:

    #Cleaning
    name = name.replace(" ","")

    #spliting
    name = name.split('-')

    return name


def get_group(name : str):

    for i in range(3,5) :

        pre = prefix_table.get(name[:i])

        if pre :

            suf = name[i:]
            group = base_suffix_table.get(suf[:2])

            if group :

                functional = suffix_table.get(suf[2:])

            else:
                functional = None

            return Organic(pre, group, functional)

    return False



