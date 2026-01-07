def myrange(*args):
    
    if len(args)>=3:
        raise ValueError("More params")
    
    if len(args)==1:
        start = 0
        end = args[0]
    else:
        start , end = args
    
    if start == end:
        end = start+end
    elif start > end:
        
        start,end = end, start
    
    while start < end:
        yield start
        start+=1

for i in myrange(20,10):
    print(i)