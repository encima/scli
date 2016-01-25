import time, sys, argparse
from bs4 import BeautifulSoup
from urllib import urlopen
from subprocess import call
from blessings import Terminal

def read_file(f_name, speed):
    words = []
    with open(f_name) as f:
	    for line in f:
		    words += line.split(' ')
    speed_read(words, speed)


# http://docs.python-guide.org/en/latest/scenarios/scrape/
def read_link(address, speed):
    page = urlopen(address).read()
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.body.get_text()
#TODO get straight body content
    speed_read(content.split(' '), speed)

def speed_read(words, speed):
    term = Terminal()
    call(['clear'])
    for w in words:
        print w.strip().center(term.width - 10)
        time.sleep(speed)
        call(["clear"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-l', action='store', dest='link_address',
                    help='Use a link as the source')
    parser.add_argument('-f', action='store', dest='f_name',
                    help='Use a file as the source')
    parser.add_argument('-s', action='store', dest='speed', default=0.2,
                    help='Set the speed', type=float)

    args = parser.parse_args()
    if args.f_name is not None:
        read_file(args.f_name, args.speed)
    elif args.link_address is not None:
        read_link(args.link_address, args.speed)
