# FastAPI Blog

- Develop a web application following the MVC design pattern.(Meaning 3 different Levels for Routing, Business Logic, DB calls for each call Functionality)
- Interface with a MySQL database using SQLAlchemy for ORM.
- Implement field validation and dependency injection as needed.
- Use Python and FastAPI for building the application.

## How Setup and Execution code

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Andrii-Bezkrovnyi/fastapi_blog.git
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    venv\Scripts\activate (on Windows) 
    source venv/bin/activate  (on Linux)
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```
4. **Add SECRET_KEY to the .env for JWT**

5. **Running a MySQL container via Docker**

    ```sh
     docker-compose up -d 
    ```
6. **Create new MySQL DB via Docker**

    ```sh
      docker exec -it lucid_dreams-mysql-1 mysql -u myuser -pmypassword -e "CREATE DATABASE mydatabase;"
    ```
7. **It can be also delete old MySQL DB and create new one via Docker**

    ```sh
      docker exec -it lucid_dreams-mysql-1 mysql -u myuser -pmypassword -e "DROP DATABASE mydatabase; CREATE DATABASE mydatabase;"
    ```
8. **Apply Migration**

    ```sh
      alembic upgrade head
    ```
9. **Start FastAPI application**

    ```sh
      uvicorn app.main:app --reload  
    ```
10. **Test the application in another console**
    
      ```sh
     venv\Scripts\activate (on Windows) 
     source venv/bin/activate  (on Linux)
     ```
      ```sh
     pytest tests/test_main.py -v
     ```

## Application Diagram
```
fastapi_blog/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── auth.py
│   │   └── posts.py
│   ├── auth_utils.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
│
├── tests/
│   ├── pytest.ini
│   ├── conftest.py
│   └── test_main.py
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│
├── alembic.ini
├── .env.dist
├── requirements.txt
└── Dockerfile
```