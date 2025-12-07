from playwright.sync_api import Page, expect


class FavoritesPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_favorites_view(self):
        btn = self.page.get_by_test_id("favorites")
        btn.click()
        fav_view = self.page.locator(".favorites")
        expect(fav_view).to_be_visible()

    def assert_book_in_favorites(self, title):
        fav_locator = self.page.locator("div.favorites li.book").filter(has_text=title)
        expect(fav_locator).to_be_visible()

    def assert_no_favorites(self):
        expect(self.page.locator("li.book")).to_have_count(0)
