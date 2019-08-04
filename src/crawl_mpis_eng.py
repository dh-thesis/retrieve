import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlencode

from .utils_paths import BASE_DIR

WRITE_DIR = BASE_DIR + 'mpis/scrape/'

# func to write json file

def write_json_file(path, data):
    print("creating file:", path)
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=2))

##################################################
### CRAWL LIST OF MAX PLANCK INSTITUTES (MPIs) ###
##################################################

BASE_URL = 'https://www.mpg.de/11741001/research_page'


params = {'tab':'institutes'}

driver = webdriver.Firefox()
data = {}

url = BASE_URL + '?' + urlencode(params)
driver.get(url)
tab_content = driver.find_element_by_class_name('tab-content')
button = tab_content.find_element_by_link_text('Show more')

while button:
    button.click()
    try:
        tab_content = driver.find_element_by_class_name('tab-content')
        button = driver.find_element_by_link_text('Show more')
    except NoSuchElementException:
        button = None

institutes = tab_content.find_elements_by_class_name('meta-information')

for institute in institutes:
    title = institute.find_element_by_xpath(".//h3/a").text
    data[title] = {}
    location = institute.find_element_by_xpath(".//div/p").text
    data[title]['loc'] = location
    tags_data = institute.find_element_by_class_name('tags')
    tags_spans = tags_data.find_elements_by_xpath(".//span")
    tags = []
    for tag in tags_spans:
        tags.append(tag.text)
    data[title]['tags'] = tags


write_json_file(WRITE_DIR + 'all.json', data)

##################################################
### CRAWL LIST OF CATEOGRIES WITH RELATED MPIs ###
##################################################

CATEGORIES = ['astronomy-and-astrophysics','biology-and-medicine','material-and-technology','environment-and-climate','humanities']

cat_data = {}

for category in CATEGORIES:
    cat_data[category] = []
    params['category'] = category
    url = BASE_URL + '?' + urlencode(params)
    driver.get(url)
    tab_content = driver.find_element_by_class_name('tab-content')
    button = tab_content.find_element_by_link_text('Show more')
    while button:
        button.click()
        try:
            tab_content = driver.find_element_by_class_name('tab-content')
            button = driver.find_element_by_link_text('Show more')
        except NoSuchElementException:
            button = None
    institutes = tab_content.find_elements_by_class_name('meta-information')
    for institute in institutes:
        title = institute.find_element_by_xpath(".//h3/a").text
        cat_data[category].append(title)


driver.close()
print("done with scraping!")

write_json_file(WRITE_DIR + 'categories.json', cat_data)
