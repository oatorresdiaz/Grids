
# Introduction

## What is Grids?
  Grids is an easy-to-use easy-to-learn game design programming language based on the use of grids. Through the application of a straightforward and elegant syntax, Grids allows creators to bring their game ideas to life in a quick and simple way.
  
## How did Grids come to be? 
  Grids was born out of our love for video games and simplicity. Anyone who's ever been a kid has, at some point or another, loved a game. Whether it's board games, card games, video games or even conversation games, games are a part everyone's life. With Grids, we hope to provide a tool that anyone can use to expand their game library with only one requirement: their imagination!
  
# About the language

## Features
  Grids is all about bringing forth the most functionality with simplicity. To achieve this and more, the language implements the following:
  
- A simple and elegant syntax, making the commands easy to learn.
- An easy-to-use grid-based design.
- Importing of images into the game to use as object sprites.
- Rules to define game conditions.

## Grids Architecture

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/155153101@N04/39924120831/in/dateposted-public/" title="arch"><img src="https://farm5.staticflickr.com/4607/39924120831_d42d81dd3b.jpg" width="411" height="313" alt="arch"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

1. First and foremost, code is written in Grids. 
2. This code is then passed to the lexer in the grids.py file, where the code is tokenized. 
3. After tokenization is successful the parser comes into play (also located in the grids.py file). The parser makes sure the grammar rules are followed and takes the data from the commands. 
4. That data is used to run the intermediate python code. 
5. The main component of the intermediate code is the controller.py file which brings everything together.

# Getting Started with Grids

## Installation

1. Install Python 3 (Get at: https://www.python.org/downloads/)
2. Install Pillow (Instructions at: https://wp.stolaf.edu/it/installing-pil-pillow-cimage-on-windows-and-mac/)
3. Download Grids (https://github.com/orlandoecool/Grids/archive/master.zip)
4. You're all set and ready to start making your first game!

## Making your first game

1. First things first, we need to create our play area. The play area is the window where the game will run. To do this we will first create a window of size 500x500px. Afterwards will add a gameplay grid on top. To achieve this, we must run the following commands:
 
   Create Window(500,500)
   Create Grid(3,3)
 
2. Now that we have our play area, we’ll want to add some sprites to our game to use as our player objects. For that, we’ll do:
 
   Create Sprite(x.png, 150, 150)
   Create Sprite(o.png, 150, 150)     	
 
   Note: We can call x.png and o.png this way because they are located in Grids source folder, otherwise we’d have to use their file path.
 
3. Next we must deal with the game’s winning condition. As we all know, tic-tac-toe is won by filling three consecutive slots with your corresponding player (x’s or o’s).  In our game, that means that the player’s sprite must occupy three consecutive slots. We’ll check for this by adding winning positions in every possible direction as follows:
 
   Add WinPos((0,0), (0,1), (0,2))
   Add WinPos((1,0), (1,1), (1,2))
   Add WinPos((2,0), (2,1), (2,2))
   Add WinPos((0,0), (1,0), (2,0))
   Add WinPos((0,1), (1,1), (2,1))
   Add WinPos((0,2), (1,2), (2,2))
   Add WinPos((0,0), (1,1), (2,2))
   Add WinPos((0,2), (1,1), (2,0))
 
   Note: Each one of these lines define a winning line on the grid. The player must get a sprite on each of the parameter position to win by one of these rules.
 
4. All that is left now is to add a Controller object to receive player input, and a Draw object to handle the drawing of the sprites.
 
   Create Controller
   Create Draw(x.png, o.png)
 
5. Finally, our tic-tac-toe is ready to be played!
 
   Start

## Watch the video below to see all the steps executed:'

<iframe width="560" height="315" src="https://www.youtube.com/embed/asMcIkwMqhQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

# Documentation
Learn more about Grids [here](https://github.com/orlandoecool/Grids/wiki).

