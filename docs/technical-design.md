# Air Combat Command Design Map             

- modified file structure by adding and removing files from game folder including removing attacks.py, movent.py, and class.py and adding ui.py (done due to changes in design structure)

- removed random timer for enemy movent and fire (was removed due to time constraints)

- removed enemy cluster class (scrapped due to time constraints)

- modified the portion relating to where the game state lives to be more accurate to where it lives now. it resides in the main loop as it made more sense when designing

- added ui elements to classes (needed due to how i ended up approaching ui)

- modified player class by removing life which was removed due time constraints also added the methods attached to the player class

- removed attacks and enemy classes and added corresponding enemy and enemy bullets as well as there methods

## File Structure          
                          
overall folder structure                  
                       
sdev1200-project1            
├── game/                  
│    ├── main.py             
│    ├── ui.py                   
│    ├── enemy.py            
│    ├── player_char.py              
│    ├── script.py                                     
│    └── sprites/                                
├──docs/             
└──README.md   

## classes
                                                                          
 
- title
sprite(file)
xy_location(int,int)
size(int,int)             

- start_button
sprite(file)
xy_location(int,int)
size(int,int)    

- game_over
sprite(file)
xy_location(int,int)
size(int,int)             

- restart
sprite(file)
xy_location(int,int)
size(int,int)

- win
sprite(file)
xy_location(int,int)
size(int,int)             

- title
sprite(file)
xy_location(int,int)
size(int,int)             

- score
font(string)
xy_location(int,int)
text_color(int,int,int)

- player                   
hp (int)             
position (x, y)              
sprite (file)   
size (int,int)
restart(method)
player_con(method)(int)
player_fire(method)
damage(method)

- player_bullet
sprite (file)
fire(method)(x,y)
update(method)

- enemie_orange             
sprite (file)   
size (int,int)
atk(method)
spawn(method)(x)
update(method)

-orange_bullet
sprite(file)
fire(method)(x,y)
update(method)

-enemie_blue
sprite (file)   
size (int,int)
attackL(method)
attackR(method)
attackC(method)
spawn(method)(x)
update(method)

-blue_bullet
sprite(file)
fire(method)(x,y)
update(method)

-blue_bullet2
sprite(file)
fire(method)(x,y)
update(method)

-blue_bullet3
sprite(file)
fire(method)(x,y)
update(method)

-enemie_green
sprite (file)   
size (int,int)
shots_fired(int)
last_shot(int)
attack(method)
spawn(method)(x)
update(method)

-green_bullet
sprite(file)
fire(method)(x,y)
update(method)

## game states

currently the game state lives in the main loop and frequently uses the tick time to reference a function to check a list to see what changes to make

## processes

the game will check for several key events when running

- check game state 

- check in script to check which event/enemies to initiate next 

- check user input for action for player character to take 

- hit detection for shots fired 

- tick game clock up by one 

- run function to move enemy or fire bullet 

- update/draw frame 
