import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



chromedriver_path = r'engine\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--remote-debugging-port=8989")
chrome_options.add_argument("--user-data-dir=F:\\ChromeProfile\\Profile")
chrome_options.binary_location = r"F:\ChromeProfile\chrome-win64\chrome.exe"
service = Service(executable_path=chromedriver_path)



class web_automations:  
    
    def chatgpt3(prompt): 
        bot = webdriver.Chrome(service=service, options=chrome_options)
        bot.get("https://chat.openai.com")        
        inputElement = bot.find_element(By.ID, "prompt-textarea")        
        inputElement.send_keys(prompt) 
        inputElement.send_keys(Keys.RETURN)        
        time.sleep(2)          
        while True:
            
            if(bot.find_element(By.TAG_NAME, "code")):
                output = bot.find_element(By.TAG_NAME, "code").text
                time.sleep(5)
                if  bot.find_element(By.TAG_NAME, "code").text == output:
                    break
                else:                
                    output=bot.find_element(By.TAG_NAME, "code").text
                    time.sleep(5)
            else:               
            
                output = bot.find_element(By.CLASS_NAME, "markdown").text
                time.sleep(5)
                if  bot.find_element(By.CLASS_NAME, "markdown").text == output:
                    break
                else:                
                    output=bot.find_element(By.CLASS_NAME, "markdown").text
                    time.sleep(5)     
        
        bot.quit()        
        #print("ChatGPT Says :"+output)
        return output
    def upload_youtube_shorts():
        bot = webdriver.Chrome(service=service, options=chrome_options)
        dir_path = '.\\shorts_videos'
        count = 0

        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        print(count, "videos found in the videos folder, ready to upload...")
        time.sleep(6)

        for i in range(count):    

            bot.get("https://studio.youtube.com")
            time.sleep(3)
            upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
            upload_button.click()
            time.sleep(1)

            file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
            simp_path = 'shorts_videos/vid{}.mp4'.format(str(i+1))
            abs_path = os.path.abspath(simp_path)
            file_input.send_keys(abs_path)
            time.sleep(7)
            
            vid_title = bot.find_element(By.XPATH, '//*[@id="textbox"]')
            vid_title.send_keys("Title working")
            time.sleep(500)

            
            print("Until this success !!!")
            # next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
            # for i in range(3):
            #     next_button.click()
            #     time.sleep(1)

            # done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
            # done_button.click()
            # time.sleep(5)
            bot.quit()




