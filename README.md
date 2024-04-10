# Achieving Endless Cycle Backseated

## Run this code, leave your game overnight, get Reincarnation and Endless Cycle achievements

> This works with v2.052 and probably with most of older version, though is not guaranteed. For any question/problems fell free to contact me.

:cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie:

> I chose to _copy_ a bunch of code  
> Instead of clicking a bunch of times.  

## What is this

This is a script, an automated process to ascend a certain number of times: more specifically, it asks the current number of ascensions done and performs the remaining to reach 1000. To make it, the program needs the user to record their mouse position in some key places in order to achieve ascensions without further help.

## Requirements

- Cookie Clicker Game Running
- Any Python IDE (Visual Studio Code, PyCharm, ...)
- Python installed in your computer (If you don't know how to install it don't worry, it's just one Google search away i promise :)
- Open your terminal (search it on the app-bar) and move inside the folder of the project
-  Install the requirements by copy and pasting the following on your terminal (Write terminal in your app bar)

````bash
python -m pip install -r requirements.txt
````

Once you got everything ready, you can run the script pasting the following on your terminal

````bash
python endless.py
````

## Instructions

\-> Once the script starts, after asking the current number of ascension already done, it will ask you to do an ascension alt-tabbing to the script until it gathers all the information it needs, and then it will repeat the process all the times you set it for. The script takes into account this first ascension.

:exclamation::exclamation::exclamation: Remember to _**UN VAULT**_ any upgrade you might have vaulted! If the vault appears in one off the ascensions all the pots will move (because the game needs to pop the vault in between) and it might fail to ascend!

Spots that the script will ask you for:
<!-- markdownlint-disable MD033-->
| 1. Buy All Upgrades Button | 2. Buy Cursors Button  | 3. Buy Grandmas Button
| ------------- | ------------- | ------------- |
| <a href="https://imgur.com/qzpUl6i"><img src="https://i.imgur.com/qzpUl6i.jpg" title="source: imgur.com" /></a> | <a href="https://imgur.com/xGTRaww"><img src="https://i.imgur.com/xGTRaww.jpg?1" title="source: imgur.com" /></a> | <a href="https://imgur.com/2LwE58Q"><img src="https://i.imgur.com/2LwE58Q.jpg?1" title="source: imgur.com" /></a> |
<!-- markdownlint-enable MD033-->
Then, the 2 lasts spots are the 'Legacy' button and the 'Reincarnate' button, and that will be the final steps of the 'hand-made' ascension. After that, the script will start copying the process.
<!-- markdownlint-disable MD033 -->
| 6. Legacy Button | 7. Reincarnate Button  |
| ------------- | ------------- |
|<a href="https://imgur.com/HalsZm0"><img src="https://i.imgur.com/HalsZm0.jpg" title="source: imgur.com" /></a>  | <a href="https://imgur.com/kWjBlW3"><img src="https://imgur.com/kWjBlW3.jpg" title="source: imgur.com" /></a> |
<!-- markdownlint-enable MD033-->
And everything's ready! :sunglasses: Now the script will start to run when you press 'Enter'.

## Advanced tips (only if you know a little about Python)

\-> Speed of the script may be improved: change _tinySleep_, _mediumSleep_ or _endingDelay_ and test your setup. Both your pc performance and the prestige levels you already have will affect how fast you can ascend. Remember prestige scales, and in 1000 ascensions it _does_ scale.

````text
Package Versions:
- Python: 3.10 (with modules time and threading)
- PyAutoGUI: 0.9.53
- keyboard: 0.13.5
````

> Inspired by Pegasus280.
