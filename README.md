### Python Version Python 3.10.7
### Create Virtual env
```python3 -m venv venv```

### Install Dependencies
```pip install -r requirements.txt```

### Database - API

start database
- run 
```docker-compose up -d```

start api
- run ```flask --app api run```

migrate csv
- ```curl --location --request POST 'localhost:5000/migrate'```

find query on database
- ```curl --location --request GET 'localhost:5000/mostRated?limit=1&genere=News&sort_by=rating_count_tot'```

### Application
in order to create json and csv files run 
- ```python app.py```