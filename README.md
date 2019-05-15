# Conference Contact Combo

Application gives two User Interfaces. One is responsible for managing Conference Room Reservations, second one handles Contact Box functionality.

* Conference Room Reservations:
  * add, remove, modify rooms.
  * add, remove reservations.
  * search for reservations.
* Contact Box:
  * add, remove, modify person.
  * add, remove:
    * phone number,
    * email address,
    * address,
    * group membership.
    
Project is supposed to test full CRUD design, User authentication (login, logout, registration, password reset). Tests, fixtures, custom commands are also in use.

## Getting Started

Application is available on heroku. Please feel free to test it there. If you want to download and test it locally please follow Installing guidelines.

### Installing

* Create local virtual environment. [docs](https://docs.python.org/3/tutorial/venv.html)

* Run virtual environment and use ```requirements.txt.``` file:

```
pip install -r requirements.txt
```
* Set up DB using ```settings.py```. You can find there postgres set up including database name. It needs to be created beforehand.

* In order to fill DB with fake data use:
  * Fixtures:
  ```python manage.py loaddata general/fixtures/general_fixture.json```
  
  * Dedicated commands:
  ```python manage.py update_contact_box``` and ```python manage.py update_conf_room```.

## Tests

Tests for views, models and forms. Python built in unittest used along with selenium for functional tests.
Please use:

* Test entire project: ```python manage.py test```
* Test conference rooms reservations only: ```python manage.py test conference_rooms_reservations```
* Test contact box only: ```python manage.py test contact_box```

## Built With

* Python
* Django
* Jquery
* HTML
* Bootstrap
* Postgres
* Selenium

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Author

Marcin Szyc
