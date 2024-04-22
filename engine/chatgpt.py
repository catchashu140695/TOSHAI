from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pyvirtualdisplay import Display


class chatgpt:
    def chatgpt3(prompt):
        
        #to run the selenium program without opening the browser
        # display = Display(visible=0, size=(800, 600))
        # display.start()
        
        
        # Set up Firefox options
        options = Options()
        options.headless = True  # Set headless option to True

        # Create a new instance of the Firefox driver
        driver = webdriver.Chrome(options=options)

        # Go to the OpenAI URL
        driver.get("https://chat.openai.com")

        # Find the element that's name attribute is q (the google search box)
        inputElement = driver.find_element(By.ID, "prompt-textarea")

        # Type in the search
        inputElement.send_keys(prompt)       

        # Submit the form (although google automatically searches now without submitting)
        inputElement.send_keys(Keys.RETURN)
        
        time.sleep(2)       
        
        while True:
            output = driver.find_element(By.CLASS_NAME, "markdown").text
            time.sleep(2)
            if  driver.find_element(By.CLASS_NAME, "markdown").text == output:
                break
            else:                
                output=driver.find_element(By.CLASS_NAME, "markdown").text
                time.sleep(2)          
        
        
        # Close the browser
        driver.quit()
        #display.stop()
        print("ChatGPT Says :"+output)
        return output   
   
    
        