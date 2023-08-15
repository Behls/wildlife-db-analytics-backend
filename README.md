#Backend Service

##pgAdmin 4 & PostgreSQL

This project uses a local host within the postgresql database ecosystem. It can be managed using pgAdmin. The following applications should be installed:
- [pgAdmin]()
- [postgresql]()

**Once installation begins, you will be asked to create a user/master login details and password. Note these down as they are needed to connect to the database**

-pgAdmin has built in psql tool support for running command line instructions incase the terminal on mac or cmd on windows doesnt recognise the psql command. 

**creating a new database**
1. Once pgadmin 4 is loaded, right click on the sidebar on the option PostgreSQL, select create, then databae.
2. In the dialogue pop up, call the database wildlife and set the owner to postgres.



**DB Script**
Run the following SQL Query:

```


```


##Project Installation

1. Clone the repository with the following command:
```
git clone https://github.com/Behls/wildlife-db-analytics-backend.git

```

2. Inside the folder is a file called `requirements.txt` which contains all the enviroment packages required for the project. To install them use the following command:
```
pip install requirements.txt

```

3. once installed used the following command to start the flask web server:
```
flask run

```

In the terminal you should have a link to the local host for the server. This serves as the base url for calling the endpoints.
```

 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

**Troubleshooting**
If there is an error with the ports being used and the server is unable to start, navigate to the `app.py` file and pass in a port paramater into the app.run function. _make sure it's an unused port value._ An example would be:

```

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port:8001)

```

##API Get Requests
- API endpoints can be called using postman with the servers local host as the base url attaching one of the following endpoints. 
An example GET request would be:

```
# url construction for postman -> baseurl/api/getSpecies/18
http://127.0.0.1:5000/api/getSpecies/18

```

**List of API endpoints**

| API Enpoints          | Responses     | Protocol      |
| --------------------- | ------------- | ------------- | 
| /api/species/:id      | Returns a json object of a species matching {:id}     | GET |
| /api/species/         | Returns a json object of all species                  | GET |
| /api/users/:id        | Returns a json object of a users matching {:id}       | GET |
| /api/users/           | Returns a json object of all users                    | GET |
| /api/donations/:id    | Returns a json object of a donations matching {:id}   | GET |
| /api/donations/       | Returns a json object of all donations                | GET |
| /api/patients/:id     | Returns a json object of a patient's matching {:id}   | GET |
| /api/patients/        | Returns a json object of all patients                 | GET |
| /api/treatments/:id   | Returns a json object of a treatments matching {:id}  | GET |
| /api/treatments/      | Returns a json object of all treatments               | GET |
| api/notes/:id         | Returns a json object of a notes matching {:id}       | GET |
| /api/notes/           | Returns a json object of all note                     | GET |
| /api/medicine/:id     | Returns a json object of a medicine matching {:id}    | GET |
| /api/medicine/        | Returns a json object of all medicine                 | GET |
