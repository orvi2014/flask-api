# Flask-api

Make sure that you have installed 
`python=3.8`
`pip3=30.0.2`
`virtualenv`

First, you need to create a virtual enivortionment in your system.
`python3 -m venv venv`

After that, you have to activate the environment by using
`source venv/bin/activate`

the venv name showed in front of the directory now.

Now clone the flask application `git clone https://github.com/orvi2014/flask-api`
Go to the directory using `cd flask-api`
Now install the dependencies `pip3 install -r requirements.txt`
Finally run the server `python3 main.py`

If everything is okay the server will run at `http://localhost:5000`

To run it forever in EC@ linux `screen python3 main.py`

Now  let's hit the api endpoint where you can extract the information of csv file.

Api endpoint: `{{BaseUrl}}/info`
Method: Get
req.query: 
```
rowsize = 5
item= '{'industries': 'Education', 'assets': 'banner ads', 'languages': 'English', 'professions': 'writer', 'skills':'', 'skills_andor': 'Strategy'}'
```

it will show 

```
{"schema":
{"fields":[
{"name":"index","type":"integer"},
{"name":"id","type":"integer"},
{"name":"firstname","type":"string"},
{"name":"lastname","type":"string"},
{"name":"email","type":"string"},
{"name":"country-2","type":"string"},
{"name":"Total Score","type":"string"},
{"name":"start_date","type":"string"},
{"name":"end_date","type":"string"},
{"name":"is_available","type":"string"},
{"name":"avail","type":"string"}],
"primaryKey":["index"],"pandas_version":"1.4.0"},
"data":[{
"index":0,
"id":1,
"firstname":"Alex",
"lastname":"Lim",
"email":"alex.lim@hotmail.com",
"country-2":"SG",
"Total Score":"20","start_date":"",
"end_date":"",
"is_available":"TRUE",
"avail":"14"},
{"index":1,
"id":2,
"firstname":"Sarah",
"lastname":"Lee",
"email":"sarah.lee@hotmail.com",
"country-2":"SG",
"Total Score":"17.66666667",
"start_date":"2020-11-28",
"end_date":"",
"is_available":"TRUE",
"avail":"14"},
{"index":2,
"id":3,
"firstname":"Felicia",
"lastname":"Lee",
"email":"felicia.lee@gmail.com",
"country-2":"SG",
"Total Score":"23",
"start_date":"2020-12-01",
"end_date":"",
"is_available":"TRUE",
"avail":"14"},
{"index":3,
"id":4,
"firstname":"Ubent",
"lastname":"Zhao",
"email":"ubent.zhao@gmai.com",
"country-2":"UK",
"Total Score":"25",
"start_date":"",
"end_date":"",
"is_available":"TRUE",
"avail":"14"},
{
"index":4,
"id":5,
"firstname":"Edwina",
"lastname":"Yeo",
"email":"edwina.yeo@gmail.com",
"country-2":"SG",
"Total Score":"8",
"start_date":"2021-01-01",
"end_date":"",
"is_available":"TRUE",
"avail":"14"}]
}
```
