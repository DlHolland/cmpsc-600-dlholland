
import sys, time
import subprocess
import os
import bandit.cli.main as bandit
import flake8.main.cli as flake8
import autoflake
import eradicate
import isort.main as isort
import pydocstyle.__main__ as pydocstyle
import tryceratops.__main__ as tryceratops
import ruff.__main__ as ruff

def reset_args():
    values = len(sys.argv) -1
    while len(sys.argv) > 0:
        del sys.argv[values]
        values -= 1
    sys.argv.append("")
    

def run():
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
    

    try:
        # flake8
        print("FLAKEY")
        sys.argv.append("/home/dylan/codonDevs/bandit/bandit")
        flake8.main()
    except PyError as e:
        print(e)
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
        print(e)
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

    """
    try:
        # Pydocstyle
        print("PYDOCSTYLE")
        sys.argv.append("/home/dylan/codonDevs/bandit/bandit/cli")
        pydocstyle.main()
    except PyError as e:
        print(e)
        if str(e) == "0":
            pass
    reset_args()
    """
    try:
        # Tryceratops
        print("TRYCERATOPS")
        sys.argv.append("/home/dylan/codonDevs/bandit/bandit/cli")
        tryceratops.main()
    except PyError as e:
        print(e)
        if str(e) == "0":
            pass
    reset_args()

    """
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
    """
  
# def fib(n):
    # return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    t0 = time.time()
    run()
    # fib(40)
    t1 = time.time()
    print(t1 - t0)
