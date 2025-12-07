from behave import given, when, then


@given(u'användaren navigerar till "Lägg till bok"')
def step_navigate_to_add_book(context):
    context.page.goto(context.base_url)
    context.add_book_page.go_to_add_book_view()


@when(u'ett formulär visas')
def step_show_form(context):
    context.add_book_page.show_form()


@when(u'användaren fyller i "Titel" med "{title}"')
def step_fill_title(context, title):
    context.add_book_page.fill_title(title)


@when(u'användaren fyller i "Författare" med "{author}"')
def step_fill_author(context, author):
    context.add_book_page.fill_author(author)


@when(u'användaren klickar på knappen "Lägg till ny bok" och formuläret är tomt igen')
def step_submit_new_book(context):
    context.add_book_page.submit()
    context.add_book_page.assert_submit_button_disabled()


@then(u'boken med titeln "{title}" och författaren "{author}" läggs till i "Katalog"')
def step_new_book_added_to_catalog(context, title, author):
    context.catalog_page.go_to_catalog_view()
    context.catalog_page.wait_for_catalog()
    context.catalog_page.assert_book_in_catalog(title, author)


@then(u'knappen "Lägg till ny bok" är inaktiverad och det går inte att lägga till boken i "Katalog"')
def step_submit_button_disabled(context):
    context.add_book_page.assert_submit_button_disabled()
