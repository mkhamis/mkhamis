import json
import yaml
import requests
from bs4 import BeautifulSoup
from datetime import date

#Collect data from temp yaml file and reformat, collecting additional information by scraping from google scholar
#Note: google scholar stops accepting these requests after somewhere around 50 requests

with open('temp.json', 'r') as file:
    data = json.load(file)


#Collect list of dicts from existing yaml files
existing_data = []
unreviewed_data = []

try:
    with open('_data/publist.yml') as file:
        try:
            existing_data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(e)

    with open('_data/crawled_publist.yml') as file:
        try:
            unreviewed_data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(e)
except IOError as e:
    print(e)


#Use information to crawl those missing from the lists generated above, adding new entries to unreviewed_data list

#Loop over all collected SerpApi data
for d in data:
    
    #Check if the title is already accounted for in the two lists
    flag = False
    for existing in existing_data:
        if d['title'].lower().strip(" .'") == existing['title'].lower().strip(" .'"):
            flag = True
    if not flag:
        for unreviewed in unreviewed_data:
            if d['title'].lower().strip(" .'") == unreviewed['title'].lower().strip(" .'"):
                flag = True
    print(d['title'] + ": " + str(flag)) #Prints each item and if it was found before

    #If there was a hit, move on to next data point
    if flag:
        continue

    #Prepare for scraping from scholar
    scrape_url = d['link']

    req = requests.get(scrape_url)
    content = req.text

    soup = BeautifulSoup(content, features="html.parser")

    #Get title
    try:
        title = soup.find(id="gsc_oci_title").string
    except:
        #Scholar no longer accepting requests
        print("Scholar not accepting requests")
        break
    #print(title)
    
    #Initialise dict
    temp_dict = {'title': None, 'description': None, 'image': None, 'authors': None, 'link':{'url': None, 'display': None, 'DOI': None, 'video': None, 'talk':None, 'bibtex': None}, 'highlight': None, 'year': None, 'type': None, 'news2': None, 'award': None}
    
    #Get tabular scholar data
    for div in soup.body.findAll("div", class_="gs_scl"):
        field_name = div.find("div", class_="gsc_oci_field").string.lower() #Get scholar fieldname
        
        field_value = div.find("div", class_="gsc_oci_value").string #Get value of field
        field_links = div.find('a') #Collect any links
        
        #Check for publication info
        if field_name == "book":
            temp_dict['link']['display'] = str(field_value) #Can't trust scholar for book credit so don't change type
            continue
        elif field_name == "journal":
            temp_dict['link']['display'] = str(field_value)
            temp_dict['type'] = "journal"
            continue
        elif field_name == "conference":
            temp_dict['link']['display'] = str(field_value)
            temp_dict['type'] = "conference"
            continue
            
        if field_name == "pages":
            temp_dict['link']['display'] = temp_dict['link']['display'] + ", pages " + str(field_value)
            continue
        
        if field_name == "publication date":
            continue
        
        if field_value != None:
            temp_dict[str(field_name)] = str(field_value)
        if field_links != None:
            temp_dict['link']['url'] = "https://scholar.google.com" + str(field_links.get("href"))
    
    temp_dict['title'] = str(title).strip(" .'")
    temp_dict['highlight'] = 0 #default
    temp_dict['year'] = int(d['year'])
    
    unreviewed_data.append(temp_dict)

#Check if collected item in the list of dict in data
#Main issue here is the problem of title changes and such, which would result in multiple entries of the same item
#In these cases, the publist would have to be manuallly checked!

#Save to yaml file

def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')

yaml.add_representer(type(None), represent_none)

with open(r'_data/crawled_publist.yml', 'w') as file:
    outputs = yaml.dump(unreviewed_data, file)


#Finally, set a last-updated in file
with open('_data/last_updated.yml','w') as file:
    outputs = yaml.dump(date.today().strftime("%d/%m/%Y"), file)