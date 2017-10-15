def alarm_clock(day, vacation):
   week = 1 <= day <= 5
   #alarm clock for weekdays and weekends
   return ( '7:00' if week and not vacation else
            '10:00' if week ==      vacation else
            'off')
