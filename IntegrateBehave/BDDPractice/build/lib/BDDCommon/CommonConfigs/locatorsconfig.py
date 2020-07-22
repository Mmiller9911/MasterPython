LOCATORS = {
    'main navigation': {'type': 'id', 'locator': 'mainnav'},
    'top navigation': {'type': 'id', 'locator': 'top'},
    'options': {'type': 'css selector', 'locator': '.options-bar'}
}

MY_ACCOUNT_LOCATORS = {
    'login_user_name': {'type': 'id', 'locator': 'username'},
    'login_user_password': {'type': 'id', 'locator': 'password'},
    'login_button': {'type': 'css selector', 'locator': 'button[name="login"]'},
    'left_nav': {'type': 'css selector', 'locator': 'div.entry-content nav.woocommerce-MyAccount-navigation'},
    'left_nav_logout_btn': {'type': 'css selector', 'locator': 'div.entry-content nav.woocommerce-MyAccount-navigation ul li:nth-of-type(6)'},
    'error_box': {'type': 'xpath', 'locator': "//ul[@class='woocommerce-error']"}
}

HOME_PAGE_LOCATORS = {
    'all_add_cart_btns': {'type': 'css selector', 'locator': 'li.product a.ajax_add_to_cart'},
    'cart_info_box': {'type': 'xpath', 'locator': '//a[@class="cart-contents"]'}

}

CART_PAGE_LOCATORS = {
    'free_shipping_radio': {'type': 'xpath', 'locator': "//input[@id='shipping_method_0_free_shipping3']"},
    'proceed_to_checkout_btn': {'type': 'css selector', 'locator': 'div.wc-proceed-to-checkout a.checkout-button'}

}
CHECKOUT_PAGE_LOCATORS = {
    'page_header': {'type': 'css selector', 'locator': 'header.entry-header h1.entry-title'},
    'checkout_form': {'type': 'css selector', 'locator': 'header.entry-header h1.entry-title'},
    'billing_f_name_input': {'type': 'css selector', 'locator': 'input#billing_first_name'},
    'billing_l_name_input': {'type': 'css selector', 'locator': 'input#billing_last_name'},
    'billing_company_input': {'type': 'css selector', 'locator': 'input#billing_company'},
    'billing_address1_input': {'type': 'css selector', 'locator': 'input#billing_address_1'},
    'billing_address2_input': {'type': 'css selector', 'locator': 'input#billing_address_2'},
    'billing_city_input': {'type': 'css selector', 'locator': 'input#billing_city'},
    'billing_zip_input': {'type': 'css selector', 'locator': 'input#billing_postcode'},
    'billing_phone_input': {'type': 'css selector', 'locator': 'input#billing_phone'},
    'billing_email_input': {'type': 'css selector', 'locator': 'input#billing_email'},
    'place_order_button': {'type': 'css selector', 'locator': 'button#place_order'},
}

ORDER_RECEIVED_PAGE_LOCATORS = {
    'page_header': {'type': 'xpath', 'locator': '//h1[@class="entry-title"]'},
    'thank_you_notice': {'type': 'xpath', 'locator': "//p[@class='woocommerce-notice woocommerce-notice--success woocommerce-thankyou-order-received']"},
    'order_details_order': {'type': 'css selector', 'locator': 'ul.order_details li.order'},
    'order_details_date': {'type': 'css selector', 'locator': 'ul.order_details li.date'},
    'order_details_total': {'type': 'css selector', 'locator': 'ul.order_details li.total'},
    'order_details_method': {'type': 'css selector', 'locator': 'ul.order_details li.method'}
}