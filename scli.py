import time, sys, argparse
from subprocess import call
from blessed import Terminal
from newspaper import Article

def read_file(f_name):
    words = []
    with open(f_name) as f:
	    for line in f:
		    words += line.split(' ')
    return words


# http://docs.python-guide.org/en/latest/scenarios/scrape/
def read_link(address):
    page = Article(address, language='en')
    page.download()
    page.parse()
    return page.text.split(' ')

def speed_read(words, speed):
    term = Terminal()
    call(['clear'])
    with term.fullscreen():
        for w in words:
            printable = w
            print(term.move_y(term.height // 2) + term.center(term.bold(printable)).rstrip())
            time.sleep(speed)
            call(["clear"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Speed read!')
    parser.add_argument('-l', action='store', dest='link_address',
                    help='Use a link as the source')
    parser.add_argument('-f', action='store', dest='f_name',
                    help='Use a file as the source')
    parser.add_argument('-p', action='store', dest='plain',
                    help='Use provided text as the source (surround with quotes)')
    parser.add_argument('-s', action='store', dest='speed', default=0.2,
                    help='Set the speed', type=float)

    args = parser.parse_args()
    text = ""
    if args.f_name is not None and 'txt' in args.f_name:
        text = read_file(args.f_name)
    elif args.link_address is not None:
        text = read_link(args.link_address)
    elif args.plain is not None:
        text = args.plain.split(' ')
    else:
        parser.print_usage()

    if len(text) > 0:
        speed_read(text, args.speed)
