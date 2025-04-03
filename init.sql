CREATE DATABASE fastapi_db;

CREATE USER fastapi_user WITH PASSWORD 'fastapi_password';

GRANT ALL PRIVILEGES ON DATABASE fastapi_db TO fastapi_user;
