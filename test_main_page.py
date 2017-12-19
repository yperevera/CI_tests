import tests.tests as tests

# Test Step 1 Open main page
def test_open_main_page(driver, url):
    tests.open_url(driver, url)


# Test Step 2 Verify count of article items 
def test_count_of_article_items(driver):
    tests.verify_count_of_article_items(driver)


# Test Step 3 Verify count of item's titles in article section (without region item)
def test_article_items_title_count_no_region(driver):
    tests.verify_article_items_title_count_no_region(driver)


# Test Step 4 Verify order of item's titles in article section (without region item)
def test_article_items_title_order_no_region(driver):
    tests.verify_article_items_title_order_no_region(driver)


# Test Step 5 Verify title of region item in article section
def test_article_item_title_region(driver):
    tests.verify_article_item_title_region(driver)


# Test Step 6 Verify count of the items in favourites section
def test_favourites_items_count(driver):
    tests.verify_favourites_items_count(driver)


# Test Step 7 Verify sum of the 'lc' attribute of items in favourites section
def test_favourites_items_lc_attr_sum(driver):
    tests.verify_favourites_items_lc_attr_sum(driver)
