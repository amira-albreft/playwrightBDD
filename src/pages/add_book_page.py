from playwright.sync_api import Page, expect


class AddBookPage:
    def __init__(self, page: Page):
        self.page = page
        self.title_input = page.get_by_test_id("add-input-title")
        self.author_input = page.get_by_test_id("add-input-author")
        self.submit_button = page.get_by_test_id("add-submit")

    def go_to_add_book_view(self):
        button = self.page.get_by_test_id("add-book")
        button.click()
        add_book = self.page.get_by_test_id("add-submit")
        expect(add_book).to_be_visible()

    def show_form(self):
        form = self.page.locator("div.form")
        expect(form).to_be_visible()
        expect(form.locator('input[data-testid="add-input-title"]')).to_be_visible()
        expect(form.locator('input[data-testid="add-input-author"]')).to_be_visible()
        expect(form.locator('button[data-testid="add-submit"]')).to_be_visible()

    def fill_title(self, title):
        self.title_input.fill(title)

    def fill_author(self, author):
        self.author_input.fill(author)

    def submit(self):
        self.submit_button.click()
        expect(self.submit_button).to_be_disabled()
        title_input = self.page.get_by_test_id("add-input-title")
        author_input = self.page.get_by_test_id("add-input-author")
        expect(title_input).to_have_value("")
        expect(author_input).to_have_value("")

    def assert_submit_button_disabled(self):
        expect(self.submit_button).to_be_disabled()


