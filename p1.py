#!/usr/bin/env python
import time
import webbrowser
option='''Press 1:Search words in different tabs 
Press 2:Search images
Press 3:URL Names
Press 4:Current date and time
Press 5:Open Default Web browser
Press 6:All network IP
Press 7:Enter Domain and get owner ,contct no,email

'''
print option

ch=raw_input()

if ch=='1':
	x=raw_input("Enter    ")
	stripped_x=x.strip()
	final_x=stripped_x.split()
	for i in final_x:
		webbrowser.open_new_tab("https://www.google.com/search?q="+i)
	


elif ch=='2':
	x=raw_input("Enter    ")
	stripped_x=x.strip()
	final_x=stripped_x.split()
	for i in final_x:
		webbrowser.open_new_tab("https://www.google.co.in/search?q="+i+"&tbm=isch")





elif ch=='4':
	print time.ctime()

elif ch=='5':
	webbrowser.open("https://www.google.com",1)
else:
	print "wrong input"	

