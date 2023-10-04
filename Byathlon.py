open   = 0
closed = 1

def is_open(a):
    if a == open:
        return True
    elif a == closed:
        return False
    
def is_closed(a):
    if a == closed:
        return True
    elif a == open:
        return False
    
def new_targets():
    targetlist = [open,open,open,open,open]
    return targetlist

def close_target(targets,position):
    targets[position] = closed
    return targets

def points(targets):
    n = 0
    for i in targets:
        is_closed(i)
        if is_closed(i) == True:
            n = n + 1
    return n

def targets_to_string(targets):
    
    for x in targets:
        if targets[int(x)] == 0:
            targets[int(x)] = ("0")
            
        elif targets[int(x)] == 1:
            targets[int(x)] = ("*")
                       
            
    return targets       
    

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                Biathlon")
    print("                 ¤ ¤ ¤      ")
    print("            A hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

