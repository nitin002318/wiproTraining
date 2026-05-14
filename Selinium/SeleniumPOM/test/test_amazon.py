import time

import pytest
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    print("\nOpened Amazon Homepage. Title & URL verified.")

@pytest.mark.parameterize("searchproduct" ,[
    ("wireless_mouse"), ("shoes")
])
def test_search_product(driver, searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print(f"Search results page loaded successfully - {searchproduct}")

@pytest.mark.parameterize("searchproduct" ,[
    ("wireless_mouse"), ("shoes")
])
def test_find_elements_amazon(driver):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Search results page loaded sucessfully - {searchproduct}")
    homepage.click_search_button()

    assert

    productlistingpage = ProductListingPage(driver)
    productlistingpage.find_product_title()
    val =productlistingpage.all_products()
    assert val, "No products found on Amazon search results"


@pytest.mark.parameterize("searchproduct" ,[
    ("wireless_mouse"), ("shoes", "Nike")
def test_find_brand(driver):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print()


    productlistingpage = ProductListingPage(driver) 
    productlistingpage.find_product_title() val =productlistingpage.all_products()
    assert val, "No products found on Amazon search results"


