from selenium.webdriver.common.by import By

# elements
main_page_div = "//div[@class='wrapper']"
article_items_list_xpath = "//article[@id='feed']/section"
article_items_title_list_xpath = "//article[@id='feed']/section/h2/a"
article_item_region_title_xpath = "//article[@id='feed']/section/div/a[@data-show='show-regions']"
favourites_items_list_xpath = "//div[@class='favorites-block__list d-clear']//a"

# expected
expected_article_items_count = 16
expected_article_items_titles_no_region_list = ["Головне", "Політика", "Економіка", "Події", "Суспільство", "Технології", "Наука", "Авто", "Спорт", "Здоров'я", "Шоу-бізнес", "За кордоном", "Курйози", "Фоторепортаж", "Відео"]
expected_article_item_region_title = "Київські новини"
expected_favourites_items_count = 12
expected_favourites_items_lc_attr_sum = 5350


def open_url(driver, url):
    driver.get(url)
    driver.find_element(By.XPATH, main_page_div)


def get_list_of_elements_xpath(driver, element):
    return driver.find_elements(By.XPATH, element)


def get_element_xpath(driver, element):
    return driver.find_element(By.XPATH, element)


def verify_count_of_article_items(driver):
    assert len(get_list_of_elements_xpath(driver, article_items_list_xpath)) == expected_article_items_count


def verify_article_items_title_count_no_region(driver):
    assert len(get_list_of_elements_xpath(driver, article_items_title_list_xpath)) == len(expected_article_items_titles_no_region_list)


def verify_article_items_title_order_no_region(driver):
    i = 0
    for item in get_list_of_elements_xpath(driver, article_items_title_list_xpath):
        if item.text != expected_article_items_titles_no_region_list[i]:
            assert item.text == expected_article_items_titles_no_region_list[i], "Order of the article items is not correctly displayed!"
        i += 1


def verify_article_item_title_region(driver):
    assert get_element_xpath(driver, article_item_region_title_xpath).text == expected_article_item_region_title


def verify_favourites_items_count(driver):
    assert len(get_list_of_elements_xpath(driver, favourites_items_list_xpath)) == expected_favourites_items_count


def verify_favourites_items_lc_attr_sum(driver):
    items_list = get_list_of_elements_xpath(driver, favourites_items_list_xpath)
    actual_sum = 0
    for item in items_list:
        value = int(item.get_attribute("lc"))
        actual_sum += value
    assert actual_sum == expected_favourites_items_lc_attr_sum
