al = [None, 'fillA', 'fillB', 'emptyA', 'emptyB', 'fillAfromB', 'fillBfromA', 'emptyBintoA', 'emptyAintoB']

def branching_factor(s):
    actions = []
    X, Y = s

    if X < 4:
        actions.append(al[1])
    if Y < 3:
        actions.append(al[2])
    if X > 0:
        actions.append(al[3])
    if Y > 0:
        actions.append(al[4])
    if X + Y >= 4 and Y > 0:
        actions.append(al[5])
    if X + Y >= 3 and X > 0:
        actions.append(al[6])
    if X + Y <= 4 and Y > 0:
        actions.append(al[7])
    if X + Y <= 3 and X > 0:
        actions.append(al[8])

    return actions

def result(state, action):
    X, Y = state
    if action == al[1]:
        return [4, Y]
    elif action == al[2]:
        return [X, 3]
    elif action == al[3]:
        return [0, Y]
    elif action == al[4]:
        return [X, 0]
    elif action == al[5]:
        return [4, Y - (4 - X)]
    elif action == al[6]:
        return [X - (3 - Y), 3]
    elif action == al[7]:
        return [X + Y, 0]
    elif action == al[8]:
        return [0, X + Y]
    return [X, Y]

def neighbors(s):
    action_list = branching_factor(s)
    successors = [result(s, action) for action in action_list]
    print('The neighbors of state', s, 'are:', successors)
    return successors

def goal_test(goal, state):
    return state == goal

def dfs(start, goal):
    explored = []
    frontier = [start]
    print('Searching from:', start, 'to', goal)

    while frontier:
        print('Frontier:', frontier)
        state = frontier.pop()
        explored.append(state)

        print('Now in:', state)

        if goal_test(state, goal):
            print('Destination reached')
            return state

        for neighbor in neighbors(state):
            if neighbor not in explored and neighbor not in frontier:
                frontier.append(neighbor)

    print('Failure')

initial = [0, 0]
goal = [2, 0]
dfs(initial, goal)



def neighbors(s):
    actions=branching_factor(s)
    succ=[result(s,actions) for action in actions ]
    return succ

def dfs(start,goal):
    explored=[]
    frontier=[start]

    while frontier:
        state=frontier.pop()
        explored.append(state)

        if goal_test(state,goal):
            print('destination reached')
            return state
        
        for neighbor in neighbors(state):
            if neighbor not in explored and neighbor not in frontier:
                frontier.append(neighbor)