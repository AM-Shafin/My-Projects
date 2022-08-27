import sys

def main():
    s = sys.stdin.readline().strip()
    for i in range(1, len(s), 2):
        print(s[i] + s[i-1], end='')
    if len(s) % 2 != 0:
        print(s[-1])

main()