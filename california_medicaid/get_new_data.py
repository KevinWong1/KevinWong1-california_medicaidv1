from bs4 import BeautifulSoup
import io
from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_date():
    chrome_driver_path = "/Users/kevin/Desktop/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://www.dhcs.ca.gov/services/Pages/ff.html")

# wait for page to finish loading
    timeout = 3

    try:
        element_present = EC.presence_of_element_located(
            (By.LINK_TEXT, 'Show'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")

    # click show more button
    driver.find_element_by_xpath(
        '/html/body/table[2]/tbody/tr[1]/td/div[1]/div[2]/div[3]/span/a').click()

    # saving html from medicaid website to a file
    html_source = driver.page_source

    # exit selenium webdriver
    driver.quit()

    f = io.open("website.html", "w", encoding="utf-8")
    f.write(html_source)
    f.close()

    # extract html info using beautiful soup

    # with open("website.html") as file:
    #     contents = file.read()
    #
    # soup = BeautifulSoup(contents, 'html.parser')
    #
    # list_of_dictionary = []
    # y = soup.select('.ffitem .body-sml span')
    #
    # for x in y:
    #     temp_dictionary = {}
    #     a = x.select('h3')
    #     for _ in a:
    #         temp_dictionary['drug_name'] = _.getText()
    #     b = x.select('p')
    #
    #     for _ in b:
    #
    #         if 'cd1' in str(_):
    #             temp_dictionary['restricted'] = _.getText()
    #         elif 'codes' in str(_):
    #             temp_dictionary['code'] = _.getText()
    #         else:
    #             temp_dictionary['other'] = _.getText()
    #     if temp_dictionary:
    #         list_of_dictionary.append(temp_dictionary)
    #
    # sorted_list = sorted(list_of_dictionary, key=lambda i: i['drug_name'])
    # print(sorted_list)

# for drug_dictionary in sorted_list:
#     # print(drug_dictionary['drug_name'])
#     print(f"{'<h3>'}{drug_dictionary['drug_name']}{'</h3>'}")
#     if 'restricted' in drug_dictionary:
#         print(f"{'<p>'} {drug_dictionary['restricted']}  {'</p>'}")
#     print(f"{'<p>'} {drug_dictionary['code']}  {'</p>'}")
#     print(f"{'<p>'} {drug_dictionary['other']}  {'</p>'}")

# for drug_dictionary in sorted_list:
#     # print(drug_dictionary['drug_name'])
#     print(f"{drug_dictionary['drug_name']}")
#     if 'restricted' in drug_dictionary:
#         print(f" {drug_dictionary['restricted']}")
#     print(f" {drug_dictionary['code']} ")
#     # print(f"{drug_dictionary['other']}")
