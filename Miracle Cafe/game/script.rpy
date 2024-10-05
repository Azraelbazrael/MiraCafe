# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define nar = Character(None, kind=nvl, what_color="#FFFF")
define nar2 = Character(None, what_ypos=65 , ctc="ctc_heart", ctc_position="nestled")
define amb1 = Character("Ambrosia", image="Ambrosia", ctc="ctc_heart", ctc_position="nestled")
define TM = Character("Tamura", image="Tamura", ctc="ctc_heart", ctc_position="nestled")
define CH = Character ("Charon", image="Charon", ctc="ctc_heart", ctc_position="nestled")
define MD = Character("Madoc", image="Madoc", ctc="ctc_heart", ctc_position="nestled")
define LY = Character("Lyra", ctc="ctc_heart", ctc_position="nestled")
define HV = Character("Harvey", ctc="ctc_heart", ctc_position="nestled")
define huh = Character("???", ctc="ctc_heart", ctc_position="nestled")
define huhbegin = Character("???", image="Ambrosia", ctc="ctc_heart", ctc_position="nestled")
define Mo = Character("Moira", ctc="ctc_heart", ctc_position="nestled")
define GY = Character("Gal Pals", image="Gyaru", ctc="ctc_heart", ctc_position="nestled")

#default holiness = 100
default Work_stats = { "Reputatn.": 30, "Clean":30, "Cuisine": 30, "Charm": 50 }
default Self_stats = { "Holiness": 100, "Social" : 50, "Fitness": 40, "Smarts": 50, "Stylish" : 50 }


define day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
default day_of_week_number = 1
default current_day = 0

default total_days = 1
default month_day = 1
define month = ["July", "August", "September", "October", "November", "December"]
default current_month = 0
default energy = 3

define bites = ImageDissolve("transitions/old/bites.webp", 1.5, ranplen= 36)
define flash = Fade(1.1, 0.0, 0.5, color="#fff")

default money = 0


default current_profit = 0
default current_clean = 0

default sign_up = False

default lib_event = False
default park_event = False
default gym_event = False
default ice_cream_event = False
default beach_event = False
default mall_event = False
# weekly events
default chance = 0


default cook_event = False
default clean_event = False
default serve_event = False
default pray_event = False
default rounded_money = 0
default current_topic = ""
## -- Python stuff
init python:
    ## items

    def holy_water():
        global Self_stats
        global rounded_money
        rounded_money -= 50
        Self_stats["Holiness"] += 30


    def special_sign():
        global Work_stats
        global rounded_money
        global sign_up 
        sign_up = True
        Work_stats["Reputatn."] += 50
        rounded_money -= 100

### ACTIONS!
    class Pray():

        def success():
            global Self_stats
            global Work_stats
            nar2("A prayer brought serenity.")
            Self_stats["Holiness"] += renpy.random.randint(10,15)
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
    
    class Cook():
        def success():
            global Self_stats
            global Work_stats
            
            
            nar2("Ambrosia ventures onto dangerous cuisine territory!")
            Work_stats["Cuisine"] += renpy.random.randint(5,8)
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Charm"] += renpy.random.randint(3,5)
            Self_stats["Smarts"] += renpy.random.randint(3,5)
            Work_stats["Clean"] -= renpy.random.randint(2,3)


        def slightly_less():
            global Self_stats
            global Work_stats
            
            nar2("Ambrosia ventures onto dangerous cuisine territory--! To mixed effect!")
            current_cook += renpy.random.randint(2,5)
            Work_stats["Cuisine"] += renpy.random.randint(3,5)
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Charm"] += renpy.random.randint(3,5)
            Self_stats["Smarts"] += renpy.random.randint(3,5)
            Work_stats["Clean"] -= renpy.random.randint(2,3)
  

        def sucks_():
            global Self_stats
            global Work_stats
            nar2("Who could ever imagine soup could be a sickly purple! ...Not Ambrosia! Or the customers!")
            current_cook += renpy.random.randint(1,3)
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Charm"] += renpy.random.randint(3,5)
            Self_stats["Smarts"] += renpy.random.randint(3,5)
            Work_stats["Clean"] -= renpy.random.randint(2,3)


        def holy_switcher():
            global Self_stats 
            global energy 
            energy -= 1
            renpy.show_screen("cook_action")
            if(Self_stats["Holiness"] >= 60):
                
                Cook.success()
                renpy.pause(1.8, hard=True)
            elif (Self_stats["Holiness"] >= 40):
                
                Cook.slightly_less()
                renpy.pause(1.8, hard=True)
            else:
                Cook.sucks_()
                renpy.pause(1.8, hard=True)

    class Serve():
        #social, charm, clean
        def success():
            global Self_stats
            global Work_stats
            global sign_up
            nar2("Customers poured in by the tenfold!")
            Self_stats["Holiness"] -= renpy.random.randint(5,8)
            Self_stats["Social"] += renpy.random.randint(5,8)
            Work_stats["Clean"] += renpy.random.randint(3,5)
            if sign_up == True:
                Work_stats["Reputatn."] += renpy.random.randint(5,8)
                
            else:
                Work_stats["Reputatn."] += renpy.random.randint(3,5)

        def slightly_less():
            global Self_stats
            global Work_stats
            nar2("Customers drip in, with mixed chatter!")
            Self_stats["Holiness"] -= renpy.random.randint(5,8)
            Self_stats["Social"] += renpy.random.randint(3,5)
            Work_stats["Clean"] += renpy.random.randint(1,3)
            if sign_up == True:
                Work_stats["Reputatn."] += renpy.random.randint(5,8)
            else:
                Work_stats["Reputatn."] += renpy.random.randint(3,5)    

        def sucks_():
            global Self_stats
            global Work_stats
            nar2("Ambrosia could hear the patrons loudly typing bad reviews...")
            Self_stats["Holiness"] -= renpy.random.randint(5,8)
            Self_stats["Social"] += renpy.random.randint(3,5)
            if sign_up == True:
                Work_stats["Reputatn."] += renpy.random.randint(1,3)
            else:
                pass

        def holy_switcher():
            global Self_stats
            renpy.show_screen("serve_action")
            global energy 
            energy -= 1
            if(Self_stats["Holiness"] >= 60):
                Serve.success()
                renpy.pause(1.8, hard=True)
            elif (Self_stats["Holiness"] >= 40):
                Serve.slightly_less()
                renpy.pause(1.8, hard=True)
            else:
                Serve.sucks_()
                renpy.pause(1.8, hard=True)
    
    class Clean:
        def success():
            global Self_stats
            global Work_stats
            nar2("Floors were no match for Ambrosia's might!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Stylish"] += renpy.random.randint(5,8)
            Work_stats["Clean"] += renpy.random.randint(3,5)
            Work_stats["Reputatn."] += renpy.random.randint(1,3)
            

        def slightly_less():
            global Self_stats
            global Work_stats
            nar2("Ambrosia kept missing spots..!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Stylish"] += renpy.random.randint(3,5)
            Work_stats["Clean"] += renpy.random.randint(1,3)
            Work_stats["Reputatn."] += renpy.random.randint(1,3)   

        def sucks_():
            global Self_stats
            global Work_stats
            nar2("May the goddess smite him down, how does soap explode.")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Reputatn."] -= renpy.random.randint(1,3)
            Self_stats["Stylish"] += renpy.random.randint(3,5)

        def holy_switcher():
            global Self_stats
            global energy 
            energy -= 1
            renpy.show_screen("clean_action")
            if(Self_stats["Holiness"] >= 60):
                Clean.success()
                renpy.pause(1.8, hard=True)
            elif (Self_stats["Holiness"] >= 40):
                Clean.slightly_less()
                renpy.pause(1.8, hard=True)
            else:
                Clean.sucks_()
                renpy.pause(1.8, hard=True)


## -- Map stuff


    class Beach:
        def success():
            global Self_stats
            global Work_stats
            
            nar2("The morning was spent in the sun!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Fitness"] += renpy.random.randint(5,8)
            Self_stats["Stylish"] += renpy.random.randint(1,3)
            Self_stats["Social"] += renpy.random.randint(3,5)

        def slightly_less():
            global Self_stats
            global Work_stats

            nar2("The cool breeze inspires Ambrosia!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Fitness"] += renpy.random.randint(5,8)
            Self_stats["Social"] += renpy.random.randint(3,5)   

        def sucks_():
            global Self_stats
            global Work_stats

            nar2("The cool breeze inspires Ambrosia...?")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Stylish"] -= renpy.random.randint(1,3)
            

        def holy_switcher():
            global Self_stats
            renpy.show_screen("beach_action")
            global energy 
            energy -= 1
            if(Self_stats["Holiness"] >= 60):
                Beach.success()
                renpy.pause(1.8, hard=True)
            elif (Self_stats["Holiness"] >= 40):
                Beach.slightly_less()
                renpy.pause(1.8, hard=True)
            else:
                Beach.sucks_()
                renpy.pause(1.8, hard=True)



    class Gym:
        def success():
            global Self_stats
            global Work_stats
            nar2("One.. Two.. three..!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Fitness"] += renpy.random.randint(5,8)
            Self_stats["Social"] += renpy.random.randint(3,5)
            Work_stats["Clean"] -= renpy.random.randint(3,5)

        def slightly_less():
            global Self_stats
            global Work_stats
            nar2("One.. Two.. three...")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Fitness"] += renpy.random.randint(5,8)
            Work_stats["Clean"] -= renpy.random.randint(3,5)   

        def sucks_():
            global Self_stats
            global Work_stats
            nar2("Ambrosia felt too dizzy to get up...")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Clean"] -= renpy.random.randint(1,3)
            

        def holy_switcher():
            global Self_stats 
            global energy 
            energy -= 1
            renpy.show_screen("gym_action")
            if(Self_stats["Holiness"] >= 60):
                Gym.success()
                renpy.pause(1.8, hard=True)
            elif (Self_stats["Holiness"] >= 40):
                Gym.slightly_less()
                renpy.pause(1.8, hard=True)
            else:
                Gym.sucks_()
                renpy.pause(1.8, hard=True)
    
    class Ice_cream:
        def success():
            global Self_stats
            global Work_stats 
            nar2("Yum!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Charm"] += renpy.random.randint(5,8)
            Self_stats["Fitness"] -= renpy.random.randint(3,5)
            Work_stats["Cuisine"] += renpy.random.randint(5,8)
        def slightly_less():
            global Self_stats
            global Work_stats
            nar2("Yum...!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Charm"] += renpy.random.randint(3,5)
            Self_stats["Fitness"] += renpy.random.randint(3,5)
            Work_stats["Cuisine"] += renpy.random.randint(5,10)
            Work_stats["Clean"] -= renpy.random.randint(3,5)
        def sucks_():
            global Self_stats
            global Work_stats
            nar2("Yum...")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Charm"] += renpy.random.randint(1,5)
            Self_stats["Social"] += renpy.random.randint (3,5)
            Self_stats["Fitness"] += renpy.random.randint(3,5)
            Work_stats["Clean"] -= renpy.random.randint(3,5)
    
        def holy_switcher():
            global Self_stats
            global energy 
            energy -= 1
            renpy.show_screen("ice_cream_action")
            if(Self_stats["Holiness"] >= 60):
                Ice_cream.success()
                renpy.pause(1.8, hard=True)
            elif (Self_stats["Holiness"] >= 40):
                Ice_cream.slightly_less()
                renpy.pause(1.8, hard=True)
            else:
                Ice_cream.sucks_()
                renpy.pause(1.8, hard=True)

    class Park:
        # cleanliness, fitness and social
        def success():
            global Self_stats
            nar2("The morning jog refreshed Ambrosia immensely!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Charm"] += renpy.random.randint(3,5)
            Self_stats["Social"] += renpy.random.randint(3,5)

        def slightly_less():
            global Self_stats
            nar2("The morning jog refreshed Ambrosia somewhat!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Charm"] += renpy.random.randint(3,5)
            Self_stats["Social"] += renpy.random.randint(1,3)
            Work_stats["Clean"] -= renpy.random.randint(3,5)   

        def sucks_():
            global Self_stats
            nar2("The morning jog almost made Ambrosia collapse!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Work_stats["Clean"] -= renpy.random.randint(1,3)
            Self_stats["Social"] += renpy.random.randint(1,3)
            

        def holy_switcher():
            global energy 
            energy -= 1
            global Self_stats 
            renpy.show_screen("park_action")
            if(Self_stats["Holiness"] >= 70):
                Park.success()
                renpy.pause(1.8, hard=True)
            elif (Self_stats["Holiness"] >= 40):
                Park.slightly_less()
                renpy.pause(1.8, hard=True)
            else:
                Park.sucks_()
                renpy.pause(1.8, hard=True)

    class Mall:
        def success():
            global Self_stats
            global Work_stats
            nar2("The morning was spent windowshopping carefully!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Social"] += renpy.random.randint(5,8)
            current_intel -= renpy.random.randint(1,3)
            reputation += renpy.random.randint(3,5)

        def slightly_less():
            global Self_stats
            global Work_stats
            nar2("The morning was spent almost shoplifting!!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Social"] += renpy.random.randint(3,5)
            Self_stats["Smarts"] -= renpy.random.randint(1,3)
            Work_stats["Reputatn."] += renpy.random.randint(1,3)   

        def sucks_():
            global Self_stats
            global Work_stats
            nar2("Ambrosia is beginning to tire of the same stores...")
            Self_stats["Social"] += renpy.random.randint(1,3)
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Smarts"] -= renpy.random.randint(3,5)
            

        def holy_switcher():
            global Self_stats
            global energy 
            energy -= 1
            renpy.show_screen("mall_action")
            if(Self_stats["Holiness"] >= 60):
                Mall.success()
                renpy.pause(1.8, hard=True)
            elif (Self_stats["Holiness"] >= 40):
                Mall.slightly_less()
                renpy.pause(1.8, hard=True)
            else:
                Mall.sucks_()
                renpy.pause(1.8, hard=True)
    
    class Library:
        def success():
            global Self_stats
            global Work_stats
            nar2("Hours flew with the pages, absorbing knowledge!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Smarts"] += renpy.random.randint(5,8)
            Self_stats["Social"] -= renpy.random.randint(1,3)
            Work_stats["Charm"] += renpy.random.randint(3,5)

        def slightly_less():
            global Self_stats
            global Work_stats
            nar2("Hours flew with the pages, absorbing knowledge...!")
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Social"] += renpy.random.randint(3,5)
            Self_stats["Smarts"] -= renpy.random.randint(1,3)
            Work_stats["Charm"] += renpy.random.randint(1,3)   

        def sucks_():
            global Self_stats
            global Work_stats
            nar2("Hours flew with the pages.... absorbing-- Hey! Ambrosia! get up!")
            Self_stats["Smarts"] += renpy.random.randint(1,3)
            Self_stats["Holiness"] -= renpy.random.randint(3,5)
            Self_stats["Social"] -= renpy.random.randint(3,5)
            

        def holy_switcher():
            global energy 
            energy -= 1
            global Self_stats
            renpy.show_screen("read_action")
            if(Self_stats["Holiness"] >= 60):
                Library.success()
                renpy.pause(1.8, hard=True)

            elif (Self_stats["Holiness"] >= 40):
                Library.slightly_less()
                renpy.pause(1.8, hard=True)
            else:
                Library.sucks_()
                renpy.pause(1.8, hard=True)

    class Cheat_code:
        def hide_stats_screen():
            renpy.hide_screen("read_action")
            renpy.hide_screen("pray_action")
            renpy.hide_screen("mall_action")
            renpy.hide_screen("beach_action")
            renpy.hide_screen("ice_cream_action")
            renpy.hide_screen("park_action")
            renpy.hide_screen("cook_action")
            renpy.hide_screen("clean_action")
            renpy.hide_screen("serve_action")
            renpy.hide_screen("gym_action")
            
            
## IMAGES
init:
    transform flip:
        xzoom -1.0

transform squash:
    #xanchor 0.99
    #
    xzoom 1.05 yzoom 0.9 xoffset 0.5
    ease 0.2 xzoom 0.95 yzoom 1.05 xoffset 0
    linear 0.2 xzoom 1 yzoom 1 xoffset 0

transform open_squish:
    xzoom 1.1 yzoom 0.1
    ease 0.2 xzoom 1.05 yzoom 1.1
    ease 0.2 xzoom 1 yzoom 1 

transform zoomie:
    xzoom 1.1 yzoom 1.1


image ctc_heart:
    "gui/feather_ctc.png"
    yalign 0.5
    ease 0.2 yalign 1
    linear 0.2 yalign 0.5
    repeat


image side Ambrosia default = "images/Ambrosia_side.png"
image side Ambrosia happy = "images/Ambrosia_happy.png"
image side Ambrosia flush = "images/Ambrosia_flustered.png"
image side Ambrosia excite = "images/Ambrosia_excited.png"
image side Ambrosia ugh = "images/Ambrosia_ugh.png"
image side Ambrosia srs = "images/Ambrosia_serious.png"
image side Ambrosia cur = "images/Ambrosia_curious.png"
image side Ambrosia sweat = "images/Ambrosia_nervous.png"

image side Tamura default = "images/Tamura_default.png"
image side Tamura proud = "images/Tamura_proud.png"
image side Tamura blush = "images/Tamura_blush.png"
image side Tamura hes = "images/Tamura_hesitant.png"
image side Tamura scream = "images/Tamura_scream.png"

layeredimage Tamura default:
    always "images/stand_sprites/tam_stand_default.png"
    group dress:
        ypos 410
        xsize 1145 ysize 650
        attribute summer default:
            "images/stand_sprites/tam_def_summer.png"

layeredimage Tamura proud:
    always "images/stand_sprites/tam_stand_proud.png"
    group dress:
        ypos 410
        xsize 1145 ysize 650
        attribute summer default:
            "images/stand_sprites/tam_summer_proud.png"

layeredimage Tamura blush:
    always "images/stand_sprites/tam_stand_default.png"
    
    group dress:
        ypos 410
        xsize 1145 ysize 650
        attribute summer default:
            "images/stand_sprites/tam_def_summer.png"
    group face:
        xpos 450
        ypos 330
        attribute summer default:
            "images/stand_sprites/tam_blush.png"

layeredimage Tamura scream:
    
    group hair:
        ypos 360
        attribute hype:
            "images/stand_sprites/tam_hair_scream_hype.png"

    always:
        ypos 820
        xpos 100
        "images/stand_sprites/tam_body_scream.png"
    
    
    group arms:
        ypos 820
        attribute hype:
            "images/stand_sprites/tam_arms_scream_hype.png"
    group clothes:
        ypos 720
        attribute hype_summer:
            "images/stand_sprites/tam_summer_scream_hype.png"
    group head:
        ypos 550
        xpos 370
        attribute hype:
            "images/stand_sprites/tam_head_scream_hype.png"
            
    
layeredimage Tamura hes:
    always "images/stand_sprites/tam_stand_hesitant.png"
    group clothes:
        attribute summer default:
            "images/stand_sprites/tam_hes_summer.png" 

image side Charon default = "images/Charon_default.png"
image side Charon aww = "images/Charon_aww.png"
image side Charon sass = "images/Charon_sass.png"
image side Charon srs = "images/Charon_serious.png"
image side Charon srs2 = "images/Charon_serious2.png"
image side Charon reg = "images/Charon_regret.png"

image side Madoc default = "images/Madoc_default.png"
image side Madoc smile = "images/Madoc_smile.png"
image side Madoc happy = "images/Madoc_happy.png"
image side Madoc huh = "images/Madoc_curious.png"
image side Madoc shock = "images/Madoc_Shocked.png"

image side Gyaru 1 = "images/camreon_side.png"
image side Gyaru 2 = "images/damon_side.png"

### - backgrounds
image amb_bed = "images/Ambrosia_bedroom.png"
image upstairs = "images/Upstairs_hallway.png"
image kitchen = "images/Kitchen_background.png"
image dot_bg = "images/dot_background.png"
image cafe_lobby_close = "images/Cafe_interior_2.png"
## -- char CGs
image tam_box1 = "images/tam_box1.png"
image tam_box2 = "images/tam_box2.png"
image cauldron = "images/cauldron_cg.png"
image deep_fry = "images/grab_deepfry_cg.png"

image amb_list = "images/amb_list.png"
image char_meet_1 = "images/char_meet_1.png"
image char_meet_2 = "images/char_meet_2.png"

image mad_door_1 = "images/mad_door_1.png"
image mad_door_2 = "images/mad_door_2.png"

image Tam_r_u_fuckin_srs_rn = "images/Tam_srs.png"
## --char event flags


default lyra_warned = False

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

default is_demo = False
## chara affection variables


default Total_affec = {"Madoc": 0, "Charon": 0,"Tamura": 0}
#default highest_affec = max(Total_affec, key = lambda x: Total_affec[x])

## Topic dicts/list
default Topics = {"sweet or sour foods?" : "Sweet_or_sour_foods", "favorite artist?" : "Favorite_artist", "favorite meal???": "Favorite_meal", "Inspiration?" : "Inspiration", "weather????" : "Weather"}
default Talking_points = [x for x in Topics]

default current_host = ""




label start:

    #hide screen quick_menu
    python:
        is_demo = True
        
    
        

label begin:
    scene image Solid("#fff")
    #show screen item_list_test
    play music "audio/asayakenomachi.mp3"
    nar2 "One sunday morning, the wonderfully earthy scent of gasoline and smog greets a new bubbling visitor."
    huhbegin default "this is it..."
    nar2 "He laments, soft as a mouse."
    nar2 "With a small turn, the fresh face witnessed his first ever mission."
    nar2 "An odd place and an odd job, for one lone cherub."
    nar2 "{i}Steal a heart without an arrow{/i}, they said."
    huhbegin happy "This is it!!"
    nar2 "with that, a soft palm presses against the door, hope helplessly undetered with wide eyes."
        

    play sound "audio/shop-door-bell-6405.mp3"
    scene cafe_lobby_close
    show tam_box1
    with dissolve
    nar2 "Dust cleared the air, a mane of bright red hair stood through the empty space."

    show tam_box2 
    with dissolve



    TM default "AH! hello!"
    
    TM "Glad to know that bell actually works..."
    extend proud " you must be Ambrosia, right?"
    amb1 happy "Yep!! Wouldn't be anyone else if I tried!"
    TM "Oh, now I know you're Ambrosia, I'd know that enthusaism from just your resume! Hah-hoh!"
    nar2 "The towering figure flops a handful of boxes atop the counter, bulky arms highlighted by dim lights, a sure smile cracking from his lips."
    nar2 "This was none other soon-to-be cafe's manager, Blaze Tamura. Ambrosia could recall gleaming notes from guardian angel reports."
    nar2 "Resting in the center of immposibly thousands of humans, his file couldn't have even began to describe how grand his presence just was."
    nar2 "The man that stood ahead of him, he was everything Ambrosia could ever dream of."
    
    TM default "You caught us at a good time! everyone's already unpackin', yeah?"
    TM "The boys upstairs are great!"
    play sound "audio/51163__rutgermuller__running-up-the-stairs.mp3" 
    extend proud " They're terrific company, you'll fit right in."
    
    
    huh "Hah?? Is that the new guy??"

    
    hide tam_box1 
    hide tam_box2 
    show char_meet_1
    with dissolve
    nar2 "Steps weighed in the distance, a new figure emerged behind the manager."
    nar2 "He strides in, chest puffed like a proud bird, striking colors dazzling every inch of him."
    CH default "Woaaaahh--! This is the Ambrosia you were talking about, Blaze???"
    CH aww "He's so pretty!" 
    hide char_meet_1
    show char_meet_2
    with dissolve
    CH default "Hihi! I'm Charon, you're new roomate!"
    CH  "...Housemate?"
    CH "Housemate!"
    nar2 "Angel's nectar fled to ambrosia's cheeks, bewildered. A hard grin in place before he even realised."
    CH "You HAVE to come with me, Madoc said he wanted to say hi personally! You HAVE to let me tour you around!"


    amb1 flush "HAHAHAHAHAH! OKAY!!"
    
    
    scene upstairs
    show upstairs
    with bites
    nar2 "Through stairs and corridors, the enthusiastic Charon rivaled the starry-eyed Ambrosia in giddy. With bated breath, the two landed outside a tall door."
    nar2 "Untained with even a spec of dust, Ambrosia's makeshift tour-guide swivels next to him with a proud grin."
    CH default "This... This is Madoc's room! Next to that, mine!"
    nar2 "he began, not a breath skipped."
    amb1 default "And my room-- it's all the way on the end of the corridor, right?"
    CH "Yep!! It's a bit of a fixer--upper... But hey, no one said you have to do it alone!"
    CH aww "I'm basically the resident fixer-upper-er!"
    play sound "audio/460542__coosemek__door-creak.mp3"
    show mad_door_1
    with dissolve
    nar2 "The door carefully cranes open, darkened eyes peep through the cracks."
    MD default "Charon, can you keep it down... I'm trying to focus here."
    MD smile "...Please."
    CH default "Hey! I was just trying to give our new housemate a little tour, see? You wanted to say hi, right?"

    show mad_door_2
    with dissolve
    MD default "...Hi."
    MD "My name's Madoc, but you already knew that."
    MD "If you need anything, I'm always here. Just not right now."
    nar2 "The whisper of a cute smile fades as soon as it peaked out, the door hushing him back into the distance."
    hide mad_door_1
    hide mad_door_2
    with bites
    CH reg "Oh! God,"
    extend sass " right!"
    nar2 "Charon spoke, slapping his own forehead with the tough part of his palm."
    CH  reg "Shoot! Blaze like- BEGGED me not to bug you too much, I tend to do that..." 
    extend aww " Whoopsie!"
    amb1 "What? No, no no!! I really appreciated it!!"
    amb1 happy "thank you!"
    nar2 "Graciously, he bowed. Charon only shares a delighted giggle in response."
    CH aww "I'll be out of your hair in a pinch, anyhow."
    CH  "I like, covered all your bases..."
    CH default "You're free to explore more! Just.. Don't explode, alright?"

    play sound "audio/460542__coosemek__door-creak.mp3"
    nar2 "Charon soon doddles off into his space, darting looks between the door and the new roomie."
    nar2 "The door creaked a loud farewell, the sneakers of the enthusiastic Charon vanishing behind."
    play sound "audio/710064__johnytud__door01_open.mp3"
    show amb_bed 
    with bites
    nar2 "Slowly, Ambrosia paced to his own door, unveiling it as carefully as the enterance."
    nar2 "Just beyond his nose, the angel was presented with a small room, a single bed tucked into the corner."
    nar2 "the room's other corners made home for small arachnids, intricate webs lacing the two surfaces, dust caking the floors."
    nar2 "Ambrosia scanned ceilings and walls, each plane dressed snug with grease and cracks."
    nar2 "His hand gently grazes the surface, a curiosity embued in his very finger tips."
    nar2 "For 6 months and 7 and a half days, this quaint and delightfully human area was his home."
    play sound "audio/656366__straynerd__falling-on-mattress-owi.mp3"
    nar2 "Flopping back first onto the bed, a firm embrace of the mattress greeting his sides."
    amb1 cur "Steal a heart without an arrow, huh...."
    nar2 "He mused, quietly."
    nar2 "The mission was simple,"
    extend " here, right under this warm cafe, Ambrosia brushed past many hearts."
    nar2 "He could toss up a smile, dance, sing... learn what it means to be loved."
    amb1 happy "I can't wait!!"
    
    stop music fadeout 1.0

label daily:
   
    play music "audio/konekonoosanpo.mp3" fadein 1.0 fadeout 1.0
    if Self_stats["Holiness"] <= 40:
        play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
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
## endings
label game_over1:
    play music "audio/houkagonoyuzora.mp3"
    scene L + ratio
    LY "Oh, a pity that is..."
    LY "OH-HOH-HOH-HO!!! Can't say I didn't warn you, did I?"
    menu:
        "No--!":
            jump .no
        "Wait!!":
            jump .no

label .no:
    LY "There is no resistence when it comes to the ALMIGHTY HEAVENS!"
    LY "Let's hope you said your farewells, Amb-rooo-sia!"
    call screen game_over
     
label .wait:
    LY "There is no resistence when it comes to the ALMIGHTY HEAVENS!"
    LY "Let's hope you said your farewells, Amb-rooo-sia!"
    nar2 "A faint instinct wells up inside of the small angel, just for a glimmering moment."
    nar2 "But, he couldn't could he...?"
    amb1 "Lyra... {i}You're{/i} my favorite."
    nar2 "Adopting a sultry voice, he closes into Lyra's breastplate."
    amb1 "What if this was my plan all along, hm...?"
    nar2 "His fingers lace the edge of the holy armor, savoring the way it burned against his tips."
    LY "I-- you-- YOU- wh-?!"
    LY "YOUR TEMPTATIONS DO NOT REACH MY EARS! LA-LA-LA-LA!!"
    LY "NOT LISTENING!"
    amb1 "What? Am I... Making you nervous?"
    LY "FOOLISH CHERUB! At this rate, you'll get your wings clipped!! Cease this behaviour at once!!"
    nar2 "Ambrosia locks in place, his eyes knowing nothing but a sweet desperation."
    LY "Wh- why did you stop..?"
    amb1 "I'm listening to you, aren't I?"
    amb1 "Use your woooordsss, hehehehe!"
    with hpunch
    Mo "ALRIGHT. THAT'S ENOUGH. GAME OVER, GOOD BYE."
    call screen game_over

label game_over2:
    play music "audio/houkagonoyuzora.mp3"
    TM "We lost the shop."
    CH "What?!"
    TM "Yeah, all these scathing reviews are KILLING out business... And we uh..."
    MD "How did that..."
    amb1 "(oh... oh goodness...)"
    amb1 "(that wasn't my fault, was it?)"
    call screen game_over

label common_end:
    "things go okay! But... you still failed, lol."
    return

# -- common events
label lyra_warn:
    
    scene cafe_lobby_close
    with dissolve
    play music "audio/yuugurepierrot.mp3" fadein 1.0 fadeout 1.0
    hide screen day_display
    $ lyra_warned = True
    $ Total_affec.update({"Lyra" : 0})
    LY "Oh-hoh-ho! Look at what we have here, are you lost????"
    LY "Do we need to have a big, stronger angel come pick you up???"
    LY "Send you back to the heavens????"
    amb1 ugh "Hi Lyra.."
    LY "IT IS SIR LYRA THE BOLD, SKILLED SWORDSANGEL AND GUARDIAN OF THE POWERS RANK TO YOU, CHERUB."
    amb1 ugh "..."
    LY "Well I'm not leaving until you address me properly!"
    
    menu:
        "You wanna see me that bad..?":
            call .flirt
        "Yes, Sir... Lyra the bold and skilled swordsangel and guardian of the powers rank.":
            call .listen
    play music "audio/konekonoosanpo.mp3"
    return


label .flirt:
    
    LY "!?!?!?!!?"
    LY "Never you mind that line of thought, HEATHEN! I have not a breath to waste for you!"
    LY "I simply came for a messsage!"
    LY "Keep your connections with the divine strong, that is all we ask. {b}Make sure your holiness stat doesn't reach 0{/b}"
    LY "Lest your affairs end too soon... How sad!"
    LY "That is all!"
    amb1 ugh "..."
    amb1 default "(I hope he runs into a window on his way out!)"
    play music "audio/konekonoosanpo.mp3"
    return
label .listen:
    LY "Good, good."
    LY "You're worth for something, at least!"
    LY "I came for a messsage! From the Goddess herself, mind you."
    LY "Lucky you are for her time..."
    LY "Keep your connections with the divine strong, that is all we ask. {b}Make sure your holiness stat doesn't reach 0{/b}"
    LY "Lest your affairs end too soon... How sad!"
    LY "That is all!"
    amb1 ugh "..."
    amb1 default "(I hope he runs into a window on his way out!)"
    play music "audio/konekonoosanpo.mp3"
    return



label tam_surprise:
    scene upstairs
    with fade
    play music "audio/hajimetenookashidukuri.mp3" fadein 1.0 fadeout 0.5
    nar2 "In the early morning, pots and pans clank feverishly through the halls."
    nar2 "Against walls, against floors, against the sanity of the inhabitants."
    TM proud "BREAKFAST IS READDDDYYYYY!"
    CH sass "{i}Isn't it too earlllyyy for breakfast?{/i}"
    nar2 "Doors hesitantly creak open, greeted by an enthusiastic Blaze."
    MD huh "Charon's right, you know. What are you up to...?"
    TM "It's something real big, yeah?"
    TM "Thought I'd butter you up first before clamouring 'bout it! C'mon!"
    nar2 "He raced down the steps with a giggle passing through his breath, almost like a child."
    nar2 "Charon scans the room, between the two left in his dust."
    CH aww "SO? any clues?"
    nar2 "He yawns, turning to Ambrosia."
    amb1 cur "Nnnooonnne at all..."
    MD huh "Maybe we're getting a raise...?"
    CH sass "Knowing Blaze it's probably something-- fancy. Like, something that'll make things easier for us!"
    menu:
        "What about fancy aprons?!":
            call .apron
        "Oh! What about a new duster??":
            call .duster
    return
label .duster:
    $ Total_affec["Charon"] += 2
    CH aww "AWHHH-- you really think so?"
    MD "The ones we have work just as fine, from what I remember... Not sure if Blaze would go that far."
    CH "Pff-- let me dream! Wouldn't it be cool?"
    amb1 "The bristles would be fluffier than a feather, sheltering all those dust bunnies...."
    MD "I guess so... Guess we'll have to see for ourselves."
    call .harveys_home
    return

label .apron:
    $ Total_affec["Madoc"] += 2
    MD "Hahah... Wouldn't that be nice."
    amb1 "And there'd be ruffles and everything! We'd live like princesses!"
    MD "When you put it that way... I'll have to ask if it comes in black, first."
    CH aww "NO WAY! Blaze is totally attached to our current ones! Trust me, dude."
    CH "He'll change it when PIGS fly!"
    MD "I heard they have helicopters now."
    CH "pffhhttb... Okay, okay, we should see what the fuss is downstairs now."
    call .harveys_home
    return

label .harveys_home:
    scene cafe_angle
    with bites
    play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
    nar2 "as the three gather downstairs, their eyes drew to the feast sitting atop one of the tables."
    nar2 "A large, warm bowl of miso soup, garnished with tofu and leeks sat left of the middle,"
    nar2 "A long body of salmon, dressed in ginger and onion, blanketed in soy sauce waits patiently just over."
    nar2 "The sight was elevated with a sense of grandeur poured into each and every fiber, 5 more bowls circling around the two plates."
    nar2 "wait, {i}5?{/i}"
    CH aww "Blazzzeee? What's all this?"
    nar2 "He was the first to break the silence, awe stilling the rest."
    TM proud "Like I said..."
    nar2 "He pauses, with a sniffle."
    TM proud "BIG news!"
    TM "H-Harvey! You can come out now!"
    MD shock "...Is that--"
    CH reg "THE ARISON KID?!"
    CH "H-h- what??!"
    CH "What is he doing here?!? Is he a food inspector now--???"
    nar2 "The well dressed man clicks his tongue, glancing away from the adoring crowd."
    HV "It's Harvey. {i}Just{/i} Harvey."
    HV "I needed somewhere to stay, and Mr. Tamura is an old friend of mine."
    nar2 "Keeping away from the eyes, he gathers to the counter, the rest following suit."
    if met_harvey == True:
        amb1 cur "Hey, I remember seeing you around!"
        HV "Who doesn't..."
        nar2 "His throat caught more of a grumble than a show of pride."
    CH "WH-whah- WHAT?!"
    CH aww "BLAZZZEEE! blaze, blaze, blaze! Why didn't you tell me before?!"
    TM hes "Well, uh--"
    HV "We haven't talked in a while."
    HV "I couldn't talk to him, for a while..."
    CH reg "YOU'VE BEEN S-"
    nar2 "Madoc instinctively cover's Charon's mouth, impatience distilling across his face."
    amb1 cur "??????"
    TM hes "oh? OH. No, no- no! Hahahahahah! It's not like that, I-I don't... Swing that way!"
    nar2 "The atmosphere grew thick, stirring in confusion."
    CH "(muffled) {i}Are you sure?{/i}"
    MD "What about that time when--"
    TM blush "Doesn't count."
    CH "{i}OR ABOUT WHEN YOU TOLD US-{/i}"
    TM "Hey! That was ONE time!"
    if gym_bros == True:
        amb1 ugh "...?"
        nar2 "He stares up Blaze, curious himself."
        nar2 "The larger man carried a wince, sorrow tucked behind those eyes."
    HV "The details probably aren't important anyway. We're here to eat, not chat."
    HV "Thank you, Mr. Tamura."
    TM proud "Yeah, no problem!"    
    $ harv_homebody = True
    if is_demo == True:
        jump demo_end
    else:
        call next_day 
        call day_change
        call month_change
        play music "audio/konekonoosanpo.mp3" fadein 1.0 fadeout 1.0
        jump day
    


label demo_end:
    scene void
    with bites
    $ highest_affec = max(Total_affec, key = lambda x: Total_affec[x])
    play music "audio/konekonoosanpo.mp3" fadein 1.0 
    if highest_affec == "Madoc":
        show Madoc at right
        MD default "Hello."
        MD "You've reached the end of the demo..."
        MD "Would you like to complete a quick servay to earn a 20 percent discount on your next order...?"
        menu:
            "It went great!":
                call demo_end_2
            "It was okay...":
                call demo_end_2
            "You tried!":
                call demo_end_2


    elif highest_affec == "Charon":
        show Charon at right
        CH aww "Hi-hiii!"
        CH "You made it! You made it to the end of the demo!!"
        CH "I'm glad you have SUCH good taste!"
        CH "My presence here? No accident!"
        CH "...Hey, wait! Before you go..."
        CH "You BETTER come again, okay?!"
        CH "hehe! No, no, I'm kidding."
        CH "I'll be seeing you around, okay?"

    elif highest_affec == "Tamura":
        show Tamura at right
        TM scream "HAHHHH!!"
        TM proud "Heya, bud!"
        TM blush "Looks like you sat through everything we had so far..."
        TM hes "Guess i wanted to say... I'm proud of ya?"
        TM "Fer stickin' around... Sayin' hi."
        TM "I'm glad ya like this place so much, y'know?"
        TM "..."
        TM "Don't be gone too long, alright?"
        TM "We'll always have a door open for ya at the Miracle Cafe!"
        TM default "I hope to see you again!"

    elif highest_affec == "Lyra":
        show Lyra at right
        LY "Oh-hoh-hoh!"
        LY "CHERUB!"
        LY "Looks like this is the end of the line for y-"
        LY "Oh."
        LY "Oh, it's... Quite literally the end for all of us."
        LY "Well in that case, looks like your time on earth wasn't spent SO uselessly!"
        LY "Wait..."
        LY "{i}I{/i} have your highest affection?"
        LY "Thats... ABSURD!"
        LY "BEGONE!"
        LY "...Wait."
        LY "It isn't polite to leave without a proper goodbye... Looks like your foolish ways rubbed off on me."
        LY "Goodbye, Ambrosia! We hope to see you VERY soon!"

    elif highest_affec == "Harvey":
        HV "..."
        HV "You again..."
        HV "What are we doing in a place like this...?"
        HV "Oh, demo's over? My bad-- ahem."
        HV "Congrats, Ambrosia. You reached the end."
        HV "Can't say I know you that well, but..."
        HV "Thank you. For being here."
        HV "I hope to see more of you in the future."
        HV "Oh! uerm-- ahem."
        HV "Thank you for choosing the Miracle Cafe. I hope to see you again."

    $ MainMenu(confirm=False)()

label demo_end_2:
    MD huh "I see..."
    MD "thank you."
    MD happy "Regardless, I've had fun."
    if mad_helped == True and amb_goth == True:
        MD "Seeing you serve a smile for the first time,"
        MD "Trying new things."
    MD "It's been an honor, thank you."
    MD "I really, truly, hope to see you again..."
    $ MainMenu(confirm=False)()
    

label halloween:
    TM "day off!"
    CH "ahhh I'm possessed!"
    return


## --upstairs character events


label mad_door:
   
    play sound "audio/710064__johnytud__door01_open.mp3"
    scene upstairs
    play music "audio/hajimetenookashidukuri.mp3" fadein 0.5 fadeout 1.0
    if Total_affec["Madoc"] >= 80:
        MD smile "Ambrosia-- it's-- Nice seeing you around. Come in."
        call mad_room
                

    elif Total_affec["Madoc"] >= 50:
        MD shock "Hello. What brings you here..?"     
        call mad_room

                
    else:
        MD default "...Ambrosia, was it? Hello."
        menu:
            "Don't need anything, just wanted to check up!":
                call mad_room
                
            "...":
                MD "...Take your time."
                nar2 "They spend their time in silence. Only with a gaze, waiting for the other to speak."
    return
label mad_room:
    scene mad_room
    if amb_goth == True:
        $ Topics.update({"Makeup tips??" : "Makeup_Tips"})
    call screen topic_options
    
    $ renpy.call(current_host + "." + current_topic)
    return

label .Favorite_artist:
    $ Total_affec["Madoc"] += 2
    MD default "Hard to say, really."
    MD huh "There's many that dragged me out of bad times, many that made me reconsider my thoughts and feelings."
    MD "That's probably not what you wanted to hear, wasn't it?"
    MD "Hm..."
    MD "Depends on what you consider art."
    nar2 "Madoc rose himself upward, placing himself across a library of vinyls strung across the wall."
    MD default "My favorite kinds of art are the ones that motivate and inspire."
    MD smile "Like... Music."
    nar2 "His fingers carefully flip through a crate, pausing to gaze at each cover."
    MD happy "Ah, wait... That's still quite a broad horizon..."
    MD default "When I was younger, my folks, they took me to the local shows."
    MD "There were big crowds, dancing to their own rythym."
    MD "They met on the scene, those two."
    MD "The world of music brought them together... In a way, it made my existence."
    MD "Medkit, Brothers of Sacrilige..."
    MD "it's Hard to pin my adoration onto an individual, it was the group effort and the community that made it so special."
    amb1 default "Oh, yeah I see where you come from!!! I mean everyone here is so amazing too, I think..."
    amb1 ugh "I mean... How am I supposed to-- pick a favorite?"
    MD "Maybe. We're hardly any Arabella Requiems..."
    if mad_helped == True:
        $ Total_affec["Madoc"] += 3
        nar2 "He turns to Ambrosia, resting a hand on his own cheek."
        MD "Well, not yet, anyway."
        MD "I get the feeling that with you on board, we might just turn this place into something spectacular."
        MD "Ambrosia, what're you in the mood for? maybe I can put on something nice..."
    return


label .Sweet_or_sour_foods:
    $ Total_affec["Madoc"] += 2
    MD default "...Ah."
    MD "Hm..."
    MD "Sometimes, I'd eat only one thing for months."
    MD huh "There's seemingly no rhyme or reason to what I like, from what I notice."
    MD "How about you...?"
    amb1 happy "Sweet all the way! I mean, where I'm from, we don't even have chocolate!"
    MD "Is that so? I'm so sorry."
    amb1 default "Huh, what for?"
    MD "Oh, it's nothing. Discard that."
    amb1 "Don't worry about it, okay? It's uh... A cultural thing!"
    amb1 "Something about not needing temporary fleeting things, y'know?"
    MD "That sounds... Hard."
    amb1 "What? Not at all! I've been getting well just fine!"
    MD "I see, I'll take your word for it..."
    amb1 happy "Hey! wait!"
    amb1 "I dunno if anyone's ever told you this but I love the way you talk...!"
    MD happy "hahah... That's something I picked up from {i}my{/i} folks."
    return


label .Favorite_meal:
    $ Total_affec["Madoc"] += 2
    MD default "right now?"
    MD smile "Right now... It's the croissants. Ah, and with a side of a macchiato, too?"
    MD "It's so good."
    MD huh "If only Blaze was less tight lipped about some of his recipes.."
    amb1 happy "I'll HAVE to try them out for myself, then!"
    MD default "My tastes are very... Diverse. Croissants and some caffine is just, one in a long list."
    MD "Have you ever had those... Snails?"
    MD "I tried those with a friend a few years back."
    MD "...It's not on my list of favorites, though."
    amb1 "That's so cool! Maybe one day I could try every single one!"
    MD smile "If I remember to write them down, sure."
    return


label .Inspiration:
    $ Total_affec["Madoc"] += 2
    MD default "Music."
    MD "That's where I find mine."
    MD "it's a beautiful thing, isn't it?"
    MD "People working through their experiences and translating it into poems and songs."
    MD "Something about that-- it almost... Transcends words."
    MD "Don't you think...?"
    amb1 default "Ah... I think I get what you mean, I used to listen to harps and lutes and trumpets..."
    amb1 "Never played myself, though! I wasn't allowed to."
    MD huh "Oh, I see..."
    MD "If you don't mind me asking, how come...?"
    nar2 "Hands in his lap, he shifts closer to the angel, ever so slightly."
    amb1 "Just wasn't allowed to, it's not what u-- I was supposed to do..."
    amb1 "I know a thing or two about archery though!"
    amb1 "I'm practically an expert!"
    MD default "Wow, I'm jealous..."
    MD "I never touched a bow before..."
    MD "But I do know a few things about instuments..."
    amb1 happy "Maybe a little trade-off is in order, then!"
    MD smile "I'm not against the idea, myself."
    return

label .Weather:
    $ Total_affec["Madoc"] += 2
    MD default "It's hot."
    MD huh "...Don't like it."
    amb1 happy "oh, man! Preaching to the choir here!"
    amb1 "Winter is superior in every way!"
    amb1 "I just have to catch a snowflake on my tongue... That seems so fun!"
    MD default "...You haven't before?"
    amb1 "OH? oh!"
    amb1 "Where I'm from didn't have any... Still new in town! Hahah..."
    MD "I see. Sorry if that was... Insensitive of me."
    amb1 "No, not one bit!"
    MD huh "Must be exhausting there, for me it'd be..."
    amb1 ugh "Guess I never thought about it before...?"
    amb1 happy "I just can't wait to see what sorta experiences this place gives me!"
    MD "yeah, I do too."
    MD smile "I hope this place treats you well."
    return


label .Mystery_Customer:
    $ Total_affec["Madoc"] += 2
    MD huh "Poor guy, that one."
    MD "I'd feel a little more bad if he wasn't super rich, but still."
    amb1 "Who? Exactly? Is he?"
    MD "Someone who gave our services an interesting spotlight. Charon showed me the tabloids..."
    MD "Harvey Arison, I think."
    MD "heir to the Arison company. Some business that capitalizes off of the well-being of their kids."
    MD "Celebrities."
    MD "They're writing that he's-- some sort of weird body double that replaced one of the Arison sisters, way back."
    MD "Whatever that means."
    MD "I don't get why everyone wants to know about him, it's no that big a deal."
    MD "It's none of my business, really."
    MD "We should just worry about keeping everything afloat with all this influx of attention."
    amb1 "Don't worry about me, I've handled things fine already, right?"
    MD happy "That you did, Ambrosia... That you did."
    return

label .Makeup_Tips:
    MD happy "Alright, alright..."
    MD smile "Just remember your end of the bargain."
    nar2 "Turning to find one of his vinyl records, he carefully sets a disk upon the reader."
    play music "audio/BGM_-_043_-_Despair.mp3" fadein 0.5
    nar2 "Soon, the arm's fine thorn scratches the surfcase. The air begins to fill with a tune."
    
    nar2 "Amrbosia claps his hands, a great smile bestowed across him."
    ## goth ambrosia cg here
    nar2 "Madoc finished powdering the last of the pale foundation over his new pupil."
    MD "Think you can handle it from here?"
    MD huh "Everything seems to depend on the person... So it's all about seeing what works best for you."
    amb1 "yeah! Okay! I.. Think!"
    nar2 "Ambrosia's wrist inched carefully over the hood of his eye, the more intent his strokes were, the more uneven they became."
    amb1 sweat "Is-- is your eyeliner cursed?"
    MD "No."
    MD "I'd have a fun story to tell if I did, though..."
    MD "Sounds counter productive, but sometimes you need confidence in your lines."
    amb1 "So like... Do it fast?"
    MD "Pretty much."
    MD "Unless you wanted to use one of my knives to angle things correctly..."
    amb1 "WHAT."
    MD smile "...I'm joking."
    MD default "Here, I have some wipes around here somewhere..."
    nar2 "As the chorus heightens, Ambrosia's lock on the eyeliner followed suit."
    nar2 "Madoc came into view with a small package of wet tissues in tow, carefully placing them atop the wooden vanity."
    MD "This sort of thing takes practice, okay? Don't be too hard on yourself."
    nar2 "In one hand, Ambrosia cleared the evidence of his past, and the other a sheer determination."
    amb1 srs "Okay! I think I got this!"
    nar2 "In one, furious swoop, ink slashed diagonally across his face."
    nar2 "Residue pours down the sides on his face, spilling like dark tears."
    MD shock "Sick...."
    amb1 sweat "Oh... Uhm... Did I overdo it...?"
    MD happy "No. Ambrosia, you did great..."
    MD "Looks like you'll have to teach me a thing or two next time.."
    play music "audio/konekonoosanpo.mp3"
    return


label char_door:
    play sound "audio/710064__johnytud__door01_open.mp3"
    scene upstairs
    $ current_topic = ""
    play music "audio/hajimetenookashidukuri.mp3" fadein 0.5 fadeout 1.0
    if Total_affec["Charon"] >= 80:
        CH sass "You again??? woooowww... "
        CH "No, no, I'm joking! See?"
        CH "YOU of all people are always welcome, hehe!"
        call char_room
                

    elif Total_affec["Charon"] >= 50:
        CH "What's a guy like you doing at a place like this, hm...?"
        CH "Welp, bed's not gonna warm itself! C'mon in!"
        call char_room

                
    else:
        CH aww "Heeeell-ooo! What's up! What's up?"
        menu:
            "Hihi!! Charon can we chat??":
                call char_room
                
            "...":
                CH sass "Cat got your tongue? It's okay though, I LOVE shy guys! ...I'm still totally busy, though, sorry Ambrosia..."
    
    return
label char_room:
    scene char_room
    with dissolve
    call screen topic_options
    $ renpy.call(current_host + "." + current_topic)
    return

label .Favorite_artist:
    $ Total_affec["Charon"] += 2
    CH sass "That's easy,"
    CH aww "Pink Diamond, duh!"
    CH "Can't you tell?"
    nar2 "He spoke, gestering to his outfit."
    amb1 ugh "And.... um--"
    amb1 "Who is that?"
    nar2 "Charon gasps, reeling to his cushions in surprise."
    CH "NO. WAY."
    CH "I get to intoduce you to the BEST girl's group ever! This is so exciting!"
    amb1 "Girls... group???"
    CH "SHHSHSHSHS... Don't ruin this, okay."
    CH "Hold on, here's my favorite track of theirs..."
    play music "audio/ポッピンスキップ.mp3" fadein 0.5
    nar2 "The room fills with this estatic beat, bold lyrics dancing against the rythym."
    amb1 flush "OH!"
    CH "Empowering right? Gets you thinking AND dancing!"
    amb1 default "..."
    amb1 happy "Y'know what? Yeah! It's fun!"
    play music "audio/konekonoosanpo.mp3"
    return

label .Sweet_or_sour_foods:
    $ Total_affec["Charon"] += 2
    CH sass "You're actually insane."
    CH aww "Sweet food!"
    CH default "Wait..."
    CH "Actually, no.. Sour gummies are so good... oh!"
    CH sass "What would you answer?"
    amb1 default "I'd say sweet food, I think...?"
    CH default "oooh, I'm sensing hesitation! How come?"
    amb1 ugh "I... Didn't have a lot of sweet food before."
    CH "WHAT? Okay that's even crazier."
    CH sass "Do you wanna try some? or is this like... A dietary thing."
    amb1 "Well, now wanna try some... It looks so goooooddd...."
    CH aww "You came to the right place, at least. We've got a master chef just a few doors over."
    nar2 "He scoffs at his own joke."
    amb1 "I have had fruits before! I'd day... My favorites gotta be a green apple..."
    amb1 "They're like crispy surprises!"
    CH "Well, I have had flavored greep-apple things... If that's anything to go by..."
    CH "Good choice!"
    CH sass "But..." 
    extend " Isn't that sour?"
    amb1 "I-it is? No, no apples are sweet!"
    CH sass "Like, barely... We've gotta get you to try something else."
    return


label .Favorite_meal:
    $ Total_affec["Charon"] += 2
    CH sass "Can't say all of the above, can I?"
    CH "No... That'd be cheating."
    nar2 "Mulling over, he rests a hand on his other arm."
    CH "Honestly, I'm not even picky. I ate tons of weird crap beforee...."
    CH "I mean, like... When it comes to non-desserts,"
    CH default "I guess... Eel Sushi?"
    CH aww "Does that count? Too bad. It does now."
    amb1 cur "Oh! wow-- I can't even imagine that!"
    CH "You NEVER tried it???"
    amb1 "nooooo...?"
    CH reg "THAT'S SO TRAGIC!"
    CH "I swear, I'll like-- BEG blaze to get us some sometime!"
    CH "You will NOT regret it, okay?"
    CH "The texture? To DIE for, okay?"
    CH "TO DIE FOR!!"
    return

label .Inspiration:
    $ Total_affec["Charon"] += 2
    CH default "Myself."
    amb1 ugh "Really? How does... That work?"
    CH "Every morning I get up, look in the mirror and go"
    CH aww "{i}Yeah, you can do it, big bitch.{/i}"
    CH "And it works! I'm still kicking, aren't I?"
    amb1 "I wish I could do that..."
    CH sass "And who says you can't?"
    amb1 "myyyselllf--?"
    CH sass "Oh, that's TERRIBLE. Being your own worst enemy."
    CH "There's like, only one of you, you know?"
    CH "Hype yourself up!"
    CH "it's how my skins so clear..."
    amb1 ugh "I guess, also.. Um.. Social expectations at large? I'm not exactly-- uhh..."
    CH "Oh c'mon. Don't be like that."
    CH "You're just gonna sit around and take all that crap? for how long?"
    amb1 "Wh-wha.. I thought that was what you're supposed to do!!"
    CH "And are you HAPPY with how this is?"
    amb1 cur "(Humans are so fascinating...)"
    amb1 "I mean, not all that much, no!"
    CH "So fight back! Be yourself and spit in the eyes of people that get you down!"
    CH sass "well, not literally. That could like, totally land you in jail."
    return

label .Weather:
    $ Total_affec["Charon"] += 2
    CH "what's not to love? It's nice and sunny,"
    CH "Flowers are blooming, birds and chirping..."
    CH "Plus, bands are making their world tours and stuff!"
    CH "Shit for the environment, but... Y'know at least nice for the ears!"
    CH "I loooveee outting during the summer... ugh. Why can't it be summer all the time?"
    amb1 "Why indeed..."
    amb1 "What kinda holidays come in the summer, now that I think about it?"
    CH "happiness. Happiness does."
    amb1 "Do. Do you not feel happiness any other season?"
    CH "No."
    CH "Okay I'm kidding but-- still! There's so much to do! It's so exciting!"
    return

label .Mystery_Customer:
    $ Total_affec["Charon"] += 5
    CH aww "I CANNOT believe it. The Arison guy came in."
    CH "came HERE! Of all places! HERE!"
    CH "How do I look? Do you think he saw me?"
    amb1 sweat "Ah-- woah! Isn't that a lot?"
    CH "Not for an Arison!! God, if we got married I'd never had to work a day in my life!"
    CH "And I'd get all of the press he does, too... Wouldn't that be great?!"
    amb1 "?!?! That sounds overwhelming! And I don't even know what his deal is!"
    CH "YOU DOOOON'T?! He's the first guy in the famous all-female enterprise! Son on a ceo!"
    CH "Thing is, They used to have a duaghter, so the rumors say... And people are saying they were late-baby swapped."
    CH "OR! That He's not even a boy, which is SO weird... I know a man when I see one."
    CH "He's like, one of the town's hottest gossips! Eeep!"
    amb1 ugh "I kinda feel bad when you put it that way..."
    CH "He'll be fine! It's not like he can hear us from here, right?"
    amb1 cur "I guess not!"
    
    return



label tam_door:
    play sound "audio/710064__johnytud__door01_open.mp3"
    scene upstairs
    $ current_topic = ""
    
    if Total_affec["Tamura"] >= 80:

        TM "WOA-ho-hoh, it's you, Bro-sia! You need anything?"
        menu:
            "I need you.":
                nar2 "quickly, his cheeks flush a deep red."
                TM blush "WOW! Uhm-- What's that supposed to mean? HAHAHAHAH. Uhm."
                TM "...I'll need some time to myself."
            "Just wanted to hang!":  
                call tam_room
                

    elif Total_affec["Tamura"] >= 50:
        TM "Heyyyyy, Ambrosia! What's up?"
        menu:
            "The sky, silly!":
                TM "HAHAHAH! Now that's a good one!! C'mon in, bud!"
                
                call tam_room
                

            "Nothing much, what about you":
                
                call tam_room
                
    else:
        TM "Huh, 'sup little buddy? You need anything?"
        menu:
            "Just wanted to say hi!":
                
                call tam_room
                
            "...":
                TM "Oh! Uhm... Don't just sit there and look at me... It freaks me out..."
    return
    
label tam_room:
    scene tam_room
    with dissolve
    call screen topic_options
    $ renpy.call(current_host + "." + current_topic)
    

label .Favorite_artist:
        $ Total_affec["Tamura"] += 2
        nar2 "Tamura cushions himself further into the bed, holding his head in his palm."
        TM proud "Art, is like... Everything!! If it's made by human hands it's gotta be some kinda art, yeah?"
        amb1 default "Even working the kitchen...?"
        TM "Are you kidding?! ESPECIALLY working the kitchen! Cuisine and-- and baking and all that,"
        TM "It's one of the purest form of art!"
        TM "To think... One day, some cavemen a long time ago threw together leaves and berries and meat n' a couple bazillions years later.. we're here."
        TM "doing all these fancy-schmancy measurements, with critics governin' opinion of the masses..."
        TM blush "...What were we talkin' 'bout again?"
        extend default " Oh!"
        TM proud "Well, in terms 'a food, there's one person I gotta credit for where I am in this crazy- cookin' journey! My ma, of course!"
        amb1 "(I wonder what that's like...)"
        amb1 happy "One day! I hope to taste some of her food, mr. Tamura!"
        TM "Hahah..."
        TM "For now, whiles it might not be by her hands... I like baking with the same love she did, y'know?"
        nar2 "Tamura kept his gaze apart from Ambrosia, an odd chuckle breaking through."
        return

label .Sweet_or_sour_foods:
        $ Total_affec["Tamura"] += 2
        TM hes "Nooo... Don't make me pick one...."
        amb1 ugh "Was it something I said???"
        TM "It's not that, sweet and sour flavors have their time AND their place!"
        TM "Choosing only one would turn your back to the importance of the other!"
        TM "As a cook, I CAN'T allow myself to do that!"
        amb1 "Well what about preference...?"
        TM "It's not that easy...."
        TM "The highs of a sugary drink out in the sun or the punching delectability and healthiness of citrus and rhubarb..."
        TM "Things change day to day, your needs change day to day!"
        TM "What makes me smile one day can make me sigh on others...."
        TM "Uh... Can I opt for spices?"
        amb1 "What? but wouldn't that be turning your back on both?!"
        TM "I mean--! Spices CAN be in both sweet and sour foods! It's the best of both worlds in a way!"
        TM "Can't say I've ever had enough of that envigorating capsaicin, either!"
        amb1 "I see!! That's so cool!"
        return
    
label .Favorite_meal:
    $ Total_affec["Tamura"] += 2
    TM proud "Oh, this? This one's easy! no contest!"
    TM scream "TANTAMEN RAMEN!!"
    with vpunch
    amb1 "Oh!"
    extend ugh " er-- What's that...?"
    TM proud "Seasame based broth in a bowl of noodles, y'know?"
    TM "yeah, yeah with all of the instant stuff it kinda makes your head spin thinkin' about e'rrything out there."
    TM default "thing is, my favorites' an old family recipe! Got it from great, great, great, great, great, great"
    extend ", great, GREAT grandma, who imported the recipe over from the south!"
    TM "It's got these sleek noodles n' chile oil and pork!"
    TM "Gotta 'dmit, not the most traditional stuff we have, we take a lotta cues from down south, y'see!"
    TM proud "Don't mean it's not served with the fiery passion of a peppercorn! I'd rather drop dead then eat a half-hearted meal!"
    return

label .Inspiration:
    $ Total_affec["Tamura"] += 2
    TM hes "Would it cheap to say... uh-- everyone here?"
    amb1 "Huh, how so?"
    TM default "Well, customers, they come in, and they leave with a smile on their face..."
    TM "Then we have our crew, my friends... You."
    TM "They're all great people who wanna make the street a little more lively in their own little ways, y'hear?"
    TM hes "Madoc's so precise and formal in a way that's so-- welcomin'.."
    TM "And Charon, he's a bit much SOMETIMES but he'd rather jump ship than give up before reachin' perfection!"
    amb1 "And me...?"
    TM "What is there to say? You're you! You're new, and that feels so exciting and fresh!"
    TM "Makes me wanna work even harder to make sure you've got a fun time here, no?"
    amb1 "D'aww... Shucks, I didn't know you felt like that 'bout little old me..."
    TM blush "Not in like-- A weird way! But-- still! I just wanna make sure you're havin' a good time, too!"
    return

label .Weather:
    $ Total_affec["Tamura"] += 2
    TM default "Well, I mean it's real hot..."
    TM  proud "Really gets the blood pumpin' don't it!"
    amb1 ugh "That's one way to put it..."
    nar2 "A glint of determination brews in Blaze's eyes"
    TM proud "'s about my favorite season too, summer!"
    TM "Park's garden's open, gym's open.... Beach, too?"
    TM "I just can't NOT  move around, y'know?"
    amb1 default "I was more of a winter fella, myself!"
    amb1 happy "I mean... fresh snow looks so cloudy...!"
    TM "Hm... Now that I think abouts it, it also gets my blood pumpin. It's so cold it makes me wanna..."
    TM proud "Burn up! Excercisin'!!"
    amb1 "????"
    amb1 "I guess so?"
    return

label .Mystery_Customer:
    $ Total_affec["Tamura"] += 5
    TM hes "So I wasn't hallucinating..."
    TM "He's really here..."
    TM "'is name's Harvey, yeah?"
    TM default "wait, you took his order, didn't you? You already knew that!"
    TM hes "We went wayyy back! Used to be attached at the hip, y'know?"
    TM "But, past is passed, right?"
    TM "Now he won't even look at me straight..."
    TM hes "Then all this mumbo jumbos on the news, turnin' him into this-- this..."
    TM default "Man. Sorry. Don't mean to be such a downer, y'know?"
    TM "He probably wouldn't wanna see me like this, anyway."

    return

    

## --actions
label stats_action:
    show screen action_screen
    
    return

label rest_action:
    nar2 "Ambrosia drifts into a deep sleep..."
    $ energy -= 1
    return

label cook_action:
    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    if tam_helped == True:
        $ Total_affec["Tamura"] +=1
    call stats_action
    $ Cook.holy_switcher()
    
    
    
    
    return

label clean_action:
    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    call stats_action
    if ch_helped == True:
        $ Total_affec["Charon"] +=1
    $ Clean.holy_switcher()
    
    #pause     
    return

label serve_action:

    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    call stats_action
    $ Serve.holy_switcher()
    if met_harvey == True:
        $ Total_affec["Harvey"] += 1
    if mad_helped == True:
        $ Total_affec["Madoc"] += 1
    
    return

label pray_action:
    
    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    call stats_action
    $ Pray.holy_switcher() 
    
    return


# -- Stat events

label stat_events:
    $ Cheat_code.hide_stats_screen()
    hide screen action_screen
    if (Work_stats["Reputatn."] >=68) and (total_days <= 30) and (met_harvey == False):
        
        $ met_harvey = True
        call harvey_meet
    
    elif (Work_stats["Clean"] <= 20) and (total_days >= 8) and (char_chasted == False):
        $ char_chasted = True

        call charon_chast

    elif (Work_stats["Cuisine"]<= 50) and (total_days >= 16) and (cant_cook == False):
        $ cant_cook = True
        call tam_chast
    
    elif (Work_stats["Clean"] >= 80) and (char_amazed == False):
        $ char_amazed = True
        call char_amaze

    elif (cook_event == True) and (tam_helped == False):
        $ tam_helped = True
        call tam_help
        
    elif (clean_event == True) and (ch_helped == False):
        $ ch_helped = True
        call ch_help

    elif (serve_event == True) and (mad_helped == False):
        $ mad_helped = True
        call mad_help

    elif (cook_event == True) and (can_cook == False) and (Work_stats["Cuisine"] >= 80):
        $ can_cook = True
        hide screen action_screen
        call tam_rival
    
    elif (Work_stats["Charm"] <=30) and (serve_event == True) and (mad_sad == False) and (total_days >= 16):
        $ mad_sad = True
        call mad_concern

    elif (Work_stats["Charm"] >=90) and (serve_event == True) and (mad_pep == False):
        $ mad_pep = True
        call mad_stand
    return

label harvey_meet:
    play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
    nar2 "Rush hour broke between the cafe,"
    nar2 "Souls dance in and out, grateful or at the very least- begrudging smiles across their faces as they grab their orders."
    nar2 "Within the sea of faces, a tall figure parted from the rest."
    nar2 "With every step, murmurs blanket the crowd, all eyes just barely grazing past his cold stare."
    nar2 "A permanent disdain marked the stranger's expression, carrying his head high while long locks grace his shoulders."
    nar2 "He scans Ambrosia, a brow furrowed with a lingering sense of curiosity."
    huh "Just a black coffee for me, please and thank you."
    amb1 "Can I get a name for that?"
    HV "...Harvey."
    HV "Harvey Arison."
    $ Topics.update({"Mystery Customer?": "Mystery_Customer"})
    $ Total_affec.update ({"Harvey": 0})
    return

label tam_help:
    camera:
        xzoom 1.1 yzoom 1.1
        xalign 0.56
    scene kitchen 
    with bites
    $ energy -= 1
    play music "audio/hajimetenookashidukuri.mp3" fadeout 1.0
    
    show Tamura scream hype hype_summer:
        xalign 1.0 yalign 1.0 
        linear 0.1 xalign 1.09
        linear 0.1 xalign 1.0
        linear 0.1 xalign 1.09
        ease 0.3 xalign 1.0
    with vpunch
    TM scream "AH!!"

    show Tamura at right, squash
    TM hes "You-- scared me, Ambrosia... You should really be knockin' first, y'know?"

    menu:
        "Just wanting to practice, haha!":
            call .practice_haha
        "*Get on your knees and apologize*":
            call .apologize
        

    return

label .apologize:
    show Tamura at right, squash
    TM "WOAH! Okay, there's... uh... No need for all that."
    show Tamura proud at right, squash
    TM proud "C'mon, now! We're all boys here!"
    
    TM " 's a safe space 'n all that. No need for sorries, yeah?"
    amb1 ugh "OH........ I see......"
    nar2 "gradually pulling himself back up, Ambrosia continued his wet, pitiable streak with a slouch."
    amb1 "Just wanted to make a GOOD impression! That's all..."
    TM "Oh what?"
    TM default "You don't need to worry about all that, yeah? I let'cha in didn't I?"
    show Tamura proud at right, squash
    TM proud "My words 'r as trustworthy as a hot slab of superglue! Just ask any of the others!"
    with hpunch
    nar2 "With that, the great Tamura gave thunderous pats on the back to the wet noodle before him."
    return

label .practice_haha:
    $ tam_cook == True
    show Tamura scream scream hype hype_summer at right, squash
    with vpunch
    TM scream "YEAHHH! Practice makes PERFECT!!"
    
    nar2 "Chest high in the air, Tamura's roar bellowed through the walls."
    $ Total_affec["Tamura"] += 5
    show Tamura proud at truecenter, squash
    with easeinright
    TM proud "Hows about where your skill levels at? Maybe I could whip up a thing or two with ya for good measure!"
    nar2 "From what Ambrosia's read, in this town, standards are lower than the 7th circle of hell itself. In fact, the bottom half of his passionate little resume showed with a bit of loreum ipsum."
    nar2 "Perhaps he got points for making it entirely handwritten."
    amb1 happy  "Absolutely zero, Mr. Tamura!"
    nar2 "Such proud claims were only highlighted further by another grin stretched across him."
    show Tamura proud at squash
    TM proud "WELL! In that case, Y'caught me at a good time, see? I was just about to set up the recipes up here. We're all fresh, y'know?"
    amb1 default "I mean..."
    amb1 "What else is there?"
    show Tamura default at squash
    TM default "Ex-act-ly! Frozen food never has the hard labour of love poured into it!!"
    hide Tamura with dissolve
    

label .practive_haha_cont:

    nar2 "Soon enough, large bags of flour, buttermilk and yeast gets lifted in."
    
    scene comic_thing
    show image Solid("#fff")
    with Dissolve(0.2)
    show Tamura proud at center, squash
    with Dissolve(0.2)
    nar2 "With a hefty PLOMP, powder scattered through the air like fine pixie dust, coloring the atmosphere in a pale hue."
    
    show Tamura proud at center
    TM proud "Alright, this should be pretty simple! it's honey glazed donuts! it's pretty much just bread with a couple or so extra steps, yeah?"
    amb1 happy "...Right!"
    nar2 "True to his words, Ambrosia hasn't had a lick of knowledge for human cuisine."
    nar2 "Not apart from it's status as one of the many gateways to the heart, that is."
    hide Tamura with Dissolve(0.2)
    camera:
        xzoom 1 yzoom 1
    show dot_bg with dissolve
    
    TM proud "I'll start up the fryer, 'n everything's written on that board over there! easy peasy!"
    show deep_fry at zoomie, truecenter
    with easeinright
    nar2 "The angel watched the other reach to set the strange bowl,"
    hide deep_fry 
    with easeoutleft
    show cauldron:
        xalign 0.5
        yalign 0.45
    with easeinright
    nar2 "filling the cauldron with a greasy elixr."
    hide cauldron with easeoutleft
    show amb_list:
        xalign 0.5
        yalign 0.4
    with easeinright
    nar2 "Ambrosia draws to the lettering."
   
    nar2 "eggs, yeast, nutmeg... sugar, vanilla... milk.... and just a pinch of salt."
    show amb_list:
        matrixcolor TintMatrix("#A7BE4F")*BrightnessMatrix(0.05)*ContrastMatrix(1.05)
    with Dissolve(0.2)
    show Tamura hes:
        xzoom 0.7 yzoom 0.7
        yalign 1.1 xalign 0.2
    with easeinbottom
    TM hes "I-- Forgot to get us an electric mixer... Think you have enough elbow grease to pull it together?"
    hide Tamura with easeoutbottom
    hide amb_list
    show amb_list:
        xalign 0.5
        yalign 0.4
    amb1 happy "Oh..?"
    amb1 "Oh!"
    amb1 "Yes, I think so!"
    hide amb_list 
    with easeoutleft
    nar2 "Determined, Ambrosia made a show of himself, stringing together all his might."
    nar2 "bits of batter fly across the countertops, hands unwielding for even a moment."
    TM blush "WOAH?! woah! Okay, okay, I think you're overmixing a little bit--!"
    amb1 "I-- I am?"
    TM "Just a little bit..."
    TM proud "Hey, hey! Don't sweat it, I remembered the towels!"
    nar2 "On top of the raw dough, Ambrosia was quickly caked by a towel- well meaning rough-housing keeping him in place."
    TM proud "There! I think I got all of it!"
    stop music
    TM default "Don't worry, the process usually isn't this... messy... I think you got a little something--uh..."
    nar2 "Tamura's hand makes it's way towards Ambrosia's cheek."
    play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
    nar2 "Ambrosia froze in place."
    nar2 "Tamura's thumb grazes gently against the fuzz of his cheeks."
    nar2 "Not something you'd expect for such rough hands."
    nar2 "a swarm of adrenaline rushes through Ambrosia's chest."
    TM proud "Er- Don't take this the the wrong way, but you should join me at the gym!"
    extend default " I'd love to get a look at your routine! hahah!"
    nar2 "Standing parallel to one another, the moment quiets. The air blooms with a richness that was hard to parse."
    nar2 "That warm glint Blaze held in his eyes harboured a spark of something else, something new."
    TM hes "..."
    nar2 "Admiration, respect..."
    nar2 "No, in front of Ambrosia was that reached beyond his usual kindness."
    TM "UHM!"
    play music "audio/hajimetenookashidukuri.mp3"
    extend proud " Right! right.."
    TM proud "We have ta' cut em into little holes now! Hows about you watch n' learn, yeah?"
    amb1 flush "YEAH! Sounds... sounds good!"
    
    jump daily
    

label ch_help:
    $ energy -= 1
    scene cafe_angle
    with bites
    play music "audio/dozikkomarch.mp3" fadein 0.5 fadeout 1.0
    CH sass "Oh, the second brooms and stuffs over there, by the way."
    nar2 "The voice slithered like a large shadow cast upon a wall, freexing the angel in place."
    nar2 "The bleach blonde gave pause, carefully studying the other head to toe."
    CH "Y'know... As resident fixer-upper-er, I hope you realize keeping this place pristine is SERIOUS business..."
    CH default "Like, do NOT get me wrong... But-- to double check, you sure you're up for it?"
    menu:
        "YEAH-- of course I do!":
            call .of_course
        "Well, now I'm not sure...":
            call .not_sure
    return

    
label .not_sure:
    CH aww "Don't sweat it! Most people aren't..."
    CH "Besides, I'm sure you'll get along just fine in the cleaning department eventually, Ambrosia!"
    CH "I mean, look at you!"
    CH "You can fix yourself up just fine!"
    amb1 flush "OH! uhm.. Thank you!"
    play music "audio/konekonoosanpo.mp3" fadein 1.0 fadeout 1.0
    jump daily

label .of_course:
    $ Total_affec["Charon"] += 5
    $ ch_broom = True
    nar2 "Charon scoffs lightly, transfering a hand to his hip."
    CH aww "Looks like you actually have some bite to you!"
    amb1 flush "(???????)"
    CH default "I got this whole system I got going on, see?"
    CH aww "But, with a drive like that, I think you'll be able to catch up just fine!"
    nar2 "A soft giggle leaving his lips, Charon dashes away to sweep across corners."

label .of_course_cont:
    with dissolve
    nar2 "Ambrosia kept intent on the dust, as miniscule as they might come."
    nar2 "Counters, floors, tables, none were a match to Ambrosia's meticulous attention."
    CH sass "Huh..."
    nar2 "The charming voice pokes through his concentration, Ambrosia pulls away from the desk."
    amb1 ugh "Am I doing something.... Wrong?"
    CH default "No, no, not at all!"
    CH "The opposite, really... When you do it-"
    CH aww "it's like you clean with 7 arms! Super swift!"
    amb1 default "Thanks, I think...!"
    CH "Oh, don't give me that, you we're great..."
    CH default "If I were to give pointers-- here-!"
    nar2 "In place, he makes mutliple digs at the floor, almost like waving a baton to the ground."
    CH "You're suppised to like, alternate between ways to sweep so your wrist doesn't cramp up!"
    amb1 "................"
    CH "ah.... can I--  use your broom?"
    play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
    nar2 "With a nod, Charon paces behind him."
    nar2 "Slinking behind him, Charon sweeps his arms beneath Ambrosia's."
    amb1 flush "(?!!!????)"
    CH "See? easy! Like this!"
    nar2 "His hands kept away from grazing Ambrosia's, displaying their positions shyly."
    CH "Like, rememember to switch up what you're doing every few minutes."
    CH "Don't think you're safe from wrist cramps! Okay?"
    nar2 "His soft breath grazed his ear, hands just a hair away from Ambrosia's."
    amb1 "{i}yeah, yeah easy....!{/i}"
    nar2 "Without another glance, Ambrosia could feel a smirk bubbling across the other's lips."
    CH "You know, Ambrosia... I think, with practice... You'll be perfect as my assistant!"
    amb1 "WHWHWH--"
    CH "Oh, don't sweat it, you'll be great! Pinkie promise!"
    CH aww "Oooh! Should we try wrist excercises next...?"
    jump daily

label mad_help:
    $ energy -= 1
    play music "audio/dozikkomarch.mp3" fadein 0.5 fadeout 1.0
    MD default "Cute."
    amb1 flush "sorry? Did you- mean me?"
    nar2 "Quickly, a sharpness pierced the divine being, warmth flooding from ear to ear."
    nar2 "Ambrosia bolds up like a soldier, complete with a salute."
    MD shock "Ah..."
    nar2 "Madoc pulls back, glance slowly wandering apart."
    nar2 "In that instant, the weapon that pierced the angel's lung shattered."
    MD "I misspoke..."
    MD huh "I'm saying you're doing a good job, being... You."
    nar2 "He lofts his head to the side, a smile gradually sharpening from ear to ear."
    MD default "Have you done-- this before...? Serving, dealing with people?"
    menu:
        "No, not really...":
            call .not_really
        "Yeah, no sweat!":
            call .no_sweat

    return
label .no_sweat:
    MD huh "Is that so?"
    nar2 "He paused, in thought."
    MD "I would've thought I would've remembered your face from somewhere, then..."
    MD shock  "I guess it's no surprise. You seem like a natural."
    nar2 "Fibs weren't Ambrosia's strong suit, admittedly."
    nar2 "Even still, his cheeks ached the more the minutes pass."
    amb1 flush "Thank you! I won't let you down!"
    MD smile "I don't doubt you will."
    jump daily  


label .not_really:
    $ Total_affec["Madoc"] += 5
    MD huh"I see, that's a shame."
    MD  "This business, it gets hectic. Especially with tons of people pouring in."
    nar2 "His gaze narrowed, poorly concealing the wrinkle crossed over his nose."
    MD default "It's a lot to handle at first, but I have some pointers."
    MD "First though,"
    nar2 "He paused, turning his eyes towards Ambrosia's direction."
    MD "that posture is perfect, don't worry about that."
    MD "Also... Keep-- smiling like that."
    MD "It gets people talking and giving tips..."
    MD "Hm..."
    nar2 "His tone was set firm, but was the furthest from cold."
    nar2 "His even that short hum carried that affirming, smooth texture. It's like running your hands against a lucky pebble you'd find in the grass."
    MD "Maybe you learn better with examples..." 
    nar2 "He suggested, softly."
    MD "How about-- we practice?"
    amb1 happy "Ah... doesn't sound like a bad idea!"
    amb1 ugh "But no one's here yet..."
    MD "I meant-- I'm the practice customer."
    amb1 default "OH! oh...."
    nar2 "With a nod, the angel turned the corner." 
    nar2 "Upon his welcome re-arrival, he painted his expression with the most cheesed smile any divine or man could wish for."

label .not_really_cont:
    with bites
    scene cafe_angle
    play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
    nar2 "Madoc sat atop the plush seat, big arms folded across the counter. Trying hard not to return a stare, he gazed blankly at a wall." 
    amb1 default "Ah-- Hello!"
    nar2 "A little notebook was prepared in Ambrosia's hand, pried to an innocuous page."
    nar2 "His mind narrowed into the pen fixed between his fingers, gently bouncing it off of the paper."
    amb1 "Good morning! Welcome to the Miracle Cafe, how may I take your order...?"
    nar2 "The air quiets."
    nar2 "The world gives pause to Madoc's smile, quickly, the air around them chiming with his laughter."
    MD happy "That's good!"
    nar2 "He spoke, hands fidgeting against each other."
    MD "I mean it... We can workshop that."
    MD default "It takes a lot of patience."
    MD smile "The trick is to pretend like you're talking to a friend."
    amb1 ugh "Oh, Are we-- not friends right now???"
    MD huh "No, I meant when I'm In the customer role..."
    MD "You can pretend you're talking to me, then?"
    amb1 "{i} That's just gonna make me more nervous...{/i}"
    MD "I-it will? Sorry..."
    amb1 ugh "That's a good thing! I swear!"
    amb1 happy "As a wise man once said you're just... REALLY good at being you!"
    MD default "Oh...?"
    MD smile "Clever. I like that..."
    MD happy "Thank you."
    play music "audio/asayakenomachi.mp3"
    jump daily 

label tam_rival:
    
    if tam_cook == True:
        $ Total_affec["Madoc"] += 5
    else:
        $ Total_affec["Madoc"] += 2
    TM proud "You're never gonna believe this, Ambrosia..."
    TM "The customers, the ones writin' all the reviews- They love the pastries!!"
    nar2 "He gave a loud sniffle, staring the angel with wet eyes."
    TM "BUT! They're sayin' they like yours the most, when ya handle the stove...!"
    TM "You're growin' so fast, bud!! I have ta' step up my game!!"
    return

label char_amaze:
    if ch_broom == True:
        $ Total_affec["Charon"] += 5
        CH "See? What did I say?"
    else:
        $ Total_affec["Charon"] += 2
    nar2 "Giggling, he marvels at the countertops and floors with a grin."
    CH aww "It's like no one was even there! You're AMAZZING, Ambrosia!"
    amb1 happy "Really?"
    CH "Really, really!"
    CH "tch, at this rate I might have to retire..."
    CH "Kidding!"
    return
    
label charon_chast:
    $ Total_affec["Charon"] -= 2
    CH reg "OH-- my god... Oh my god."
    CH "What is that smell--- is that from the kitchen?! Lemme find the air freshener--!"
    amb1 sweat "(Goodness... It's not that bad, is it??)"
    CH "Lend a hand out here, will you? I'm practically working overtime heree!"
    return

label tam_chast:
    $ Total_affec["Madoc"] -= 2
    TM hes "err.... Maybe you should sit this one out, bud."
    TM "I'll handle things just fine out here in the kitchen, kay?"
    amb1 ugh "(I haven't been that bad at cooking... Right?)"
    return 

label mad_concern:
    if mad_helped == True:
        MD huh "Are you okay...?"
        MD "You haven't been looking... like usual."
        MD "Maybe you should do something less taxing for now, like cleaning...?"
    else:
        nar2 "Madoc glares the other server down, while he can't muster words, his eyes show great pity."
    return 

label mad_stand:
    if mad_helped == True:
        $ Total_affec["Madoc"] += 5
    else:
        $ Total_affec["Madoc"] +=2
    nar2 "Crusing past his coworker, Madoc's hand hesitates over Ambrosia's shoulder."
    amb1 "Oh, it's okay! Feel free to!"
    MD smile "You do great out there. You keep doing great out there."
    MD "I think our ratings got up by tenfold, Ambrosia..."
    MD happy "I couldn't have done it without you."
    nar2 "As a grin was flashed, Ambrosia's chest couldn't help but ache."
    return

label week_events:
    
    call stat_events
    if cook_event == True:
        call cook_action
    elif clean_event == True:
        call clean_action
    elif serve_event == True:
        call serve_action
    elif pray_event == True:
        call pray_action
        
    return


label rand_events:
    $ Cheat_code.hide_stats_screen()
    hide screen action_screen
    
    if (chance == 2) and (Self_stats["Social"] >= 70) and (Work_stats["Cuisine"] >= 30) and (food_war == False):
        $ food_war = True
        call .food_fight
    elif (chance == 3) and (mad_pep == True) and (mad_poet == False):
        $ mad_poet = True
        call .mad_poetry
    elif (chance == 4) and (gym_bros == True) and (current_month >= 1) and (early_bird == False):
        $ early_bird = True
        call .gets_worm
    elif (chance == 2) and (Self_stats["Stylish"] >= 60) and (mad_makeover == False):
        $ mad_makeover = True
        call .makeover_makeover
    elif (chance == 5) and (Work_stats["Charm"] >= 60) and (music_lovers == False):
        $ music_lovers = True
        call .music_loving
    return    

label .food_fight:
    scene cafe_angle
    with bites 
    play music "audio/hajimetenookashidukuri.mp3" fadein 1.0 fadeout 1.0
    CH aww "And that's why ketchups are basically soup!"
    MD default "...No."
    CH sass "What do you {i}MEAN{/i} no? I thought my arguement was pretty conclusive!"
    CH "Don't tell me you disagree with something so fool-proof..."
    MD "I violently disagree that ketchup is a soup."
    MD "When you go to the store or a market, ketchup isn't placed in the soup aisle."
    MD "Because just it doesn't make sense. Ketchup's not a soup."
    CH "Ah but that's what the big corperations WANT you to think!"
    MD "Listen, I don't like them either but what-- exactly would they benefit from doing that?"
    CH default "I dunno! You'll have to ask a big-corp-ceo next time you walk past one!"
    MD "You are... Impossible sometimes, I hope you know that."
    MD "You can't {i}drink{/i} ketchup, because Ketchup isn't meant to be consumed like that. Ketchup is a sauce."
    CH "One can be two things at once, no?"
    MD "...That doesn't apply to ketchup."
    MD "Because ketchup. Isn't. Soup."
    CH sass "And why not?"
    MD "If you make soup with tomatoes, it already has a name."
    MD "Tomato soup."
    MD "You simply do not turn on a stove and put a pot on it and go-"
    MD "Today I'm making a nice bowl of ketchup."
    MD "You call it tomato soup. The texture is creamy, but not too thick to be a solid."
    MD "Because tomato soup is, in fact, a soup."
    CH aww "Not so fast! Here's where i get you!"
    CH "See, not all ketchups are the same consistency! Some are runnier than others. Thats why some bottles some with instructions!"
    MD huh "You've just contradicted yourself."
    CH "Huh? Where?"
    MD default "Your arguement was ALL ketchup is classified as a soup."
    MD "If you state that only some ketchups fall under the umbrella of soup that's not what you initally proposed."
    CH "..."
    CH "...Hey, has anyone ever told you you'd be a good lawyer growing up whenever you corrected someone?"
    MD default  "Yeah, why?"
    CH "....Nothing, no reason."
    CH "hey! Blaze! Blaze, Blaze, Blaze! You're an expert, right?"
    CH "Is ketchup a soup?"
    stop music
    window hide
    #put cg here
    show Tam_r_u_fuckin_srs_rn
    with Dissolve (0.2)
    pause 
    play music "audio/hajimetenookashidukuri.mp3"
    MD "I think that's a no."
    play music "audio/konekonoosanpo.mp3"
    jump daily 

label .mad_poetry:
    scene cafe_angle
    play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
    nar2 "The night barely bid the sun a farewell, light trickling in gently through the windows."
    MD default "Ambrosia...? You're up early..."
    nar2 "sat comfortably atop the chairs, Madoc sat against the shy sun."
    nar2 "A pen sat between his fingers, scribbling down notes using one of the various notepads around the lot."
    amb1 "I'd say the same about you, y'know... Did you get all 8 hours of sleep?"
    MD "..."
    MD "....."
    MD smile "....Yes."
    amb1 ugh "That sounds like a lie."
    nar2 "Madoc sighs, hanging his head"
    MD "I'll go back to bed soon, promise..."
    MD hes "I Just feel more... Um."
    MD happy "inspired at this time of day."
    MD "No one's here to judge, the sun's just getting up...."
    nar2 "Ambrosia smiled, pouring his attention to the golden rays."
    amb1 "yeah! I get what you mean... It's one of earths core beauties, isn't it?"
    MD "Yeah... Yeah."
    MD "If you're not doing anything, you're welcome to join me."
    menu:
        "Join him":
            call .joining
        "Do not":
            play music "audio/asayakenomachi.mp3"
    return 

label .joining:
    $ Total_affec["Madoc"] += 5
    nar2 "Ambrosia plopped to the seat, settling deep into the cushions."
    amb1 "Oh-- wow these things are soft--!"
    MD "No kidding. Guess it helps you concentrate better with the food... or something."
    MD "I know it helps me concentrate with writing..."
    nar2 "Ambrosia studied the way his hands moved across the page, each letter scribed so intently."
    amb1 "What {i}are{/i} you writing anyway?"
    MD "...I'm not sure yet."
    MD "I'm just... Scribbling down concepts and feelings until I work out something..."
    nar2 "He glances up from the page, tilting across his head."
    MD "Hmph..."
    MD "Can I use you for inspiration?"
    MD "I think I have something."
    amb1 flush "......Me? you-- you mean me? me?"
    MD "Yes, exactly."
    amb1 "I'm flattered!!!"
    nar2 "Reading Ambrosia, Madoc shuffles back in his chair."
    MD "If it makes you overwhelmed, I can always find something else."
    MD "I dunno, something about overcoming new experiences with pride. Something like what you do everyday."
    MD "It's nice."
    amb1 "Well-- don't sell yourself too short here! I-I'm sure you'll find tons of inspiration from-- um, yourself, too!"
    MD "Hah..."
    MD "My story, the one about how I got here. It's not all that interesting in comparison."
    MD "Blaze's a classmate of mine who wanted to do me a few favors, that's all."
    amb1 "Are you kidding?! That's super interesting!"
    amb1 "Mr. Tamura showed you kindness! That's super cool!!"
    amb1 "Plus you're hardly a bad fit for this place... I haven't seen a single frown on a customer the second you leave their table!"
    nar2 "Madoc widens his eyes, turning his gaze to his muse."
    MD "...Wow."
    nar2 "His voice curls."
    nar2 "The resonance fell soft on the ears, butter on a hot pan."
    amb1 "When you're done one of your other poems, I'd love to read it!"
    amb1 "Or- or listen! If you like reading them yourself."
    MD "...Thank you."
    MD "I think I might just need your optimism for this next piece."
    jump daily 



label .gets_worm:
    TM "if i dont work i die"
    amb1 "OK"
    return

label .makeover_makeover:
    scene kitchen
    with bites
    play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
    nar2 "The sun was ripe and early, orange hue dusting the surfaces."
    nar2 "Tamura started setting up camp for the long road ahead, mixers displayed across counters, dishes all in order."
    nar2 "To his left, an enthused Charon organizing each clean bowl and plate with size, shape and color... If dust wasn't his core problem already."
    nar2 "Like clockwork, Madoc found himself in front of a coffee dispenser. One of few that sat around the room, the only one that took instant coffee for an answer."
    if tam_helped == True:
        nar2 "Safe to say it was something of a reluctant pity gift."
    nar2 "Ambrosia saunters to the kitchen floor, coolness greeting his skin."
    nar2 "With a cusory glance around the room, each soul seemed where it belonged."
    nar2 "Seeing the folk idling to a rythym their heart made was a sight akin to watching the autumn saturate trees or noticing shiny raindrops trickle down glass."
    nar2 "To no one else, Ambrosia sighed."
    nar2 "One deep sigh, drenched in an admiration the rest would never understand."
    nar2 "but Ambrosia couldn't watch forever, no."
    nar2 "Levelling himself, he hid behind the goth, mimicking the lines formed each afternoon."
    amb1 default "(Alright, me! It's customary to make small talk in situations like this!)"
    play music "audio/hajimetenookashidukuri.mp3" fadein 1.0 fadeout 1.0
    nar2 "Just as the brew just reaches the end of the brim, it's mug made a home in Madoc's hands."
    nar2 "Madoc quickly shrank in a jolt."
    MD shock "Ambrosia? Hi."
    nar2 "He began, almost warily."
    MD huh "Pardon me. I'm not usually this jumpy..."
    nar2 "A wry laugh worms out of Ambrosia, racing for the very-human, very-nomral activity."
    nar2 "Reaching for the cappuccino pod, he sorts out his own order."
    amb1 sweat "Didn't mean to give you a heart attack, hahah!"
    MD default "No, no it's nothing."
    amb1 sweat "(Okay! Now go in for the strike! You got this!)"
    amb1 cur "Can I ask you something? you prolly get this a lot..."
    MD huh "....Sure..."
    amb1 "Do you get up really early to do your makeup like that?"
    MD huh "You wanted to ask {i}me{/i} that?"
    amb1 happy "I'm not talking to anyone else right now, so no!"
    MD "..."
    MD "In a way, yes."
    MD default "Wouldn't have this on, otherwise."
    amb1 happy "Aha! So those brows aren't natural!"
    MD happy "Of course not... They don't grow that neatly."
    MD default "I got it from my parents, who got it from their favorite bands. Who got it from their parents and their favorite bands."
    MD huh "In a way, it's like family tradition..."
    amb1 cur "Really? I didn't know that!"
    nar2 "Madoc notes the height in Ambrosia's voice, the way his eyes ooze with such a raw wonder."
    nar2 "With an exhale, he peeked at the clocks handles."
    MD "We have the time. I can show you how it's done if you want."
    amb1 "Like-- a do-over??"
    MD "No, no, like... A makeover. Not forcing you, to, though."
    menu:
        "Accept":
            call .accept
        "Deny":
            call .deny

    return
label .accept:
    scene mad_room
    with bites
    $ Total_affec["Madoc"] += 5
    $ amb_goth = True
    nar2 "The walls were as well dressed as it's owner, top to bottom in a stylish licorice black."
    nar2 "Shelves across the room were lined with picutres and names Ambrosia's never heard of, provocative covers decorating the fronts."
    nar2 "The wood felt archaic and well loved, even down the the dresser and it's intricate carvings."
    nar2 "Ambrosia was firm against a high seat, curling his fingers over the round brim."
    scene image Solid("#000")
    with dissolve
    amb1 "Can I open my eyes yet?"
    MD default "You keep squirming, so no."
    amb1 "It feels weird on my eyes.... I can't help it."
    MD "That's normal."
    MD "Just-- hang on and..."
    pause 
    ## cg here
    scene amb_goth
    with bites
    amb1 happy "WOAH, wait?!"
    amb1 "That looks so... I look so..."
    amb1 "That's actually me?!"
    amb1 "Can I wear this all the time?"
    MD huh "If you want clogged pores, sure."
    nar2 "Ambrosia clicks his tongue... Followed with a light shake of the head."
    amb1 "Gah... Now I wanna ask for this every day!"
    MD happy "Okay, let's not go that far..."
    MD default "I can always teach you the basics. My only charge is listening to bands with me, deal?"
    amb1 "EEEE!! Okay! deal!"
    jump daily 

label .deny:
    MD "If you say so."
    MD "If you have any further questions, my door is always open."
    jump daily 

label .music_loving:
    play music "audio/houkagonoyuzora.mp3" fadein 1.0 fadeout 1.0
    nar2 "The morning was fresh as daisies."
    nar2 "The cafe's layout, never felt stale beneath the early sun."
    nar2 "From it's soft parralel chairs, to tidy counter tops. The way the flooring shimmers to a bright amber."
    nar2 "Entering the scene, Ambrosia was met with the tables all in place, decor waiting patiently where they always had."
    nar2 "That, and a Madoc and Blaze heaving around the corner."
    nar2 "In their arms, they shared an embrace with a hulking machine with a rounded top. The gizmo towered over the former, just barely reaching the head of the latter."
    amb1 happy "Oh! I think I remember those!"
    nar2 "With a collective grunt, the pair rested the machine to the ground. Tamura carries a large grin, the glint in Madoc's expression brightening ever so slightly."
    TM hes "Sorry to wake you up this early, bud... Hope it wasn't too hectic."
    amb1 default "No! Not at all I wake up this early anyway!"
    MD default "Do you like the new jukebox?"
    TM proud "It was his suggestion and thank the heavens for that, amirite?"
    amb1 happy "Yeah! I mean, music is one of the greatest gifts humanity has!!"
    amb1 "It's so awesome that even our PATRONS can share it around!"
    MD smile "My thoughts exactly."
    MD huh "I couldn't wrack the funds for a an older piece but..."
    nar2 "Pausing, he pats the top of the rounded rome."
    MD happy "This beauty still works."
    nar2 "Running to the front, Ambrosia's excitement muttles into confusion."
    amb1 "...."
    amb1 "Okay how does this one work?"
    MD smile "It accepts CDs and Apods."
    amb1 "Ohhhh! Apods, I remember those too..."
    TM "I used to have one of those before, too! When I was a small fella..."
    TM blush "Dunno why we ever stopped using them..."
    amb1 sweat "PEOPLE DON'T USE THEM ANYMORE?!"
    TM "No???"
    MD shock "I do, if that counts..."
    jump daily 

## - Free Time Events, affection based events that trigger after hitting a certain point

#label ft_events:
    #make this a funtion at some point
    #return
    #affection-based events that take up your night slot!

## -- Map actions
label LI_sched:
    if (met_harvey == True) and (harv_book == False) and (lib_event == True):
        $ harv_book = True
        call harvey_book
    elif (gym_event == True) and (gym_bros == False) and (gym_event == True):
        $ gym_bros = True
        call tam_gym
    elif (jogging_pals == False) and (park_event == True) and (chance == 3):
        $ jogging_pals = True
        call tam_park
    elif (mall_event == True) and (ch_boba == False):
        $ ch_boba = True
        call ch_boba
    elif (beach_event == True) and (chance == 2) and (ch_beach == False):
        $ ch_beach = True
        call ch_beach
    return

label map_actions:
    $ Cheat_code.hide_stats_screen
    
    call LI_sched
    
    if lib_event == True:
        call library_action
    elif gym_event == True:
        call gym_action
    elif ice_cream_event == True:
        call ice_cream_action
    elif beach_event == True:
        call beach_action
    elif park_event == True:
        call park_action
    elif mall_event == True:
        call mall_action
    return

label ch_boba:
    scene mall
    play music "audio/dozikkomarch.mp3" fadein 0.5 fadeout 1.0
    GY 2 "Wait, isn't that--?"
    GY 1 "Oh my god, shut up! He can hear us, you know! shhh-shh-shhh..."
    nar2 "Ambrosia whips around, spinning towards the distant chatter."
    GY 1 "See? Look what you did, idiot!"
    amb1 cur "Hello...?"
    amb1 "Can I help you...?"
    GY 2 "OH CRAP WHAT DO WE DO NOW!"
    GY 1 "Don't look at me! You're the one who got us into this!"
    GY 2 "Hey! You, over there! In the red!"
    nar2 "Ambrosia nods expectantly, head tipped over to the side."
    GY 2 "Have you seen Char' around?? He was supposed to meet us on [day_of_week[current_day]]s here!"
    nar2 "Hollers the stranger, cut off by a force of the elbow."
    GY 2 "Or, you know... Like every other day, too."
    GY 1 "You're like, his co-worker, riiighhht???"
    amb1 "Uhm-- yeah!"
    nar2 "The clamour hushes as a new face emerges past the crowds."
    nar2 "Shining against the sun pouring from the glass ceiling, Charon effortlessly wore a confident expression."
    CH aww "So sorry~!"
    nar2 "He began, leaning foreward to the two people."
    CH sass "I kept having to fix my hair, like over and over again... You know how it is."
    nar2 "He throws a glance towards a new subject, moving into a smirk."
    CH aww "Ambro-sia~! Hey!"
    CH "We were just out for some bubble tea, right?"
    nar2 "The other two nod frivilously in response."
    CH "Since you're already here, It seems like we already deemed you cool enough to join us!"
    CH "Well, what do you say...?"
    nar2 "Ambrosia rushes to pad down his pockets, nearly breaking into a sweat."
    nar2 "Charon snickers, shifting his hand to the other hip."
    CH "No, no, you can save it... It's your first time with us, so it's on me!"
    GY 2 "Hey! That's not fair! You never paid for us before!"
    CH sass "...Fineee, fine. You all get free drinks. But just this one time..."
    CH default "So?~"
    menu:
        "YEAH! Sure thing!!":
            call .sure_thing
        "I'm busy...":
            call .busy
    return
label .sure_thing:
    $ Total_affec["Charon"] += 5
    nar2 "Charon couldn't help stifling another giggle, filling the air with bliss."
    CH aww "Good! Good! I knew you were fun!"
    CH default "The boba here is like... The best. No competition."
    CH aww "You're so lucky we got to you! Saves you all the trial and error!"
label .drinking_it:
    with bites
    CH "Ambrosia. Okay, okay, okay, we're like up next what do you want?"
    amb1 cur "Uhhhhh..."
    nar2 "Scanning the menu overhead, the words seem to swirl together."
    nar2 "They sat so compact, organized in a disorganized way."
    amb1 flush "Uhhhhhhmmmm! You! What're you having?"
    GY 1 "Okay, you should definitely get the mango. You will NEVER regret getting the mango."
    GY 2 "I'm pretty sure he was talking to blondie, genius."
    GY 1 "I WAS JUST SAYING!!! God!!"
    nar2 "More bursts of giggles slip from Charon's lips."
    CH aww "Yeah, I don't blame you. Pinkie promise."
    CH default "How about... A coconut blend?"
    CH "You seem like a coconut guy."
    nar2 "The angel balls his fists, raising them to his chin with wonder."
    amb1 happy "reaa-lyy??~"
    amb1 "Okay! I trust your judgement! Order away! Hahahahahah!!"
    GY 1 "..."
    nar2 "The two Gals pause, throwing glances to each other."
    GY 2 "......"
    GY 2 "{i}Is this guy serious?{/i}"
    GY 1 "He is RIGHT here! Stop!!"
    jump daily 

label .busy:
    $ Total_affec["Charon"] -= 2
    nar2 "Charon clicks his tongue, turning to his collegues with a soft pout."
    CH "Alright! There's always next time, okay? You are like... ALWAYS welcome!"
    GY 2 "Are we still getting free drinks?"
    play music "audio/konekonoosanpo.mp3" fadein 1.0 fadeout 1.0
    jump daily 

label ch_beach:
    scene beach
    with bites
    play music "audio/dozikkomarch.mp3" fadein 0.5 fadeout 1.0
    CH aww "Ambroooosiaaa!~"
    nar2 "His song called out across the cold breeze, the hum of gulls circling overhead."
    nar2 "He stood against the open sky, shirt open, donning that same friendly grin."
    CH "You're up early, aren't you?"
    CH "Tsk! Looks like I'll have to share this view from now on, huh?"
    amb1 ugh "Oh, really? I can always go.. or--"
    CH default "No, no no, it's nice! Really!"
    CH "This place, being here..."
    CH "It had to happen eventually, hah?"
    nar2 "The waves wash like mighty clouds, kissed gently by the sun, ebbing and flowing into view."
    nar2 "The pristine waves offer a nice ambience, tides trickling in to greet the shore."
    
    menu:
        "Sit next to him.":
            call .stick_around
        "Turn back.":
            call .leave_early
    return
label .stick_around:
    $ Total_affec["Charon"] -= 5
    play music "audio/houkagonoyuzora.mp3" fadein 0.5 fadeout 1.0
    nar2 "Side by side, the waves brushed against their feet."
    nar2 "In that moment, the texture of sand felt cushioned like plush."
    nar2 "Minutes melt beneath the pink sky, waves baked in a golden hue."
    nar2 "The peace broke with a gentle sigh from Charon's lips."
    amb1 cur  "What's wrong?"
    CH srs2 "Oh, nothing."
    CH "You should've told me you were coming around earlier, y'know. I would've brought a volleyball."
    amb1 default "I think sitting here, right here is just fine by me!"
    CH srs "It just... 'dunno, feels weird having someone next to me."
    CH "watching the same sun. Seeing the same, like-- horizon."
    nar2 "Charon rests his head on his knees, humming so idly."
    CH srs "I used to dream of a sight like this before..."
    CH "Have a beach house, sell lemonades and seashells..."
    CH srs2 "Now it's right here, just around the corner!"
    CH "Except I'm selling coffees instead of lemonades."
    amb1 cur "..."
    CH "Sorry, it's dumb! Right?"
    amb1 srs "What? That's not dumb at all!"
    amb1 "To dream is a wonderful thing!"
    nar2 "Charon chuckles, brushing his bang behind his ear."
    CH srs2 "You're a really sweet guy, Ambrosia..."
    amb1 "I mean it! I do!"
    CH "Something about the ocean... It feels so... Freeing, doesn't it?"
    nar2 "Ambrosia blinks, settling back to the breathing painting ahead of him."
    amb1 default "Ah... ah."
    amb1 "I think I get what you mean."
    amb1 "More than you know, really!"
    amb1 srs "there's so much out there, all at once."
    extend ugh " And it's just... A little out of reach."
    CH default "Yeah! Exactly!"
    CH aww "Took the words outta my mouth..!"
    nar2 "Ambrosia watched Charon light back up, joy lacing back into his tone, excitement bubbling in his eyes."
    nar2 "He couldn't help but share a grin."
    play music "audio/konekonoosanpo.mp3" fadein 1.0 fadeout 1.0
    jump daily 

label .leave_early:
    CH sass "Tch.. That's a shame..."
    CH "Catch you later, Ambrosia!"
    play music "audio/konekonoosanpo.mp3" fadein 1.0 fadeout 1.0
    jump daily 


label harvey_book:
    $ harv_book = True
    with bites
    HV "It's you again..."
    nar2 "Their hands nearly graze, making their way for the same title."
    nar2 "Just one aptly named 'how to talk to people'"
    amb1 "Ah-? oh, hello."
    menu:
        "Mister Arison...?":
            call .mister_arison
        "...":
            call .silence
    return
label .mister_arison:
    $ Total_affec["Harvey"] += 5
    amb1 "Mister... Arison, right?"
    HV "SHHH!"
    nar2 "He fixes his back closer to his torso, tossing half a wince towards Ambrosia."
    amb1 default "{i}AH- Mister Arison, right?{/i}"
    HV "{i}That's what I said, didn't I?{/i}"
    amb1 ugh "{i}Right...{/i}"
    HV "{i}I was going to thank you, you know, about the coffee.{/i}"
    HV "{i}It was instant, sure but... Not that bad for that variety.{/i}"
    amb1 default "{i}Oh?{/i}"
    HV "{i}I barely had time to you see, Annoying, right?{/i}"
    nar2 "The man parrallel to Ambrosia heaves a short sigh, hanging his head."
    amb1 cur "{i}I was wondering myself-- Mr. Arison, who exactly are you...?{/i}"
    nar2 "Harvey nearly chokes midair, covering his lips with his fist."
    HV "{i}You must be new here, aren't you?{/i}"
    amb1 ugh "{i}I said what I said...{/i}"
    HV "{i}Heir of the PRESTIGEOUS Arison name, Harvey.{/i}"
    HV "{i}Don't think about it too hard, it's no big deal anyway.{/i}"
    amb1 "{i}You sure?! Everyone kept oggling you back there--!{/i}"
    HV "{i}People tend to do that-- yes...{/i}"
    HV "{i}I'm something of a controversial figure...{/i}"
    HV "{i} Right now, just consider me another one of your patrons.{/i}"
    HV "{i} I'll be sure to give you half of your paycheck's worth in tips, alright?{/i}"
    amb1 "?????"
    amb1 "{i}That-- won't be necessary, really! I just do what I do for the fun of it!{/i}"
    HV "{i}...{/i}"
    HV "{i}You're-- an odd one...{/i}"
    HV "{i}I can see why Blaze got you on board...{/i}"
    jump daily 
label .silence:
    nar2 "All Ambrosia gave was a nod, passing by Harvey without another word."
    jump daily  
label tam_gym:
    
    scene gym
    with bites
    play music "audio/hajimetenookashidukuri.mp3" fadein 1.0 fadeout 1.0
    nar2 "The lot was decorated with machines, mats and tools at every end."
    nar2 "Almost like a toy store for those who left their childhoods behind, only much sweatier."
    nar2 "Stationed here were the determined faces of lives who for a second, cross with ours, but fleet as they pass."
    nar2 "Ambrosia soaks in the hard-working atmosphere, not short of another smile."
    if tam_helped == True:
        TM proud "Woah you actually came by--!"
    else:
        pass
    TM proud "Ambrosia--!! Nice to see ya 'round here!"
    TM default "Wanna come join me for some morning reps?"
    menu:
        "Sure thing, bro!":
            call .bros
        "No, I'm good!":
            call .im_good
    return
label .im_good:
    TM proud "Alright!! No pressure!!"
    TM "doin' it in public anyhow is nerve wreckin' enough and all that I hear! Hah-hoh!"
    jump daily  

label .bros:
    $ Total_affec["Madoc"] += 5
    TM "YEAHHH! That's what I'm talkin' about!"
    #TM "I've GOT to know your arm routine, dude..."
label .bros_cont:
    with bites
    nar2 "soaring past loops of clouds, races across the endless plane."
    extend "Not to mention the bows and arrows with their sweet targets."
    nar2 "Those were the instruments Ambrosia knew by heart."
    nar2 "Instead, the angel was confronted by metal disks hung at the ends of poles,"
    nar2 "tall machines where you tug strings, or the occasional band."
    nar2 "sheepishly, he tails behind Tamura, awaiting his next move."
    amb1 ugh "(...This should be easy, right?)"
    amb1 "(yes, easy!)"
    if tam_helped == True:
        amb1 "(Just don't break anything!! Heaven probably won't cover the insurance!!)"
    nar2 "Side by side, Ambrosia challenged the machine next to the hulking figure."
    nar2 "The angel observed the other alternating between each arm, the rich skin glistening beneath the light."
    nar2 "With all his might, he held back his strength-- a task that made him sweat as much as his companion."
    TM "WOAH? You're-- CRAZY strong--!"
    amb1 flush "I-- I am?"
    nar2 "With Tamura as his audience, Ambrosia mustered the most determined expression he could, gradually pacing his movements faster."
    nar2 "The room felt louder, between each stretch of movement."
    nar2 "between the deepening breath of his new... friend, the subtle sound of sweat rolling down his brow..."
    nar2 "A subtle skip of his heart between it's racing."
    nar2 "As Tamura switches his tools, Ambrosia felt a smirk rise across him."
    play music "audio/konekonoosanpo.mp3" fadein 1.0 fadeout 1.0
    jump daily 

label tam_park:
    with bites
    play music "audio/hajimetenookashidukuri.mp3" fadein 1.0 fadeout 1.0
    if gym_bros == True:
        TM proud "You're telling me you do your morning jog here, too?"
        TM "No wonder you're so... Massive, bro!"
        amb1 flush "Er-- that and genetics!"
        nar2 "A chuckle breaking through the two of them, the hours melt."
        nar2 "They race across the path, neck and neck-- even as Ambrosia had to tone it down multiple times."
        $ Total_affec["Madoc"] += 5
    
    else:
        TM "Woah, hey Ambrosia!"
        TM "Didn't expect to see you out here! I'm just on a jog, see?"
        TM "Catch ya later!"
    jump daily 

label gym_action:
    scene gym
    with bites
    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    call stats_action
    if gym_bros == True:
        $ Total_affec["Madoc"] += 1
    $ Gym.holy_switcher()

    return

label ice_cream_action:
    scene parlor
    with bites
    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    call stats_action
    $ Ice_cream.holy_switcher()
    return
        
label park_action:
    #social, fitness
    scene park
    with bites
    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    call stats_action
    $ Park.holy_switcher()
    return

label beach_action:
    scene beach
    with bites
    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    call stats_action
    $ Beach.holy_switcher()

    return

label mall_action:
    scene mall
    with bites
    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    call stats_action
    $ Mall.holy_switcher()

    return

label library_action:
    scene library
    with bites
    play sound "audio/MenuSFX/MP3/Abstract/abs-confirm-1.mp3"
    call stats_action
    $ Library.holy_switcher()
    
    return

## -- The grind

label sunday_break:
    $ energy -= 1
    scene cafe_morning
    show cafe_lobby_close
    with dissolve
    $ current_profit += (49 + reputation) /2
    $ money = current_profit * .05 * 100
    $ rounded_money = round(money,2)

    amb1 happy "it's sunday!"
    if (total_days == 7) and (lyra_warned == False):
        call lyra_warn
        call screen sunday_options
        
    else:    
        call screen sunday_options

    #if pray_event == True:
        #Total_affec["Lyra"] += 4
    call next_day
    call day_change
    call month_change



    



label day:
    $ chance = renpy.random.randint(1,5)
    scene cafe_lobby_close
    

    show screen day_display
    show screen opening_options
    
    with bites
    if total_days == 1:
        amb1 happy "(Okay! Step one of earning a human's love is acting like one!)"
        extend " (Probably!) (I'm pretty sure!)"
        amb1 default "(This should be easy!)"
    hide screen opening_options
    call screen opening_options
    
    call rand_events
    
    
    
    
    
    if day_of_week_number == 1:
        scene cafe_lobby_close
        show cafe_lobby_close:
            matrixcolor TintMatrix("#FFD2BD")*BrightnessMatrix(0.05)*ContrastMatrix(1.05)
        with dissolve
        amb1 default "what should I focus on this week?"
        hide screen action_screen
        $ Cheat_code.hide_stats_screen()
        call screen day_options
    #hide screen action_screen
    return

label opening_hours:
    
    scene cafe_lobby_close
    show cafe_lobby_close:
        matrixcolor TintMatrix("#FFD2BD")*BrightnessMatrix(0.05)*ContrastMatrix(1.05)
    
    $ Cheat_code.hide_stats_screen()
    call week_events
    
    return
    

    
    
label night:
    hide screen action_screen
    $ Cheat_code.hide_stats_screen()
    scene cafe night
    show cafe_lobby_close:
        matrixcolor TintMatrix("#d19ee8")*ContrastMatrix(1.45)*BrightnessMatrix(-0.25)
    with dissolve
    #call ft_events
    amb1 happy "moons out...!"
    call screen night_options
    return
    

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
