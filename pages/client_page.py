import time


class Clients_page:
    def __init__(self, selenium):
        self.selenium = selenium

    flag = True

    # search client by specific data in the search field and validate that the found item is what was searched
    def search_and_validate(self, data_input, search_by):
        try:
            time.sleep(2)

            # insert valid data in the searched fields
            self.selenium.clear_element_field('xpath', "//input[@type='text']")
            self.selenium.write(data_input, 'xpath', "//input[@type='text']")
            self.selenium.write(search_by, 'xpath', "//select[@class='select-css']")

            # get the number of pages
            pages = self.selenium.text_from_element('xpath', "//div[@class='page-numbers']")
            page = pages.split()
            first_page = page[0]
            last_page = page[2]

            # check if the client exists
            is_exists = self.selenium.element_is_exists('xpath', "//tr[@class = 'clientDetails']")
            if not is_exists:
                return 'The client is not found'

            # if there's more than one page, check within all pages
            all_pages = range(int(first_page), int(last_page) + 1)
            for i in all_pages:
                flag = True
                # print page
                print(f'{i}/{last_page}')
                # get the list of all clients
                client_details = self.selenium.find_elementList_by('xpath', "//tr[@class='clientDetails']")

                # get all details in a list of each client
                for client in client_details:
                    details = self.selenium.text_from_element('xpath', "//tr[@class='clientDetails']", client)
                    all_details = details.split()

                # extract the following from the list and check if it is as searched:
                    # full name
                    if search_by.capitalize() == 'Name':
                        joined_name = ' '.join(all_details[:2])
                        if data_input != joined_name:
                            flag = False
                            print(joined_name)
                    # country
                    elif search_by.capitalize() == 'Country':
                        joined_country = ' '.join(all_details[2:3])
                        if data_input != joined_country:
                            flag = False
                            print(joined_country)
                    # email
                    elif search_by.capitalize() == 'Email':
                        joined_email = ' '.join(all_details[3:4])
                        if data_input != joined_email:
                            flag = False
                            print(joined_email)
                    # owner
                    elif search_by.capitalize() == 'Owner':
                        joined_owner = ' '.join(all_details[4:6])
                        if data_input != joined_owner:
                            flag = False
                            print(joined_owner)
                    # sold
                    elif search_by.capitalize() == 'Sold':
                        joined_sold = ' '.join(all_details[6:7])
                        if data_input.upper() != joined_sold:
                            flag = False
                            print(joined_sold)
                    # email-type
                    elif search_by.title() == 'Email Type':
                        joined_emailType = ' '.join(all_details[8:])
                        if data_input.upper() != joined_emailType:
                            flag = False
                            print(joined_emailType)

                if i < int(last_page):
                    self.selenium.click_element('xpath', "//img[@name='next']")

                # validate all data matches
                if not flag:
                    return f'The {search_by} is NOT the same for all clients'
                else:
                    return f'The {search_by} is the same for all clients'
        except:
            print(f'Couldn\'t get all details from client')
