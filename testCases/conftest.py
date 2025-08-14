from selenium import webdriver
import pytest


@pytest.fixture()    # fixture method return driver when call this fixture
# if you are using specific browser like chrome
# def setup():
#     driver=webdriver.Chrome()
#     return driver



# if you want to run in desired browser, code is here
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'Edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Ie()      # for default browser if no browser name pass at run time
    # driver.command_executor._client_config._timeout = 300
    driver.set_page_load_timeout(300)
    driver.set_script_timeout(300)

    return driver

def pytest_addoption(parser):     # this will get value from CLI/hooks (command line)
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):    # this will return the browser value to setup method
    return request.config.getoption("--browser")


##### to gerate Pytest HTML report ################

#
# # It is hook for adding environment info to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester']= 'Vintee'
#
# # It is hook for delete/modify environment info to HTML report
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA HOME", None)
#     metadata.pop("Plugins", None)


# def pytest_configure(config):
#     # Skip worker nodes (used by pytest-xdist)
#     if hasattr(config, 'workerinput'):
#         return  # Don't set metadata on worker processes
#
#     if hasattr(config, '_metadata'):
#         config._metadata['Project Name'] = 'nop commerce'
#         config._metadata['Module Name'] = 'Customers'
#         config._metadata['Tester'] = 'Vintee'
#
# # @pytest.hookimpl(optionalhook=True)
# # def pytest_metadata(metadata):
# #     metadata.pop("JAVA_HOME", None)
# #     metadata.pop("Plugins", None)


def pytest_configure(config):
    print(">>> pytest_configure executing")  # Debug print
    if hasattr(config, 'workerinput'):
        return
    if not hasattr(config, '_metadata'):
        config._metadata = {}

    config._metadata['Project Name'] = 'nopCommerce'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Vintee'
    config._metadata['Test Run'] = 'Daily Build'
    config._metadata['Extra Info'] = 'This is a test'
#

