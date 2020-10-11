# -- Main Function -- #
from maze import Maze
from player import Player

def main():
    maze = Maze("grid01.txt")
    end = False
    maze.add_items()
    for line in maze.grid:
            print(''.join(line))
    cmd = ""
    while cmd != "q" and end == False:
        cmd = input()
        x, y = maze.player_location()


        if cmd == "a" or cmd == "A":
            
            if maze._grid[x][y-1] != "X":
                if maze.grid[x][y-1] != " ":
                    maze._player.backpack = maze.grid[x][y-1]
                maze.grid[x][y] = " "
                y -= 1
                maze.grid[x][y] = "P"
                
        

        elif cmd == "s" or cmd == "S":

            if maze.grid[x+1][y] != "X":
                if maze.grid[x+1][y] != " ":


                    maze._player.backpack = maze.grid[x+1][y]
                maze.grid[x][y] = " "
                x += 1
                maze.grid[x][y] = "P"


        elif cmd == "w" or cmd == "W":

            if maze.grid[x-1][y] != "X":
                if maze.grid[x-1][y] != " ":
                    maze._player.backpack = maze.grid[x-1][y]
                maze.grid[x][y] = " "
                x -= 1
                maze.grid[x][y] = "P"
                

        elif cmd == "d" or cmd == "D":
            if maze.grid[x][y+1] != "X":

                if maze.grid[x][y+1] != " " and maze.grid[x][y+1] != "E":
                    maze._player.backpack = maze.grid[x][y+1]

                
                y += 1
                if maze.grid[x][y] != "E":
                    maze.grid[x][y-1] = " "
                    maze.grid[x][y] = "P"
                else:
                    if len(maze._player.backpack) == 4:
                        print("Congratulations, You finished the game!")
                        end = maze.is_exit(x, y)
                
        for line in maze.grid:
            print(''.join(line))
        print(maze._player.backpack)

main()

