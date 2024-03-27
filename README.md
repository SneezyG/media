# media
API development with django-ninja using celery for asynchronous task management


## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SneezyG/media
    ```

2. Navigate to the root directory:

    ```bash
    cd media
    ```

3. Install dependencies:

    ```bash
    poetry install
    ```
    
4. Add .env file at the root directory with following variable:
     
    ```bash
    secret = "your secret"
    dbname = "your postgres database name"
    dbhost = "your postgres database host"
    dbport = "your postgres database port"
    dbuser = "your postgres database user"
    dbpass = "your postgres database password"
    redis = "your redis url"
    ```


## Usage

1. Navigate to the project directory:

    ```bash
    cd media
    ```

2. Start the neccessary services(redis, postgress and celery:

    ```bash
    redis-server
    service postgresql start
    poetry run python -m celery -A media worker -l info --logfile=celery.log --detach
    poetry run python -m celery -A media beat -l info --logfile=celery.beat.log --detach
    ```

3. Start the development server:

    ```bash
    poetry run python manage.py runserver
    ```

4. Open your web browser and navigate to [http://127.0.0.1:8000/api/docs](http://localhost:8000) to view the project.


