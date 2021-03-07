# Frontend-backend server

Project for business documentation handling. Is divided on two parts: 

1. postgres database
2. server
   
## How to start server

You can start app using `docker-compose`:

1. Build `docker-compose` containers:

    ```
    docker-compose -f docker-compose-front-back.yml build
    ```

2. Up `docker-compose` containers:

    ```
    docker-compose -f docker-compose-front-back.yml build
    ```

Now you have access to the app:
`http://0.0.0.0:9000/`

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [marshmallow](https://marshmallow.readthedocs.io/en/stable/) - For converting different non-python datatypes to python datatypes
* [PostgreSQL](https://www.postgresql.org) - Relational database management system used 


## Authors

* **Vadim Titko** aka *Vadbeg* - 
[LinkedIn](https://www.linkedin.com/in/vadtitko/) | 
[GitHub](https://github.com/Vadbeg/PythonHomework/commits?author=Vadbeg)