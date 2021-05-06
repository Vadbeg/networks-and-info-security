DROP TABLE IF EXISTS document_controller;
DROP TABLE IF EXISTS document_creator;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS "user";
DROP TABLE IF EXISTS document;


CREATE TABLE document (

    id SERIAL PRIMARY KEY,
    document_name VARCHAR(50),
    document_type VARCHAR(25),
    date_of_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_of_registration TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(25),
    second_name VARCHAR(25),
    is_internal BOOLEAN,
    position VARCHAR(25),
    email VARCHAR(50),
    phone_number VARCHAR(25)
);

CREATE TABLE app_user (
    id SERIAL PRIMARY KEY,
    email VARCHAR(50),
    password VARCHAR(256),
    access_token VARCHAR(256)
);

CREATE TABLE factory (
    id SERIAL PRIMARY KEY,
    factory_name VARCHAR(50),
    size INTEGER,
    city VARCHAR(50)
);


CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    task_name VARCHAR(50),

    executor_id INTEGER,  /* Only one executor for one task */
    document_id INTEGER,
    factory_id INTEGER,

    FOREIGN KEY (executor_id) REFERENCES "user" (id)
        ON DELETE CASCADE,
    FOREIGN KEY (document_id) REFERENCES document (id)
        ON DELETE CASCADE,
    FOREIGN KEY (factory_id) REFERENCES factory (id)
        ON DELETE CASCADE
);



CREATE TABLE document_creator (
    document_id INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,

    FOREIGN KEY (document_id) REFERENCES document (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (creator_id) REFERENCES "user" (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE document_controller (
    document_id INTEGER NOT NULL,
    controller_id INTEGER NOT NULL,

    FOREIGN KEY (document_id) REFERENCES document (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        FOREIGN KEY (controller_id) REFERENCES "user" (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
