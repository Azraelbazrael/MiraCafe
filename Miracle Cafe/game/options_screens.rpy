
#transform show_hide_dissolve:
    #on show:
        #ImageDissolve("transitions/Pack 01/011.webp", 1.5)
    #on hide:
        #ImageDissolve("transitions/Pack 01/011.webp", 1.5)
style visit_button_text:
    font "fonts/pink_chicken/PinkChicken-Regular.ttf"
    color "#FFFFD8"
    #hover_color ("#FFDADA")
    #insensitive_color "#FFFFD8"
    xsize 35

style visit_button:
    background None
    hover_background "#914F1E"
    xsize 180
style visit_frame:
    background Frame("gui/map_box.png")

style actions_frame:
    xsize 597
    ysize 708
    xalign 0.89 yalign 0.52
    background Image("gui/text_boxes.png")

style actions_vbox:
    xalign 0.2
    yalign 0.35
    spacing 2

style actions_button:
    background "gui/button/options_bg.png" 
    hover_background "gui/button/options_bg_hover.png"
    yminimum 75
    xminimum 300
    
style actions_button_text:
    font "fonts/pink_chicken/PinkChicken-Regular.ttf"
    color "#BD3144"
    #selected_color "#FFDADA"
    hover_color ("#FFDADA")
    size 40
    xalign 0.35


style upstairs_button_text:
    font "fonts/pink_chicken/PinkChicken-Regular.ttf"
    color "#BD3144"
    #selected_color "#FFDADA"
    hover_color ("#FFDADA")
    size 40
    xalign 0.38

style topics_frame:
    xsize 597
    ysize 708
    xalign 0.89 yalign 0.52
    background Image("gui/text_boxes.png")

style topics_vbox:
    xalign 0.2
    yalign 0.35
    spacing 2
    
style topics_button:
    background "gui/button/topics_bg_idle.png" 
    hover_background "gui/button/topics_bg_hover.png"
    yminimum 72
    xminimum 405
    
style topics_button_text:
    font "fonts/pink_chicken/PinkChicken-Regular.ttf"
    color "#BD3144"
    #selected_color "#FFDADA"
    hover_color ("#FFDADA")
    size 40
    xalign 0.27
    


    

screen action_screen():
    
    
    frame:
        #background 
        xsize 800 ysize 500
        xalign 0.25 yalign 0.43
 

screen day_options():
    style_prefix "actions"
    
        #ImageDissolve("transitions/Pack 01/011.webp", 1.5)
    frame:
        #at show_hide_dissolve 
        vbox:

            textbutton "cook":
                tooltip "( -holiness, +smarts , +cuisine, -cleanliness )"
                action [SetVariable("cook_event", True), Return()] 
            textbutton "clean":
                tooltip "( -holiness, +cleanliness, +reputation, +style )" 
                action [SetVariable("clean_event", True), Return()] 
            textbutton "serve":
                tooltip "( -holiness, +cleanliness, +reputation, +social, +charm )"
                action [SetVariable("serve_event", True), Return()] 
            textbutton "pray":
                tooltip "( +holiness, -reputation )"
                action [SetVariable("pray_event", True), Return()] 
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
            
        
screen night_options():
    style_prefix "actions"
    frame:
        vbox:
  
            textbutton "rest": 
                action [Call("rest_action"), Return()] 
                tooltip "No stat changes. Just let Ambrosia sleep!"
            textbutton "pray":
                action [Call("pray_action"), Return()]
                tooltip "( +holiness, -reputation )" 
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

screen sunday_options():
    style_prefix "actions"
    frame:
        vbox:
            textbutton "shop":
                action ToggleScreen("store") activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Shop.mp3" 
                tooltip "Buy an item for boosting stats or getting gifts for a certain someone ;)"
            textbutton "pray":
                action [Call("pray_action"), Return()]
                tooltip "( +holiness, -reputation )"
            textbutton "upstairs":
                action ToggleScreen("target_options") activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Shop.mp3" text_style "upstairs_button_text"
                tooltip "Visit someone? seems appropriate since everyone's home."
            textbutton "map":
                action ToggleScreen("map_screen") activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Shop.mp3"
                tooltip "travel, get stats... Run into a familiar face?" 
            textbutton "rest":
                action [Call("rest_action"), Return()]
                tooltip "No stat changes. Just let Ambrosia sleep!"

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
            
            

screen target_options():
    style_prefix "map"
    frame:
        #background Frame("gui/text_boxes2.png")
        xalign 0.52 yalign 0.44
        xsize 360 ysize 437
        frame:
            #background Frame("gui/text_boxes2.png")
            ysize 60
            xsize 230
            xalign 0.5
            yalign 0.09
            hbox:
                xalign 0.5
                text "MENU" size 50
                box_wrap True
                add Image("images/mug-saucer-solid.png") xsize 50 ysize 45
                
        vbox:
            yalign 0.4
            xalign 0.6
            box_wrap True
            textbutton "{u}Madoc{/u}" action [ToggleScreen("target_options"), SetVariable("current_host", "mad_room"), Call("mad_door")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
            textbutton "{u}Charon{/u}" action [ToggleScreen("target_options"), SetVariable("current_host", "char_room"), Call("char_door")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
            textbutton "{u}Tamura{/u}" action [ToggleScreen("target_options"), SetVariable("current_host", "tam_room"), Call("tam_door")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
            #textbutton "Rest" action [ToggleScreen("target_options"), Call("rest_door")] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
            
            
screen topic_options():
    style_prefix "topics"
    frame:
        vbox:
            for item in (Topics):
                textbutton "[item]":
                    action [SetVariable("current_topic", Topics.get(item)), Return()] activate_sound "audio/MenuSFX/SoupTonic UI1 SFX Pack 1 - mp3/SFX_UI_Pause.mp3"
   
        


screen game_over():

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        #background Image("gui/quit_frame.png")
        vbox:
            xalign .5
            yalign .5
            spacing 45

            text "Mission Failed!"  xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Quit") action Quit()
                textbutton _("Retry?") action ShowMenu("load")

    ## Right-click and escape answer "no".
    #key "game_menu" action no_action