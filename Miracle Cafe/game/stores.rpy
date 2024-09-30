style map_button_text:
    font "fonts/pink_chicken/PinkChicken-Regular.ttf"
    color "#FFFFD8"
    xsize 300
    
    #xalign 0.13

style map_button:
    background None
    hover_background "#914F1E"
    xsize 300
    ysize 50

style map_text:
    color "#FFFFD8"
    font "fonts/bubbly_3/Bubbly-Regular.otf"

style map_frame:
    background Frame("gui/map_box.png")
    xsize 360 ysize 437

screen store():
    style_prefix "map"
    frame:
        xalign 0.52 yalign 0.5
        
        vbox:
            box_wrap True
            xalign 0.5
            yalign 0.09
            text "Tonight's" size 50
            text "{u}Special{/u}" size 50 xalign 0.5
        frame:
            ypos 0.3
            xpos 0.05
            background None
            vpgrid:
                xfill True
                cols 2
                rows 4
                #spacing 60
                yspacing 30
                xspacing 130
                # Change this to a dict thing, like the topics. Tool tip can be the second value.. I'll have to figure out how to store a third value for prices
                textbutton "Holy Water":
                    if rounded_money >= 50:
                        action Function(holy_water)
                    else: 
                        action NullAction()
                    tooltip "(+ 30 holiness)"
                    activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
                    
                text "50"
                textbutton "Special Sign":
                    if sign_up == False and rounded_money >= 100:
                        action Function(special_sign) 
                    else: 
                        action NullAction()
                    
                    tooltip "(+ Reputation, gives a faster reputation boost. One time purchase)" 
                    activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
                text "100"


screen map_screen():
    style_prefix "map"
    frame:
        #background Frame("gui/map_box.png")
        xalign 0.52 yalign 0.54
        #xsize 360 ysize 437
        vbox:
            xalign 0.5
            yalign 0.09
            text "Today's Map" size 50

        vbox:
            xalign 0.5
            yalign 0.8
            textbutton "- Library" action [ToggleScreen ("map_screen"), SetVariable("lib_event", True),Call("map_actions")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
            textbutton "- Mall" action [ToggleScreen ("map_screen"), SetVariable("mall_event", True),Call("map_actions")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
            if total_days <= 61:
                textbutton "- Gym" action [ToggleScreen ("map_screen"), SetVariable("gym_event", True),Call("map_actions")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
                textbutton "- Park" action [ToggleScreen ("map_screen"), SetVariable("park_event", True), Call("map_actions")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
                textbutton "- Beach" action [ToggleScreen("map_screen"), SetVariable("beach_event", True), Call("map_actions")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
                textbutton "- Ice Cream Stand" action [ToggleScreen ("map_screen"), SetVariable("ice_cream_event", True), Call("map_actions")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
            elif total_days <= 122:
                textbutton "- Park" action [ToggleScreen ("map_screen"), SetVariable("park_event", True), Call("map_actions")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
                textbutton "- Fishing Dock" activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
            else:
                textbutton "- Skiing hills" activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
                textbutton "- Skating rink" activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
    
                


