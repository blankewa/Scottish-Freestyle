#for running on linux mac systems

import sys
import os
import multiprocessing

mainServer = sys.executable + " -m flask run -p 3000 --debug"

def run(string):
    os.system(string)

commands = [
    f""" sh -c '{mainServer}' """
]

if __name__ = "__main__":
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(run, commands)


