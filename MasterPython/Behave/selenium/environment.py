from selenium import webdriver
import logging as logger
import time

# before_step(context, step), after_step(context, step) - # These run before and after every step. The step passed in is an instance of Step.
# before_scenario(context, scenario), after_scenario(context, scenario) # These run before and after each scenario is run. The scenario passed in is an instance of Scenario.
# before_feature(context, feature), after_feature(context, feature) # These run before and after each feature file is exercised. The feature passed in is an instance of Feature.
# before_tag(context, tag), after_tag(context, tag) # These run before and after a section tagged with the given name. They are invoked for each tag encountered in the order they’re found in the feature file. See Controlling Things With Tags. The tag passed in is an instance of Tag and because it’s a subclass of string you can do simple tests like:
# before_all(context), after_all(context)


# def after_scenario(context, scenario):
#     context.users_list = []
#     logger.info("scenario complete")


# def after_step(context, scenario):
#     time.sleep(10)
#     logger.info("step complete")


def after_all(context):
    logger.info("all scenarios complete")


# def after_scenario(context):
#      time.sleep(10)


def before_scenario(context, scenario):
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    context.driver = driver
    return driver


