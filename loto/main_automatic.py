import time
import random
from GameMaster import GameMaster
from BoardHandler import BoardHandler

#As a function of number of games and number of players:
#Statistics of having 2 winners at the time, 3 winners at the time, n winners at the time (for quinne, double, and carton, and altogether)
#Statistics of winning double quin when having quine, carton when quine, carton when haveing double, carton and double and quin. 

#1000 boards have been sold
#You play a 27 series game, 1000 times
#What is the minimum/maximum number of times someone will win out of these 27 games, 1000 times?? 
#Minimum: one line:0, two lines:0, three lines:0
#Maximum: one line:3, two lines:3, three lines:3
def minimum_and_max_won_games():
    stats_dict = dict()
    nr_boards=1000
    board_handler = BoardHandler()
    boards = board_handler.generate_boards(nr_boards)
    gameMaster = GameMaster(boards)
    current_nr_boards_stats_max=dict()
    current_nr_boards_stats_max[1]=0
    current_nr_boards_stats_max[2]=0
    current_nr_boards_stats_max[3]=0
    current_nr_boards_stats_min=dict()
    current_nr_boards_stats_min[1]=9999
    current_nr_boards_stats_min[2]=9999
    current_nr_boards_stats_min[3]=9999
    for i in range(1000):
        if i%10==0: print(i)
        winners_one_line=dict()
        winners_two_line=dict()
        winners_three_line=dict()
        for i in range(nr_boards):
            winners_one_line[str(i)]=0
            winners_two_line[str(i)]=0
            winners_three_line[str(i)]=0

        for i in range(27):
            endOfGame = False
            nr_lines=1
            while not endOfGame:
                there_is_winner, drawn_number, endOfGame = gameMaster.draw_number_and_check_boards()
                if there_is_winner:
                    for idd in gameMaster.get_winner_board_ids():
                        if nr_lines==1:
                            winners_one_line[idd]=winners_one_line[idd]+1
                        elif nr_lines==2:
                            winners_two_line[idd]=winners_two_line[idd]+1
                        elif nr_lines==3:
                            winners_three_line[idd]=winners_three_line[idd]+1
                    nr_lines+=1
            gameMaster.reinitialize()
            current_max_one_line=max(winners_one_line.values())
            current_max_two_line=max(winners_two_line.values())
            current_max_three_line=max(winners_three_line.values())
            current_min_one_line=min(winners_one_line.values())
            current_min_two_line=min(winners_two_line.values())
            current_min_three_line=min(winners_three_line.values())

        if current_nr_boards_stats_max[1]<current_max_one_line:
            current_nr_boards_stats_max[1]=current_max_one_line
        if current_nr_boards_stats_max[2]<current_max_two_line:
            current_nr_boards_stats_max[2]=current_max_two_line
        if current_nr_boards_stats_max[3]<current_max_three_line:
            current_nr_boards_stats_max[3]=current_max_three_line

        if current_nr_boards_stats_min[1]>current_min_one_line:
            current_nr_boards_stats_min[1]=current_min_one_line
        if current_nr_boards_stats_min[2]>current_min_two_line:
            current_nr_boards_stats_min[2]=current_min_two_line
        if current_nr_boards_stats_min[3]>current_min_three_line:
            current_nr_boards_stats_min[3]=current_min_three_line
            
    print(current_nr_boards_stats_max)
    print(current_nr_boards_stats_min)


#Nr winners vs number of rounds that had to be played since the last winners
#Results: count of number of winners per "quine" per 27 games. 
#1)accross 27 games we have: quine: 3 vainqueurs: 4, 2 vainqueurs: 2, 1 vainqueur: 8,... and then average of 1000 games
#2)Number of rounds vs number of winners. average overs 27000 games for each 3 category.Example: 3 vainqueurs: needs on average 10,5 rounds for quine
def nr_winners_vs_rounds():
    nr_boards=1000
    nr_winners=dict()
    nr_winners[1]=[]
    nr_winners[2]=[]
    nr_winners[3]=[]
    rounds_until_winner=dict()
    rounds_until_winner[1]=[]
    rounds_until_winner[2]=[]
    rounds_until_winner[3]=[]
    board_handler = BoardHandler()
    boards = board_handler.generate_boards(nr_boards)
    gameMaster = GameMaster(boards)
    for i in range(1000):
        if i%10==0: print(i)
        for i in range(27):
            endOfGame = False
            nr_lines=1
            rounds_until_winner_nr=0
            while not endOfGame:
                rounds_until_winner_nr+=1
                there_is_winner, drawn_number, endOfGame = gameMaster.draw_number_and_check_boards()
                if there_is_winner:
                    if nr_lines==1:    
                        nr_winners[1].append(len(gameMaster.get_winner_board_ids))
                        rounds_until_winner[1].append(rounds_until_winner_nr)
                    elif nr_lines==2:
                        nr_winners[2].append(len(gameMaster.get_winner_board_ids))
                        rounds_until_winner[2].append(rounds_until_winner_nr)
                    elif nr_lines==3:
                        nr_winners[3].append(len(gameMaster.get_winner_board_ids))
                        rounds_until_winner[3].append(rounds_until_winner_nr)
                    rounds_until_winner_nr=0
                    nr_lines+=1
            gameMaster.reinitialize()
        
    

if __name__ == "__main__":
    #minimum_and_max_won_games()
    nr_winners_vs_rounds()


