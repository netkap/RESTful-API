# Installation and run
Download this repo and **delete** db.sqlite(if present)

open terminal in the folder where app.py is located
(usually shift + right click -> open powershell for windows) and type :

    pip install -r requirements.txt

In the same or new powershell type **python** and press enter to open python  and type:

    from app import db
    db.create_all()
    exit()
    python app.py

![image](https://github.com/netkap/RESTful-API/assets/100796046/69ceff5c-12bd-4a23-a3f4-7d8dd7fde07f)


In your folder there will be a new file db.sqlite


![image](https://github.com/netkap/RESTful-API/assets/100796046/580b93c2-4344-48e4-8f94-aba314becaef)





# RESTful
Restful API for products.

Go to Localhost/apidocs for docmentation.
for example http://localhost:5000/apidocs/ or http://127.0.0.1:5000/apidocs/

![ex](https://github.com/netkap/RESTful/assets/100796046/69368ec6-a3e0-4c66-a696-c0e151beff0b)

This RESTful API runs **Flask** server , uses **SQLALCHEMY** as DataBase Toolkit also **Marshmallow** is used for object serialization and deserialization.
SWAGGER UI for API Documentation

**Further Scope**:

    Adding authentication

    Creating Docker images
    
    Set CI CD pipelines
    
    Deploying to web




