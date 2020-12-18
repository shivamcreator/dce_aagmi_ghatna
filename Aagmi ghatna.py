from bs4 import BeautifulSoup 
import requests
import webbrowser
import pyfiglet
import time
from random import randint
from yaspin import yaspin, Spinner
from printy import printy

URL = 'https://ggnindia.dronacharya.info/upcomingevents.aspx'
content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
contentDiv  = soup.find('div', { "class" : "panel-body newsbody3"})
notices=contentDiv.find_all('a')
list1=[]
for n in notices:
  list1.append(n.get_text())

project_href = [i['href'] for i in contentDiv.find_all('a', href=True)]

mapped={}

keys=[]
for i in range(1,len(list1)+1):
  keys.append(i)

for key in keys:
   for value in project_href:
     mapped[key]=value
     project_href.remove(value)
     break
x=1

banner=pyfiglet.figlet_format("DCE  AAGMI  GHATNA")

printy(banner,"r")
for i in list1:

  print(str(x)+":",i)
  x=x+1
print()
result = pyfiglet.figlet_format("Choose from above options", font = "digital" ) 
printy(result,"y")
while True:
 enter=int(input("Enter the option:"))

 if(enter in keys):
  
  with yaspin(text="Loading", color="yellow") as spinner:
   time.sleep(4) 
  webbrowser.open_new("https://ggnindia.dronacharya.info/" + mapped[enter])


 else:
 
  print("Please enter the correct option")
