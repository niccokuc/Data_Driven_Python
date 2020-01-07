'''
Created on 7 Jan. 2020

@author: NerminKuc
'''
'''
Created on 7 Jan. 2020

@author: NerminKuc
'''
import requests
import json
import csv

#The DarkSky API key
API_Key_DarkSky = "70aa22b49abb3f52ebfe2aa2438265ee"

with open('Latitude_Longitude.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        
        #Skip the first Row and Make it a Column Heading
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
      
            
        # Enter the Longitude and Latitude value
        lat = str(row["Latitude"])
        long = str(row["Longitude"])
        
        print("Your Latitude request is : " + lat)
        print("Your Longatude request is : " + long)
        
        API_URL = 'https://api.darksky.net/forecast/'+API_Key_DarkSky+'/' + str(lat) + ',' + str(long)
        print("The API URL string used is : " + API_URL)
        
        # Make the GET request from the API
        r = requests.get('https://api.darksky.net/forecast/'+API_Key_DarkSky+'/' + str(lat) + ',' + str(long))
        status_API = int(r.status_code)
        print(r.content)

        # Verify the GET API is working
        if status_API == 200:
            print("[+] The API call is good to go! ")
            j = json.loads(r.text)
        else:
            print("[-] The API call is BAD! " )
            exit
        # What is the current weather at that location?
        print("[+] The weather is : " + j['currently']['summary'])

        line_count += 1


