import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import stack3
Lstack = stack3.Stack()
Rstack = stack3.Stack()

with open('c:/pyfile/editor2.txt','r') as f:
    test=list(f.read().split('\n'))

for item in test[0]:
    Lstack.push(item)
cursor = Lstack.stack[-1][0]


def left(Lstack,Rstack,cursor):
    if cursor != Lstack.stack[1][0] :
        Rstack.push(Lstack.stack[-1][0])
        Lstack.pop()
        cursor = Lstack.stack[-1][0]
    else:
        pass
    return cursor

def right(Lstack,Rstack,cursor):
    if  Rstack.stack[0][-1]!=None:
        Lstack.push(Rstack.stack[-1][0])
        Rstack.pop()
        cursor = Rstack.stack[-1][0]
    else:
        pass
    return cursor

def del_left(Lstack,Rstack,cursor):
    if Lstack.stack[0][-1]!=None:
        Lstack.pop()
        cursor = Lstack.stack[-1][0]
    else:
         pass
    return cursor

def add_right(Lstack,Rstack,add_ch,cursor):
    Rstack.push(add_ch)
    Lstack.push(Rstack.stack[-1][0])
    Rstack.pop()
    cursor = Rstack.stack[-1][0]
    return cursor

switch_cmd = {
        'L' : left,
        'D': right,
        'B': del_left,
        'P': add_right
        }

for item in range(int(test[1])):
        if len(test[item+2]) == 1:
            switch_cmd[str(test[item+2])] (Lstack,Rstack,cursor)
        else:
            switch_cmd['P'] (Lstack,Rstack,str(test[item+2][-1]),cursor)

pl = []
pr = []
for item in Lstack.stack:
    if item[-1]!= None:
        pl.append(item[0][0])

for item in Rstack.stack:
    if item[0]!= 'None':
            pr.append(item[0][0])

print("".join(pl),"".join(reversed(pr)))
