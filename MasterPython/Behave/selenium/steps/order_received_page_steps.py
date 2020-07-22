from behave import step
from config.locatorsconfig import ORDER_RECEIVED_PAGE_LOCATORS
from helpers.webcommon import WebCommon


@step("the 'order received page' should load with correct data")
def the_order_received_page_should_load_with_correct_data(context):
    context.execute_steps("""
    then Order received heading should be displayed
    then Thank you message should be displayed
    then Verify order number and label displayed
    """)


@step("Order received heading should be displayed")
def order_received_heading_should_be_display(context):
    wc = WebCommon()
    header_locator = ORDER_RECEIVED_PAGE_LOCATORS['page_header']
    wc.assert_element_contains_text(context, 'Order received', header_locator['type'], header_locator['locator'])


@step("Thank you message should be displayed")
def thank_you_message_should_be_displayed(context):
    wc = WebCommon()
    thank_you_locator = ORDER_RECEIVED_PAGE_LOCATORS['thank_you_notice']
    wc.assert_element_contains_text(context, 'Thank you. Your order has been received.', thank_you_locator['type'], thank_you_locator['locator'])


@step("Verify order number and label displayed")
def verify_order_number_and_label_displayed(context):
    wc = WebCommon()
    order_detail_locator = ORDER_RECEIVED_PAGE_LOCATORS['order_details_order']
    elm = wc.find_element(context, order_detail_locator['type'], order_detail_locator['locator'])
    order_text = elm.text
    order_text_list = order_text.split('\n')
    label = order_text_list[0]
    order_id = order_text_list[1]

    assert label == 'ORDER NUMBER:', f"Order Received page - The label for the order number is not correct.  Expected 'ORDER NUMBER:' but was {label}"
    assert order_id.isnumeric(), f"Order Received page - The order id is not numeric.  Actual {order_id}"
    context.order_id = order_id
