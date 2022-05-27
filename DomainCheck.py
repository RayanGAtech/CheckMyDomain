import whois
import csv
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

#function to check wether the domain is registered or not and return boolean value
def is_registered(domain_name):
    try:
        w = whois.whois(domain_name)
        return bool(w)
    except:
         return False

# show an "Open" dialog box and return the path to the selected file
Tk().withdraw() 
filename = askopenfilename() 
upload_file = str(filename)

#new list to append the checked domains
l = []

# open and read the uploaded files
with open(upload_file, 'r') as file:
    data = file.read().split('\n')

# iterate over the uploaded domains
    for domain in data:
        if is_registered(domain):
            l.append(domain + " is registered\n") 
        else: 
            l.append(domain + " is not registered\n")

# create a new csv file to save the result
f = open('ready/ready.csv', 'w', newline='\n')
writer= csv.writer(f,delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE)
writer.writerow(l)
f.close()

print('Done! Please check *ready folder*')