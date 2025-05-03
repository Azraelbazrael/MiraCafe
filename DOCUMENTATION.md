
# Ren'py
Ren'py is a language used specifically for the engine of the same name, opporating similarly to and accepting support for python 3. Each new game project under that engine uses one specific script for the entire game unless programmed otherwise internally. How it opporates is that it takes each `label` as an individual function that it runs in order to how its formatted unless directed otherwise with `jumps`, starting from the `start` label. 
<br>While there might be other scripts used to format UI or 2D assets, only one script is used to run dialogue in this project.

# Stats

```sh
#default holiness = 100
default Work_stats = { "Reputatn.": 30, "Clean":30, "Cuisine": 30, "Charm": 50 }
default Self_stats = { "Holiness": 100, "Social" : 50, "Fitness": 40, "Smarts": 50, "Stylish" : 50 }

## For lyra's's's appearances!
default Secret_stats = {"Sabatoge": 0}
```
Stats, apart from Holiness is broken up into dictionaries. I found this was easier than estabishing a lot of different variables to reference later on. Work stats are indicative of our MC's work skills and self-skills are more about his personal improvements.
<br> `Sabatoge` in this case keeps tabs on when the player intentionally chooses incorrect dialogue options and thus gives more of a likelihood for a secret romance option showing up.

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

## Stat Generating

## Stat events


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

