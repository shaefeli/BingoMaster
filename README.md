# BingoMaster

## Setup 
->Code is working in Python 3.6 (other versions not tested)  
->PIL library needed, install into your python working environment:  
`pip install pillow`  

## Code entry points
### Creating a Bingo Game with boards, and manage numbers drawing, winners and everything needed in a Bingo Game
In order to run a manual game of bingo: `python loto/main_manual.py`  
  
Parameters have to be defined in the code itself of loto/main_manual.py (improvements to the code and parameter handling may come in a later version):    
*nr_boards*: The number of boards we play with (needed if we want to generate them)  
*generate_the_boards*: If we want to generate the boards of not. If this is set to true, it will create both the metadata needed to define a board, and the boards themselves that can be printed. (and can be found in the loto/boards folder. 10 have been generated and uploaded to this repo as an example)   
*selected_boards*: In case you generated boards on beforehand, you can specify here with what baords you want to play.    
  
At each step you can select one of the options to continue palcing the game  
Try it out, it should be self explaining!  
### Simulations on bingo games
In order to simulate a high number of bingo games, run `python loto/main_automatic.py`  

The number of boards, number of games, and more parameters can be defined and run a high number of times. Use this as a base code to collect statistics of your choice you want to implement! 
