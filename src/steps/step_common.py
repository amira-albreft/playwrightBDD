from behave import given


@given(u'användaren navigerar till startsidan')
def step_navigate_to_home(context):
    context.page.goto(context.base_url)
