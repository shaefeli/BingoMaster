import time

from GameMaster import GameMaster
from BoardHandler import BoardHandler

#Define variables
nr_boards=10
path_to_boards="boards"

#Want to generate the boards or are they already?
generate_the_boards = True
selected_boards="all"  #["1","8"] for example if we want to select only some boards

#Define variables for programm
board_handler = BoardHandler()

if generate_the_boards:
    board_handler.generate_boards_and_save(nr_boards,path_to_boards)

boards = board_handler.load_boards(path_to_boards, selected_boards)
gameMaster = GameMaster(boards)

#First selection
start_number="0"
while start_number!="1":
    start_number = input("Select the first action:\n" \
                "\t1) Start the game by drawing next number\n" \
                "\t2) Select a particular board to display\n" \
                "\t3) Show all the boards\n")

    if start_number=="2":
        id_to_display = input("Select the id of the board you want to display\n")
        print(gameMaster.show_board_by_id(id_to_display))
    elif start_number=="3":
        print(gameMaster.show_all_boards())
    elif start_number != "1":
        print("Choice invalid")


#Start of the game loop
endOfGame = False
while not endOfGame:
    there_is_winner, drawn_number, endOfGame = gameMaster.draw_number_and_check_boards()
    print("Drawn number:",drawn_number)
    if there_is_winner:
        print(gameMaster.show_winner_boards_ids())
    else:
        print("No winner for this round!")
    
    next_number="0"
    while next_number != "1":
        next_number = input("Select the next action:\n" \
                    "\t1) Continue the game by drawing next number\n" \
                    "\t2) Display all the winning boards\n" \
                    "\t3) Select a particular board to display\n" \
                    "\t4) Show the currently drawn numbers\n" \
                    "\t5) Show the current state of all the boards\n")
        if next_number=="2":
            print(gameMaster.show_complete_winner_boards())
        elif next_number=="3":
            id_to_display = input("Select the id of the board you want to display\n")
            print(gameMaster.show_board_by_id(id_to_display))
        elif next_number=="4":
            in_order, sorted_nr = gameMaster.get_drawn_numbers()
            print("Numbers in order of drawing:",in_order)
            print("Numbers drawn sorted:",sorted_nr)
        elif next_number=="5":
            print(gameMaster.show_all_boards())
        elif next_number !="1":
            print("Choice invalid")

print("End of game!")


