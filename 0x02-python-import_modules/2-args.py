#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    oko = len(sys.argv) - 1
    if oko == 0:
        print("0 arguments.")
    elif oko == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(oko))
    for i in range(oko):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
