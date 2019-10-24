# dynamic programming stuff

class Jug():
    def __init__(self, size=1):
        self.size = size
        self.__contents = 0
        
    def empty(self):
        self.__contents = 0
        
    def is_empty(self):
        return self.contents == 0
    
    def not_empty(self):
        return not self.is_empty()
    
    def is_full(self):
        return self.contents == self.size
    
    def not_full(self):
        return not self.is_full()
        
    def fill(self):
        while self.not_full():
            self.add_one()
            
    def pour_one(self):
        if self.not_empty():
            self.__contents -= 1;
        
    def add_one(self):
        self.__contents += 1
        
    def pour_from_jug(self, other_jug):
        if self == other_jug:
            return
        
        while (self.not_full() and
               other_jug.not_empty()):
            other_jug.pour_one()
            self.add_one()
        
    @property
    def contents(self):
        return self.__contents
    
    def __str__(self):
        level = self.contents if self.contents > 0 else '-'
        return f"{self.size}:\\{level}/"
    

def fibonacciVal(n):
  memo = [0] * (n+1)
  memo[0], memo[1] = 0, 1
  for i in range(2, n+1):
      memo[i] = memo[i-1] + memo[i-2]
  return memo[n]



"""
  * fill a jug
  * empty a jug
  * pour one jug into another (without over flow)
  
"""
def _print_jugs(jugs, dir=" "):
    output = [str(jug) for jug in jugs]
    print(output[0] + " " + dir + " " + output[1])

def water_jug():
    large = Jug(4)  # empty four gallon jug
    small = Jug(3) # empty three gallon jug
    jugs = [small, large]
    _print_jugs(jugs)
    
    small.fill()
    _print_jugs(jugs)
    large.pour_from_jug(small)
    _print_jugs(jugs, '>')

    small.fill()
    _print_jugs(jugs)
    large.pour_from_jug(small)
    _print_jugs(jugs, '>')
    
    large.empty()
    _print_jugs(jugs)
    large.pour_from_jug(small)
    _print_jugs(jugs, '>')


if __name__ == "__main__":
    print("Dynamic Programming")
    #print( fibonacciVal(1000) )
    water_jug()
