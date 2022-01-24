from sys import argv
file = argv[1]
f = open(file)
end = open(file.split('.')[0]+'.css','w')
py = ['import','print','for','if','else:','elif','from','for','def','class','exec','input','eval']
def comment():
    pass
class Class:
    def __init__(self,name):
        self.name = name
    def addColor(self, color):
        end.write('\n.'+self.name+'{ color: '+color+'; }')
    def addAlign(self, align):
        end.write('\n.'+self.name+'{ text-align: '+align+'; }')
    def addBox(self,value):
        end.write('\n.'+self.name+'{ border: '+value+'; }')
    def addBg(self,color):
        end.write('\n.'+self.name+'{ background-color: '+color+'; }')
class Tag:
    def __init__(self,name):
        self.name = name
    def addColor(self,color):
        end.write('\n'+self.name+'{ color: '+color+'; }')
    def addAlign(self, align):
        end.write('\n'+self.name+'{ text-align: '+align+'; }')
    def addBox(self,value):
        end.write('\n'+self.name+'{ border: '+value+'; }')
    def addBg(self,color):
        end.write('\n'+self.name+'{ background-color: '+color+'; }')
for line in f:
    if line.split('(')[0] in py or line.split(' ')[0] in py:
        print('Error: Unidentified command.')
    elif line.startswith('//'):
        comment()
    else:
        exec(line)