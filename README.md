# 🚧: Currently undergoing improvements and a thorough refactor


## Breakout Nether
> Breakout is an arcade game developed and published by Atari, Inc., and released on May 13, 1976. Breakout, a layer of bricks lines the top third of the screen and the goal is to destroy them all by repeatedly bouncing a ball off a paddle into them

Python @ version 3.7.2

## You want to play? Here is your TL;DR
- Clone repository, and navigate into `/breakout`
- Install dependecies `python -m pip install pygame`
- Run game `py breakout.py`
- Standard keys for movement, if unsure - see below

## Controls
| Key | Description |
| --- | --- |
| Left/right arrow | Move paddle horizontally |
| Esc | Exit game |



## Article
- [Contents of repository](#contents)
- [Tech usage and reasoning](#tech-usage-and-reasoning)
- [Design](#design)
- [Final Thoughts](#final-thoughts)
- [References](#references)

# Contents 
Featuring the classical functionalities that the orginal Breakout game came with.
- Arrow-key controlled paddle
- Multiple line sof bricks for you to break
- A bouncing ball that destroys bricks
- Counter of bricks breaken
- Feedback on game statuses: win or loss!

# Tech Usage and Reasoning
Written in Python. Great OOP language, many brillianty helpful modules to use when developing games. 

## Sprite

The term sprite origins back to the older game machines in a time where the animation of a
game was not fast enough for them to work as games. The “sprite” objects with its limitations
can draw and be updated very fast and is common whenever a 2D game is animated. Sprit can
be split into two classes.

The first class is the “Sprite Class” which is used as a base for all the game objects, without
actually doing anything, they are carrying different functions to help control the game object.
This sprite keeps track of which groups it belongs to. It consists of a class constructor (__init__)
that takes an argument of a Group that this Sprite should belong to, in this assignment i.e. the
brick Sprite belongs to the bricks Group. You are able to change the Group membership as you
would like for the Sprite by add() and remove() methods.

The other class is the “Group Class” which is a container that holds the different Sprite objects,
these with executable tasks such as, draw all the elements they contain. As a container it gives
you similar functions as the Sprite class so you can add() and remove() what sprites belong to
the specific group. In this game animation is involved, and the Group class has another ability
where it has an update method, which would call on an update on every sprite in the group and
animate. Here in the game as an example it would be the player pad updating its position.

Now combining these two classes is the most efficient use of them, as these two separately do
not do much more than what simple list and classes can do for game objects. Adding and
removing groups and sprites from each other goes more quickly, as with blocks, instead of
adding “block1”, “block2” attributes, it can simply be placed in groups.

## Collision Detection

The sprite module also comes with collision detection functions, which works great for simpler
games like this version of breakout. There are two functions, but the one used here is:
“spritecollide(sprite, group, dokill)”, which checks for a collision between a single sprite and
the sprites in a group, if it detects a collision, then the “dokill” must be true/false and executes
the following thereafter.

# Design
All objects are of the type Sprite with their assigned group classes. Referring to figure 1 under,
the three sprites(block, ball, player) are connected to the each other which finally turns to the
breakout main. The player is the object that controls the game, without interacting here, much
wont happen other than ball will fall below screen and game will be lost. The player object is
controlled by key intel so that if the ball collides with the player, it bounces, and further on if
the ball gets controlled properly so the ball object manages to go to a block object, it will
remove the block and bounce again. If the ball is controlled in a way it collides with the wall
instead, then it is the breakout-part that decides the outcome, and not the object classes, as the

boundaries are bound to the width and height of the screen which is connected to the breakout-
part. There will only be one ball and one pad at all times, but the amount of blocks are easily

changed externally outside the main game file. This is also a part of the design to split up the
game code into parts, one for the graphics, one for the variables, and the main file which takes
use of the two files to prevent bugs during value changes.
<p align="center">
	<img src="https://user-images.githubusercontent.com/64463510/141191903-be4c2f06-8abf-4157-bc0b-107e9ae3d42d.png" />
</p>

# Final Thoughts
I find a lot of personal joy through playing this game, and hence the motivation behind this project and reasoning for why I wanted to update this older project of mine. 

# References
- [Pygame Sprite Module Introduction](https://www.pygame.org/docs/tut/SpriteIntro.html)
- [Making Breakout in Python Part 1: Creating our game screen](https://www.youtube.com/watch?v=_IuG6FvDqdY)
- [Making Breakout in Python Part 2: Creating our paddle](https://www.youtube.com/watch?v=AAQAQvwWfNs)
- [Program Arcade Games](http://programarcadegames.com/python_examples/show_file.php?file=breakout_simple.py)
- [Pygame Shmup Part 7: Score (and Drawing text)](https://www.youtube.com/watch?v=U8yyrpuplwc)
- [Bricka (a simple Breakout clone)](https://www.pygame.org/project-Bricka+(a+simple+Breakout+clone)-1832-.html)
- [Breakout UML Class Diagram](https://creately.com/diagram/example/hdfowvci2/Breakout%20UML%20Class%20Diagram)
