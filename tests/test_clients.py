from helper import base_page
from pages import home_page
from pages import client_page
import allure


class Test_client:
    def __init__(self):
        self.testSelenium = base_page.Base_page().selenium
        self.homePage = home_page.Home_page(self.testSelenium)
        self.clientPage = client_page.Clients_page(self.testSelenium)

    @allure.title('Test: Search and validate')
    @allure.description('Search client by specific data (Name/ Country/ Email/ Owner/ Sold/ Email Type) and validate'
                        'that the data was found matches the search')
    @allure.severity(allure.severity_level.NORMAL)
    def search_and_validate(self, data_input, search_by):
        self.homePage.navigate_to_homePage()
        self.homePage.click_nav('clients')
        validation = self.clientPage.search_and_validate(data_input, search_by)
        if validation == f'The {search_by} is the same for all clients':
            print(validation)
            assert True
        if validation == 'The client is not found':
            print(validation)
            assert True
        else:
            print(validation)
            assert False


test = Test_client()


@allure.feature('search')
@allure.description('search a client by valid or invalid data and validate the data is as expected')
def test_search_and_validate():
    test.search_and_validate('Bella Bellisima', 'Name')
    test.homePage.close()
