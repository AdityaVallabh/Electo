# Electo
Django-based Election Portal

## Instructions

- Clone the repository

    ```bash
    git clone https://github.com/AdityaVallabh/Electo.git
    ```

- A [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) is preferred. Here's how you can install `virtualenv` and activate it in on a Windows OS:

    ```cmd
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate
    ```

- Install the requirements

    ```cmd
    cd Electo
    pip install -r requirements.txt
    ```
- Get the files ready
  - Copy the following files into [/data](/data) folder in the given CSV format:
    - [voterlist.csv](/data/voterlist.csv)
    - [posts.csv](/data/posts.csv)
    - [nominees.csv](/data/nominees.csv)
    - [house.csv](/data/house.csv)
  - Copy the symbols of the contestants as `Full Name.jpg` in [/static/symbols](/static/symbols) folder

- Create and populate the database

    ```cmd
    python manage.py migrate
    python manage.py load
    ```

- Create a superuser/admin for the site

    ```cmd
    python manage.py createsuperuser
    ```

- Run the application

    ```cmd
    python manage.py runserver 0.0.0.0:80
    ```

Your Election Portal is now up and running!
