#import necessary libraries
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, os
import urllib.request
from io import BytesIO
from PIL import Image
import hashlib
import re
import pytz
from datetime import datetime

logPATH = os.path.join(os.path.dirname(__file__),'log.txt') 



def openbrowser():

    def loginTwitter():
        def get_xpath_from_html(html: str, text: str) -> str:
            from lxml import etree
            parser = etree.HTMLParser()
            tree = etree.fromstring(html, parser)
            xpath = f"//*[contains(text(), '{text}')]"
            result = tree.xpath(xpath)
            if result:
                return tree.getroottree().getpath(result[0])
            else:
                return "Text not found in HTML"

        # Navigate to the Twitter login page
        driver.get('https://twitter.com/i/flow/login')

        elements = driver.find_elements(By.XPATH,'//*')
        html = ''
        for element in elements:
                try:
                    inputs = driver.find_elements(By.TAG_NAME,"input")
                    list1= []
                    for input in inputs:
                        list1.append(input.get_attribute("outerHTML"))
                    if element.text != '':
                        if "Telefon, e-mail nebo uživatelské jméno" in element.text:
                            html = element.get_attribute("outerHTML")
                            xpath = get_xpath_from_html(element.get_attribute("outerHTML"), "Telefon, e-mail nebo uživatelské jméno")
                            print(xpath)
                            wanted = element.find_element(By.XPATH, xpath)
                            '''for elementchild in list:
                                #html = elementchild.get_attribute("outerHTML")
                                #element = driver.find_element(By.XPATH, xpath)'''
                            #wanted.send_keys("AHOJ")
                            wanted.send_keys(Keys.CONTROL, 'v')
                            print("end")

                            #print(element.tag_name, element.text)
                            break
                except Exception as e:
                    print(e)
        
        # Find the email and password fields and enter your login information
        email_field = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
        email_field.send_keys(Credentials["email"])

        password_field = driver.find_element_by_xpath('//input[@name="session[password]"]')
        password_field.send_keys('your_password')
        # Submit the login form
        password_field.send_keys(Keys.RETURN)
    def loginTwitter2():
        # Navigate to the Twitter login page
        driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        body = driver.find_element(By.TAG_NAME,"body")
        body.send_keys(Keys.TAB)
        
        body.send_keys(Keys.TAB)
        body.send_keys(Keys.TAB)
        #body.send_keys(Keys.CONTROL, 'v')
        body.send_keys(Keys.ENTER)

    def loginTwitter3():
        import keyboard
        driver.get('https://twitter.com/i/flow/login')
        keyboard.wait('enter')
        '''time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys('username')
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys('passwd')
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
        time.sleep(5)'''
    #instantiate the Chrome class web driver and pass the Chrome Driver Manager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--enable-javascript")

    #Maximize the Chrome window to full-screen
    driver.maximize_window() 

    loginTwitter3()

    return driver
Credentials = {
    "email":"janprokop@engineer.com",
    "password":"bnk7ez0fwMkC4kKYa4bz"
}

MyAccounts = [
    "https://twitter.com/CT24zive",
    "https://twitter.com/strakovka",
    "https://twitter.com/HradOfficial"
]

MyXPATHS = {
    "login_email": "",
    "login_password": "",

    "header": "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div",
    "profil_photo": "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div/a/div[3]/div/div[2]/div/img",
    "number_of_tweets":"/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div",
    "main_photo":"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/a/div/div[2]/div/img",
    "name":"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/span",
    "description":"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/span",
    "labels":"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]",
    "following":"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span",
    "followers":"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span",
    
    "tweets"        :"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div",             
    "tweet"         :"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[",
    "tweet_text"    :"]/div/div/article/div/div/div[2]/div[2]/div[2]/div/span",
    "tweet_text2"   :"div > div > article > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > span",
    "tweet_author"  :"]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/a/div/span",
    "tweet_time"    :"]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[3]/a/time",
    "tweet_link"    :"]/div/div/article/div/div/div[2]/div[2]/div[3]",
    "tweet_like_short":"]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div[3]/div/div/div[2]/span/span/span",
    "tweet_like"    :"]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[3]/div/div/div[2]/span/span/span",
    "tweet_reach"   :"]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[4]/a/div/div[2]/span/span/span",
    "tweet_video"   :"]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/video"
    }

#promc=driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div')

class readAccount:
    def __init__(self):
        pass
    '''def retry(func):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}")
                    time.sleep(1)
        return wrapper'''
    def retry(max_retries=2, wait_time=1):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for i in range(max_retries):
                    try:
                        result = func(*args, **kwargs)
                        return result
                    except Exception as e:
                        print(f"Error: {e}")
                        time.sleep(wait_time)
                raise Exception("Max retries exceeded.")
            return wrapper
        return decorator
    
    @retry()
    def findElement(path):
        return driver.find_element(By.XPATH, path)
    
    def read_header():
        header = {}
        header["name"] = readAccount.findElement(MyXPATHS['name']).text
        #header["header"] = driver.find_element(By.XPATH, MyXPATHS['header']).text      
        header["description"] = driver.find_element(By.XPATH, MyXPATHS['description']).text
        header["followers"] = driver.find_element(By.XPATH, MyXPATHS['followers']).text
        header["following"] = driver.find_element(By.XPATH, MyXPATHS['following']).text
        """header["labels"]=[]
        for item in driver.find_elements(By.XPATH, MyXPATHS['labels']):
            header["labels"].append(item.text) """
        header["labels"] = driver.find_element(By.XPATH, MyXPATHS['labels']).text
        header["number_of_tweets"] = driver.find_element(By.XPATH, MyXPATHS['number_of_tweets']).text
        header["profil_photo"] = Image.open(BytesIO(urllib.request.urlopen(readAccount.findElement(MyXPATHS['profil_photo']).get_attribute('src')).read()))
        header["main_photo"] = Image.open(BytesIO(urllib.request.urlopen(readAccount.findElement(MyXPATHS['main_photo']).get_attribute('src')).read()))
        header["profil_photo"].save(f"{header['name']}_profilphoto.jpg")
        header["main_photo"].save(f"{header['name']}_mainphoto.jpg")

        return header

    def printToLog(log):
        global logPATH
        with open(logPATH, "a") as f:
            f.write(f"{str(log)}\n")

    def scroll_to_bottom(driver):
        def readTweet(i):
            tweet = {}
            text = readAccount.findElement(MyXPATHS["tweet"] + str(i) + MyXPATHS["tweet_text"]).text
            tweet["id"] = hashlib.sha256(text.encode()).hexdigest()
            tweet["text"]=text
            tweet["time"]=readAccount.findElement(MyXPATHS["tweet"] + str(i) + MyXPATHS["tweet_time"]).text
            tweet["author"]=readAccount.findElement(MyXPATHS["tweet"] + str(i) + MyXPATHS["tweet_author"]).text
            tweet["link"]=readAccount.findElement(MyXPATHS["tweet"] + str(i) + MyXPATHS["tweet_link"]).text
            tweet["like"]=readAccount.findElement(MyXPATHS["tweet"] + str(i) + MyXPATHS["tweet_like"]).text
            tweet["reach"]=readAccount.findElement(MyXPATHS["tweet"] + str(i) + MyXPATHS["tweet_reach"]).text

        def readTweet2(html):
            #el = readAccount.findElement(MyXPATHS["tweet"] + str(i) + "]")
            #html = el.get_attribute('innerHTML')     
            #soup = BeautifulSoup(html, 'html.parser')
            soup=html
            tweet={}
            
            for link in soup.find_all('time'): 
                utc_time = link.get('datetime')
                utc_dt = datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%S.%fZ')
                cet_tz = pytz.timezone('Europe/Prague')
                cet_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(cet_tz)
                tweet["time"] = cet_dt.strftime('%Y-%m-%d %H:%M:%S')

            for link in soup.find_all('a'): 
                href = link.get('href')
                if re.search(r'\b{}\b'.format('analytics'), href):
                    tweet["views"] = int(link.get('aria-label').split()[0])

            for link in soup.find_all('div'):
                label=link.get('aria-label')
                labels=[] 
                if label is not None: labels.append(label)

                for label in labels:
                    if re.search(r'\b{}\b'.format('Lajk'), label): 
                        tweet["likes"] = int(label.split()[0])
                        continue

                    if re.search(r'\b{}\b'.format('Retweet'), label): 
                        tweet["retweets"] = int(label.split()[0])
                        continue

                    if re.search(r'\b{}\b'.format('Odpověď'), label): 
                        tweet["comments"] = int(label.split()[0])
                        continue
            
            texts = []
            for link in soup.find_all('span'): 
                try:
                    texts.append(link.get_text())
                except Exception as e:
                    readAccount.printToLog(tweet["time"]+e)
                    print(e)
            #tweet["text"] = list(dict.fromkeys(texts)) #odebira duplikaty 
            try:
                tweet["text"] = soup.select_one(MyXPATHS["tweet_text2"]).text
            except Exception as e:
                readAccount.printToLog(tweet["time"]+e)
                print(e)
                tweet["text"] = "ERROR"


            tweet["photos"] = []
            for i, link in enumerate(soup.find_all('img')): 
                src = link.get('src')
                if src[-3:]=='svg':
                    continue
                    from svglib.svglib import svg2rlg
                    from reportlab.graphics import renderPDF, renderPM
                    image_data = BytesIO(urllib.request.urlopen(src).read())
                    drawing = svg2rlg(image_data)
                    buffer = BytesIO()
                    renderPM.drawToFile(drawing, buffer, fmt="jpg")
                    tweet["photos"].append(buffer.getbuffer())
                    with open(os.path.join(f"{os.path.dirname(__file__)}/tweetdata", f"{filename}_tweetphoto_{str(i)}.jpg"), "wb") as f:
                        f.write(buffer.getbuffer())
                elif src[-3:]=='jpg':
                    tweet["photos"].append(Image.open(BytesIO(urllib.request.urlopen(src).read())))
                    filename = re.sub(r'[^\w\s]', '', tweet['time']).replace(' ', '_')
                    tweet["photos"][-1].save(os.path.join(f"{os.path.dirname(__file__)}/tweetdata", f"{filename}_tweetphoto_{str(i)}.jpg"))
                else:
                    pass
            tweet["videos"] = []
            for link in soup.find_all('video'): 
                tweet["videos"].append(link.get('src'))

            #video nefunguje
            '''video = driver.find_element(By.XPATH, MyXPATHS["tweet"] + str(i) + MyXPATHS["tweet_video"])
            src = video.get_attribute("src")
            urllib.request.urlretrieve(src, "video.mp4")'''

            tweet["html"] = html

            return tweet  
        def readAllTweets():
            el = readAccount.findElement(MyXPATHS["tweets"])
            html = el.get_attribute('innerHTML')
            soup = BeautifulSoup(html, "html.parser")
            divs = soup.find_all("div", recursive=False)
            return divs

        # Function for scrolling to the bottom of Google
        '''last_height = driver.execute_script('\
        return document.body.scrollHeight')'''

        tweets=[[]]
        repetition = 0
        while True and len(tweets)<50: #opakuje do te doby nez nacte dany pocet tweetu
            repetition += 1
            try:
                for x,oneTweet in enumerate(readAllTweets()):
                    tweet = readTweet2(oneTweet)
                    if tweet["time"] in tweets[0]: pass
                    else: 
                        tweets.append(tweet)
                        tweets[0].append(tweet["time"])
            except Exception as e:
                readAccount.printToLog(e)
                print(e)
                pass

            scrollHeight= 1000
            driver.execute_script('\
            window.scrollTo(0,' + str(scrollHeight*repetition)+ ')')
            new_height = driver.execute_script('\
            return document.body.scrollHeight')

            '''driver.execute_script('\
            window.scrollTo(0,document.body.scrollHeight)')
            new_height = driver.execute_script('\
            return document.body.scrollHeight')'''

            # checking if we have reached the bottom of the page
            '''if new_height == last_height:
                break'''
            if x==0: break

            last_height = new_height

        return tweets, driver
       
def readlist(MyAccounts, driver):
    data=[]
    for link in MyAccounts:
        #go to Twitter's Homepage
        driver.get(link)
        dicti={}
        dicti["header"]=readAccount.read_header()
        dicti["tweets"], driver = readAccount.scroll_to_bottom(driver=driver)
        data.append(dicti)
    return data

driver = openbrowser()
data = readlist(MyAccounts, driver)

print("end")

'''#tweet (prvni)
promc=driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]')
for c in promc:
    dicti.append(c.text)'''


#promc=driver.find_elements(By.TAG_NAME, 'div')
#promc = driver.find_elements(By.CSS_SELECTOR, 'div.css-1dbjc4n')

'''print(driver.page_source)
soup = BeautifulSoup(driver.page_source)

prom=[]
prom.append(soup.name)
prom.append(soup.html.body.div.text)'''


'''f = open("demofile2.png", "wb")
f.write(driver.get_screenshot_as_png())
f.close()
'''

'''for y in range(10):
    driver.execute_script('\
        window.scrollTo(0,'+str(y*1000)+')')'''

'''def searchInSearchBar(driver):
    query="czarmy"
    # Finding the search box
    box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
 
    # Type the search query in the search box
    box.send_keys(query)

    # Pressing enter
    box.send_keys(Keys.ENTER)'''
