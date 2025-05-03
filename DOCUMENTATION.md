
# Ren'py
Ren'py is a language used specifically for the engine of the same name, opporating similarly to and accepting support for python 3. Each new game project under that engine uses one specific script for the entire game unless programmed otherwise internally. How it opporates is that it takes each `label` as an individual function that it runs in order to how its formatted unless directed otherwise with `jumps`, starting from the `start` label. 
<br>While there might be other scripts used to format UI or 2D assets, only one script is used to run dialogue in this project.

# Gameplay Loop
The play session consists of "work days" and "sundays" which can be broken up similarly. 
<br> With each work day heres an "early morning" phase, "afternoon" phase and "night" phase.
On an in-game "monday" you choose what action takes over that slot for the entire week, increasing and decreasing certain values. By improving or diminishing some traits, you can capture the attention of the various love interests. 
<br>Sundays are "free days" where the afternoon is replaced with another morning slot, and the option to go shop for special items.
<br>
Early mornings and nights serve to help balance the players stats. Mornings even opening the possibility to take "map" events which give different stat boosts and events. For example, if holiness has been exhausted to a low enough amount, you can pray during either period at the cost of your reputation. Its a game of keeping your numbers balances and also in the favor of which route you might want to take.

# Stats

```sh
#default holiness = 100
default Work_stats = { "Reputatn.": 30, "Clean":30, "Cuisine": 30, "Charm": 50 }
default Self_stats = { "Holiness": 100, "Social" : 50, "Fitness": 40, "Smarts": 50, "Stylish" : 50 }

## For lyra's's's appearances!
default Secret_stats = {"Sabatoge": 0}
```
Stats, apart from Holiness is broken up into dictionaries. I found this was easier than estabishing a lot of different variables to reference later on. Each stat interacts with each other in a different way, for example: when visiting the library your smarts and charm stats will increase while social and holiness decreases. Stats can increase or decrease based off of an action the player decides to take.
<br> Holiness works a lot like a "stress meter" found in this genre of game, the player starts out with 100 holiness and this decreases with every chosen action. Like the titles that came before it, if this central stat isn't managed, the player recieves consequences that can affect your stats and your ending if things get too bad.
<br> `Sabatoge` in this case keeps tabs on when the player intentionally chooses incorrect dialogue options and thus gives more of a likelihood for a secret romance option showing up.

<br>

```sh
#for flag checks
default Total_affec = {"Madoc": 0, "Charon": 0,"Tamura": 0}
```

```sh
default current_topic = ""

## Topic dicts/list
default Topics = {"sweet or sour foods?" : "Sweet_or_sour_foods", "favorite artist?" : "Favorite_artist", "favorite meal???": "Favorite_meal", "Inspiration?" : "Inspiration", "weather????" : "Weather"}
default Talking_points = [x for x in Topics]

default current_host = ""
```
These stats are love-interest specific. Those dictionaries hold the affection levels for the current romancable interests and talking points the player can access on sundays. 

## Stat Generating
Stats are managed and generated with "Actions". Functions related to stat generating are located in `action_funcs.rpy`. <br> 
Because of the `init python:` to the top of the script, each class is read at initalization time, just before the rest of the game. 
Every action found within the game has a class associated with it, it's structure can be broken up into 4 different parts.

```sh
 class Pray():

        def success():
            global Self_stats
            global Work_stats
            nar2("A prayer brought serenity.") ## narration
            Self_stats["Holiness"] += renpy.random.randint(10,15) ## pulls random intergers between two specified numbers
            Work_stats["Reputatn."] -= renpy.random.randint(3,5)

        def slightly_less():
            global Self_stats
            global Work_stats
            nar2("A desprate prayer brought some peace.")
            Self_stats["Holiness"] += renpy.random.randint(10,15)
            Work_stats["Reputatn."] -= renpy.random.randint(3,5)    

        def sucks_():
            global Self_stats
            global Work_stats
            nar2("A desprate prayer brought some clarity.")
            Self_stats["Holiness"] += renpy.random.randint(20,25)
            Work_stats["Reputatn."] -= renpy.random.randint(3,5)

        def holy_switcher():
            global Self_stats
            global energy 
            energy -= 1
            renpy.show_screen("pray_action")
            if(Self_stats["Holiness"] >= 60):
                
                Pray.success()
                renpy.pause(1.8, hard=True)
            elif (Self_stats["Holiness"] >= 40):
                
                Pray.slightly_less()
            else:
                
                Pray.sucks_()
```
```sh
label pray_action:

    call stats_action ## shows action_screen
    $ Pray.holy_switcher() 
    
    return
```
When `pray_action` is called, the label gets the function from the pray class. From here, it checks the holiness stat to "switch" between which preformance functions the results fall under. The `$` tells the engine that the rest of the line is python and that's where to pull from.
<br>

During gameplay, an action is called when the player is prompted with a screen of buttons, like so:
```sh
screen opening_options():
    style_prefix "actions"
    frame:
        vbox:
            
            textbutton "cook":
                tooltip "( -holiness, +smarts , +cuisine, -cleanliness )"
                action [Call("cook_action"), Return()]  
            textbutton "clean":
                action [Call("clean_action"), Return()]
                tooltip "( -holiness, +cleanliness, +reputation, +style )" 
            textbutton "pray":
                action [Call("pray_action"), Return()]  
                tooltip "( +holiness, -reputation )"
            
            if total_days != 1: 
                textbutton "map":
                    tooltip "travel, get stats... Run into a familiar face?" 
                    action ToggleScreen("map_screen") activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Shop.mp3"
            textbutton "stats" action ToggleScreen("stats_display") activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Shop.mp3"
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            #prefer_top True

            frame:
                background Frame("gui/text_boxes2.png")
                yminimum 200 ymaximum 400
                xsize 310
                xoffset -370
                yoffset -50
                hbox:
                    #box_wrap_spacing 
                    #xsize 195
                    #box_wrap True
                    xalign 0.5
                    yalign 0.35
                    xsize 280
                    text "[tooltip]" color ("#FFFFD8") size 35
```
During the different time periods, different screens are called to the front. Each button has a tool tip displaying the basics of what each action entails.

## Stat events


# Calendar 
```sh
label next_day:
    $ Cheat_code.hide_stats_screen()
    hide screen action_screen
    $ energy = 3 
    $ park_event = False
    $ beach_event = False
    $ lib_event = False
    $ gym_event = False
    $ ice_cream_event = False
    nar2 "the next day"
    return
```
```sh

label day_change:
## make it week change. week and sunday

    
    $ day_of_week_number += 1

    if day_of_week_number == 8:
        $ day_of_week_number = 1
        $ current_day = 0 
        $ cook_event = False
        $ clean_event = False
        $ pray_event = False
        $ serve_event = False
    

    elif day_of_week_number == 1:
        $ current_day = 0 
    
    elif day_of_week_number == 2:
        $  current_day = 1
    
    elif day_of_week_number == 3:
        $  current_day = 2
    
    elif day_of_week_number == 4:
        $  current_day = 3
    
    elif day_of_week_number == 5:
        $  current_day = 4
    
    elif day_of_week_number == 6:
        $  current_day = 5
    
    elif day_of_week_number == 7:
        $  current_day = 6
    else:
        $ current_day ="NUH UH"
    return
```
```sh
label month_change:
    $ total_days += 1
    $ month_day += 1

    if total_days == 31:
        $ Topics.clear()
        $ month_day = 1
        $ current_month += 1
    if total_days == 61:
        $ month_day = 1
        $ current_month += 1
    if total_days == 92:
        $ month_day = 1
        $ current_month += 1
    
    if total_days == 122:
        $ month_day = 1
        $ current_month += 1

    if total_days == 153:
        $ month_day = 1
        $ current_month += 1
    return   

```
# Day/Night Loop
Each ingame "day" consists of a loop broken up by elif statements. 

```sh
label daily:
   
    play music "audio/konekonoosanpo.mp3" fadein 1.0 fadeout 1.0
    if Self_stats["Holiness"] <= 40:
        play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
```
This section keeps track of the "holiness" stat and changes music throughout to let the player know if that central stat is too low. 
```sh
    while True:

        if day_of_week_number == 7:
            call sunday_break
        elif total_days == 30:
            call tam_surprise
        
        elif Self_stats["Holiness"] == 0:
            jump game_over1
        elif Self_stats["Holiness"] <= 0:
            jump game_over1
        elif Work_stats["Reputatn."] == 0:
            jump game_over2
        elif Work_stats["Reputatn."] <= 0:
            jump game_over2
        elif total_days == 182:
            jump common_end
              
        else:
            if energy >= 3:
                call day
            elif energy == 3:
                call day
            elif energy == 2:
                call opening_hours
            elif energy == 1:
                call night
        
            else:
                call next_day
                call day_change
                
                call month_change
                

    return
```

