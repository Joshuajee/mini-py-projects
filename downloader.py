import requests 


url =  "https://www.appclick.ng/assets/img/hero/appclick-academy-courses-top-notch-IT-consulting-company-in-ibadan-lagos-nigeria.jpg"

r = requests.get(url)

print(r.status_code)
 
if r.status_code == 200:
    f = open("my-pic.jpg", "xb")
    f.write(r.content)
    f.close()