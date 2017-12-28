import sys


def main(a):
    f = open(a,'w')
    f.write('hello world')
    f.close()
    print 'hello world'
if __name__ == '__main__':
    for i in range(1,len(sys.argv)):
        url = sys.argv[i]
        main(url)