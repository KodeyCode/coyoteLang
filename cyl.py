from sys import argv
file = argv[1]
f = open(file)
end = open(file.split('.')[0]+'.html','w')
end.write('<html>\n  <head>\n    <body>')
py = ['import','print','for','if','else:','elif','from','for','def','class','exec','input','eval']
dent = '\n      '
class Section():
    def __init__(self,_class):
        end.write(dent+'<div class="'+_class+'">')
        self.dent = dent+'  '
    def addButton(self,text,link,_class):
        end.write(self.dent+'<button href="'+link+'" class="'+_class+'">'+text+'</button>')
    def addLink(self,text,link,_class):
        end.write(self.dent+'<a href="'+link+'" class="'+_class+'">'+text+'</a>')
    def addText(self,text,_class):
        end.write(self.dent+'<p class="'+_class+'">'+text+'</p>')
    def pack(self):
        end.write(dent+'</div>')
def style(_file):
    end.write(dent+'<link rel="stylesheet" href="'+_file+'" type="text/css">')
def finnish():
    end.write('\n    </body>\n  </head>\n</html>')
def comment():
    pass
for line in f:
    if line.split('(')[0] in py or line.split(' ')[0] in py:
        print('Error')
    elif line.startswith('//'):
        comment()
    else:
        exec(line)
