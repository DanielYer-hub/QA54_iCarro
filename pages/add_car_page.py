from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select


class AddCarPage:
    ADD_CAR_LINK = (By.CSS_SELECTOR, "a[href='/let-car-work']")
    CITY_INPUT = (By.ID, "city")
    MAKE_INPUT = (By.NAME, "manufacture")
    MODEL_INPUT = (By.NAME, "model")
    YEAR_INPUT = (By.NAME, "year")
    FUEL_SELECT = (By.NAME, "fuel")
    SEATS_INPUT = (By.NAME, "seats")
    CAR_CLASS_INPUT = (By.NAME, "carClass")
    REGISTRATION_NUMBER_INPUT = (By.NAME, "serialNumber")
    PRICE_INPUT = (By.NAME, "pricePerDay")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open_add_car_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_CAR_LINK)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CITY_INPUT)
        )

    def fill_field(self, locator, value):
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(str(value))

    def fill_city(self, city):
        self.fill_field(self.CITY_INPUT, city)

    def fill_make(self, make):
        self.fill_field(self.MAKE_INPUT, make)

    def fill_model(self, model):
        self.fill_field(self.MODEL_INPUT, model)

    def fill_year(self, year):
        self.fill_field(self.YEAR_INPUT, year)

    def select_fuel(self, fuel):
        dropdown = Select(
            self.driver.find_element(*self.FUEL_SELECT)
        )
        dropdown.select_by_value(fuel)

    def fill_seats(self, seats):
        self.fill_field(self.SEATS_INPUT, seats)

    def fill_car_class(self, car_class):
        self.fill_field(self.CAR_CLASS_INPUT, car_class)

    def fill_registration_number(self, registration_number):
        self.fill_field(
            self.REGISTRATION_NUMBER_INPUT,
            registration_number
        )

    def fill_price(self, price):
        self.fill_field(self.PRICE_INPUT, price)

    def fill_car_form(self, car):
        self.fill_city(car.city)
        self.fill_make(car.make)
        self.fill_model(car.model)
        self.fill_year(car.year)
        self.select_fuel(car.fuel)
        self.fill_seats(car.seats)
        self.fill_car_class(car.car_class)
        self.fill_registration_number(car.registration_number)
        self.fill_price(car.price)

    def submit_car(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        button.click()