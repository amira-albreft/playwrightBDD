from playwright.sync_api import Page, expect
import re


class CatalogPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_catalog_view(self):
        button = self.page.get_by_test_id("catalog")
        if not button.is_disabled():
            button.click()
        catalog = self.page.locator(".catalog")
        expect(catalog).to_be_visible()

    def assert_welcome_text(self):
        welcome_heading = self.page.get_by_text("Välkommen!")
        expect(welcome_heading).to_be_visible()

    def wait_for_catalog(self):
        self.page.locator(".catalog .book")

    def get_first_book_title(self):
        first_book = self.page.locator("div.catalog div.book").first
        title_text = first_book.inner_text() # Get the raw inner text
        title_text = re.sub(r'^[^\w"]+', '', title_text) # Remove the heart emoji or any other non-alphanumeric
        # characters at the start
        title = title_text.split(",")[0].strip().replace('"', '') # Extract the title (before the comma)
        return title

    def click_first_heart(self):
        heart = self.page.locator('[data-testid^="star-"]').first
        heart.click()

    def assert_first_heart_selected(self):
        heart = self.page.locator('[data-testid^="star-"]').first
        expect(heart).to_contain_class("selected")

    def assert_book_in_catalog(self, title, author):
        text = f'"{title}", {author}'
        book_locator = self.page.locator("div.catalog div.book").filter(has_text=text)
        expect(book_locator).to_be_visible()