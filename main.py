from os import system
from sys import argv

if argv[1] == 'make':
    makefile = open(argv[2])
    for line in makefile:
        rem = line.replace('\n', '')
        tokens = rem.split(':')
        if tokens[0] == 'page':
            system('python3 cyl.py '+tokens[1])
        if tokens[0] == 'style':
            system('python3 cys.py '+tokens[1])
if argv[1] == 'init':
    system('mkdir '+argv[2])
    stylefile = open('style.cys')
    mainpfile = open('main.cyl','w')
    mainpfile.write('style("style.cys")')
    makefile = open('make.clm','w')
    makefile.write("page:main.cyl\nstyle:style.cys")