# Backend Service

## pgAdmin 4 & PostgreSQL

This project uses a local host within the postgresql database ecosystem. It can be managed using pgAdmin. The following applications should be installed:
- [pgAdmin](https://www.pgadmin.org/download/)
- [postgresql](https://postgresapp.com/downloads.html)

**Once installation begins, you will be asked to create a user/master login details and password. Note these down as they are needed to connect to the database**

-pgAdmin has built in psql tool support for running command line instructions incase the terminal on mac or cmd on windows doesnt recognise the psql command. 

**creating a new database**
1. Once pgadmin 4 is loaded, right click on the sidebar on the option PostgreSQL, select create, then database.
2. In the dialogue pop up, call the database wildlife and set the owner to postgres.



**DB Script**
Run the following SQL Query:

```
CREATE TABLE public.donations (
    id bigint NOT NULL,
    type text,
    amount double precision,
    date text
);

ALTER TABLE public.donations ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.donations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999999999
    CACHE 1
);

CREATE TABLE public.medicine (
    id bigint NOT NULL,
    medication_name text,
    dosage double precision
);

ALTER TABLE public.medicine ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.medicine_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999999999
    CACHE 1
);

CREATE TABLE public.notes (
    id bigint NOT NULL,
    date_added date,
    note text,
    added_by bigint
);

CREATE TABLE public.patients (
    id bigint NOT NULL,
    name text,
    weight double precision,
    status text,
    admitted date,
    discharge text,
    firstname text,
    surname text,
    email text,
    address text,
    contact text,
    postcode text,
    city text,
    organisation text,
    rescue_note text,
    treatment bigint,
    species_id bigint
);

ALTER TABLE public.patients ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.patients_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999999
    CACHE 1
);

CREATE TABLE public.species (
    id bigint NOT NULL,
    name text,
    type text
);

ALTER TABLE public.species ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.species_species_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);

CREATE TABLE public.stuff (
    donation_id integer NOT NULL,
    donation_type character(255),
    donation_amount numeric(2,2),
    date_processed character(255)
);

CREATE TABLE public.treatments (
    id bigint NOT NULL,
    patient_id bigint,
    medication_id bigint,
    created_by bigint,
    note_id bigint,
    amended text,
    future_treatment text,
    current_treatment text
);

CREATE TABLE public.users (
    id bigint NOT NULL,
    usertype text,
    firstname text,
    surname text,
    email text,
    address text,
    password_hash text,
    contact text,
    organisation text,
    treatment_id bigint,
    notes_id bigint
);

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999
    CACHE 1
);

ALTER TABLE ONLY public.donations
    ADD CONSTRAINT donations_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.medicine
    ADD CONSTRAINT id UNIQUE (id);

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.species
    ADD CONSTRAINT species_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.stuff
    ADD CONSTRAINT stuff_pkey PRIMARY KEY (donation_id);

ALTER TABLE ONLY public.treatments
    ADD CONSTRAINT treatment_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.users
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);

CREATE INDEX fki_created_by ON public.treatments USING btree (created_by);

CREATE INDEX fki_medication_id ON public.treatments USING btree (medication_id);

CREATE INDEX fki_note_id ON public.treatments USING btree (note_id);

CREATE INDEX fki_notes_id ON public.users USING btree (notes_id);

CREATE INDEX fki_patient_id ON public.treatments USING btree (patient_id);

CREATE INDEX fki_species_id ON public.patients USING btree (species_id);

CREATE INDEX fki_treatment_id ON public.users USING btree (treatment_id);

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT added_by FOREIGN KEY (added_by) REFERENCES public.users(id) NOT VALID;

ALTER TABLE ONLY public.treatments
    ADD CONSTRAINT created_by FOREIGN KEY (created_by) REFERENCES public.users(id) NOT VALID;

ALTER TABLE ONLY public.treatments
    ADD CONSTRAINT medication_id FOREIGN KEY (medication_id) REFERENCES public.medicine(id) NOT VALID;

ALTER TABLE ONLY public.treatments
    ADD CONSTRAINT note_id FOREIGN KEY (note_id) REFERENCES public.notes(id) NOT VALID;

ALTER TABLE ONLY public.users
    ADD CONSTRAINT notes_id FOREIGN KEY (notes_id) REFERENCES public.notes(id) NOT VALID;

ALTER TABLE ONLY public.treatments
    ADD CONSTRAINT patient_id FOREIGN KEY (patient_id) REFERENCES public.patients(id) NOT VALID;

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT species_id FOREIGN KEY (species_id) REFERENCES public.species(id) NOT VALID;

ALTER TABLE ONLY public.users
    ADD CONSTRAINT treatment_id FOREIGN KEY (treatment_id) REFERENCES public.treatments(id) NOT VALID;

```


## Project Installation

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

## API Get Requests
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
