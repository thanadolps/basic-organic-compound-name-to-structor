from Tokenlizer import token, get_group
from Organic import Organic
from defination import FUNCTIONAL, BASE_FUNCTIONAL

if __name__ == '__main__':
    name = input()
    hydrocarbon = get_group(name)

    if not hydrocarbon :
        print('FALSE')
        exit()
    hydrocarbon : Organic

    print(hydrocarbon)
    hydrocarbon.print_out()

