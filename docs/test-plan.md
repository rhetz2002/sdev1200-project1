| Test ID | Category | Description | Expected Output | Actual Output | Pass/Fail |               
|---------|----------|-------------|-------|-----------------|---------------|-----------|               
| TC-001  | Normal | win 10 games in a row | all games run without issue and ready for an 11th game |  |  |         
| TC-002  | Normal | lose 10 games in a row | all games run without issue and ready for an 11th game |  |  |             
| TC-003  | Normal | mixed batch win/lose 10 games in a row | all games run without issue and ready for an 11th game |  |  |            
| TC-004  | Normal | all enemies survive till end | game ends without issue ready for next game |  |  |            
| TC-005  | Edge   | die off screen | game over/ restarts as normal when prompted |  |  |            
| TC-006  | Edge   | "spam" clicking to reset game during game over/win | restart game as normal |  |  |             
| TC-007  | Edge   | (try to) trigger a death as an action input is proccessed | game over should run as normal ready for next game |  |  |              
| TC-008  | Edge   | (try to) trigger an action input right as win is achived | win should run as normal ready for next game |  |  |                   
| TC-009  | Edge   | kill enemies while player is offscreen | enemies should die as normal despawning/removed from active game|  |  |            
| TC-010  | Edge   | have enime kill player while inside another enemie | should prompt game over ready for another game |  |  |              