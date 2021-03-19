# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://httpbin.org/json"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
  
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
author = data['slideshow']['author']
date = data['slideshow']['date']

# printing the output 
print("Author:%s\nDate:%s"
      %(author, date))
