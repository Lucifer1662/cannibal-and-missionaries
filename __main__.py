


def cannibalsGtMissionaries(state):
    return (state[0][0] > 0 and state[0][0] < state[0][1]) or (state[1][0]>0 and state[1][0] < state[1][1])

def goal(state):
    return state[0][0] == 0 and state[1][1] == 0 

def possible_moves(state):
    boatCap = 2
    moves = []
    side = 0
    src = 0
    dst = "right"
    if(state[2] == "right"):
        src = 1
        dst = "left"
    

    moves.append((0,0,dst))
    if(state[src][0] >= 1):
        moves.append((1,0,dst))
        if(state[src][1] >= 1):
            moves.append((1,1,dst))
    
    if(state[src][1] >= 1):
        moves.append((0,1,dst))

    if(state[src][0] >= 2):
        moves.append((2,0,dst))
    if(state[src][1] >= 2):
        moves.append((0,2,dst))
    
    return moves

def update_state(state, move):
    (m,c,dst) = move
    if(dst == "left"):
        return ((state[0][0]+m, state[0][1]+c),(state[1][0]-m, state[1][1]-c), "left")
    else:
        return ((state[0][0]-m, state[0][1]-c),(state[1][0]+m, state[1][1]+c), "right")


def recurse(state:tuple, visited:set):

    visited.add(state)
    if(cannibalsGtMissionaries(state)):
        return (False, None)
    
    if(goal(state)):
        return (True, [])

    moves = possible_moves(state)
    for move in moves:
        newState = update_state(state, move)
        if(not newState in visited):
            (success, track) = recurse(newState, visited)
            if(success):
                track.append((state, move))
                return (True, track)
    
    return (False, None)

def __main__():
    print("start")
    visited = set()
    (success, track) = recurse(((3,0),(0,3),"left"), visited)
    if(success):
        track.reverse()
        print("Success")
        for track in track:
            line = "Move "
            if track[1][0] > 0:
                line += track[1][0].__str__() + " missionaries"
                if track[1][1] > 0:
                    line += " and "

            if track[1][1] > 0:
                line += track[1][1].__str__() + " cannibals "
            
            line += "to the " + track[1][2]
            print(line)
    else:
        print("Failure")



if __name__ == "__main__":
    __main__()