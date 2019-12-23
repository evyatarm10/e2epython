class Home_page:
    def __init__(self, selenium):
        self.selenium = selenium

    # navigate to home page and validate the url
    def navigate_to_homePage(self):
        try:
            self.selenium.getURL('https://lh-crm.herokuapp.com/')
            self.selenium.validateURL('lh-crm.herokuapp')
        except:
            print('Couldn\'t navigate to home page')

    # click on one of the options on the navigation button (clients, actions, analytics)
    def click_nav(self, nav):
        nav = nav.lower().capitalize()
        try:
            self.selenium.click_element('xpath', f"//input[@value='{nav}']")
            self.selenium.validateURL(nav[:-1])
        except:
            print('Couldn\'t click on navigation button')

    # close the browser
    def close(self):
        self.selenium.close()
