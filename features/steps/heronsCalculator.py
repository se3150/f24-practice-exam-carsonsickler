import time
@when("I enter the sides of the triangle as {a}, {b}, {c}")
def step_impl(context, a, b, c):
    context.behave_driver.find_element_by_id("a").send_keys(a)
    context.behave_driver.find_element_by_id("b").send_keys(b)
    context.behave_driver.find_element_by_id("c").send_keys(c)


@then('I should see the area of the triangle as {area}')
def step_impl(context, area):
    assert (context.behave_driver.find_element_by_id("_d").get_attribute("value")) == area