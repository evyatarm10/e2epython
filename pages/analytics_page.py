class Analytics_page:
    def __init__(self, selenium):
        self.selenium = selenium

    # get employee sales
    def employee_sales_in_country(self, country, employee_name):
        # get the number of sales of an employee
        self.selenium.write(country, 'xpath', "//div[@class ='employees-sales-by-country-chart']//ancestor::select")
        employee_sales_str = self.selenium.text_from_element('xpath', f"//*[contains(@class,'recharts-pie-label-text')]//*[contains(text(),'{employee_name.title()}')]")
        employee_sales_spl = employee_sales_str.split(' ')
        num_sales = int(" ".join(employee_sales_spl[2:]))
        print(num_sales)
        return num_sales
