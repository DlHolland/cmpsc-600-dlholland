#! /home/dylan/.codon/bin/codon run

from python import sys
from python import bandit.cli.main as bandit
from python import autoflake
from python import eradicate
from python import isort.main as isort

def reset_args():
    values = len(sys.argv) -1
    while len(sys.argv) > 0:
        del sys.argv[values]
        values -= 1
    

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
    """
    reset_args()
    print(sys.argv)
    try:
        # Autoflake
        sys.argv.append("")
        sys.argv.append("../Documents/tests/autoflake-test.py")
        autoflake.main()
    except PyError as e:
        if str(e) == "0":
            pass

    reset_args()

    try:
        # Eradicate
        sys.argv.append("")
        sys.argv.append("../Documents/tests/eradicate.py")
        eradicate.main()
    except PyError as e:
        if str(e) == "0":
            pass
    reset_args()

    try:
        # Isort
        sys.argv.append("")
        sys.argv.append("../Documents/bandit")
        isort.main()
    except PyError as e:
        if str(e) == "0":
            pass
    reset_args()

if __name__ == "__main__":
    run()
