class Stack:

    def __init__(self, items = None, limit = 100):
      self.items=items if items is not None else []  
      self.limit=limit

    def isEmpty(self):
        return len(self.items)==0
        pass

    def push(self,value):
        if self.limit is not None and len(self.items) >= self.limit:
            return ("Stack is full.")
        self.items.append(value)

        pass

    def pop(self):
        
        if not self.items:
            return None  
        return self.items.pop()

        pass

    def peek(self):
        if self.isEmpty():
            return None
        
        return self.items[-1]
        pass
    
    def size(self):
        return len(self.items)
        pass

    def full(self):
        return self.limit is  not None and  len (self.items) >=self.limit
        pass

    def search(self, target):
    
        try:
            # Reverse the stack to search from the top
            reversed_items = self.items[::-1]
            return reversed_items.index(target)
        except ValueError:
            return -1

        pass
