style stats_action_bar:
    left_bar Frame ("/gui/bar/left.png")
    right_bar Frame ("/gui/bar/right.png")
    xsize 160

style stats_action_text:
    size 40
    color ("#FFFFD8")


style stats_action_frame:
    background Frame("gui/text_boxes2.png")
    xalign 0.8 yalign 0.33
    xsize 500 



screen pray_action():
    style_prefix "stats_action"
    frame:
        
        vbox:
            vpgrid:
                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True

                
                text "Holiness"
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)
                text "[Self_stats.get('Holiness')]"

                text "Reputatn."
                bar:
                    value AnimatedValue(Work_stats.get("Reputatn."),200)
                text "[Work_stats.get('Reputatn.')]"
                    
screen cook_action():
    style_prefix "stats_action"
    frame:
        vbox:
            vpgrid:
                
                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True                     
                text "Holiness:  " 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)

                text " [Self_stats.get('Holiness')]"
                text "Cuisine:"
                bar:
                    value AnimatedValue(Work_stats.get("Cuisine") ,200)
                text " [Work_stats.get('Cuisine')]"
                text "Charm:" 
                bar:
                    value AnimatedValue(Work_stats.get("Charm"),200)
                text " [Work_stats.get('Charm')]" 
                text "Smarts: " 
                bar:
                    value AnimatedValue(Self_stats.get("Smarts"),200)
                text " [Self_stats.get('Smarts')]" 

screen clean_action():
    style_prefix "stats_action"
    frame:
        
        vbox:
            vpgrid:
                
                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True                    
                text "Holiness: " 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)
                text " [Self_stats.get('Holiness')]"
                text "Style:" 
                bar:
                    value AnimatedValue(Self_stats.get("Stylish"),300)
                text " [Self_stats.get('Stylish')]" 
                text "Reputatn.: " 
                bar:
                    value AnimatedValue(Work_stats.get("Reputatn."),200)
                text " [Work_stats.get('Reputatn.')]"
                text "Clean:" 
                bar:
                    value AnimatedValue(Work_stats.get("Clean"),200)
                text " [Work_stats.get('Clean')]"  
            
screen serve_action():
    style_prefix "stats_action"
    frame:
        vbox:
            vpgrid:
                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True 
                text "Holiness: " 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)
                    # xysize (237,39)
                text " [Self_stats.get('Holiness')]"
                text "style:" 
                bar:
                    value AnimatedValue(Self_stats.get("Stylish"),300)
                text " [Self_stats.get('Stylish')]" 
                text "Reputatn.: " 
                bar:
                    value AnimatedValue(Work_stats.get("Reputatn."),200)
                text " [Work_stats.get('Reputatn.')]"
                text "clean:" 
                bar:
                    value AnimatedValue(Work_stats.get("Clean"),200)
                text " [Work_stats.get('Clean')]"  
                text "social:" 
                bar:
                    value AnimatedValue(Self_stats.get("Social"),200)   
                text " [Self_stats.get('Social')]"
    
                
screen read_action():
    style_prefix "stats_action"
    frame:
        
        vbox:
            vpgrid:
                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True
                text "Holiness: " 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)
                text " [Self_stats.get('Holiness')]"

                text "Social:" 
                bar:
                    value AnimatedValue(Self_stats.get("Social"),200)   
                text " [Self_stats.get('Social')]"
                text "Charm:" 
                bar:
                    value AnimatedValue(Work_stats.get("Charm"),200)
                text " [Work_stats.get('Charm')]"
                text "smarts: " 
                bar:
                    value AnimatedValue(Self_stats.get("Smarts"),200)
                text " [I]"
                    
screen mall_action():
    style_prefix "stats_action"
    frame:
        
        vbox:
            vpgrid:
                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True 
                text "Holiness: " 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)
                text " [Self_stats.get('Holiness')]"

                text "social:" 
                bar:
                    value AnimatedValue(Self_stats.get("Social"),200)   
                text " [Self_stats.get('Social')]"
                text "Reputn.:" 
                bar:
                    value AnimatedValue(Work_stats.get("Reputatn."),200) 

                text " [Work_stats.get('Reputatn.')]"
                text "smarts: " 
                bar:
                    value AnimatedValue(Self_stats.get("Smarts"),200)
                text " [Self_stats.get('Smarts')]"
                    
screen beach_action():
    style_prefix "stats_action"
    frame:
        
        vbox:
            vpgrid:

                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True    
                text "Holiness: " 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)
                text " [Self_stats.get('Holiness')]"
                text "Stylish:"
                bar:
                    value AnimatedValue(Self_stats.get("Stylish"),200)   
                text " [Self_stats.get('Stylish')]"

                text "Social:" 
                bar:
                    value AnimatedValue(Self_stats.get("Social"),200)   
                text " [Self_stats.get('Social')]"

                text "Fitness:" 
                bar:
                    value AnimatedValue(Self_stats.get("Fitness"),200)
                text " [Self_stats.get('Fitness')]"

screen ice_cream_action():
    style_prefix "stats_action"
    frame:
        
        vbox:
            vpgrid:
                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True 
                text "Holiness: " 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)
                text " [Self_stats.get('Holiness')]" 

                text "Charm:" 
                bar:
                    value AnimatedValue(Work_stats.get("Charm"),200)   
                text " [Work_stats.get('Charm')]"

                text "Clean:" 
                bar:
                    value AnimatedValue(Work_stats.get("Clean"),200)   
                text " [Work_stats.get('Clean')]"

                text "fitness:" 
                bar:
                    value AnimatedValue(Self_stats.get("Fitness"),200)
                text " [Self_stats.get('Fitness')]"
                text "Cuisine:"
                bar:
                    value AnimatedValue(Work_stats.get("Cuisine"),200)
                text " [Work_stats.get('Cuisine')]"

screen gym_action():
    style_prefix "stats_action"
    frame:
        vbox:
            vpgrid:
                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True    
                text "Holiness: " 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)
                text " [Self_stats.get('Holiness')]"

                text "Social:" 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)   
                text " [Self_stats.get('Holiness')]"
                    
                text "clean:" 
                bar:
                    value AnimatedValue(Work_stats.get("Clean"),200)
                text " [Work_stats.get('Clean')]"

                text "Smarts: " 
                bar:
                    value AnimatedValue(Self_stats.get("Smarts"),200)
                text " [Self_stats.get('Smarts')]"
                    
                text "Fitness:" 
                bar:
                    value AnimatedValue(Self_stats.get("Fitness"),200)
                text " [Self_stats.get('Fitness')]"

screen park_action():
    style_prefix "stats_action"
    frame:
        
        vbox:
            vpgrid:
                cols 3
                rows 7
                xpos 0.05
                ypos 0.12
                xfill True 
                text "Holiness: " 
                bar:
                    value AnimatedValue(Self_stats.get("Holiness"),200)
                text " [Self_stats.get('Holiness')]"

                text "Fitness:" 
                bar:
                    value AnimatedValue(Self_stats.get("Fitness"),200)
                text " [ Self_stats.get('Fitness')]"
                text "Social:" 
                bar:
                    value AnimatedValue(Self_stats.get("Social"),200)   
                text " [ Self_stats.get('Social')]"