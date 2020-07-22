
from behave import given, when, then, step
from BDDCommon.CommonFuncs import webcommon

import pdb


@step('I go to the "{page}" page')
@given('I go to the page "{page}"')
def go_to_page(context, page):
    print("Navigating to the site: {}".format(page))
    context.driver = webcommon.go_to(context, page)


@then('the page title should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    webcommon.assert_page_title(context, expected_title)


@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    webcommon.assert_current_url(context, expected_url)