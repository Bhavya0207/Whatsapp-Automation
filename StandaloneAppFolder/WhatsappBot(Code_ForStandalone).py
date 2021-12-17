from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))
#PATH="driver/chromedriver.exe"
#driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()


text= "Dear "
text2=", He is offline right now! He will reply to your texts when he gets on. This is an auto generated reply from his bot. Thanks!"

# Time provided to scan the QR code of Whatsapp Web
time.sleep(15)


namelist = ["Vind","Humare Ghar ki kahani","Chahat"]

while(1):
    for name in namelist:
        # Click on the search-bar 
        getsearchbox = driver.find_element(By.XPATH,"//*[@id='side']/div[1]/div/label/div/div[2]")
        getsearchbox.click()
        time.sleep(2)

        # Type the name of contact
        getsearchbox.send_keys(name)
        time.sleep(3)

        # Check if there is any unread message
        unreadMsgs=False

        getlist=driver.find_elements(By.XPATH,"//span[@class ='_23LrM']")
        if(len(getlist)):
            unreadMsgs=True

        
        # If there is no unread message, then click on back in the search bar
        if not unreadMsgs:
            cutit=driver.find_element(By.XPATH,"//*[@id='side']/div[1]/div/button")
            cutit.click()
        
        # If an unread message exists, reply to the contact
        else:
            # Click on the Chat
            user=driver.find_element(By.XPATH,'//span[@title = "{}"]'.format(name))
            user.click()

            # Type the message on the Chatbox
            textbox=driver.find_element(By.XPATH,'//div[@class="p3_M1"]')
            #textbox.send_keys(text)
            #textbox.send_keys(name)
            #textbox.send_keys(text2)
            textbox.send_keys(text+name+text2)
            time.sleep(3)

            # Send Message
            send=driver.find_element(By.XPATH,'//button[@class="_4sWnG"]')
            send.click()

            
            print(name,"texted you!")

            time.sleep(5)
    
    time.sleep(120)

driver.quit()
