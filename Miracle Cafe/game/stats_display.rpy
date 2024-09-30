style stats_display_text:
    size 35
    color ("#FFFFD8")

style stats_display_bar:
    left_bar Frame ("/gui/bar/left.png")
    right_bar Frame ("/gui/bar/right.png")
    xsize 120
    ysize 39

style stats_display_frame:
    background Frame("gui/text_boxes2.png")

style stats_display_button:
    background None
    hover_background "#914F1E"

style stats_display_button_text:
    size 35
    color ("#FFFFD8")



screen stats_display():
    style_prefix "stats_display"
    frame:
        xalign 0.58 yalign 0.96
        
        xsize 380 ysize 420
        vbox:
            yalign 0.09
            
            xpos 0.19
            text "work stats" size 58 font "fonts/bubbly_3/Bubbly-Regular.otf"
            xsize 490
        vpgrid:
            
            cols 3
            rows 7
            xpos 0.05 
            yalign 1.1
            spacing 4
            xfill True
            for item in Work_stats:
                text "[item]: "
                bar:
                    value AnimatedValue(Work_stats.get(item),200)
                text " [Work_stats.get(item)]"
            text "Money:"
            text "[money]$"
            
    frame:
        
        
        xalign 0.32 yalign 0.96
        xsize 380 ysize 420
        vbox:
            xpos 0.2
            yalign 0.09
            text "self stats" size 58 font "fonts/bubbly_3/Bubbly-Regular.otf"
        vpgrid:
            cols 3
            rows 7
            xpos 0.05
            yalign 1.05
            spacing 4
            xfill True
            for item in Self_stats:
                text "[item]: "
                bar:
                    value AnimatedValue(Self_stats.get(item),200)
                text " [Self_stats.get(item)]"


