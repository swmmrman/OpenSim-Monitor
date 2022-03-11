import psutil
import sys
from time import sleep

sim_list = []
running = True


def get_sim_list(filename='simlist.txt'):
    try:
        the_list = [sim.strip() for sim in open(filename, 'r').readlines()]
    except FileNotFoundError:
        print(F"The sim list file \"{filename}\" was not found.")
        sys.exit(1)
    return the_list


if __name__ == '__main__':
    sim_list = get_sim_list()
    print(sim_list)
    while running:
        ps_list = [ps.cmdline() for ps in psutil.process_iter() if ps.name() == "mono"]
        sleep(1)