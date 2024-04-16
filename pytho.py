
####### Data Structures #######
# Array
class CustomArray:
  data=[]
  def __init(self, arr):
    self.data = arr
    self.pointer = -1
    
  def get(self, i = int):
    return self.data[i]
  
  def pop(self):
    if (self.pointer == -1 ):
      return
    
    pointer -= 1
    return self.data[pointer+1]
    
  def push(self, newValue):
    self.pointer += 1
    self.data[self.pointer] = newValue
    
  def getLength(self):
    return self.pointer+1
    
  def first(self):
    return self.data[-1]

  def last(self):
    return self.data[0]
  
  
  
# Queue
class CustomQueue:
  data=[]
  def __init(self, arr):
    self.data = arr
    self.start = 0
    self.end = 0
    
  def isStart(self):
    if (self.data == []):
      return True
    return False
    
  def push(self, i):
    if self.isStart():
      self.data[0] = i
    else:
      self.end += 1
      self.data[self.end] = i

  def pop(self, index):
    newArr = self.data
    desiredVal = None
    for i in range(0, self.end):
      if (i == index):
        desiredVal = self.data[i]
        continue
      newArr.append(self.data[i])
    self.data = newArr
    self.end -= 1
    return desiredVal
    
  def append(self, newValue):
    self.end += 1
    self.data[self.end] = newValue
    
  def insert(self, desiredIndex, newValue):
    newArr = []
    for i in range(0, self.end):
      if (i == desiredIndex):
        newArr.append(newValue)
      newArr.append(self.data[i])
    self.data = newArr
    self.end += 1
      
      

# Stack
class CustomStack:  
  data=[]
  def __init(self, arr):
    self.data = arr
    self.pointer = -1
    
  def push(self, newNum):
    self.pointer += 1
    self.data[self.pointer] = newNum
    
  def pop(self):
    if (self.pointer == -1):
      return 

    self.pointer -= 1
    return self.data[self.pointer+1]
    
  def first(self):
    return self.data[-1]

  def last(self):
    return self.data[0]
  
  def stack(self):
    return self.data

  
  
class CustNode:
  currentNode = 0
  nodes = []
  
  def __init__(self, data=""):
    self.data = data
    self.next = None
    self.prev = None
        
    # if no other nodes exist, no previous node
    if (self.nodes == []):
      self.nodes.append(self)
    else:
      self.nodes.append(self)
      self.prev = CustNode.nodes[CustNode.currentNode]
      CustNode.nodes[CustNode.currentNode].next = self
      print(CustNode.currentNode)  
      CustNode.currentNode += 1
    
    self.pointer = self.currentNode
          
  def get(self, index):
    # checks if index is valid
    if (index < -1 and index > CustNode.currentNode):
      print("invalid index")
      return
    
    if (self.pointer == index):
      print('Here it is!')          
      return self.data
    # needs next node 
    if (self.pointer < index):
      print('Need next one')
      return self.next.get(index)        
    # needs previous node 
    elif (self.pointer > index):
      print('Need prev one')
      return self.prev.get(index)
    else:
      print("Some error occured")
                
  def getPrev(self):
    return self.prev
  def getNext(self):
    return self.next

node1 = CustNode('item1')
node2 = CustNode('item2')
node3 = CustNode('item3')
node4 = CustNode('item4')
node5 = CustNode('item5')

print(node5.get(2))