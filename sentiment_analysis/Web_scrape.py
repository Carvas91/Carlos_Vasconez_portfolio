import time
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

scrollingScript = """ 
      document.getElementsByClassName('m6QErb DxyBCb kA9KIf dS8AEf')[0].scroll(0, 500000)
    """


# Create a Chrome options instance
options = Options()
# Set the user agent
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.200 Safari/537.36")

service = Service(executable_path="chromedriver.exe")
# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com/maps/place/Lambton+College/@43.6274247,-79.6771064,17z/data=!4m8!3m7!1s0x882b409fb8a947f9:0x418640e93fdafd13!8m2!3d43.6274208!4d-79.6745315!9m1!1b1!16s%2Fg%2F11c1ldpfm2?entry=ttu")

time.sleep(random.uniform(4.0,5.0))

scrolls = 0
while scrolls != 20:
    driver.execute_script(scrollingScript)
    sleep(random.uniform(5,6))
    scrolls += 1

# Locating the 'More' links and clicking them to expand the review texts
more_links = driver.find_elements(By.XPATH, "//button[contains(text(), 'More')]")
for link in more_links:
    try:
        link.click()
        # Wait a bit for the content to load
        time.sleep(1)
    except Exception as e:
        print(f"Error clicking link: {e}")

# Locating the review comments elements
review_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'MyEned')]/span[@class='wiI7pd']")

# Locating the star rating elements
star_rating_elements = driver.find_elements(By.XPATH, "//span[contains(@class, 'kvMYJc')]")


import pandas as pd

# Locating the names are in an element with a specific class, find them
name_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'd4r55')]")

# Extracting names, complete reviews, and star ratings
data = []
for name_element, review_element, star_rating_element in zip(name_elements, review_elements, star_rating_elements):
    name = name_element.text  # Get the text directly since the name is the text content of the div
    review_text = review_element.text
    star_rating = star_rating_element.get_attribute('aria-label')
    data.append((name, review_text, star_rating))


# Creating a Pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Comment', 'Rating'])

# Display the DataFrame
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv('reviews.csv', index=False)


print(df.Comment)
