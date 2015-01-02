import re, datetime, calendar

year = ['January',  'February',  'March',  'April',  'May',  'June',  'July',  'August',  'September',  'October',  'November',  'December']

def main():
    today = datetime.datetime.date(datetime.datetime.now())
    current = re.split('-', str(today))
    current_no = int(current[1])
    current_month = year[current_no-1]
    current_day = int(re.sub('\A0', '', current[2]))
    current_yr = int(current[0])
    print '<html>'
    print '<body>'
    print '<h1> %s %s </h1>' %(current_month, current_yr)
    print ''' 
<table id="month" > 
<thead > 
<tr > 
<th >Monday</th> 
<th >Tuesday</th> 
<th >Wednesday</th> 
<th >Thursday</th> 
<th >Friday</th> 
<th class="weekend">Saturday</th > 
<th class="weekend">Sunday</th > 
</tr> 
</thead> 
<tbody > '''
    month = calendar.monthcalendar(current_yr, current_no)
    weeksInMonth = len(month)
    for w in range(0,weeksInMonth): 
        week = month[w] 
        print "<tr>" 
        for x in xrange(0,7): 
            day = week[x]
            if x == 5 or x == 6: 
                classtype = 'weekend' 
            else:
                classtype = 'day' 
 
            if day == 0: 
                classtype = 'previous' 
                print '<td class="%s"></td>' %(classtype) 
            elif day == current_day: 
                print '<td class="%s"><strong><div class="%s">%s</strong></div></td>' %(classtype, classtype,day) 
            else: 
                print '<td class="%s"><div class="%s">%s</div></td>' %(classtype, classtype,day)
        print "</tr>" 
 
    print '''</tbody> 
</table> 
</div> 
</body> 
</html>''' 


if __name__ == "__main__":  main()
