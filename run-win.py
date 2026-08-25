#run on windows local server

import sys
import multiprocessing
import os

mainServer = sys.executable + " -m flask run -p 3000 --debug"

commands = [
        f""" powershell "Invoke-Expression '{mainServer}'" """
]

def run(string):
    os.system(string)

if __name__ = "__main__":
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(run, commands)


