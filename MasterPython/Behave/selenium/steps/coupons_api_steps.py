import json

from behave import step
from helpers.utilitiesHelper import UtilitiesHelper
from apis import coupons_api
from dao.couponsDAO import CouponsDAO
import pdb


@step('I create a "{discount_type}" coupon')
def i_create_a_discount_type_coupon(context, discount_type):
    uh = UtilitiesHelper()
    code = uh.generate_random_coupon_code()
    data = {
        "code": code,
    }
    if discount_type.lower() != 'none':
        context.expected_discount_type = discount_type
        data["discount_type"] = discount_type

    else:
        context.expected_discount_type = 'fixed_cart'

    response_api = coupons_api.create_coupon(data)
    context.new_coupon_info = response_api


@step('the coupon should exist in the database')
def the_coupon_should_exist_in_the_database(context):
    coupon_dao = CouponsDAO()
    coupon_id = context.new_coupon_info['id']
    db_coupon = coupon_dao.get_coupon_by_id(coupon_id)
    assert db_coupon, f"coupon not found in database.  Coupon id {coupon_id}"
    coupon_meta = coupon_dao.get_coupon_metadata_by_id(coupon_id)
    assert coupon_meta['discount_type'] == context.expected_discount_type, \
        f"unexpected 'discount_type' for new coupon." \
        f"Expected: {context.expected_discount_type}, actual {coupon_meta['discount_type']}"
    #pdb.set_trace()


@step('I create a coupon with given parameters')
def i_create_a_coupon_with_given_parameters(context):
    uh = UtilitiesHelper()
    data_raw = context.text
    data = json.loads(data_raw)
    data['code'] = uh.generate_random_coupon_code()

    response_api = coupons_api.create_coupon(data)
    context.new_coupon_info = response_api


@step("I verify the given data in the database")
def i_verify_the_given_data_in_the_database(context):
    expected_values_raw = context.text
    expected_values = json.loads(expected_values_raw)

    coupon_id = context.new_coupon_info['id']
    db_meta = CouponsDAO().get_coupon_metadata_by_id(coupon_id)
    #pdb.set_trace()

    failed_values = []
    for key, value in expected_values.items():
        if str(db_meta[key]) != str(value):
            failed_values.append(
                {
                key: {'expected': value,
                      'db': db_meta[key]}
                 }
            )

    if failed_values:
        raise Exception(f"unexpected metadata. failed fields {failed_values}")


@step("I get a valid {pct}% off coupon")
def i_get_a_valid_pct_off_coupon(context, pct):
    if int(pct) == 50:
        context.coupon_code = "TEST50"
    else:
        raise Exception("Not implemented")





