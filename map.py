from collections import deque
import math

jumps = {"a": 1, "b": 1, "c":1}

def breadth_first_search(grid, s, end):
    N = len(grid)

    if (s[0] < 0 or s[0] > N or s[1] < 0 or s[1] > N):
        return 100

    def is_clear(cell):

        a = False
        
        try:
            if grid[cell[0]][cell[1]] == '.' or grid[cell[0]][cell[1]] == 'a' or grid[cell[0]][cell[1]] == 'b' or grid[cell[0]][cell[1]] == 'c':

                a = True

            return a
        except:
            return False

    def get_neighbours(cell):
        (i, j) = cell
        
        neighbours = []
        if (i-1 >= 0):
            if (grid[i-1][j] != "X"):
                neighbours.append([i-1,j])
        if (i+1 < N):
            if (grid[i+1][j] != "X"):
                neighbours.append([i+1,j])
        if (j-1 >= 0):
            if (grid[i][j-1] != "X"):
                neighbours.append([i,j-1])
        if (j+1 < N):
            if (grid[i][j+1] != "X"):
                neighbours.append([i,j+1])
        if (i+1 < N and j+1 < N):
            if (grid[i+1][j+1] != "X"):
                neighbours.append([i+1,j+1])
        if (i-1 >= 0 and j-1 >= 0):
            if (grid[i-1][j] != "X"):
                neighbours.append([i-1,j-1])
        if (i+1 < N and j-1 >= 0):
            if (grid[i+1][j-1] != "X"):
                neighbours.append([i+1,j-1])
        if (i-1 >= 0 and j+1 < N):
            if (grid[i-1][j+1] != "X"):
                neighbours.append([i-1,j+1])

        return (neighbours)

    start = s
    goal = end

    queue = deque()
    if is_clear(start):
       
        queue.append(start)
    visited = set()
    path_len = {start: 0}

    while queue:
        cell = queue.popleft()
       
        if cell in visited:
            continue
        if cell == goal:
       
            return path_len[cell]
        visited.add(cell)
        
        for neighbour in get_neighbours(cell):
        
            if tuple(neighbour) not in path_len:
    
                path_len[tuple(neighbour)] = path_len[cell] + 1

            queue.append(tuple(neighbour))

    
    return 100

grid = list()
for i in range(0,12):

    grid.append([])

    for j in range(0,12):

        grid[i].append('.')
'''
grid[2][2] = 'X'
grid[2][3] = 'X'
grid[2][3] = 'X'
grid[2][5] = 'X'
grid[2][6] = 'X'
grid[2][7] = 'X'

grid[1][1] = "X"
grid[2][1] = "X"
grid[3][1] = "X"
grid[4][1] = "X"

grid[7][1] = "X"
grid[7][2] = "X"
grid[7][3] = "X"
grid[6][3] = "X"
grid[5][3] = "X"

grid[7][5] = "X"
grid[7][6] = "X"
grid[7][7] = "X"
grid[7][8] = "X"   

'''
grid[3][0] = 'X'
grid[3][1] = 'X'
grid[3][2] = 'X'
grid[3][3] = 'X'
grid[3][4] = 'X'
grid[3][5] = 'X'
grid[3][6] = 'X'

grid[6][6] = "X"
grid[6][7] = "X"
grid[7][6] = "X"
grid[6][3] = "X"
grid[6][4] = "X"
grid[7][4] = "X"

grid[10][4] = "X"
grid[10][5] = "X"
grid[10][6] = "X"
grid[10][7] = "X"
grid[10][8] = "X"


pursuer1 = [0,0]
pursuer2 = [0,11]
pursuer3 = [11,11]

grid[pursuer1[0]][pursuer1[1]] = 'a'
grid[pursuer2[0]][pursuer2[1]] = 'b'
grid[pursuer3[0]][pursuer3[1]] = 'c'

evader1 = [11,7]
evader2 = [11,0]

grid[evader1[0]][evader1[1]] = '1'
grid[evader2[0]][evader2[1]] = '2'

evader_caught = False
curr_pos = pursuer1

def Move_Evader(grid, curr_pos, tag):

    move_to = input(f"\nUse W,A,S,D to move evader {tag}: ")
    print()

    if grid[curr_pos[0]][curr_pos[1]] == "1" and tag != "1":
        pass
    elif grid[curr_pos[0]][curr_pos[1]] == "2" and tag != "2":
        pass
    else:
        grid[curr_pos[0]][curr_pos[1]] = "."

    if move_to == "w":

        grid[curr_pos[0] - 1][curr_pos[1]] = tag

    elif move_to == "a":

        grid[curr_pos[0]][curr_pos[1] - 1] = tag

    elif move_to == "s":

        grid[curr_pos[0] + 1][curr_pos[1]] = tag

    elif move_to == "d":

        grid[curr_pos[0]][curr_pos[1] + 1] = tag

    else:

        return("x")

    return(move_to)

def Move_pursuer(grid,curr_pos, tag, joint_info, capture_info):

    d1e = joint_info[tag+"_"+"1"]
    d2e = joint_info[tag+"_"+"2"]

    d1p = 0
    d2p = 0
    d3p = 0
    d4p = 0
    d5p = 0
    d6p = 0
    d7p = 0

    if tag == "a":

        d1p = joint_info[tag+"_"+"b"]
        d2p = joint_info[tag+"_"+"c"]
        d3p = joint_info["b"+"_"+"c"]
        d4p = joint_info["b"+"_"+"1"]
        d5p = joint_info["b"+"_"+"2"]
        d6p = joint_info["c"+"_"+"1"]
        d7p = joint_info["c"+"_"+"2"]

    if tag == "b":

        d1p = joint_info[tag+"_"+"a"]
        d2p = joint_info[tag+"_"+"c"]
        d3p = joint_info["a"+"_"+"c"]
        d4p = joint_info["a"+"_"+"1"]
        d5p = joint_info["a"+"_"+"2"]
        d6p = joint_info["c"+"_"+"1"]
        d7p = joint_info["c"+"_"+"2"]
      
    if tag == "c":

        d1p = joint_info[tag+"_"+"a"]
        d2p = joint_info[tag+"_"+"b"]
        d3p = joint_info["a"+"_"+"b"]
        d4p = joint_info["a"+"_"+"1"]
        d5p = joint_info["a"+"_"+"2"]
        d6p = joint_info["b"+"_"+"1"]
        d7p = joint_info["b"+"_"+"2"]
    
    '''
    if d1e <= d2e:
        target = evader1
    else:
        target = evader2

    '''
    score1 = d1e - (d6p + d4p)*(d3p)
    score2 = d2e - (d7p + d5p)*(d3p)
   
    if score1 <= score2:
        target = evader1
    else:
        target = evader2

    if e1_caught == True:

        target = evader2
    
    if e2_caught == True:

        target = evader1
    
    c1 = curr_pos
    c2 = curr_pos
    c3 = curr_pos
    c4 = curr_pos
    c5 = curr_pos
    c6 = curr_pos
    c7 = curr_pos
    c8 = curr_pos
    c9 = curr_pos

    c2 = [c2[0],c2[1] + 1]
    c3 = [c3[0],c3[1] - 1]
    c4 = [c4[0] - 1,c4[1]]
    c5 = [c5[0] + 1,c5[1]]
    c6 = [c6[0] + 1,c6[1] - 1]
    c7 = [c7[0] + 1,c7[1] + 1]
    c8 = [c8[0] - 1,c8[1] + 1]
    c9 = [c9[0] - 1,c9[1] - 1]

    b1 = breadth_first_search(grid, tuple(c1), tuple(target))
    b2 = breadth_first_search(grid, tuple(c2), tuple(target))
    b3 = breadth_first_search(grid, tuple(c3), tuple(target))
    b4 = breadth_first_search(grid, tuple(c4), tuple(target))
    b5 = breadth_first_search(grid, tuple(c5), tuple(target))
    b6 = breadth_first_search(grid, tuple(c6), tuple(target))
    b7 = breadth_first_search(grid, tuple(c7), tuple(target))
    b8 = breadth_first_search(grid, tuple(c8), tuple(target))
    b9 = breadth_first_search(grid, tuple(c9), tuple(target))
   
    kk = {tuple(c1):b1,tuple(c2):b2,tuple(c3):b3,tuple(c4):b4,tuple(c5):b5,tuple(c6):b6,tuple(c7):b7,tuple(c8):b8,tuple(c9):b9}

    min_move = min(b1,b2,b3,b4,b5,b6,b7,b8)
    next_move = curr_pos

    grid[curr_pos[0]][curr_pos[1]] = "."

    keys = list(kk.keys())

    for s in keys:

        if (s[0] < 0 or s[0] > len(grid) or s[1] < 0 or s[1] > len(grid)):

            del kk[s]

    stop = True
    while(stop):

        for i in kk.keys():
    
            if i[0] >= 0 and i[1] >= 0 and i[0] < len(grid) and i[1] < len(grid):
               
                if kk[i] == min_move and grid[i[0]][i[1]] != "X":
                    
                    next_move = i
                    stop = False

        min_move += 1

    return(next_move)

All_caught = False
e1_caught = False
e2_caught = False

for i in range(0,len(grid)):

    for j in range(0,len(grid[0])):

        print(grid[i][j], end = "")
        print(" ", end = "")

    print()

moves = 0

while All_caught == False:

    moves += 1

    if(e1_caught == False):
        enemy_move1 = Move_Evader(grid, evader1, "1")

    if(e2_caught == False):
        enemy_move2 = Move_Evader(grid, evader2, "2")

    joint_info = dict()

    joint_info["a_1"] = breadth_first_search(grid, tuple(pursuer1), tuple(evader1))
    joint_info["a_2"] = breadth_first_search(grid, tuple(pursuer1), tuple(evader2))
    joint_info["b_1"] = breadth_first_search(grid, tuple(pursuer2), tuple(evader1))
    joint_info["b_2"] = breadth_first_search(grid, tuple(pursuer2), tuple(evader2))
    joint_info["c_1"] = breadth_first_search(grid, tuple(pursuer3), tuple(evader1))
    joint_info["c_2"] = breadth_first_search(grid, tuple(pursuer3), tuple(evader2))
    
    joint_info["a_b"] = breadth_first_search(grid, tuple(pursuer1), tuple(pursuer2))
    joint_info["a_c"] = breadth_first_search(grid, tuple(pursuer1), tuple(pursuer3))
    joint_info["b_a"] = breadth_first_search(grid, tuple(pursuer2), tuple(pursuer1))
    joint_info["b_c"] = breadth_first_search(grid, tuple(pursuer2), tuple(pursuer3))
    joint_info["c_a"] = breadth_first_search(grid, tuple(pursuer3), tuple(pursuer1))
    joint_info["c_b"] = breadth_first_search(grid, tuple(pursuer3), tuple(pursuer2))

    next_move1 = Move_pursuer(grid, pursuer1, "a", joint_info, [e1_caught,e2_caught])
    next_move2 = Move_pursuer(grid, pursuer2, "b", joint_info, [e1_caught,e2_caught])
    next_move3 = Move_pursuer(grid, pursuer3, "c", joint_info, [e1_caught,e2_caught])
    
    grid[next_move1[0]][next_move1[1]] = "a"
    grid[next_move2[0]][next_move2[1]] = "b"
    grid[next_move3[0]][next_move3[1]] = "c"

    last_pos1 = pursuer1
    last_pos2 = pursuer2
    last_pos3 = pursuer3
    pursuer1 = next_move1
    pursuer2 = next_move2
    pursuer3 = next_move3

    for i in range(0,len(grid)):

        for j in range(0,len(grid[0])):

            print(grid[i][j], end = "")
            print(" ", end = "")

        print()

    if (joint_info["a_1"] == 1 or joint_info["a_2"] == 1):
        if(jumps["a"] == 1):
            jumps["a"] = 0
            print("____________________")
            print()
            print("a used his jump")
            print("____________________")
            joint_info["a_1"] = breadth_first_search(grid, tuple(pursuer1), tuple(evader1))
            joint_info["a_2"] = breadth_first_search(grid, tuple(pursuer1), tuple(evader2))
            pursuer1 = Move_pursuer(grid, pursuer1, "a", joint_info, 0)

            grid[pursuer1[0]][pursuer1[1]] = "a"
            for i in range(0,len(grid)):

                for j in range(0,len(grid[0])):

                    print(grid[i][j], end = "")
                    print(" ", end = "")

                print()
   

    if (joint_info["b_1"] == 1 or joint_info["b_2"] == 1):
        if(jumps["b"] == 1):
            jumps["b"] = 0
            print("____________________")
            print()
            print("b used his jump")
            print("____________________")
            joint_info["b_1"] = breadth_first_search(grid, tuple(pursuer2), tuple(evader1))
            joint_info["b_2"] = breadth_first_search(grid, tuple(pursuer2), tuple(evader2))
            pursuer2 = Move_pursuer(grid, pursuer2, "b", joint_info, 0)
            grid[pursuer2[0]][pursuer2[1]] = "b"

            for i in range(0,len(grid)):

                for j in range(0,len(grid[0])):

                    print(grid[i][j], end = "")
                    print(" ", end = "")

                print()

    if (joint_info["c_1"] == 1 or joint_info["c_2"] == 1):
        if(jumps["c"] == 1):
            jumps["c"] = 0
            print("____________________")
            print()
            print("c used his jump")
            print("____________________")
            joint_info["c_1"] = breadth_first_search(grid, tuple(pursuer3), tuple(evader1))
            joint_info["c_2"] = breadth_first_search(grid, tuple(pursuer3), tuple(evader2))
            pursuer3 = Move_pursuer(grid, pursuer3, "c", joint_info, 0)
         
            grid[pursuer3[0]][pursuer3[1]] = "c"

            for i in range(0,len(grid)):

                for j in range(0,len(grid[0])):

                    print(grid[i][j], end = "")
                    print(" ", end = "")

                print()

    print("____________________")
    print()
    print(f"Jumps left: {jumps}")
    print("____________________")

    if pursuer1 == tuple(evader1) or last_pos1 == tuple(evader1) or pursuer2 == tuple(evader1) or last_pos2 == tuple(evader1) or pursuer3 == tuple(evader1) or last_pos3 == tuple(evader1):
        e1_caught = True
        grid[evader1[0]][evader1[1]] = "."
        evader1 = [-1,-1]
        print("___________________")
        print()

        print("evader 1 captured")
        print("___________________")

        for i in range(0,len(grid)):

            for j in range(0,len(grid[0])):

                print(grid[i][j], end = "")
                print(" ", end = "")

            print()

    if pursuer1 == tuple(evader2) or last_pos1 == tuple(evader2) or pursuer2 == tuple(evader2) or last_pos2 == tuple(evader2) or pursuer3 == tuple(evader2) or last_pos3 == tuple(evader2):
        e2_caught = True
        grid[evader2[0]][evader2[1]] = "."
        evader2 = [-1,-1]
        print("___________________")
        print()

        print("evader 2 captured")
        print("___________________")

        for i in range(0,len(grid)):

            for j in range(0,len(grid[0])):

                print(grid[i][j], end = "")
                print(" ", end = "")

            print()

    for i in range(0,len(grid)):

        for j in range(0,len(grid)):

                if grid[i][j] == "1" and evader1 == [-1,-1]:
                    grid[i][j] = "."

                if grid[i][j] == "2" and evader2 == [-1,-1]:
                    grid[i][j] = "."

    if e1_caught == True and e2_caught == True:
        All_caught = True
        print()
        print(f"All evaders were caught in {moves} moves")
        print("__________________________________________")

    if enemy_move1 == "w":

        evader1 = [evader1[0] - 1, evader1[1]]

    elif enemy_move1 == "a":

        evader1 = [evader1[0], evader1[1] - 1]

    elif enemy_move1 == "s":

        evader1 = [evader1[0] + 1, evader1[1]]

    elif enemy_move1 == "d":

        evader1 = [evader1[0], evader1[1] + 1]

    if enemy_move2 == "w":

        evader2 = [evader2[0] - 1, evader2[1]]

    elif enemy_move2 == "a":

        evader2 = [evader2[0], evader2[1] - 1]

    elif enemy_move2 == "s":

        evader2 = [evader2[0] + 1, evader2[1]]

    elif enemy_move2 == "d":

        evader2 = [evader2[0], evader2[1] + 1]

            
    print("\n\n")

    
    





    
    
    






        

        

