import re, datetime, calendar

year = ['January',  'February',  'March',  'April',  'May',  'June',  'July',  'August',  'September',  'October',  'November',  'December']

def main():
    print("hello")
    today = datetime.datetime.date(datetime.datetime.now())
    print(today)
    current = re.split('-', str(today))
    current_no = int(current[1])
    current_month = year[current_no-1]
    current_day = int(re.sub('\A0', '', current[2]))
    current_yr = int(current[0])
    print(current_no)
    print(current_day)
    print(current_month)    
    print(current_yr)
    print '<h1> %s %s </h1 >' %(current_month, current_yr)
    print ''' 
    <table id="month" > 
    <thead > 
    <tr > 
    <th class="weekend" >Sunday&lt;/th > 
    <th >Monday&lt;/th > 
    <th >Tuesday&lt;/th > 
    <th >Wednesday&lt;/th > 
     
    <th >Thursday&lt;/th > 
    <th >Friday&lt;/th > 
    <th class="weekend" >Saturday&lt;/th > 
    </tr > 
    </thead > 
    <tbody > 
     ''' 
    print ''' 
    <table id="month" > 
    <thead > 
    <tr > 
    <th >Monday</th > 
    <th >Tuesday</th > 
    <th >Wednesday</th > 
    <th >Thursday</th > 
    <th >Friday</th > 
    <th class="weekend" >Saturday</th > 
    <th class="weekend" >Sunday</th > 
    </tr > 
    </thead > 
    <tbody > 
     '''
    month = calendar.monthcalendar(current_yr, current_no)
    nweeks = len(month)
    for w in range(0,nweeks): 
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
                print '<td class="%s"><strong>%s</strong></span><div class="%s"></div></td>' %(classtype, day, classtype) 
            else: 
                print '<td class="%s">%s</span><div class="%s"></div></td>' %(classtype, day, classtype) 
            print "</tr>" 
 
            print ''' </tbody> 
            </table> 
            </div> 
            </body> 
            </html>''' 
    print "</tbody></table></body></html>"



if __name__ == "__main__":  main()
