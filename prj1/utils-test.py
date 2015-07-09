#prj 1 , 重构前的简单程序
import re, sys

def get_lines(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    lines.append('\n')
    return lines

def get_blocks(lines):
    block=[]
    for line in lines:
        if line.strip():
            block.append(line)
        else:
            if block:
                yield ''.join(block).strip()
                block = []

print '<html><head><title>...</title></head><body>'

lines = get_lines(sys.argv[1])
blocks = get_blocks(lines)
title = True
for block in blocks:
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'
print '</body></html>'
