# SCLI

# What?

An idea that came to me as I was writing [bookshel](https://github.com/encima/bookshelf). A terminal based speed reading client in VERY EARLY stages.

# How?

Clone the repo and run it!

```
git clone https://github.com/encima/scli
pip install -r requirements.txt
```

# Usage

usage: scli.py [-h] [-l LINK_ADDRESS] [-f F_NAME] [-s SPEED]

Process some integers.

optional arguments:
  -h, --help       show this help message and exit
  -l LINK_ADDRESS  Use a link as the source
  -f F_NAME        Use a file as the source
  -s SPEED         Set the speed (deafult 0.2)

# TODO

* [] Better formatting of retrieved HTML
* [] Attempt to extract only article content
* [] Support for more than just txt
* [x] Support for plain text as an argument
