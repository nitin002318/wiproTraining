import time
import pytest
from pages.home_page import
from pages.product_listing_page import ProductListingPage


def test_product_ordering(drive, searchproduct, brandname, mensize):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searching product")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print(f"Search results page loaded sucessfully ")

    productlistingpage = ProductListingPage(driver)

    print(f"")

    productlistingpage.select_brand_filter(brandname)
    print(f"Applying Size Filter for men's shoes -{mensize}")


