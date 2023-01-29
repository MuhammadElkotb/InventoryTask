# InventoryTask
Simple Inventory Web page using Django + MySQL + HTML/CSS + Javascript

# Requirments
  - Python 3.x
  - Django 
  - MySQL
  
# Prepare Database
  
  - At first we need to head over to inventory/inventory/settings.py module and look for global variable "DATABASES" 
    
    ![image](https://user-images.githubusercontent.com/67494587/214996720-484241c2-a057-40fc-bd57-e0463443b8f6.png)
    
        - You must change the 'YOUR PASSWORD' to be your password and 'YOUR USERNAME' to be your username
  
  - A Database should be created at first and it must be named "INVENTORY"
  - Run This SQL Script in MySQL shell or workbench
  
    ```create database INVENTORY;```
  
  **Won't Work if the database is not created or if the name is not "INVENTORY"** 

- After creating the database, head over to project directory 

  ```cd inventory```

  ```python manage.py makemigrations```

  ```python manage.py migrate```


# Running the server

  ```cd inventory```
  
  ```python manage.py runserver```
  
  
 ![image](https://user-images.githubusercontent.com/67494587/214997927-805c4bf5-e8fb-4e51-b40c-e81a4bd0413d.png)

  
