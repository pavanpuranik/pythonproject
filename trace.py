from functools import wraps
from tree import Node, Tree

recursionCount = 4 # change this later

def trace(func):
    depthNodeArray = [None]*recursionCount 
    functionName = func.__name__
    separator = '|  '
    trace.rd = 0

    @wraps(func)
    def tracedFunction(*args, **kwargs):
        print('{0}|-- {1}({2})'.format(separator*trace.rd, functionName, ", ".join(map(str, args))))
        
        n = Node(args)
        depthNodeArray[trace.rd] = n

        if trace.rd == 0: # for root
            tracedFunction.t.root = n
        else:
            depthNodeArray[trace.rd-1].children.append(n)

        trace.rd += 1


        result = func(*args, **kwargs)
        trace.rd -= 1

        
        print('{0}|-- return {1}'.format(separator*(trace.rd+1), result))
        return result

    tracedFunction.t = Tree()
    return tracedFunction
