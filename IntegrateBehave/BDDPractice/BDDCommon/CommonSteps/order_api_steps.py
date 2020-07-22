from behave import step
from BDDCommon.CommonDAO.ordersDAO import OrdersDAO


@step("I verify order is created in the database")
def i_verify_order_is_created_in_the_database(context):
    db_order = OrdersDAO().get_order_by_id(context.order_id)
    assert db_order, f"Order id {context.order_id} not found in database"
    assert db_order[0]['post_type'] == 'shop_order', f"order {context.order_id} does not have the correct type"

