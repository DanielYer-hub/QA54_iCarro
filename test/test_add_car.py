import uuid

from models.car import Car
from pages.add_car_page import AddCarPage

def test_add_car_success(authenticated):
    add_car_page = AddCarPage(authenticated)

    registration_number = str(
        uuid.uuid4().int % 100000000
    ).zfill(8)

    car = Car(
        city="Haifa",
        make="Toyota",
        model="Corolla",
        year="2022",
        fuel="petrol",
        seats="5",
        car_class="Sedan",
        registration_number=registration_number,
        price="200"
    )

    add_car_page.open_add_car_page()
    add_car_page.fill_car_form(car)
    add_car_page.submit_car()