
import sys, tarfile

def get_members(tar, prefix):
    if not prefix.endswith('/'):
        prefix += '/'
    offset = len(prefix)
    for tarinfo in tar.getmembers():
        if tarinfo.name.startswith(prefix):
            tarinfo.name = tarinfo.name[offset:]
            yield tarinfo


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) > 1:
        tar = tarfile.open(args[0], "r:gz")
        path = args[2] if len(args) > 2 else '.'
        tar.extractall(path, get_members(tar, args[1]))
        tar.close()