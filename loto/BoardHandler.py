import random
import pickle
from PIL import Image
from pathlib import Path
import os
import pickle
import shutil


from Board import Board

class BoardHandler:
    """A class that handles boards by generating them, saving them or loading them"""

    def generate_boards(self, nr_boards):
        """Generate and returns the number of specified boards

        :param nr_boards: The number of boards to generate
        :rtype: list of elements of type Board
        """

        boards = []
        current_hashes = set()
        for i in range(nr_boards):
            board = self.generate_board(i,current_hashes)
            boards.append(board)
            current_hashes.add(board.hash)
        return boards


    def generate_boards_and_save(self, nr_boards, out_path):
        """Generate the number of specified boards and save the metadata and image to the specified folder

        :param nr_boards: The number of boards to generate
        :param out_path: The root of the folder containing informations about the boards
        :rtype: Returns nothing
        """

        if os.path.exists(out_path):
            shutil.rmtree(out_path)
        Path(os.path.join(out_path)).mkdir()
        current_hashes = set()
        for i in range(nr_boards):
            board = self.generate_board(i,current_hashes)
            current_hashes.add(board.hash)
            image = board.create_image()
            Path(os.path.join(out_path,board.id)).mkdir(exist_ok=True)
            image.save(os.path.join(out_path,board.id,"img_board_"+board.id+".png"))
            with open(os.path.join(out_path,board.id,"metadata_board"+board.id), "wb") as f:
                pickle.dump(board,f)


    #1 or 2 numbers per column
    #5 numbers per row
    def generate_board(self, id, created_board_hashs):
        """Generates a unique board

        :param id: Id of the board to create
        :param created_board_hashs: Hashes of previously created boards
        :rtype: Board
        """

        found_a_unique_board=False
        while not found_a_unique_board:
            #Choose columns per row
            columns_row1 = set(random.sample(range(9),5))
            columns_row2 = set(random.sample(range(9),5))
            #We want to guarantee that row 1 and row 2 are not the same
            while  columns_row1==columns_row2:
                columns_row2 = set(random.sample(range(9),5)) 
            columns_chosen_0_times= set(range(9))-columns_row1-columns_row2
            columns_chosen_twice=columns_row1.intersection(columns_row2)
            columns_chosen_once = set(range(9))- columns_chosen_0_times - columns_chosen_twice
            columns_row3 = columns_chosen_0_times.union(set(random.sample(columns_chosen_once,5-len(columns_chosen_0_times))))
            
            #Create the possible choices per column
            possible_choices=[]
            for i in range(9):
                if i==0:
                    possible_choices.append(list(range(1,10)))
                elif i==8:
                    possible_choices.append(list(range(80,91)))
                else:
                    possible_choices.append(list(range(10+10*(i-1),19+10*(i-1))))

            #Choose numbers for each row according to choices
            rows = []
            columns = [columns_row1,columns_row2,columns_row3]
            for i in range(3):
                row = set()
                for col in columns[i]:
                    chosen_number = random.choice(possible_choices[col])
                    row.add(chosen_number)
                    possible_choices[col].remove(chosen_number)
                rows.append(row)

            #Create a potential board and check with the hash it doesn't exist yet
            probable_board = Board(rows[0],rows[1],rows[2],id)
            if probable_board.hashing() not in created_board_hashs:
                return probable_board


    def load_boards(self, boards_path, selected_boards):
        """Loads the boards from a given folder

        :param boards_path: Root path containing all the boards
        :param selected_boards: Selection of boards to load. Can be "all" for all, or a list of strings for particular boards
        :rtype: list of elements of type Board
        """

        if not os.path.exists(boards_path):
            print("Error: no boards found")
            return []
        
        boards = []
        for subdir, dirs, files in os.walk(boards_path):
            for file in files:
                if "metadata" in file:
                    if selected_boards=="all" or file.split("board")[1] in selected_boards:
                        with open(os.path.join(subdir,file),"rb") as f:
                            boards.append(pickle.load(f))
        return boards



        

            




