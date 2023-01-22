# Url-shortener-test-project
To run the project locally, please enter the next commands:
```
1. docker-compose -f docker-compose.local.yml up -d --build
2. docker exec url-shortener-test-project_web_1 python manage.py makemigrations 
3. docker exec url-shortener-test-project_web_1 python manage.py migrate
```
The database is being removed on each run of the container. 

Project has the following endpoints: 
1. http://127.0.0.1:8010/api/shorteners/: POST: it creates a shortened URL.
To create the short URl, you need to send the following JSON body:
```
{
  "target_url": "https://realpython.com",
  "expiry": "2023-04-22 08:53:20.683812+00"
}
```
The "expiry" field is not necessary, the default expiration period is 90 days. 
The "url" string in response body of this endpoint will be the address you need to use for redirect. For example, it could be TTYOY. 
2. http://127.0.0.1:8010/api/shortener/<url>/: GET: you can use it to get the full link behind the shortened url, and the expiration time of
your link. This is the example of the get request: 
http://127.0.0.1:8010/api/shortener/TTYOY/
3. http://127.0.0.1:8010/<url>/: GET - you need to use it for the redirect. Just enter this line with the shortened URL, for example:
http://127.0.0.1:8010/TTYOY/