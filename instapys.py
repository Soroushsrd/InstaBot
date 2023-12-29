import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logging.basicConfig(format='%(levelname)s - (%(asctime)s) - %(message)s - (Line: %(lineno)d) - [%(filename)s]',
    datefmt='%H:%M:%S',
    encoding='utf-8',
    level=logging.INFO)
logger=logging.getLogger(__name__)
# Replace these with your Instagram credentials

logger.info("user has started the bot.")

USERNAME = "your username"
PASSWORD = "your passowrd"
# Replace this with the target hashtag you want to search
HASHTAG = ["بدنسازی_آقایان","رژیم","کاهش_وزن","مربی",
           "مربی_آنلاین","بدنسازی","چربیسوز","سکسی_جذاب","چاقی",
           "مدلینگ","مدل","بدنساز","چربی","غذا","غذای_ایرانی","غذای_سالم",
           "غذای_خانگی","غذای_رژیمی","رژیم_لاغری","رژیم_رایگان","رژیمی",
           "رژیم_آنلاین","رژیمی_ولی_خوشمزه","رژیم_کیتوژنیک",
           "رژیم_سالم","رژیم_درمانی","رژیم_اصولی","عضله","عضلات","عضله_سازی",
           "عضلات_شکم","بانوان_ورزشکار","بانوان","بدن","بدنسازی_تغذیه","بدنسازی_زنان",
           "تغذیه","تغذیه_سالم","تغذیه_مناسب","تغذیه_کودک","تغذیه_بدنسازی"]

# Replace this with your desired comment text

driver = webdriver.Chrome()

# Open Instagram and login
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
logger.info("we are inside")

# Wait for the page to load after login
while True:
    time.sleep(10)
    for i in range(3):
        seed=random.randint(1,1000)
        random.seed(seed)
        logger.info("itteration number %s.", i)
        hash=random.choice(HASHTAG)    # Perform a hashtag search
        logger.info("choosing hashtag %s.", hash)
        seed+=1
        driver.get(f"https://www.instagram.com/explore/tags/{hash}/")

        time.sleep(15)

        COMMENT_TEXT = random.choice(["رایگان عضله سازی کن",
                                      "اگر دنبال لاغر شدنی بهم دایرکت بده راهنماییت کنم",
                                      "ساختن عضله اوتقدرا هم سخت نیست! من راهش رو بهت یاد میدم.",
                                      "منم در این مورد چندتا پست دارم. حتما پیجم رو ببینین.",
                                      "پست خیلی خوبی بود. عالی",
                                      "خیلی مفید بود مرسی. منم در این مورد چندتا پست دارم",
                                      "پست هام رو بخون و رایگان لاغر شو",
                                      "پست آخرم رو ببینین. در همین مورد هست"])
        logger.info("choosing comment %s.", COMMENT_TEXT)

    # Adjust the maximum wait time according to your page's responsiveness
        postnumber=random.choice([1,2,3,4,5])
        logger.info(f"choosing the post number {postnumber}")
        # post = driver.find_element(By.XPATH, f"(//article//a[contains(@href, '/p/')])")
        post = driver.find_element(By.XPATH, f"(//article//a[contains(@href, '/p/')])[{postnumber}]")

        post.click()

        time.sleep(10)

        for _ in range(5):  # Try up to 5 times to handle any race conditions
            try:
                comment_input = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Add a comment…']")
                time.sleep(5)
                comment_input.send_keys(COMMENT_TEXT)
                comment_input.send_keys(Keys.ENTER)
                time.sleep(10)
                logger.info("comment added.")

                break
            except Exception as e:
                if "no such element" in str(e):
                    print(f"Element not found for {hash}. Trying the next hashtag.")
                    break
                else:
                    print(f"Error while adding comment: {e}")
                    time.sleep(2)  # Wait for a few seconds and then retry

            time.sleep(10)



    sleep=random.choice([3600,4000,2000,4800,7200])
    logger.info("waiting time: %s.", sleep)

    # Wait for a few seconds before closing the browser
    time.sleep(sleep)

    # Close the browser
 