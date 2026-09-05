# Air Combat Command Design Map             
            
## File Structure          
                          
overall folder structure                  
                       
sdev1200-project1            
├── game/                  
│    ├── main.py             
│    ├── attacks.py                  
│    ├── movement.py    
│    ├── enemy.py            
│    ├── player.py              
│    ├── script.py            
│    ├── class.py                               
│    └── sprites/                                
├──docs/             
└──README.md   

## classes

- enemy 1,2,3           
hp (int)               
attack type (int)           
sprite (file)             

- attacks 1,2,3                
damage (int/range of ints)           
animation/sprite (file)              
position (x, y)                                                                   

- enemy_cluster (I envision the enemies working a little like Galaga/space invaders, moves the entirety of the enemies on screen)           
position (x,y)             
number of enemies (int)           
random movement  (int)           
 
- game state           
game time (int)            
pause (bool)          
start (bool)         
end (bool)              

- player           
life (int)          
hp (int)             
position (x, y)              
sprite (file)           

## game states

Most if not all of the game state lives in the game state class, making it clean to keep track of. I could also just have the bulk of it live in main with a clear start and end but I will see. Having it be a class may make handling a loop like (start into a menu screen, get into game, end, back to menu, restart) easier 

## processes

the game will check for several key events when running

- check game state 

- check in script to check which event/enemies to initiate next 

- check user input for action for player character to take 

- several random timers for enemy attack and movement  

- hit detection for shots fired 

- tick game clock up by one 

- run process to move enemy or player 

- update/draw frame 
