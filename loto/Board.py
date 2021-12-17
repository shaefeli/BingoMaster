import math
from PIL import Image, ImageDraw, ImageFont

#Represents one play board with 15 numbers
class Board:

    #Inits the board
    def __init__(self,row_1,row_2,row_3,id):
        self.initial_row_1=set(row_1)
        self.initial_row_2=set(row_2)
        self.initial_row_3=set(row_3)
        self.row_1=row_1
        self.row_2=row_2
        self.row_3=row_3
        self.current_finished_lines=0
        self.id=str(id)
        self.hash=self.hashing()

    #Reinitializes the board
    def reinitialize(self):
        self.row_1=set(self.initial_row_1)
        self.row_2=set(self.initial_row_2)
        self.row_3=set(self.initial_row_3)
        self.current_finished_lines=0

    #Updates the board and returns True if a new line is completed and the number of currently finished lines
    def update_board(self,number):
        if number in self.row_1:
            self.row_1.remove(number)
            if not self.row_1:
                self.current_finished_lines+=1
                return True, self.current_finished_lines
        if number in self.row_2:
            self.row_2.remove(number)
            if not self.row_2:
                self.current_finished_lines+=1
                return True, self.current_finished_lines
        if number in self.row_3:
            self.row_3.remove(number)
            if not self.row_3:
                self.current_finished_lines+=1
                return True, self.current_finished_lines
        return False, self.current_finished_lines

    #Unique representation of the board
    def hashing(self):
        return hash(tuple(list(self.initial_row_1.union(self.initial_row_2).union(self.initial_row_3))))
        

    def display(self):
        sorted_rows = [sorted(self.initial_row_1), sorted(self.initial_row_2), sorted(self.initial_row_3)]
        display_rows = []
        for i in range(3):
            indexes_row = [int(math.floor(nr/10)) if nr!=90 else 8 for nr in sorted_rows[i]] #Get the index of the column where the numbers have to be
            display_row = ["  " for i in range(9)] 
            for indexes_in_numbers,index_on_grid in enumerate(indexes_row):
                number_in_string = sorted_rows[i][indexes_in_numbers] #Get the actual number to write
                if number_in_string<10:
                    number_in_string=" "+str(number_in_string) #Leave a space for single digit number for formatting
                display_row[index_on_grid]=str(number_in_string) #W
            display_rows.append(display_row)

        board_id = "Board ID: "+self.id+"\n"
        separate_row="+--------------------------------------------+\n"
        empty_row="|    |    |    |    |    |    |    |    |    |\n"
        filled_rows=[]
        for i in range(3):
            row = ""
            for j in range(9):
                row+="| "+display_rows[i][j]+" "
            row+="|\n"
            filled_rows.append(row)

        return board_id+separate_row+empty_row+filled_rows[0]+empty_row+ \
                separate_row+empty_row+filled_rows[1]+empty_row+separate_row+ \
                    empty_row+filled_rows[2]+empty_row+separate_row                                 

    def display_with_known_numbers(self, known_numbers):
        sorted_rows = [sorted(self.initial_row_1), sorted(self.initial_row_2), sorted(self.initial_row_3)]
        display_rows = []
        for i in range(3):
            indexes_row = [int(math.floor(nr/10)) if nr!=90 else 8 for nr in sorted_rows[i]]
            display_row = ["  " for i in range(9)]
            for indexes_in_numbers,index_on_grid in enumerate(indexes_row):
                number_in_int = sorted_rows[i][indexes_in_numbers]
                number_in_string = str(number_in_int)
                if number_in_int in known_numbers:
                    number_in_string="("+str(number_in_string)+")"
                if number_in_int<10:
                    number_in_string=" "+str(number_in_string)
                display_row[index_on_grid]=str(number_in_string)
            display_rows.append(display_row)

        board_id = "Board ID: "+self.id+"\n"
        separate_row="+--------------------------------------------+\n"
        empty_row="|    |    |    |    |    |    |    |    |    |\n"
        filled_rows=[]
        for i in range(3):
            row = ""
            for j in range(9):
                number_to_display=display_rows[i][j]
                if "(" in number_to_display:
                    row+="|"+display_rows[i][j]
                else:
                    row+="| "+display_rows[i][j]+" "
            row+="|\n"
            filled_rows.append(row)

        return board_id+separate_row+empty_row+filled_rows[0]+empty_row+ \
                separate_row+empty_row+filled_rows[1]+empty_row+separate_row+ \
                    empty_row+filled_rows[2]+empty_row+separate_row       


    def create_image(self):
        width_outer = 650
        height_outer = 300
        margin_normal = 10 
        margin_top = 30
        
        im = Image.new("RGB",(width_outer,height_outer),color="white")
        draw = ImageDraw.Draw(im)
        inner_top_left_w=margin_normal
        inner_bot_right_w=width_outer-margin_normal
        inner_bot_right_h=height_outer-margin_normal
        inner_top_left_h=margin_top
        
        draw.rectangle(((inner_top_left_w, inner_top_left_h), (inner_bot_right_w, inner_bot_right_h)), fill="white", outline="black")
  

        #Do the drawings without the numbers
        width = (width_outer-margin_normal*2)/9
        height = (height_outer-margin_top-margin_normal)/3
        color="grey"
        for i in range(3):
            for j in range(9):
                if color=="grey":
                    color="white"
                else:
                    color="grey"
                draw.rectangle(((inner_top_left_w+width*j, inner_top_left_h+height*i), (width+inner_top_left_w+width*j, height+inner_top_left_h+height*i)), fill=color, outline="black")

        #Compute the display string
        sorted_rows = [sorted(self.initial_row_1), sorted(self.initial_row_2), sorted(self.initial_row_3)]
        display_rows = []
        for i in range(3):
            indexes_row = [int(math.floor(nr/10)) if nr!=90 else 8 for nr in sorted_rows[i]]
            display_row = ["  " for i in range(9)]
            for indexes_in_numbers,index_on_grid in enumerate(indexes_row):
                number_in_string = sorted_rows[i][indexes_in_numbers]
                if number_in_string<10:
                    number_in_string=" "+str(number_in_string)
                display_row[index_on_grid]=str(number_in_string)
            display_rows.append(display_row)

        #Fill in the image with the numbers and the id
        font = ImageFont.truetype("arial.ttf", 18)
        draw.text((margin_normal, margin_top/3), "Board nr: "+self.id, font=font, fill=(0,0,0))

        font = ImageFont.truetype("arial.ttf", 30)
        for i in range(3):
            for j in range(9):
                number_to_display=display_rows[i][j]
                draw.text((inner_top_left_w+width/4+width*j, inner_top_left_h+height/3+height*i), number_to_display, font=font, fill=(0,0,0))

        return im
