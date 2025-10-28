# Dungeon_of_Darkness
An RPG game created by Ted Irland and modified by Lewis Foggie.

## Purpose of This Document
This repository demonstrates code modification, evaluation, and documentation 
skills relevant to the thought process and skillset of a software engineer in relation to the Sales Engineer position at Codility.

## Skills Demonstrated for technical aspect of Sales Engineer Role  
✅ **Code Assessment** - Systematic evaluation using Codility's COMPASS framework  
✅ **Problem Identification** - Proactive recognition of scalability issues  
✅ **Balanced Analysis** - Transparent about tradeoffs and limitations  
✅ **Forward Planning** - Architectural thinking for future maintainability  

## Installation & Usage
Run from terminal on macOS:
```bash
python3 main.py
```

# Summary of Modifications from Ted's Original Code
1. Added "Settings" page button to Main Menu.
2. Added `control_scheme` variable to modify whether controls are with WASD or ARROW keys for up-down-left-right movement.  
3. Added "KO!" indicator when a monster dies.

**Changes and Evaluation Based Upon COMPASS Evaluation Criteria**  
Code changes are summarised but also evaluated according to COMPASS main criteria.  
**COMPASS Evaluation includes**  
1) Correctness (ability to solve problem and pass test cases)  
2) Efficiency (Optimisation of number of operations to complete task)  
3) Quality (Readability, Possibility to Scale and Maintain)  

## 1. Settings menu feature  
### Summary of Changes  
Added a "settings" page which enables changing the control settings for movement between WASD or ARROW keys via `control_scheme` variable.  
#### Technical Implementation  
**`main.py`**  
Added a `show_settings` game variable defaulted to "False".  
Set default `control_scheme` = "ARROWS". (Based upon Lewis' default preferences though some users may prefer defaulting to "WASD")  
Added button images   
- `settings_img`
- `wasd_img`  
- `arrows_img`

Added buttons  
- `settings_button`  
- `wasd_button`  
- `arrows_button`

Added rectangle  

Within `if not start_game:` loop  
- added `settings_button.draw(screen)` to show on main menu  
-   if button is clicked then `show_settings` = True which triggers the ->  
-> added `if show_settings:` loop  
-   draws the boxes, texts and buttons for the settings screen  
-   added a rectangle highlighting whether WASD or ARROWS control_scheme is selected  
-   added an escape so when "esc" keyboard is pressed it returns to main menu (`show_settings` = False)  
-   control the `control_scheme` variable by clicking "WASD" or "ARROWS" buttons in "Settings" page.  

In `take keyboard presses` section, added if statements for keyboard controls depending on `control_scheme` used. 

### COMPASS Evaluation  
**Correctness:** ✅  
Fully functional. Meets all requirements.  
**Efficiency:** ⚠️  
Current implementation prioritises rapid feature delivery over efficiency.  
Future problem: In the case where the "settings" window would be available in "pause" mode, there would be duplicate settings functions when there could be just one meaning more lines of code to run the same operations.  
Problem: .png files are 50% bigger than real size as defined in the code, so they take unnecessary memory. Negligible in this context but non-negligible in highly-scaled contexts.  
Recommendation: refactor to state machine pattern before scaling and reduce .png image sizes to optimise memory.  
**Quality:** ⚠️  
Current implementation prioritises rapid feature delivery over maintainability/scalability.  
Future problem:  in the case where the "settings" window would be available in "pause" mode, there would be duplicate settings functions meaning that changes would need to be made manually in both functions, and the game state itself would not mutually exclusive but instead defined as a sub-state of "pause" mode in pause mode, though it is defined as an actual state in the main menu mode.  
Recommendation: refactor to state machine pattern before scaling.  

### Other Suggested Changes  
A) Add settings page to "Pause" menu so user can change control settings whilst in game without having to quit completely.  
New state machine pattern should possibly be defined in terms of a new variable `game_state` = "PAUSE" or game_state = "SETTING" instead of `pause_state` = TRUE or FALSE.   
B) Fix red rectangle fit to WASD and ARROWS buttons.  

## 2. Adding "KO" indicator to combat mechanism  
### Summary of Changes  
**`weapon.py`**  
Added an if statement in `weapon.py` to check if object health is less than 0.  
changed `damage` to `temp_damage` in order to conduct the if statement.  
If target is dead then `damage` = -999.  

**`main.py`**  
Added an if statement in main.py to check if `damage` is -999. If it is then the target is classed as killed so the damage meter is converted to a string - "KO!"  

### COMPASS Evaluation of Combat Mechanism Changes
**Correctness:** ✅  
Fully functional. Meets all requirements.  
**Efficiency:** ⚠️  
Current implementation prioritises rapid feature delivery over efficiency.  
Future problem: There are two long lines of operations to create the damage text. It is probably possible to optimise this to less operations, negligible for now, but more important when considering future additions to damage controls:  
- damage over time
- critical hits
- self-healing

**Quality:** ⚠️  
Current implementation prioritises rapid feature delivery over maintainability/scalability.  
Future problem: The conversion of damage numbers to text requires a specific if statement. for example `damage` = -999 denotes death i.e. "KO!" but an addition of critical hits or damage-over-time would denote a "!" or "-" or "+" to represent each different damage category. For the purposes of future scalability it would possibly be necessary to instead denote a "damage type" as an input to the damage text function so as to leave it as a one-liner instead of converting e.g. -999 to "KO!" and then inputting. Otherwise there will probably end up being 5 relatively similar lines instead of a 1-liner damage function with damage type as an input.  

Author  
Lewis Foggie  

Contact link
lewisfoggiemsc@gmail.com
