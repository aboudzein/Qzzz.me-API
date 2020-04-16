![enter image description here](http://tuzlaapp.com/images/logo-black.png)

## Qzzz.Me Core
Online learning tool made to help people practice and master whatever they are learning
Not Production ready Qzzz.me Backend Layer.
With collaborative efforts from  Tuzla For Smart App's ,

## Technology
Built using :
 - Django 2.2.6  LTS & Django RestAPI Framework
 - Smart Logging for Database, Requests 
 - Elastic Solutions (FileBeat, MetricBeat and HeartBeat) 
 - Support Celery & Rabbit MQ
 - Auth System ( JWT , Social Login)
 - Unit tests ( Fully Covered Tested Solution)
 - Swagger
 
 ### Description
 
## Application Structure

```
|____qzzz.me
| |____config
|____qzzz.me_app
| |____migrations
|____compose
|____publisher_subscriber
|____requirements
```
## Running the server locally

 * Clone this repo
 * Install python3.6
 * Intall dependencies:
> pip install -r requirements.txt
 * Run the server:
> python manage.py runserver
 * Install [docker compose](https://docs.docker.com/compose/install/)
 * Run docker:
> docker-compose build

> docker-compose up
 * To check the server, open `http://localhost:8000/`

## Contributors
* Abdurahman Zeineddin 
* Aaron Lee 
* Mohammad Daabes


## License

This project is licensed under the terms of the MIT license.

