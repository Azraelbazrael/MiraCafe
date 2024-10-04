
style month_display:
    size 70
    font "fonts/cakecafe/Cakecafe.otf"
    color ("#FFDADA")

    

style day_display_text:
    font "fonts/bubbly_3/Bubbly-Regular.otf"
    size 70    

#screen item_list_test():
    #window:
        #for key, value in sorted( a.items() ):
            #text "[key] = [value]"

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

    #frame:
        #yalign 0.3 xalign 0.2
        #hbox:
            #text "max: [highest_affec]"
