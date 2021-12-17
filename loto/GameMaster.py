import random

from Board import Board


class GameMaster:

    def __init__(self, boards):
        self.nr_lines_to_win=1
        self.nr_boards=len(boards)
        self.board_hashes = set()
        self.boards=boards
        self.board_hashes = [board.hash for board in boards]
        self.possible_numbers=list(range(1,91))
        self.drawn_numbers=list()
        self.current_round_winner_boards=[]

    def draw_number_and_check_boards(self):
        self.winner_boards=[]
        drawn_number = random.choice(self.possible_numbers)
        self.drawn_numbers.append(drawn_number)
        self.possible_numbers.remove(drawn_number)
        for board in self.boards:
            is_new_line_finished,nr_lines_finished = board.update_board(drawn_number)
            if is_new_line_finished and nr_lines_finished==self.nr_lines_to_win:
                self.winner_boards.append(board)
        if len(self.winner_boards)>0:
            self.nr_lines_to_win += 1
        endOfGame = self.nr_lines_to_win>3
        return len(self.winner_boards)!=0 , drawn_number, endOfGame

    def show_winner_boards_ids(self):
        winners_str=""
        for board in self.winner_boards:
            winners_str += "->"+board.id+"\n"
        if winners_str=="":
            return "No winner for the moment!"
        winners_str="The winner boards are:\n"+winners_str
        return winners_str

    def get_winner_board_ids(self):
        ids = []
        for board in self.winner_boards:
           ids.append(board.id)
        return ids

    def show_complete_winner_boards(self):
        winners_str=""
        for board in self.winner_boards:
            winners_str+=board.display_with_known_numbers(set(self.drawn_numbers))
        if winners_str=="":
            return "No winner for the moment!"
        winners_str="The winner boards are:\n"+winners_str
        return winners_str

    def show_board(self,board):
        return board.display_with_known_numbers(set(self.drawn_numbers))

    def show_board_by_id(self,id):
        for board in self.boards:
            if board.id==id:
                return board.display_with_known_numbers(set(self.drawn_numbers))
        return "No board found with this ID!"
    
    def show_all_boards(self):
        all_boards=""
        for board in self.boards:
            all_boards+=board.display_with_known_numbers(set(self.drawn_numbers))
        return all_boards

    def reinitialize(self):
        self.nr_lines_to_win=1
        self.possible_numbers=list(range(1,91))
        self.drawn_numbers=list()
        self.current_round_winner_boards=[]
        for board in self.boards:
            board.reinitialize()

    def get_drawn_numbers(self):
        return self.drawn_numbers, sorted(self.drawn_numbers)
