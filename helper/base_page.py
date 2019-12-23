from Infrastructure import seleniumInfra


class Base_page:
    def __init__(self):
        self.selenium = seleniumInfra.Selenium_infra()
