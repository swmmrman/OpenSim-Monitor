import psutil
import sys
from time import sleep

sim_list = []

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_sim_list(filename='simlist.txt'):
    try:
        the_list = open(filename, 'r').readlines()
    except FileNotFoundError:
        print(F"The sim list file \"{filename}\" was not found.")
        sys.exit(1)
    return the_list
if __name__ == '__main__':
    print_hi('user')
    sim_list = get_sim_list()
    print(sim_list)

