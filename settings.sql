DROP DATABASE IF EXISTS allcity;
CREATE DATABASE allcity;
CREATE USER allcityuser WITH PASSWORD 'allcity';
GRANT ALL PRIVILEGES ON DATABASE allcity TO allcityuser;