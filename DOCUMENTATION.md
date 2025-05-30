
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

# Characters and Dialogue
At the top of the `script.rpy` file, I've established a lot of "Character"s. In this context, a character is an object with some established properties. From their name, to their default sprite. In my project, I've added a "callback" voice as well as a Click To Continue Icon respectively. The defined variables that represent the object can be used later in dialogue.
```sh
define amb1 = Character("Ambrosia", image="Ambrosia", ctc="ctc_heart", ctc_position="nestled",callback=angel_voice)
```

<br>
The following is an excerpt that Ren'py runs as a "say statement", which shows the character along with a dialogue box beneath them.
```sh
amb1 default "And my room-- it's all the way on the end of the corridor, right?"
```

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
These stats are love-interest specific. Those dictionaries hold the affection levels for the current romancable interests and talking points the player can access on sundays. 


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
"default" just denotes the ones the script starts out with, in the full game these topics will change with each in game month. The keys are the strings that show up in the suggested screen when topics are suggested and the value is the label name that the script jumps to when given the option.

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
When `pray_action` is called, the label gets the function from the pray class. From here, it checks the holiness stat to "switch" between which preformance functions the results fall under. The `$` tells the engine that the rest of the line is python and that's where to pull from.
<br>
```sh
label pray_action:

    call stats_action ## shows action_screen
    $ Pray.holy_switcher() 
    
    return
```


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
There are multiple components to a stat event, theres a condition and a seperate flag associated with that event in order to not repeat if the threshold is met again.
<br>
All flags can be found in `event_flags.rpy`. Each flag is sectioned off by character or location and commented accordingly. 
```sh
default lyra_warned = False
default lyra_taunted = False
default lyra_visited = False

default tam_helped = False 
default early_bird = False 
default tam_cook = False 
default gym_bros = False
default jogging_pals = False
default cant_cook = False
default can_cook = False

default ch_helped = False
default ch_mad = False
default ch_mall = False
default char_chasted = False 
default char_amazed = False
default ch_broom = False
default ch_boba = False
default ch_beach = False

default mad_helped = False
default mad_sad = False
default mad_pep = False 
default mad_poet = False
default mad_makeover = False
default food_war = False 
default music_lovers = False
default amb_goth = False

default met_harvey = False
default harv_homebody = False
default harv_book = False

```
After the "early morning" phase of the in-game day, the weeks events are called. From there, another label called the `stats_events` is called.
Each event is organized with an elif statement, due to a lack of match case in Ren'py's case. The condition is put in the expression, referencing the established dictionaries and/or flags.
```sh
if (Work_stats["Reputatn."] >=68) and (total_days <= 30) and (met_harvey == False):
        
        $ met_harvey = True
        call harvey_meet
```
There's a seperate type of event that behaves pretty similarly except the chances of them showing up are random. 
These are called *random events* or `rand_events` in the code.
During each "afternoon" phase, the script rolls a random interger between 1 and 5 and from there, that'll determine if a player might see one of the events.
```sh
label day:
    $ chance = renpy.random.randint(1,5)

scene cafe_lobby_close
    

    show screen day_display
    show screen opening_options
    
    with dissolve
    if total_days == 1:
        amb1 happy "(Okay! Step one of earning a human's love is acting like one!)"
        extend " (Probably!) (I'm pretty sure!)"
        amb1 default "(This should be easy!)"
    hide screen opening_options
    call screen opening_options
    
    call rand_events

```

One player might meet the conditions and never see that cutscene, while another might. The idea is that each playthrough feels fresh while keeping things simple.
```sh
    $ Cheat_code.hide_stats_screen()
    hide screen action_screen
    
    if (chance == 2) and (Self_stats["Social"] >= 70) and (Work_stats["Cuisine"] >= 30) and (food_war == False):
        $ food_war = True
        call .food_fight
    
    elif (chance == 4) and (gym_bros == True) and (current_month >= 1) and (early_bird == False):
        $ early_bird = True
        call .gets_worm
    
    elif (chance == 5) and (Work_stats["Charm"] >= 60) and (music_lovers == False):
        $ music_lovers = True
        call .music_loving
    return
```


# Calendar 

Established at the top of the `script.rpy` is the variables and lists that make up what works in this game's calendar.
Months and weeks are sorted into lists of strings, ensuring that each item has a specific order to them. 

```sh
define day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
default day_of_week_number = 1
default current_day = 0

default total_days = 1
default month_day = 1
define month = ["July", "August", "September", "October", "November", "December"]
default current_month = 0
default energy = 3
```

<br> What day it is currently is tracked by the `day_of_the_week_number` which ticks up with every `day_change`.
Here's an example of how this is referenced in the `day_display` (found in `day_display.rpy`)
```sh
screen day_display():
    zorder 100
 
    frame:
        background Image("gui/Day_display.png")
        #xalign 0.05 yalign 0.1
        xsize 600 ysize 236
        hbox:
            xalign 0.23 yalign 0.43
            text "[current_month +7] " style "month_display"
        hbox:
            style_prefix "day_display"
            
            box_wrap True
            xsize 310 ysize 70
            
            xalign 0.9 yalign 0.43
            text "[day_of_week[current_day]]" 
            text " [month_day]" 
            #text "Total days [total_days]"

```
The text of the day display grabs the day of the week and finds the item in that list corresponding to the current day.

<br>

A day change is handled by a list of elif statements. Whenever this function is called, the day of the week ticks up by one, and resets if this number hits 8. 
While this changes, the `current_day` will keep track of which item in the list of week strings is the currently happening.  
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
Month changes opporate similarly to a day change. One count is added to the total amount of days, and a long list of elif statements tracks if this amount exceeds 4 weeks. And under those specific conditions will the month and month_day change.
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
Each ingame "day" consists of a while loop broken up by elif statements. Once a "day" is complete, the function returns the power to the `daily` label, thus keeping the game in a working loop.

```sh
label daily:
   
    play music "audio/konekonoosanpo.mp3" fadein 1.0 fadeout 1.0
    if Self_stats["Holiness"] <= 40:
        play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
```
This section keeps track of one of the core stats, and serves as a gentle reminder if it gets too low. It also keeps the BGM from being too repetitive.  
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
```
Here specifically is where the time of day changes. Each action taken removes one energy and returns back here, thus oiling the machine.
```sh
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
At the end of each "day" the energy is replenished back to 3, just before a `day_change` is called. <p align="right">(Refer to <a href ="https://github.com/Azraelbazrael/MiraCafe/blob/main/DOCUMENTATION.md#calendar">Calendar </a>for more information)</p>
```sh
label next_day:
    $ Cheat_code.hide_stats_screen() ## Just hides all stat screens in one function
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
