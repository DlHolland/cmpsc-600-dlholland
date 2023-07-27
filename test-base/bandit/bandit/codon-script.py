#! /home/dylan/.codon/bin/codon run

from python import bandit.cli.main, sys


def run():
    main.main()

if __name__ == "__main__":
    sys.argv.append("bogus.py")
    sys.argv.append("--exit-zero")
    run()