class Actions_page:
    def __init__(self, selenium):
        self.selenium = selenium

    # add a client
    def add_client(self, first_name, last_name, country, owner, email):
        try:
            self.selenium.write(first_name, 'id', 'firstName')
            self.selenium.write(last_name, 'id', 'lastName')
            self.selenium.write(country, 'id', 'country')
            self.selenium.write(owner, 'xpath', "//tr[@class='owner']//ancestor::th/input")
            self.selenium.write(email, 'id', 'email')
            self.selenium.click_element('class name', 'add-client-btn')
            self._pop_up()
        except:
            print('Couldn\'t add a client')

    # update a client
    def update_client(self, client_name, transfer_owner=None, email_type=None, sold=None):
        self.selenium.write(client_name, 'css selector', "input[list='names']")
        if transfer_owner:
            self.selenium.write(transfer_owner, 'css selector', "input[list='owner']")
            self.selenium.click_element('css selector', "input[value='Transfer']")
            self._pop_up()
        if email_type:
            self.selenium.write(email_type, 'css selector', "input[list='emailType']")
            self.selenium.click_element('css selector', "input[value='Send']")
            self._pop_up()
        if sold:
            self.selenium.click_element('css selector', "input[value='Sold']")
            self._pop_up()

    # validate pop-up
    def _pop_up(self):
        try:
            pop_up = self.selenium.text_from_element('xpath', "//div[contains(@class,'pop-up')]")
            if pop_up == 'update success'.upper():
                print(pop_up)
            else:
                print(pop_up)
            return pop_up
        except:
            print('Couldn\'t get the pop-up')


