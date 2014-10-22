##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github
from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)


#create_square(top left x,top left y, bottom right x, bottom right y, fill color)
square = drawpad.create_rectangle(300,200,400,300,fill='red')
door = drawpad.create_rectangle(340,270,360,300,fill='brown')
#this will be all the windows 
drawpad.create_rectangle(310,220,330,240,fill='white')
drawpad.create_rectangle(370,220,390,240,fill='white')
drawpad.create_rectangle(310,260,330,280,fill='white')
drawpad.create_rectangle(370,260,390,280,fill='white')
#grass  
drawpad.create_rectangle(260,300,440,320,fill='green')
# create_oval(x,y,width,height,fill color)
oval = drawpad.create_oval(350, 280, 360, 290, fill='blue')
#create_line(top left x,top left y, bottom right x, bottom right y, fill color)
line = drawpad.create_line(300,200,350,140)
line2 = drawpad.create_line(400,200,350,140)
#chimney lines
drawpad.create_line(370,140,370,165)
drawpad.create_line(370,140,400,140)
drawpad.create_line(400,200,400,140)
root.mainloop()