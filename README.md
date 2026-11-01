# COMP-1510-Term-Project-Rewrite

This is a terminal game I made for my python term project, to play simply run game.py in your terminal.

# Playing in the browser

The same game can be played in a browser (the Python runs in the page through Pyodide). From this folder run

```
python -m http.server 8000
```

then open http://localhost:8000. No enter key needed:

- Hold `w`, `a`, `s`, or `d` to move. Time only passes while you hold a direction (3 ticks a second), so standing
  still freezes the world.
- Press `r` then a direction to rewrite once in that direction, just like typing `rw`, `ra`, `rs`, or `rd` in the
  terminal version. Press `r` again to cancel.
- Press `h` for help, and space to start a level or play again.

# Rewriting history

What you do carries over to your next playthrough, and every change can be undone by changing history again:

- Kill Hitler and next time your target is Meinard Goudier. Kill Goudier and Hitler comes back.
- Stop the meteor and the dinosaurs survive, so you play the next run as a dinosaur and have to destroy the raptors'
  meteor defense, then escape before it lands. Make the meteor fall and the humans come back.
- Beat the final boss and your character becomes the next final boss.

History only changes when you finish a level by entering the time machine. The terminal version saves it in
`timeline.json` (delete it to restore the original history) and the browser version saves it in the browser.

# Requirements

|            Requirements            | File, line number |
|:----------------------------------:|:-----------------:|
|         List comprehension         |    map.py, 47     |
|   Selection using if statements    |    map.py, 80     |
|   Repetition using the for loop    |    map.py, 103    |
| Membership operator used correctly |  levels.py, 105   |
|   Range function used correctly    |    map.py, 26     |
|      Itertools function used       |    map.py, 160    |
|         Random module used         |    map.py, 179    |
|     Nicely formatted f-strings     |   text.py, 187    |

# Screen view

Please view the game with a full screen such that the top of the screen shows the top line of the title and the right
edge of the screen still shows the text.

# An excuse for the messy GitHub pushes

Sorry I worked on the train a lot without Wi-Fi and would often get a lot done without being able to push.
I just recently figured out that I can commit the change and then push later so whoops.
I'm pretty sure you'll still dock marks but this is my reason.

# A PSA for Chris:

The "glitchy" look of using the "rewrite" action is intentional.
the fact that it obscures your vision and flips all the text in a line is also intentional.
I wanted to increase the difficulty of the game and add to
the "meddling with forces beyond your imagining"
feel of the game, without adding unnecessary complexity.

# PS

If the game is too hard, read these tips and tricks:

1. If you press r then w, a, s, or d that will create a wall if you do it again it will replace the wall with a
   floor (I don't know why everyone seems to have trouble with that)
2. If it's too hard to track where things are because of the distortion caused by rewriting,
   rewrite immediately after you create the wall in order to remove all the distortion effect.
3. the visual change caused by rewriting doesn't change their actual location on the grid.
4. If you are having trouble with mobs blocking your path, rewrite the walls twice to create a path around them.
5. You can rewrite bullets as they fly towards you.
6. if you are having trouble with the final boss stay still outside his range and keep rewriting in his general.
   direction. He will eventually walk into your range and you will.

