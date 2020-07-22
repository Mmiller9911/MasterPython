behave --no-capture --no-logcapture --tags=my_products_smoke --no-skipped -f allure_behave.formatter:AllureFormatter -o my_allure_out
allure serve my_allure_out