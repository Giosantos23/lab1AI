## Definimos la estructura nodo con su estado, parent, action y costo acumulado
class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state  
        self.parent = parent  
        self.action = action 
        self.cost = cost  
        self.node_id = id(self)  
    
    def __str__(self):
        return f"Node(state={self.state}, action={self.action}, cost={self.cost})"

# Implementación de estructuras de cola
class FIFO:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def top(self):
        if not self.isEmpty():
            return self.queue[0]
        return None
    
    def pop(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None
    
    def add(self, item):
        self.queue.append(item)

class LIFO:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None
    
    def add(self, item):
        self.stack.append(item)

class Priority:
    def __init__(self, key_function=lambda x: x.cost):
        self.queue = []
        self.key_function = key_function
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def top(self):
        if not self.isEmpty():
            return self.queue[0]
        return None
    
    def pop(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None
    
    def add(self, item):
        cost = self.key_function(item)
        i = 0
        while i < len(self.queue) and self.key_function(self.queue[i]) < cost:
            i += 1
        self.queue.insert(i, item)