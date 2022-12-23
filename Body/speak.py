# import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


# def Speak(Text):
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices', voices[0].id)
#     engine.setProperty('rate', 170)
#     print("")
#     print(f"You : {Text}.")
#     print("")
#     engine.say(Text)
#     engine.runAndWait()


# Speak("Hello Sir")

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "Database\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Emma')


def Speak(Text):
    length_of_text = len(str(Text))
    
    if length_of_text<=0:
        pass
    else:
        print("")
        print(f"AI : {Text}.")
        print("")
        Data = str(Text)
        print("")
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()
        
        if length_of_text>=30:
            sleep(4)
        elif length_of_text>=40:
            sleep(6)
        elif length_of_text>=55:
            sleep(8)
        elif length_of_text>=70:
            sleep(10)
        elif length_of_text>=100:
            sleep(13)
        elif length_of_text>=120:
            sleep(14)
        else:
            sleep(2)
        
# Speak("Hello, I am Aditi, your virtual friend.")



