from behave import then


@then(u'texten "Välkommen!" visas')
def step_welcome_text(context):
    context.catalog_page.assert_welcome_text()


@then(u'en katalog med böcker visas')
def step_book_list(context):
    context.catalog_page.go_to_catalog_view()
    context.catalog_page.wait_for_catalog()
