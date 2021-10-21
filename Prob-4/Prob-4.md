# Graphics - Problem 4

**Goal**
- Student uses interaction to create picture

**Instructions**

- You are to write a program that allows the user to draw a simple house using five mouse-clicks (see the diagram). 
- Comment sections of your code to explain what each section does.
- The first two clicks will be the opposite corners of the rectangular frame of the house. 
- The third click will indicate the **center** of the top edge of a rectangular door. 
- The door should have a total width that is 1/5 of the width of the house frame. 
- The fourth click will indicate the **center** of a square window. 
- The window is half as wide as the door. 
- The last click will indicate the peak of the roof. 
- The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.
- See the diagram below

**Suggestions**
* Develop this program incrementally:
    * Start with getting the first two points and drawing the first rectangle
    * Test to make sure this code works.
    * Then, get the next point and calculate the corners of the door. Read the specs above. How do you calculate the width of the door? What is the distance from point 3 and the top corner of the door? 
    * Test to make sure this code works.
    * Next, get point 4. Read the specs above and figure out what calculations you need to make.
    * Test to make sure this code works.
    * Last, get point 5 and draw lines to the top two corners of the house. Hint: you already have the point for one corner. You will need to calculate the point for the other corner.
* Do a final test to make sure your program behaves as expected.



![Diagram of 5-click house](5-click-house.png)