from selenium.webdriver.common.by import By

main_page_div = "//div[@class='wrapper']"
article_items_list_xpath = "//article[@id='feed']/section"
article_items_title_list_xpath = "//article[@id='feed']/section/h2/a"
article_item_region_title_xpath = "//article[@id='feed']/section/div/a[@data-show='show-regions']"
favourites_items_list_xpath = "//div[@class='favorites-block__list d-clear']//a"


def open_url(driver, url):
    driver.get(url)
    driver.find_element(By.XPATH, page)


def get_list_of_elements_xpath(driver, element):
    return driver.find_elements(By.XPATH, element)


def get_element_xpath(driver, element):
    return driver.find_element(By.XPATH, element)


def verify_url(driver, url):
    assert url == driver.current_url
