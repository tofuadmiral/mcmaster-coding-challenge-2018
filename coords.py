# read num of coords from first line

numcoords = int(raw_input())

## make a stack so we can push and pop 
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
        

coords = Stack()
counter = 0
sum = 0

for i in range (numcoords):
    input = int(raw_input())
    ## if input isn't zero, push it onto the stack, otherwise pop it 
    if input != 0:
        coords.push(input)
        counter+= 1
    else:
        coords.pop()
        counter-=1
        
for i in range(counter):
    sum += coords.pop()
   

print(sum)