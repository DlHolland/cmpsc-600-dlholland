#! /home/dylan/.codon/bin/codon run

from python import sys
from python import subprocess
from python import os
from python import bandit.cli.main as bandit
from python import flake8.main.cli as flake8
from python import autoflake
from python import eradicate
from python import isort.main as isort
from python import pydocstyle.__main__ as pydocstyle
from python import tryceratops.__main__ as tryceratops
from python import ruff.__main__ as ruff

def reset_args():
    values = len(sys.argv) -1
    while len(sys.argv) > 0:
        del sys.argv[values]
        values -= 1
    sys.argv.append("")
    

def run():
    """
    try:
        # Bandit
        sys.argv.append("-r")
        sys.argv.append("../Documents/bandit")
        sys.argv.append("--exit-zero")
        print(sys.argv)
        bandit.main()
    except PyError as e:
        if str(e) == "0":
            pass
    
    reset_args()
    """

    try:
        # flake8
        print("FLAKEY")
        sys.argv.append("/home/dylan/codonDevs")
        flake8.main()
    except PyError as e:
        if str(e) == "0":
            pass

    reset_args()

    try:
        # Autoflake
        print("AUTOFLAKE")
        sys.argv.append("--in-place")
        sys.argv.append("/home/dylan/codonDevs/monofile.py")
        autoflake.main()
    except PyError as e:
        if str(e) == "0":
            pass

    reset_args()

    try:
        # Eradicate
        print("ERADICATE")
        sys.argv.append("/home/dylan/codonDevs/monofile.py")
        eradicate.main()
    except PyError as e:
        print(e)
        if str(e) == "0":
            pass
    reset_args()

    try:
        # Isort
        print("ISORT")
        sys.argv.append("-v")
        sys.argv.append("/home/dylan/codonDevs/monofile.py")
        isort.main()
    except PyError as e:
        print(e)
        if str(e) == "0":
            pass
    reset_args()

    try:
        # Pydocstyle
        print("PYDOCSTYLE")
        sys.argv.append("bandit-script.py")
        pydocstyle.main()
    except PyError as e:
        print(e)
        if str(e) == "0":
            pass
    reset_args()

    try:
        # Tryceratops
        print("TRYCERATOPS")
        sys.argv.append("bandit-script.py")
        tryceratops.main()
    except PyError as e:
        print(e)
        if str(e) == "0":
            pass
    reset_args()


    try:
        # Ruff
        print("RUFF")
        sys.argv.append("/home/dylan/codonDevs/bandit/bandit")
        subprocess.run([os.fsdecode(ruff.find_ruff_bin()), *sys.argv[1:]])
    except PyError as e:
        print(e)
        if str(e) == "0":
            pass
    reset_args()

if __name__ == "__main__":
    run()
