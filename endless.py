import os
import threading
import time

import keyboard
import pyautogui as pya

import printables as mprint

# Setup variables

targetAscensions = None
correct = False
while not correct:
    try:
        value = int(input('Write how many ascension you already have done: '))
        assert(value > 0)
        targetAscensions = 999 - value
        correct = True
    except:
        print('The format is not correct or the number is too big')
    
# Delays, modify if your PC is Fast, mine is not.
# Default are tiny: 0.2 seconds and medium: 0.8 seconds
tinySleep = 0.2
mediumSleep = 0.8
loops = 1  # # # DON'T CHANGE THIS ONE
endingDelay = loops * 0.05  # Adds a delay before ascending

# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # DO NOT MODIFY BELOW # # # # # # # # #

# Where the coords will be stored
spotsDict = {
        'All Upgrades' : (0, 0), 
        'Cursors' : (0, 0),
        'Grandmas' : (0, 0),
        'Legacy' : (0, 0),
        'Reincarnate' : (0, 0)
        }

# Functions
def buy100s():
    pya.keyDown('shift')
    pya.click()
    time.sleep(tinySleep)
    pya.click()
    time.sleep(tinySleep)
    pya.click()
    pya.keyUp('shift')

def buyUpgrades():
    time.sleep(tinySleep)
    pya.moveTo(spotsDict['All Upgrades'], duration = 0)
    pya.click()
    time.sleep(tinySleep)
    pya.click()
    time.sleep(mediumSleep)
    pya.click()


def buyBuildings():
    time.sleep(tinySleep)
    buyUpgrades()
    time.sleep(tinySleep)
    pya.moveTo(spotsDict['Cursors'], duration = 0)
    buy100s()
    pya.moveTo(spotsDict['Grandmas'], duration = 0)
    buy100s()
    time.sleep(tinySleep) 
    buyUpgrades()
    pya.moveTo(spotsDict['Cursors'], duration = 0)
    pya.click()


# Adding a manual stop, this will finish the ascension and stop from looping
def stop():
    controller = True
    while controller:
        if keyboard.is_pressed('q'):
            os.system('cls')
            print('\n\n\t> Key \'q\' pressed, Handmade stopped.\n\t'+ str(targetAscensions-loops) + ' ascensions remaining.')
            controller = False
            altTabTo('last')
            pya.moveTo(0, 0, duration = 0)
   
# Tab function
def altTabTo(window):
    if window == 'last':
        pya.hotkey('alt', 'tab')
    else:
        pya.getWindowsWithTitle(window)[0].minimize()
        pya.getWindowsWithTitle(window)[0].maximize()
      
########################################################################### Start
thread = threading.Thread(target=stop)
os.system('cls')
mprint.cookieLine()
mprint.title()
mprint.cookieLine()
print('\n\tWelcome to Gabbo5001\'s Endless Cycle Is No More!'
      '\n\nThis is a script, it will perform automatic actions. Do not fear it. Should not harm anything.'
      '\n-Remember to disable any mods related to buy/ascend purposes.'
      '\n-Make a backup in case this does fail.'
      '\n-You can stop the process in any moment pressing \'q\' on your keyboard')
mprint.credits()
print('\n\n\tNow we need some button locations of your screen. Please do not open other tabs \
      outside Cookie Clicker and your terminal.\n')

# Loop the dict to record coords
for item in spotsDict:
    print('In your game, move your cursor where the Buy '+ item + ' button is.'
          '\nWhen ready, press \'Spacebar\' to record Buy '+ item + ' button\'s position in your screen.')
    print('Press \'Enter\' to alt-tab to Cookie Clicker.\n\t>')
    input()
    altTabTo('Cookie Clicker')
    done = False
    while not done:
        if keyboard.is_pressed('space'):
            x, y = pya.position()
            spotsDict[item]= x, y
            print(item +' button\'s location saved!\n\n')
            done = True
            altTabTo('last')

mprint.cookieLine()
print('Press \'Enter\' to start\n')
mprint.theFun()
print('\n\t>')
input()
thread.start()
altTabTo('Cookie Clicker')
pya.moveTo(spotsDict['Reincarnate'], duration = 0)
pya.click()
pya.press('enter')
loops+=1

while loops <= targetAscensions:
    # Add more buyBuildings if you don't achieve +1 prestige with 2 of them
    buyBuildings()
    buyBuildings() 
    time.sleep(mediumSleep)
    buyUpgrades()
    time.sleep(1+endingDelay) # Maybe this delay is not needed depending on your prestige level
    # Reincarnation sequence
    pya.press('home')
    time.sleep(0.2)
    pya.moveTo(spotsDict['Legacy'], duration = 0)
    pya.click()
    time.sleep(0.5)
    pya.press('enter')
    time.sleep(0.5)
    pya.press('esc')
    pya.moveTo(spotsDict['Reincarnate'], duration = 0)
    pya.click()
    pya.press('enter')
    # Console Log of The Fancy Numbers
    os.system('cls')
    mprint.cookieLine()
    mprint.ascensionTitle()
    mprint.fancyNumber(targetAscensions-loops)
    mprint.cookieLine()
    loops+=1 # Ascensions counter
