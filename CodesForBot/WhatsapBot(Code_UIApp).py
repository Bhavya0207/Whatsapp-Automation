from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from tkinter import *
from tkinter import ttk
import threading

ui = Tk()
ui.geometry("450x300")
ui.title("Whatsapp-Bot")
ui.configure(background='#172836')
ui.configure(borderwidth="1")
ui.configure(relief="sunken")
ui.configure(highlightbackground="white")
ui.configure(highlightcolor="white")
def resource_pathi(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_pathi("driver/whatsapp-bots.png")
p1 = PhotoImage(file = Logo)
ui.iconphoto(False, p1)
isclicked=False


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def whopen():
    global driver
    driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()

# Time provided to scan the QR code of Whatsapp Web
    time.sleep(15)
    #namelist = ["Vind","Humare Ghar ki kahani","Chahat"]
    namestr=name_input_area.get()
    namelist = list(namestr.split(","))

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
                msg=text_input_area.get()
                textbox.send_keys(msg)
                time.sleep(3)

            # Send Message
                send=driver.find_element(By.XPATH,'//button[@class="_4sWnG"]')
                send.click()

            
                print(name,"texted you!")

                time.sleep(5)
    
        time.sleep(120)

def exit():
    driver.quit()

style = ttk.Style()
style.configure('TEntry', foreground = '#42998c')

heading=Label(ui,text="WHATSAPP-BOT",font='Garamond 30 bold',background='#172836',fg="#42998c")
heading.pack()

text = Label(ui,text = "Text",font='Palatino 12 bold',background='#172836',fg="white")
text.place(x = 105,y = 43)
	
name = Label(ui,text = "NameList",font='Palatino 12 bold',background='#172836',fg="white")
name.place(x = 108,y = 105)
	
submit_button = Button(ui,text = "Start program",font='Palatino 12 bold',background='#135462',cursor="hand2",fg="white",command=threading.Thread(target=whopen).start)
submit_button.place(x = 110,y = 168)

exit_button = Button(ui,text = "End Program",font='Palatino 12 bold',cursor="hand2",fg="white",background='#135462',command=exit)
exit_button.place(x = 110,y = 208)
	
text_input_area = ttk.Entry(ui,font = ('courier', 15, 'bold'),width = 15,foreground='#42998c')
text_input_area.place(x = 110,y = 68)   
text_input_area.focus_force()                                        
	
name_input_area = ttk.Entry(ui,font = ('courier', 15, 'bold'),width = 15)
name_input_area.place(x = 110,y = 128)
name_input_area.focus_force()
ui.mainloop()
