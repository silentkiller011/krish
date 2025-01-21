 #THE LABYRINTH OF SPIDERS
#ATREYEE GHOSAL(16) and BRUNDHA R(17)           12-A         
#Sub-sections of code:
#    1) Codes (functions) for saving, reopening or starting new game
#    2) Classes and imports
#    3) Functions
#    4) Functions for the two games
#    5) Introduction and initialisation
#    6) Code for movements




#CODE FOR SAVING GAME


def save(L) :

    f = open("save.txt","w+")    #opens file for saving game

    L_save = []
    for i in range(len(L)) :      #converts matrix-list into save-list of strings: one row becomes 1 string
        s = ""
        for j in range(len(L[i])) :
            s+=str(L[i][j])
        L_save.append(s)

    f.writelines(L_save)      #saves save-list in file
    f.close()

    return "Game saved! Sayonara!"


#CODE FOR RE-OPENING SAVED GAME


def reopen() :

    f = open("save.txt","r+")      #opens saved file

    L_file = f.readlines()     #converts file into saved-list
    s = L_file[0]
    L_reopen = []
    n = 0
    for _ in range(41) :
        sub_reopen = []
        for j in range(41) :
            sub_reopen.append(s[n])
            n+=1
        L_reopen.append(sub_reopen)
            

    L = []
    for i in range(41) :      #converts save-list of strings into matrix-list
        sub = []
        for j in range(41) :
            if L_reopen[i][j] in ("0","1","2") :
                sub.append(int(L_reopen[i][j]))
            else :
                sub.append(L_reopen[i][j])
            if L_reopen[i][j] == "#" :
                pos_i == i
                pos_j == j
        L.append(sub)
    f.close()

    return L    #returns matrix-list


#CODE FOR OPENING NEW GAME


def new_game() :

    #labyrinth list
    L= [[2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,2,0,0,0,2],
        [2,0,2,0,2,0,2,0,2,0,2,0,2,0,1,1,2,0,2,0,1,1,1,1,1,1,1,1,2,0,2,0,2,0,2,0,2,0,2,0,2],
        [2,0,2,0,2,0,2,0,0,0,2,0,2,0,0,0,2,0,0,0,0,0,2,0,0,0,2,0,2,0,0,0,2,0,2,0,0,0,2,0,2],
        [2,0,2,0,2,0,2,1,1,1,1,1,2,0,2,0,2,1,1,1,1,0,2,0,2,0,2,0,2,1,1,1,2,0,2,1,2,0,2,0,2],
        [2,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,2,0,0,0,2,0,2,0,2,0,0,0,2,0,0,0,0,0,2,0,2,0,2],
        [2,1,1,1,1,1,1,1,1,1,1,0,2,1,1,1,1,0,2,0,2,1,2,0,2,0,2,0,2,0,2,0,2,0,1,1,2,0,2,0,2],
        [2,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,2,0,2,0,2,0,0,0,2,0,2,0,2],
        [2,0,2,0,2,1,1,1,1,1,1,1,2,0,2,1,1,1,1,0,2,0,2,0,2,1,2,0,2,1,2,0,2,0,2,0,2,0,2,0,2],
        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,2,0,2,0,0,0,2,0,2],
        [2,0,2,1,1,1,1,1,1,1,1,1,1,1,2,0,1,1,1,1,1,1,2,0,2,0,2,1,1,1,1,1,1,1,1,1,1,1,2,0,2],
        [2,0,0,0,2,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,2,"X",2,"X",2],
        [2,0,2,0,2,1,1,1,2,0,2,1,1,1,2,1,1,0,2,1,1,0,2,1,1,1,1,0,2,0,1,1,1,1,2,0,2,0,"X",0,2],
        [2,0,2,0,0,0,0,0,2,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,2,0,2,"X",2,"X",2],
        [2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,1,1,2,0,1,2,2,0,2,0,1,1,2,1,2,0,2,0,2,0,2,0,2,0,2],
        [2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,1,1,2,0,1,2,2,0,2,0,1,1,2,1,2,0,2,0,2,0,2,0,2,0,2],
        [2,0,2,0,2,1,2,0,2,1,1,1,2,0,2,1,2,0,2,0,2,0,1,1,1,1,2,0,2,0,2,0,2,0,2,0,2,1,1,0,2],
        [2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0,2,0,2,0,2,0,0,0,0,0,2,0,2,0,2,0,2,0,0,0,2,0,0,0,2],
        [2,1,1,1,2,0,1,1,2,0,1,1,1,1,2,0,2,0,2,1,1,1,1,1,2,0,2,0,2,0,2,0,2,1,1,1,2,0,1,1,2],
        [2,"X",0,"X",0,0,0,0,0,0,0,0,0,0,2,0,2,"X","X","X",0,0,2,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0,2],
        [2,0,"X",1,1,1,1,1,1,1,1,1,1,0,2,0,2,1,1,"X",2,0,2,0,2,1,1,1,1,1,1,1,1,1,1,0,2,0,2,0,2],
        [2,"X",0,"X",2,0,0,0,0,0,2,0,0,0,2,0,2,"X","X","X",0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,2],
        [2,0,2,0,2,0,2,1,2,0,2,1,1,1,2,0,2,0,2,0,2,1,1,1,2,0,2,1,1,1,2,0,1,1,1,1,1,1,1,1,2],
        [2,0,2,0,2,0,2,0,2,0,2,0,0,0,2,0,0,0,2,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,2],
        [2,1,2,0,2,0,2,0,2,0,2,0,2,0,2,1,1,1,2,1,2,0,2,0,1,1,2,0,1,1,1,1,1,1,1,1,2,0,2,0,2],
        [2,0,0,0,2,0,0,0,2,0,0,0,2,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,"X",0,"X",2,0,0,0,2],
        [2,0,1,1,2,0,2,1,1,1,1,1,2,0,2,0,2,0,2,0,2,1,1,1,2,0,2,0,2,1,1,0,2,0,"X",0,2,1,1,1,2],
        [2,0,0,0,2,0,2,0,0,0,0,0,2,0,0,0,2,0,2,0,2,0,0,0,2,0,0,0,2,0,0,0,2,"X",2,"X",0,0,0,0,2],
        [2,0,1,1,2,0,2,0,2,0,0,0,2,1,1,1,2,0,2,0,2,0,2,0,2,1,1,1,2,0,2,1,1,1,1,1,1,1,2,0,2],
        [2,0,0,0,2,0,2,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0,2,0,2],
        [2,0,2,0,2,0,2,0,2,1,1,1,1,1,1,1,1,1,2,0,2,1,1,1,2,0,2,0,1,1,2,0,2,0,2,0,2,0,2,0,2],
        [2,0,2,0,2,0,2,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,2,0,0,0,2,0,2,0,2,0,0,0,2,0,2],
        [2,0,2,0,2,0,2,1,1,1,1,0,2,0,2,0,2,1,2,0,2,0,2,0,2,0,2,1,1,0,2,1,2,0,2,1,2,0,2,0,2],
        [2,0,2,0,2,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,2],
        [2,0,2,0,2,1,1,0,2,0,2,1,1,1,1,1,1,0,2,1,1,1,1,1,1,1,2,0,2,1,1,1,1,1,1,0,2,0,2,0,2],
        [2,0,2,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,2,0,0,0,2,0,0,0,2,0,2,0,2],
        [2,0,2,1,1,1,1,1,2,1,1,1,2,0,2,0,2,1,2,0,2,1,1,1,1,0,2,0,2,1,2,0,2,0,2,1,2,0,2,0,2],
        [2,0,2,0,0,0,0,0,2,0,0,0,0,0,2,0,2,"X",0,"X",2,0,0,0,0,0,2,0,0,0,2,0,2,0,2,0,0,0,2,0,2],
        [2,0,2,0,2,1,1,0,2,0,1,1,1,1,1,1,2,0,"X",1,2,0,2,1,1,1,1,1,1,0,2,0,2,0,2,0,1,1,2,0,2],
        [2,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,"X",0,"X",2,"E",2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,"E",1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]]

    return L   #returning labyrinth list



        
#CLASSES AND IMPORTS


import random        #CLASS AND IMPORTS FOR SLIDING GAME

class Exception:
    def err():
        pass


    
import random        #CLASS AND IMPORTS FOR TIC TAC TOE GAME           
import copy
# import sys

class TicTac:              
    free=False
    def __init__(self):
        self.board = [' '] * 9
        self.player_marker = ''
        self.bot_name = 'Spidey'
        self.bot_marker = ''
        self.winning_combos =([6,7,8],[3,4,5],[0,1,2],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6],)
        self.corners = [0,2,6,8]
        self.sides = [1,3,5,7]
        self.middle = 4
        self.form = '''
           \t| %s | %s | %s | 
           \t-------------
           \t| %s | %s | %s |
           \t-------------
           \t| %s | %s | %s |
           '''                    

    def print_board(self,board = None):
        #displaying the board
        if board is None:
            print(self.form % tuple(self.board[6:9] + self.board[3:6] + self.board[0:3]))
        else:
            print(self.form % tuple(board[6:9] + board[3:6] + board[0:3]))

    def get_marker(self):
        #assigning symbols to players 
        marker = input("Would you like your marker to be X or O?: ").upper() 
        while marker not in ["X","O"]:
            print ("Please enter a valid input.")
            marker = input("Would you like your marker to be X  or O? :").upper()
        if marker == "X":
            return ('X', 'O')
        else:
            return ('O','X')

    def is_winner(self, board, marker):
        #checking if board has any of the predefined winning patterns
        #checking order: horizontals, verticals, diagonals
        for combo in self.winning_combos:
            if (board[combo[0]] == board[combo[1]] == board[combo[2]] == marker):
                return True
        return False

    def get_bot_move(self):
        #helps computer to make move

        #check if comp can win on next move
        for i in range(0,len(self.board)):
            board_copy = copy.deepcopy(self.board)
            if self.is_space_free(board_copy, i):
                self.make_move(board_copy,i,self.bot_marker)
                if self.is_winner(board_copy, self.bot_marker):
                    return i
        #check if you can win on next move
        for i in range(0,len(self.board)):
            board_copy = copy.deepcopy(self.board)
            if self.is_space_free(board_copy, i):
                self.make_move(board_copy,i,self.player_marker)
                if self.is_winner(board_copy, self.player_marker):
                    return i
        #take corners if free        
        move = self.choose_random_move(self.corners)
        if move != None:
            return move
        #take middle if free
        if self.is_space_free(self.board,self.middle):
            return self.middle
        #last option is to take sides
        return self.choose_random_move(self.sides)

    def is_space_free(self, board, index):
        #checks for free spaces
        return board[index] == ' '

    def is_board_full(self):
        #checks if board is full
        for i in range(1,9):
            if self.is_space_free(self.board, i):
                return False
        return True

    def make_move(self,board,index,move):
        #just assigns the players symbol to element of list on board
        board[index] = move

    def choose_random_move(self, move_list):
        possible_winning_moves = []
        for index in move_list:
            if self.is_space_free(self.board, index):
                possible_winning_moves.append(index)
                if len(possible_winning_moves) != 0:
                    return random.choice(possible_winning_moves)
                else:
                    return None
       
    def start_game(self):
       # chooses which player will go first 
       self.print_board(range(1,10))
       self.player_marker, self.bot_marker = self.get_marker()
       print("Your symbol is " + self.player_marker)
    if random.randint(0, 1) == 0:
        print("I will go first")
    #     self.enter_game_loop('b')
    # else:
    #     print("You will go first")
    #     self.enter_game_loop('h')


    def get_player_move(self):
        #getting input from user
        g,move=0,10
        while g==0 and (move not in [1,2,3,4,5,6,7,8,9] or not self.is_space_free(self.board,move-1)):
            try:
                move = int(input("Pick a spot to move: (1-9) "))
            except:
                print("Please type in a valid input")
            else:
                g=1
        return move - 1
    
    def enter_game_loop(self,turn):
       is_running = True
       player = turn 
       # i have used :
       # 1)the pre defined winning patterns and few functions to check status of game
       # 2)get_player_move to get the players move
       # 3)get_bot_move to get comp move

       #h for human, b for bot
       while is_running:
           # human player
           if player == 'h':
               user_input = self.get_player_move()
               self.make_move(self.board,user_input, self.player_marker)
               if(self.is_winner(self.board, self.player_marker)):
                   self.print_board()
                   print("""
Oh my!
You seem to have...
Seem to have... won...
You are free for now,
But we will meet again!""")
                   is_running = False
                   TicTac.free=True
                   
               else:
                   if self.is_board_full():
                       self.print_board()
                       print("""
It's a draw...
I think I will let you go this time.
As your skills do impress.""")
                       is_running = False
                       TicTac.free=True
                   else:
                       self.print_board()
                       player = 'b'
           
           else:
               #comp move
              bot_move =  self.get_bot_move()
              self.make_move(self.board, bot_move, self.bot_marker)
              if (self.is_winner(self.board, self.bot_marker)):
                  self.print_board()
                  print("""
MR.SPIDER HAS WON!!!!
You are doomed!
Doomed to play again!""")
                  
                  is_running = False
                  break
              else:
                  if self.is_board_full():
                      self.print_board()
                      print("""
It's a draw...
I think I'll make an exception this time,
As your skills do impress.
You are free to go!""")
                      is_running = False
                      TicTac.free=True
                  else:
                      self.print_board()
                      player = 'h'
       

#FUNCTIONS

def spider_clusters() :       #function to define clusters of spiders
    s1 = [(19,1),(19,3),(20,2),(21,1),(21,3)]
    s2 = [(19,17),(19,18),(19,19),(20,19),(21,17),(21,18),(21,19)]
    s3 = [(11,37),(11,39),(12,38),(13,37),(13,39)]
    s4 = [(25,33),(25,35),(26,34),(27,33),(27,35)]
    s5 = [(37,17),(37,19),(38,18),(39,17),(39,19)]
    return s1,s2,s3,s4,s5

                
def wall() :        #function to warn about walls
    print
    print("Oops! Ran into a wall! Try again!")
    print


def instr() :        #function to repeat instructions 
    print("Instructions:\n"
          "Use the W,A,S,D keys to move. You can only move one space at a time.\n"
          "Press W to move up. Press S to move down. Press A to move right. Press D to move left.\n"
          "Press '1' to display maze.\n"
          "Press 'e' to exit game.\n"
          "Press 'i' to repeat instructions.\n"
          "Make your way through the maze. Try not to run into spiders. But remember,\n"
          "sometimes the path to the escape lies right in the spider's den!\n"
          "Enjoy!")
    


def exitez(L) :          #function upon exiting
    print
    print("Are you sure you want to leave the maze now?")
    print("The spiders will miss you!")
    print
    sure = input("Sure you want to leave? Y/N")
    if sure.lower() == "y" :
        savez_vous = input("Do you want to save your game? Y/N")
        if savez_vous.lower() == "y" :
            save(L)
        return 1    
    elif sure.lower() == "n" :
        print("Okay! Feel free to explore!")


def spider(pos_i,pos_j,L) :                   #SUB-GAMES FOR SPIDERS
    
    s1,s2,s3,s4,s5 = spider_clusters()         #to identify spider cluster

    for i in (s1,s2,s3,s4,s5) :
        for j in i:
            if (pos_i,pos_j) == j :
                cluster = i
                break
            elif (pos_i,pos_j) == (100,100) :
                cluster = s1
                break
            elif (pos_i,pos_j) == (200,200) :
                cluster = s5
                break
            
    print
    print("The spider has captured you! Play the spider's game to escape!")
    print
    
    if cluster in (s1,s3) : 
        tictactoe(cluster,L)
    elif cluster in (s2,s4,s5) :
        sliding(cluster,L)


def win_game(cluster,L) :
    for i in cluster:
        L[i[0]][i[1]] = 0


def exit_game(cluster,L) :
    for i in cluster:
        L[i[0]][i[1]] = "X"

        
def maze(L,pos_i,pos_j) :       #function to show labyrinth 

    if (pos_i-15) < 0 :
        a = 0
    else :
        a = pos_i-15

    if pos_i+15 > len(L)-1 :
        b = len(L)
    else :
        b = pos_i+15

    for i in range(a,b):    

        if pos_j-20 < 0 :
            c = 0
        else :
            c = pos_j-20

        if pos_j+20 > len(L[i])-1 :
            d = len(L[i])
        else :
            d = pos_j+20
        
        for j in range(c,d):            
            if i==pos_i and j==pos_j :
                print("#", end=" ")
            elif L[i][j] == 0 :
                print(" ", end="")      
            elif L[i][j] == 1 :
                print("-", end=" ")
            elif L[i][j] == 2:
                print("|", end=" ")
            else:
                print(L[i][j], end=" ")
        print




#TIC TAC TOE GAME


def tictactoe(cluster,L) :
    #introduction
    print("Looks like you've run into my trap!\n"
    "It's quite simple to escape dear,\n"
    "Just play a game with  me \n"
    "A game of TIC TAC TOE."
    "I must warn you though \n"
    "You won't leave till you win!")

    #loop to ensure game doesn't end untill player wins or it's a draw
    while TicTac.free==False:
        if __name__ == "__main__":   
             TicTacToe = TicTac()
             TicTacToe.start_game()
    else :
        win_game(cluster,L)


#SLIDING GAME


def sliding(cluster,L): 
    #the puzzle blocks
    a=['1 1 1 1 1','1 1 1 1 1','1 1 1 1 1','1 1 1 1 1','1 1 1 1 1']
    b=['2 2 2 2 2','2 2 2 2 2','2 2 2 2 2','2 2 2 2 2','2 2 2 2 2']
    c=['3 3 3 3 3','3 3 3 3 3','3 3 3 3 3','3 3 3 3 3','3 3 3 3 3']
    d=['4 4 4 4 4','4 4 4 4 4','4 4 4 4 4','4 4 4 4 4','4 4 4 4 4']
    e=['5 5 5 5 5','5 5 5 5 5','5 5 5 5 5','5 5 5 5 5','5 5 5 5 5']
    f=['6 6 6 6 6','6 6 6 6 6','6 6 6 6 6','6 6 6 6 6','6 6 6 6 6']
    g=['7 7 7 7 7','7 7 7 7 7','7 7 7 7 7','7 7 7 7 7','7 7 7 7 7']
    h=['8 8 8 8 8','8 8 8 8 8','8 8 8 8 8','8 8 8 8 8','8 8 8 8 8']
    x=['          ','          ','    X     ','          ','          ']
    puzz=[]
    puzz1=[[a,b,c],[d,e,f],[g,h,x]]
    #choosing a puzzle from the pre set patterns
    puzza=[[a,b,c],[e,d,f],[h,g,x]]
    puzzb=[[g,b,d],[e,x,f],[h,c,a]]
    puzzc=[[a,b,c],[d,f,h],[g,e,x]]
    puzzd=[[a,b,e],[g,x,f],[c,d,h]]
    puzze=[[h,g,d],[c,x,a],[e,f,b]]
    p=[puzza,puzzb,puzzc,puzzd,puzze]
    puzz=p[random.randint(0,4)]

    #intro
    # **print(You ran into a spider!!!
    # To get out of this sticky web, you must solve this puzzle.
    # The aim is simple:
    # arrange the blocks in order
    # and tomorrow's paper wont say 'MURDER' !)
    
    
    
               #printing puzzle
    for i in puzz:
        for j in range (0,1):
            for k in range(0,5):
                print(i[j][k], " " , i[j+1][k]," ", i[j+2][k])
        print
        
    won=False
    k,l=0,0
    while won!=True:
        #finding the 'X' block
        for k in range(0, len(puzz)):
            for l in range(0, len(puzz[k])):
                if puzz[k][l][0]=='          ':
                    i=k
                    j=l
        g,a,move=0,0,0
        while g==0 :
            try:    #accepting input for move
                move=int(input("""
                Chose wisely!
                1 up
                2 down
                3 left
                4 right
                0 exit and return to main maze

                Your choice: """))

                #validating move and checking player doesn't go outside boundary
                
                if move==1:
                    puzz[i][j],puzz[i-1][j]=puzz[i-1][j],puzz[i][j]
                elif move==2:
                    puzz[i][j],puzz[i+1][j]=puzz[i+1][j],puzz[i][j]
                elif move==3:
                    puzz[i][j],puzz[i][j-1]=puzz[i][j-1],puzz[i][j]
                elif move==4:
                    puzz[i][j],puzz[i][j+1]=puzz[i][j+1],puzz[i][j]
                elif move==0:
                    a=1
                    
                else:
                    raise Exception("Invalid move")
            except:
                print("Oops! Wrong input")
            else:
                g=1
        
                
                      #printing puzzle
        for i in puzz:
            for j in range (0,1):
                for k in range(0,5):
                    print(i[j][k], " " , i[j+1][k]," ", i[j+2][k])
            print

        if puzz==puzz1 :   #checking winning condition
            won=True
            print("YOU WON !! YOU ARE FREE!")
        
            win_game(cluster,L)
        elif a==1:
            won = True
            exit_game(cluster,L)
            print("Game exited.")
    
                   

#INTRODUCTION AND INITIALISATION

while True:

    try : 
        load = input("Hello! \n"
            "1) Press 1 to reload saved game. \n"
            "2) Press 2 to load new game.")

        if load == "1" :
            L = reopen()
            break

        elif load == "2" :
            L =  new_game()
            break

        else :
            print("Oops! Did you mean to say something else?")

    except IOError :
        print("Oops! Saved file does not exist!")

    
#player's initial position
        
pos_i = 0   #vertical position  - row
pos_j = 19   #horizontal position - column
    
    



#welcome and instructions

# print
# print("Welcome to THE LABYRINTH OF SPIDERS!")
# print
# print """Instructions:
#     Use the W,A,S,D keys to move. You can only move one space at a time.
#     Press W to move up. Press S to move down. Press A to move right. Press D to move left.
#     Press '1' to display maze.
#     Press 'e' to exit game.
#     Press "i" to repeat instructions.
#     Make your way through the maze. Try not to run into spiders. But remember,
#     sometimes the path to the escape lies right in the spider's den!
#     Enjoy!
#     P.S: Find the easter egg if you can!"""
# print




#CODE FOR MOVEMENTS

while True :

    L[pos_i][pos_j] = "*"           #cementing current position for tracking
## 
##    try :

    print
    move = input("Move?")             #movements
    print
    
    if move.lower() == "d" :
        if L[pos_i][pos_j+1] in (1,2) :
            wall()
        elif L[pos_i][pos_j+1] == "X" :
            spider(pos_i,pos_j+1,L)
        elif L[pos_i][pos_j+1] == "E" :
            print
            print("YAY! YOU FOUND THE EXIT!")
            r = exitez(L)
            if r == 1 :
                print("Bye!")
                break
        else :
            pos_j += 1
            
    elif move.lower() == "a" :
        if L[pos_i][pos_j-1] in (1,2) :
            wall()
        elif L[pos_i][pos_j-1] == "X" :
            spider(pos_i,pos_j-1,L)
        elif L[pos_i][pos_j-1] == "E" :
            print
            print("YAY! YOU FOUND THE EXIT!")
            r = exitez(L)
            if r == 1 :
                print("Bye!")
                break
        else:
            pos_j -= 1
            
    elif move.lower() == "w" :
        if L[pos_i-1][pos_j] in (1,2) :
            wall()
        elif L[pos_i-1][pos_j] == "X" :
            spider(pos_i-1,pos_j,L)
        elif L[pos_i-1][pos_j] == "E" :
            print
            print("YAY! YOU FOUND THE EXIT!")
            r = exitez(L)
            if r == 1 :
                print("Bye!")
                break
        else :
            pos_i -= 1
            
    elif move.lower() == "s" :
        if L[pos_i+1][pos_j] in (1,2) :
            wall()
        elif L[pos_i+1][pos_j] == "X" :
            spider(pos_i+1,pos_j,L)
        elif L[pos_i+1][pos_j] == "X" :
            print
            print("YAY! YOU FOUND THE EXIT!")
            r = exitez(L)
            if r == 1 :
                print("Bye!")
                break
        else :
            pos_i += 1

    elif move == "shortcut1" :
        spider(100,100,L)

    elif move == "shortcut2" :
        spider(200,200,L)
            
    elif move == '1' :
        maze(L,pos_i,pos_j)

    elif move.lower() == "i" :
        instr()
        
    elif move.lower() == "e" :
        r = exitez(L)
        if r == 1 :
            print("Bye!")
            break