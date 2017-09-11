import os,sys
print "*****************Meeting SCRIPT*******************"
choice=""
name=""
try:
    name=sys.argv[1]
except: 
     print "\n1.Swati\n2.Scrum\n3.Renu"
     choice=int(input("Enter your meeting number"))
if choice==1 or name=="swati":
    os.system("google-chrome https://bluejeans.com/9127073372")
elif choice==2 or name=="scrum":
    os.system("google-chrome https://bluejeans.com/9127073372")
