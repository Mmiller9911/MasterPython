from behave import step
from BDDCommon.CommonDAO.productsDAO import ProductsDAO
from BDDCommon.CommonAPI import products_api
import pdb
import logging as logger


@step("I get the number of Available products from the database")
def i_get_number_of_available_products_from_db(context):
    database_rows = ProductsDAO().get_all_products_from_db()
    print("")
    print("Number of products in database is {}".format(len(database_rows)))
    context.qty_products_db = len(database_rows)


@step("I get the number of Available products from the API")
def i_get_number_of_available_products_from_api(context):
    list_of_products = products_api.list_all_products()
    number_of_products_in_api = len(list_of_products)
    print("Number of products in the API is {}".format(number_of_products_in_api))
    context.qty_products_api = number_of_products_in_api


@step("the number of products should match")
def the_number_of_products_in_db_and_api_match(context):
    assert context.qty_products_api == context.qty_products_db, "Numbers do not match" \
                                                                "DB quantity {}, API quantity {}" \
                                                                .format(context.qty_products_db, context.qty_products_api)


@step("I get {qty} random product from the database")
def i_get_random_product_or_products_from_database(context, qty):
    context.random_products = ProductsDAO().get_random_products_from_db(qty)


@step("I verify the product API returns the correct product by id")
def i_verify_product_api_returns_correct_product_by_id(context):
    #pdb.set_trace()
    logger.info("")
    logger.info("This is an INFO logging message")
    logger.warning("This is a WARNING logging message")
    product_id = context.random_products[0]['ID']
    response_get_product = products_api.get_product_by_id(product_id)

    assert response_get_product['id'] == product_id, "Product ids do not match"
    assert response_get_product['name'] == context.random_products[0]['post_title'], \
        "Wrong product name when calling 'get product by product id'. Api: {}, DB: {}".format(
            response_get_product['name'], context.random_products[0]['post_title'])


@step("I get the number of Available products from the API and the DATABASE")
def i_get_products_from_api_and_db(context):
    context.execute_steps(
        u"""
        Given I get the number of Available products from the database
        When I get the number of Available products from the API
        """
    )