
import sys, tarfile

if __name__ == '__main__':
    args = sys.argv[1:]

    assert(len(args) >= 1)

    tar = tarfile.open(args[0], "r:gz")
    tar.extractall()
    tar.close()
