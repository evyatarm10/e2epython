from helper import base_page
from pages import home_page
from pages import client_page
from pages import actions_page
import allure


class Test_actions:
    def __init__(self):
        self.testSelenium = base_page.Base_page().selenium
        self.homePage = home_page.Home_page(self.testSelenium)
        self.actionPage = actions_page.Actions_page(self.testSelenium)
        self.clientPage = client_page.Clients_page(self.testSelenium)

    @allure.title('Test: Add client and validate')
    @allure.description('Add a new client with full or partial data and validate the pop-up correspondingly.'
                        ' Then validate if the client was added or not')
    @allure.severity(allure.severity_level.NORMAL)
    def add_client_and_validate(self, first_name=None, last_name=None, country=None, owner=None, email=None, data_input=None, search_by=None):
        self.homePage.navigate_to_homePage()
        self.homePage.click_nav('actions')
        self.actionPage.add_client(first_name, last_name, country, owner, email)
        self.homePage.click_nav('clients')
        validation = self.clientPage.search_and_validate(data_input, search_by)
        if validation == f'The {search_by} is the same for all clients':
            print(validation)
            assert True
        if validation == 'The client is not found':
            print(validation)
            assert True
        elif validation == f'The {search_by} is NOT the same for all clients':
            print(validation)
            assert False

    @allure.title('Test: Update an existing client')
    @allure.description('Insert client\'s name and update owner, email type and sold (all or partial update) and '
                        'validate the pop-up correspondingly')
    @allure.severity(allure.severity_level.NORMAL)
    def update_client(self, client_name=None, transfer_owner=None, email_type=None, sold=None):
        self.homePage.navigate_to_homePage()
        self.homePage.click_nav('actions')
        validation = self.actionPage.update_client(client_name, transfer_owner, email_type, sold)
        if validation == 'update successful'.upper():
            print(validation)
            assert True
        elif validation == 'some details are missing'.upper():
            print(validation)
            assert True


test = Test_actions()


# 1 #
@allure.feature('Add a new client')
@allure.description('Add a client with full data, check the pop up correspondingly and validate the client exists')
def test_actions_add():
    print(' -------------------- add client test -------------------- ')
    test.add_client_and_validate('Bobo', 'Bobolyla', 'BubuLand', 'Barton Ramirez', 'BuBu@yahoo.com', 'Bobo Bobolyla', 'Name')

# 2 #
@allure.feature('Add a new client')
@allure.description("Negative test: add a client with partial data and check the pop up correspondingly- "
                    "should return 'some details are missing', then validate that client doesn\'t exists")
def test_actions_add_negative():
    print(' -------------------- add client - negative test -------------------- ')
    test.add_client_and_validate('Biber Bob', None, None, None, None, 'Biber Bob', 'Name')


# 3 #
@allure.feature('Update client')
@allure.description('Update a client with valid data and check the pop up correspondingly')
def test_actions_update():
    print(' -------------------- update client test -------------------- ')
    test.update_client('Burger Jan', 'Janette Welder', None, None)


# 4 #
@allure.feature('Update client')
@allure.description("Negative test: update sold without a client\'s name and check the pop up correspondingly- should "
                    "return 'some details are missing'")
def test_actions_update_negative():
    print(' -------------------- update client - negative test -------------------- ')
    test.update_client(None, None, None, 'sold')
    test.homePage.close()

