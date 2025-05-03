
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


## Stat Generating
Stats are managed and generated with "Events". Functions related to stat generating are located in `action_funcs.rpy`. 


## Stat events
```sh
#for flag checks
default Total_affec = {"Madoc": 0, "Charon": 0,"Tamura": 0}
default money = 0


default current_profit = 0
default current_clean = 0

default sign_up = False

default rounded_money = 0
default current_topic = ""

## Topic dicts/list
default Topics = {"sweet or sour foods?" : "Sweet_or_sour_foods", "favorite artist?" : "Favorite_artist", "favorite meal???": "Favorite_meal", "Inspiration?" : "Inspiration", "weather????" : "Weather"}
default Talking_points = [x for x in Topics]

default current_host = ""
```

# Calendar 

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

