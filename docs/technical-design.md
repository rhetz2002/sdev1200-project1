# Air Combat Command Design Map             

- modified file structure by adding and removing files from game folder including removing attacks.py, movent.py, and class.py and adding ui.py (done due to changes in design structure)

- removed random timer for enemy movent and fire (was removed due to time constraints)

- removed enemy cluster class (scrapped due to time constraints)

- modified the poertion relating to where the game state lives to be more acurate to where it lives now. it resides in the main loop as it made more sense when designing

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

- enemy 1,2,3           
hp (int)               
attack type (int)           
sprite (file)             

- attacks 1,2,3                
damage (int/range of ints)           
animation/sprite (file)              
position (x, y)                                                                            
 
-              

- player           
life (int)          
hp (int)             
position (x, y)              
sprite (file)           

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
