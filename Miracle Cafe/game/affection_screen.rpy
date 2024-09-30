screen affection():
    style_prefix "stats_display"
    frame:
        xsize 390 
        ymaximum 402
        xalign 0.145 yalign 0.36
        #background Frame("gui/map_box.png")
        vbox:
            
            text "Affection" size 50 
            xalign 0.5 
            yalign 0.09
        vpgrid:
            
            cols 3
            rows 7
            xpos 0.09 
            yalign 3.25
            spacing 10
            xfill True
            ### have the text be textbuttons that show little blurbs + hints
            for item in Total_affec:    
                text "[item]"
                bar: 
                    value AnimatedValue(Total_affec.get(item),200)
                text "[Total_affec.get(item)]"