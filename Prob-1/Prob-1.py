"""
NTEC 361
date: <ex: mm/dd/yyyy>
<your name>
Name: <assignment/lab name>
Description: <assignment/lab description>
"""

# INSTRUCTIONS:
#   Update comment block above
#   Insert a comment above EACH line of code in the program below to describe
#   what the code does. Make sure your lines are within the 80 column max.


from graphics import *

def main():
     win = GraphWin()
     shape = Circle(Point(50,50), 20)
     shape.setOutline("red")
     shape.setFill("red")
     shape.draw(win)
     for i in range(5):
          p = win.getMouse()
          c = shape.getCenter()
          dx = p.getX() - c.getX()
          dy = p.getY() - c.getY()
          shape.move(dx,dy)
     win.close()

main()