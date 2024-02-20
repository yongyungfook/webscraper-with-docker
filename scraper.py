from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def scraper():
    website_url = "https://www.digiheritage.com/contact-us"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(options=chrome_options, service=service)

    driver.get(website_url)

    print("I scraped", website_url)

    #Should be a class or name but there is no name/class for this
    number_element = driver.find_element(By.XPATH, "//a[contains(@href,'tel:+6 088-257487')]")

    number_text = number_element.text

    driver.quit()

    print("This is the number you want  :", number_text)

    return number_text  

if __name__ == "__main__":
    scraper()