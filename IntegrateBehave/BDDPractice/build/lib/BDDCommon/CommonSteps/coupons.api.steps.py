from behave import step
from BDDCommon.CommonHelpers.utilitiesHelper import generate_random_coupon_code
from BDDCommon.CommonAPI import coupons_api
import pdb


@step('I create a "{discount_type}" coupon')
def i_create_a_discount_type_coupon(context, discount_type):
    data = {
        "code": generate_random_coupon_code(),
    }
    if discount_type.lower() != 'none':
        data['discount_type'] = discount_type

    response_api = coupons_api.create_coupon(data)
    pdb.set_trace()