import pytest
from selenium.webdriver import Chrome
import elements as imported_elements

elements = imported_elements.main_page

# For running webdriver() before ALL tests use @pytest.fixture(scope='session')
# For running webdriver() before EACH test use @pytest.fixture
@pytest.fixture(scope='session')
def webdriver(request):
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://www.ukr.net/")
    request.addfinalizer(driver.quit)
    return driver

def test_verify_count_of_article_items(webdriver):
    list_of_article_items = webdriver.find_elements_by_xpath(elements['article_items_list_xpath'])
    assert len(list_of_article_items) == 16

def test_verify_title_of_article_items(webdriver):
    list_of_article_items_title = webdriver.find_elements_by_xpath(elements['title_article_items_list_xpath'])
    expected_list_of_items = ["Головне", "Політика", "Економіка", "Події", "Суспільство", "Технології", "Наука", "Авто", "Спорт", "Здоров'я", "Шоу-бізнес", "За кордоном", "Курйози", "Фоторепортаж", "Відео"]
    #assert len(list_of_article_items_title) == len(expected_list_of_items)
    
    i = 0
    for item in list_of_article_items_title:
        if item.text != expected_list_of_items[i]:
            assert item.text == expected_list_of_items[i], "Order of the article items is not correctly displayed!"
        else:
            if i == len(expected_list_of_items):
                assert 1==1
        i += 1

def test_verify_title_of_article_item_region(webdriver):
    article_region_item_title = webdriver.find_element_by_xpath(elements['title_region_article_item_xpath']).text
    assert article_region_item_title == "Київські новини"

def test_verify_count_of_favourites_items(webdriver):
    favourites_items_list = webdriver.find_elements_by_xpath(elements['favourites_items_list_xpath'])
    assert len(favourites_items_list) == 12
    
def test_verify_count_of_favourites_items_attributes(webdriver):
    favourites_items_list = webdriver.find_elements_by_xpath(elements['favourites_items_list_xpath'])
    expected_sum_of_attributes = 5350
    actual_sum_of_attributes = 0
    for item in favourites_items_list:
        value = int(item.get_attribute("lc"))
        actual_sum_of_attributes += value
    assert actual_sum_of_attributes == expected_sum_of_attributes
