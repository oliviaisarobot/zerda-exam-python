# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

The third exercise is using a for loop. What it does is, it goes through the letters of the string starting with the first letter. Then it checks if the current letter of the string matches the letter given as a parameter. If it does, it adds one to the counter and the for loop continues, if it doesn't, the for loop continues. The for loop will keep running until it reaches the last letter in the string. After the last letter, it breaks out of the loop and returns the value of the counter.

![alt text](https://github.com/oliviaisarobot/zerda-exam-python/blob/master/forloop.jpg?raw=true "For loop flowchart")

### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:

First you need to import a module that will allow you to create an interface, such as Tkinter. Tkinter is a built-in graphical module for python, it means it doesn't require installation. While using Tkinter, you first need to name your mainloop ("base" or "root"). The mainloop will allow the window with all the graphical elements to stay open until you click the quit button. Within the mainloop, you need to create a canvas, by defining its containter (which will be name of your mainloop), and its width and height. Once you created the canvas, you need to pack it, to allow it to be displayed in your main window. After that, you can create a rectangle right on the canvas, by defining the x and y coordinate of its top left corner, then the x and y coordinate of its bottom right corner. Optionally, you can give your canvas a background color, or your rectangle a fill or a border color.

Example code:

```python
root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_rectangle(100, 100, 200, 200, fill="pink")

root.mainloop()
```

### What does V stand for in MVC? [2p]
#### Your answer:

The MVC means Model View Controller, which is a code structuring rule that separates the code of the data from the code of the display and the code of the working logic. The V stands for the View, which includes everything that has to do with display or the visual representation of our code - everything the user will see. The View is in a uni-directional relationship with the Controller, which means that the Controller can pull information from the View, and also update for example the positioning of certain elements. The View, however, can't influence how the Controller works, and has no connection to the Model.
