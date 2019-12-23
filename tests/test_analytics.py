from helper import base_page
from pages import home_page
from pages import analytics_page
from pages import actions_page
import allure
import pytest


class Test_analytics:
    def __init__(self):
        self.testSelenium = base_page.Base_page().selenium
        self.homePage = home_page.Home_page(self.testSelenium)
        self.actionsPage = actions_page.Actions_page(self.testSelenium)
        self.analyticsPage = analytics_page.Analytics_page(self.testSelenium)

    @allure.title('Employee sales')
    @allure.description('Insert country and check for employee sales of a certain employee in that country, then add '
                        'a sale to that employee and validate if sales increased by 1')
    @allure.severity(allure.severity_level.NORMAL)
    def employee_sales_in_country(self, country, employee_name, client_name, transfer_owner=None, email_type=None,
                                  sold=None):
        self.homePage.navigate_to_homePage()
        self.homePage.click_nav('analytics')
        sales_before = self.analyticsPage.employee_sales_in_country(country, employee_name)
        self.homePage.click_nav('actions')
        self.actionsPage.update_client(client_name, transfer_owner, email_type, sold)
        self.homePage.click_nav('analytics')
        sales_after = self.analyticsPage.employee_sales_in_country(country, employee_name)
        if sales_after == sales_before + 1:
            print(f'Validation succeeded: the number of sales of {employee_name} increased by 1.'
                  f' It was {sales_before}, and after the change it is {sales_after}')
            assert True
        else:
            print(f'Validation failed: the number of sales of {employee_name} didn\'t increase by 1.'
                  f' It was' f' {sales_before} and after the change it is: {sales_after}.'
                  f' Make sure to verify 3 Pre-Requisites:\nClient\'s country is {country}; '
                  f'\nClient\'s owner is {employee_name}; \nClient\'s "Sold" is "NO"')
            assert False


test = Test_analytics()


@allure.feature('Employee sales in country')
@allure.description('search for number of sales of an employee, add a sale and validate sales increased by 1')
def test_employee_sales():
    test.employee_sales_in_country('France', 'barton ramirez', 'Gill Norris', None, None, 'sold')
    test.homePage.close()
