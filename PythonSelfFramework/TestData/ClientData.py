from pageObjects.DisposableEmailPage import DisposableEmailPage


class ClientData:
    def __init__(self, driver):
        self.driver = driver

    def getData(self):
        self.driver.execute_script("window.open('about:blank','disposable_email');")
        self.driver.switch_to.window("disposable_email")
        self.driver.get("https://www.disposablemail.com/")

        emailInbox = DisposableEmailPage(self.driver)
        email_Address = emailInbox.store_email().text
        first_name_last_name = email_Address.split(".")
        first_Name = first_name_last_name[0].capitalize()
        parsedLastname = first_name_last_name[1].split("@")
        last_Name = parsedLastname[0].capitalize()

        firstName = first_Name
        lastName = last_Name
        email = email_Address
        test_HomePage_data = dict(firstname=firstName, lastname=lastName, emailAddress=email, ssn="123456789",
                                  creditCardNumber="4111111111111111",cvv="123")
        return test_HomePage_data



