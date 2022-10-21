def isiter(thing):
    try:
        _ = enumerate(thing)
        return True
    except:
        return False

class c:  
    def __init__(self, *items):
        self.type = type(items[0])
        self.items = [self.type(item) for item in items]
        
    def __str__(self):
        ret = "c("
        for i, item in enumerate(self.items): 
            if i + 1 != len(self.items):
                ret += (str(item) + ", ")
            else:
                ret += (str(item) + ")")
        return ret
    
    def __getitem__(self, index):
        if isinstance(index, int): 
            return self.items[index - 1]
        elif isinstance(index, c):
            _selfItems, _indexItems = c.recycle(self.items, index.items)
            if index.type == int:
                return c(*[_selfItems[i-1] for i in _indexItems])
            if index.type == bool:
                return c(*[item[0] for item in zip(_selfItems, _indexItems) if item[1]])
        else: 
            raise ValueError("vector addressing must be done with int or vector of ints or bools")
    def __setitem__(self, index, other):
        _other = c.normalize(other)
        _otherItems, _ = c.recycle(_other.items, self.items)

        _index = c.normalize(index)
        _indexItems, _ = c.recycle(_index.items, self.items)

        if self.type != _other.type: 
            raise ValueError("assignment types must be equal")
        
        elif _index.type == bool:
            _using = 0
            for i, val in enumerate(_indexItems):
                if val:
                    self.items[i] = _otherItems[_using]
                    _using += 1
                        
        elif _index.type == int:
            for i, val in enumerate(_indexItems): 
                self.items[val-1] = _otherItems[i-1]
        else: raise ValueError

    def __contains__(self, item):
        return item in self.items
    
    def __len__(self):
        return len(self.items)
    
    def __add__(self, other):
        if type(other) != c:
            return c(*[item + other for item in self.items])
        else:
            _selfItems, _otherItems = c.recycle(self.items, other.items)
            return c(*[combo[0] + combo[1] for combo in zip(_otherItems, _selfItems)])
    def __iadd__(self, num):
        return c(*[item + num for item in self.items])
    
    def __sub__(self, other):
        if type(other) != c:
            return c(*[item - other for item in self.items])
        else:
            _selfItems, _otherItems = c.recycle(self.items, other.items)
            return c(*[combo[0] - combo[1] for combo in zip(_otherItems, _selfItems)])
    def __isub__(self, num):
        return c(*[item - num for item in self.items])
    
    def __mul__(self, other):
        if type(other) != c:
            return c(*[item * other for item in self.items])
        else:
            _selfItems, _otherItems = c.recycle(self.items, other.items)
            return c(*[combo[0] * combo[1] for combo in zip(_otherItems, _selfItems)])
    def __imul__(self, num):
        return c(*[item * num for item in self.items])
    
    def __truediv__(self, other):
        if type(other) != c:
            return c(*[item / other for item in self.items])
        else:
            _selfItems, _otherItems = c.recycle(self.items, other.items)
            return c(*[combo[0] / combo[1] for combo in zip(_otherItems, _selfItems)])
    def __itruediv__(self, num):
        return c(*[item / num for item in self.items])

    def __floordiv__(self, other):
        if type(other) != c:
            return c(*[item // other for item in self.items])
        else:
            _selfItems, _otherItems = c.recycle(self.items, other.items)
            return c(*[combo[0] // combo[1] for combo in zip(_otherItems, _selfItems)])
    def __ifloordiv__(self, num):
        return c(*[item // num for item in self.items])
    
    def __pow__(self, other):
        if type(other) != c:
            return c(*[item ** other for item in self.items])
        else:
            _selfItems, _otherItems = c.recycle(self.items, other.items)
            return c(*[combo[0] ** combo[1] for combo in zip(_otherItems, _selfItems)])
    def __ipow__(self, num):
        return c(*[item ** num for item in self.items])
    
    def __lt__(self, other):
        _selfItems, _otherItems = c.recycle(self.items, other.items)
        return c(*[combo[0] < combo[1] for combo in zip(_otherItems, _selfItems)])
    def __le__(self, other):
        _selfItems, _otherItems = c.recycle(self.items, other.items)
        return c(*[combo[0] <= combo[1] for combo in zip(_otherItems, _selfItems)])
    def __eq__(self, other):
        _selfItems, _otherItems = c.recycle(self.items, other.items)
        return c(*[combo[0] == combo[1] for combo in zip(_otherItems, _selfItems)])
    def __ne__(self, other):
        _selfItems, _otherItems = c.recycle(self.items, other.items)
        return c(*[combo[0] != combo[1] for combo in zip(_otherItems, _selfItems)])
    def __gt__(self, other):
        _selfItems, _otherItems = c.recycle(self.items, other.items)
        return c(*[combo[0] > combo[1] for combo in zip(_otherItems, _selfItems)])
    def __ge__(self, other):
        _selfItems, _otherItems = c.recycle(self.items, other.items)
        return c(*[combo[0] >= combo[1] for combo in zip(_otherItems, _selfItems)])

    def __and__(self, other):
        _selfItems, _otherItems = c.recycle(self.items, other.items)
        return c(*[combo[0] and combo[1] for combo in zip(_otherItems, _selfItems)])
    def __or__(self, other):
        _selfItems, _otherItems = c.recycle(self.items, other.items)
        return c(*[combo[0] or combo[1] for combo in zip(_otherItems, _selfItems)])
    def __xor__(self, other):
        _selfItems, _otherItems = c.recycle(self.items, other.items)
        return c(*[(combo[0] and not combo[1]) or (not combo[0] and combo[1]) for combo in zip(_otherItems, _selfItems)])
    def __invert__(self): #YOU HAVE TO USE ~c_instance INSTEAD OF not ~c_instance
        return c(*[not item for item in self.items])

    @staticmethod
    def normalize(cObj):
        return cObj if isinstance(cObj, c) else (c(*cObj) if isiter(cObj) else c(cObj))

    @staticmethod
    def recycle(items1, items2):
        _selfItems = items1[:]
        _indexItems = items2[:]
        _i = 0
        while (len(_indexItems) > len(_selfItems)): _selfItems.append(_selfItems[_i]); _i+=1
        while (len(_indexItems) < len(_selfItems)): _indexItems.append(_indexItems[_i]); _i+=1
        return _selfItems, _indexItems



        

