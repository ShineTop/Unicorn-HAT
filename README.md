These are my programs for the Pimoroni Unicorn HAT.

For Unicorn HAT installation insctructions, check out this site:
https://github.com/pimoroni/unicorn-hat

To get started writing your own programs for the Pimoroni Unicorn HAT, check out this site:
http://docs.pimoroni.com/unicornhat/


# Running the programs
Download the programs. You can either download them from above or use git.

![UnicornHAT_git_01](https://user-images.githubusercontent.com/13591438/71389784-716c6100-25c3-11ea-92aa-a66a0205043d.png)

After downloading or cloning, chage to that directory.

![UnicornHAT_git_02](https://user-images.githubusercontent.com/13591438/71389787-73cebb00-25c3-11ea-9870-80a0c1f3373c.png)

To see all the programs, type **ls**
![UnicornHAT_git_03](https://user-images.githubusercontent.com/13591438/71389788-76311500-25c3-11ea-8cd8-aac5a063029b.png)

To run a program, type **sudo python** and then the name of the program. For example, **sudo python pibow_candy_demo_UnicornHAT.py**
![UnicornHAT_git_04](https://user-images.githubusercontent.com/13591438/71389797-7a5d3280-25c3-11ea-9a41-9706a457399d.png)
  
Alternatively, you can make each program executable. To do this, type **sudo chmod +x** and then the name of the program.
For example, **sudo chmod +x pibow_candy_demo_UnicornHAT.py**
![UnicornHAT_git_05](https://user-images.githubusercontent.com/13591438/71392623-56ebb500-25ce-11ea-9058-7787aa65cff9.png)

Now if you type **ls**, you will notice the program is a different color.
![UnicornHAT_git_06](https://user-images.githubusercontent.com/13591438/71392630-5ce19600-25ce-11ea-8669-ff4a3684f597.png)
  
Then to run the program, type **sudo ./pibow_candy_demo_UnicornHAT.py**
![UnicornHAT_git_07](https://user-images.githubusercontent.com/13591438/71392635-60751d00-25ce-11ea-8bbe-7d7df0828340.png)

# Pibow Candy
Contains programs using only the pastel colors of the Pibow Candy case. Choose which individual ones you like, or get a taste of all of them with the pibow_candy_demo.py program. These programs are written in Python 3.

# Pibow
These programs feature only the colors of the Pimoroni Pibow Case:
 * Raspberry
 * Red
 * Orange
 * Yellow
 * Green
 * Blue
 * Violet
 * White (representing the clear layer)
 
 # Choose Your Own Colors
 These are the programs that I wrote for the Pimoroni UnicornHAT, but you get to choose your own colors.

1) Use a webite like https://rgbcolorcode.com to get RGB color codes.

2) Open the bfp_unicornhat.py file and scroll down to the following section:

```python
########################################################################
#                      CHOOSE YOUR OWN COLORS                          #
########################################################################
#   Feel free to modify the Red, Green, and Blue color tuples below.   #
#   Then make a note on the right side with that color.                #
#   Modify ONLY the section directly below.                            #
########################################################################

C1 = (255, 0, 0)         # Color 1: Red
C2 = (255, 128, 0)       # Color 2: Orange
C3 = (255, 255, 0)       # Color 3: Yellow
C4 = (0, 255, 0)         # Color 4: Green
C5 = (0, 0, 255)         # Color 5: Blue
C6 = (0, 204, 204)       # Color 6: Indigo
C7 = (127, 0, 255)       # Color 7: Violet
C8 = (255, 255, 255)     # Color 8: White
C1H = (128, 0, 0)        # Half the values of Color 1
C2H = (128, 64, 0)       # Half the values of Color 2
C3H = (128, 128, 0)      # Half the values of Color 3
C4H = (0, 128, 0)        # Half the values of Color 4
C5H = (0, 0, 128)        # Half the values of Color 5
C6H = (0, 102, 102)      # Half the values of Color 6
C7H = (64, 0, 128)       # Half the values of Color 7
C8H = (128, 128, 128)    # Half the values of Color 8
```

By default, the colors are the colors of the rainboow, but you can insert your own color codes. Each number in the tuple
represents red, green, and blue respectively. For example:

(255, 0, 0) is the RGB tuple for the color red. 255 reprents red , 0 represents green, 0 represents blue.

You can insert your own red, green, and blue color tuples. Then on the right-hand side, you can make a note of which color you
chose. For example, if you want Color 1 to be "Air Force Blue", change the line to read

```python
C1 = (93, 138, 168)         # Color 1: Air Force blue
```

Then change the C1H line to read

```python
C1H = (46, 69, 84)        # Half the values of Color 1
```

Once you have all the colors you want (even duplicate colors - you don't have to have 8 different colors) save the file and
then run one of the programs.
