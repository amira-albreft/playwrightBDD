from playwright.sync_api import Page, expect


class MainPage:
    def __init__(self, page: Page, base_url):
        self.page = page
        self.base_url = base_url
        self.catalog_button = page.get_by_test_id("catalog")
        self.add_book_button = page.get_by_test_id("add-book")
        self.favorites_button = page.get_by_test_id("favorites")

    def start_page(self):
        self.page.goto(self.base_url)
        expect(self.page.locator("body")).to_be_visible()

    def wait_for_navigation_buttons(self):
        expect(self.catalog_button).to_be_disabled()  # button disabled because we are already on the catalog page as per default
        expect(self.add_book_button).to_be_enabled()
        expect(self.favorites_button).to_be_enabled()
