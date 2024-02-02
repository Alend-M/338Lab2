# 4.1 Algorithm Selection
I would use a iterative search. Where I would walk down the left following the signs information and look at each individual room till I find EY128.

# 4.2 Steps
It would take 30 steps. This is because it would take 15 steps to progress 1 room, and another 15 steps in the searching process to check the room number. In total 30 steps.

# 4.3 Case Type
This is the worst case. 

This is because we know the range is 100 - 130 so we know the last room is 130.

 Which allows EY 128 to be anywhere in between those points, however 128 is placed at the furthest point in the 102-128 range of possible positions. 

# 4.4 Big O
### Best Case: 
Best case with this sign layout would be the second room we encounter would EY 128 while the first room is EY 130
### Worst-Case: 
The worst case is would be that the first room is EY 100 and EY 128 be the second last room we encounter walking down the left hallway. 

# 4.5 Memorization
With memorization, a improvement to the algorithm would be going right instead of left to start iterating. This is because we memorized EY 128 is near the end of the left path but near the start by the right path.


