import requests
from bs4 import BeautifulSoup
url=input("Enter website URL: ")
try:
    headers={"User-Agent":"Mozilla/5.0"}
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        soup=BeautifulSoup(response.text,"html.parser")
        headings=soup.find_all("h1")
        if headings:
            print("\nHeadings found:\n")
            for i,h in enumerate(headings,1):
                print(f"{i}. {h.text.strip()}")
        else:
            print("No headings found.")
    else:
        print("Failed to fetch website. Status code:",response.status_code)
except:
    print("Invalid URL or connection error.")