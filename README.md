# media
API development with django-ninja using celery for asynchronous task management


## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Answer](#answer)


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




## Answer
1. For content-based recommendation, I'd look at what movies users like and recommend similar ones based on their features like genre, actors, and plot. For collaborative filtering, I'd see what other users with similar tastes liked and suggest those movies. For databases, I'd use something like MySQL for storing user preferences and MongoDB for movie metadata, 'cause they're good for handling different types of data and querying them efficiently.

2. For Postgres, performance can be optimized by creating indexes on frequently queried columns, using proper data types, and tuning configuration parameters like shared_buffers and work_mem. For Neo4j, creating efficient graph structures and using indexes can fasten node and relationship retrieval, and optimize Cypher queries. For Qdrant, performance can be optimized by tuning similarity search parameters, precomputing embeddings where possible, and using appropriate indexing techniques.

3. Celery is a tool we can use with Django to do tasks that may take a while in the background. It's good for making sure our app stays responsive. And for reliability, Celery has a retry feature built-in, so if a task fails, it can try again later. And for fault tolerance, Celery has this thing called "task queues" which line up the tasks so if one fails, it doesn't mess up everything else.


