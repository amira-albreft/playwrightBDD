from behave import when, then


@when(u'sidan laddas')
def step_page_loads(context):
    context.main_page.start_page()


@then(u'menyn ska visas med knapparna "Katalog", "Lägg till bok" och "Mina böcker"')
def step_verify_menu_buttons(context):
    context.main_page.wait_for_navigation_buttons()
