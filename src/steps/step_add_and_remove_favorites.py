from behave import given, when, then


@when('användaren klickar på hjärtikonen bredvid första boken')
def step_click_first_heart(context):
    context.catalog_page.wait_for_catalog()
    context.first_book_title = context.catalog_page.get_first_book_title()
    context.catalog_page.click_first_heart()


@then('boken favoritmarkeras genom att hjärtat framträder')
def step_heart_selected(context):
    context.catalog_page.assert_first_heart_selected()


@then(u'den favoritmarkerade boken läggs till i vyn "Mina böcker')
def step_book_added(context):
    title = context.catalog_page.get_first_book_title()
    context.favorites_page.go_to_favorites_view()
    context.favorites_page.assert_book_in_favorites(title)


# Scenario: Ta bort favoritmarkering från en bok
@given('användaren har favoritmarkerat en bok i katalogen')
def step_favorite_a_book(context):
    context.page.goto(context.base_url)
    context.catalog_page.wait_for_catalog()
    context.catalog_page.click_first_heart()
    context.catalog_page.assert_first_heart_selected()


@when('användaren klickar på hjärtikonen bredvid boken')
def step_remove_first_favorite(context):
    context.catalog_page.wait_for_catalog()
    context.catalog_page.click_first_heart()


@then('boken tas bort från vyn "Mina böcker"')
def step_book_removed(context):
    context.favorites_page.go_to_favorites_view()
    context.favorites_page.assert_no_favorites()
