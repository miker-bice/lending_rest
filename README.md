# FastAPI lending_rest

A simple RESTful API made with python and powered by FastAPI. 

## Technologies Used
- Python 3.11
- FastAPI (Fast and robust RESTful API framework)
- SQLAlchemy (Object Relational Mapper)
- SQLite (SQL database)
- Pydantic (data validation)

## Installation
The first step is to clone this project to your local directory, either using **HTTPS**, **SSH** or **direct download**. Once you cloned the project we may proceed.
 
Before proceeding with running the application make sure you have Python **(version 3.11 recommended)** installed on your machine. If you do not have any python installed, download the installer from the [official website](https://www.python.org/downloads/).

Install the python installer, after installation, verify your python version by running this command on your terminal. This command should return the python version you just installed, ex **Python 3.11.2**

```bash
py -V
```

After installation, run this command, so that we can create virtual environments:

```bash
py -m pip install virtualenv
```

Once the virtualenv package is   installed, go to the directory where you cloned this application.

Make sure that you are now in the correct directory and now in your terminal, run the command below:
```bash
py -m virtual env
```
After running the command you should see a **venv** folder in your directory. Now we will activate the virtual environment using the command:
```bash
source venv/Scripts/activate
```
or in linux based systems:
```bash
source venv/bin/activate
```

To see if you have successfully activated your virtual environment, you must see a indicator **venv** or **virtualenv** in your terminal

After all those hoops, your project directory should look like:
```bash
-app/
---routers/
---__init__.py
---auth_utils.py
---config.py
---database.py
---main.py
---models.py
---schemas.py
---utils.py

-venv/  <--- this is the folder you just created
-.env
-gitignore
-sample_request.json
-sample_response.json
```

Okay, we can now start installing the required packages, execute this command to install all the required packages:
```bash
pip install fastapi['all'] sqlalchemy psycopg2
```

Once the packages are installed, we can now proceed in running the application using the **uvicorn** dev server. Run the command:
```bash
uvicorn app.main:app --reload
```
The app should start running, you will see these lines in your terminal:
```bash
INFO:     Will watch for changes in these directories: ['D:\\Temporary Files\\programming\\experiments\\lending_rest']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [17412] using WatchFiles
INFO:     Started server process [15800]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:63126 - "GET /loans/?limit=10 HTTP/1.1" 200 OK
INFO:     127.0.0.1:63131 - "POST /loans/ HTTP/1.1" 200 OK
INFO:     127.0.0.1:63131 - "POST /loans/ HTTP/1.1" 200 OK
INFO:     127.0.0.1:63131 - "GET /loans/?limit=10 HTTP/1.1" 200 OK
```

## Usage
In order to fully explore the REST API, we can use two different tools **postman** or the built-in **openAPI interactive docs** by FastAPI. For this tutorial we will use the interactive docs.

While the application is running, visit the URL **http://127.0.0.1:8000/docs** using your browser

The interactive docs should appear.

![image banner](https://github.com/miker-bice/lending_rest/blob/master/fastapi-docs.jpg?raw=true)

You can test out the application from this point. You can always refer to the [official documentation](https://fastapi.tiangolo.com/tutorial/first-steps/) of the FastAPI on how to use the interactive docs.

## Database
The application uses **SQLite** as its lightweight database. Once the app runs, a **lending-db.db** is automatically created within the directory of your project folder.

Don't worry, you can use other databases with the application, just replace the connection string in the **app/database.py**, use the one with the commented out for **postgresdb**

In other to explore the database file, you can use **DB browser for SQLite**, get the installer from its [official website](https://sqlitebrowser.org/dl/) 



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
