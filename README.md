# Manager_management_system

This is a simple Manager Management System API built using FastAPI. It provides basic CRUD (Create, Read, Update, Delete) operations for managing Employee information.

Features
Get all employee information
Get information for a specific employee by employee ID
Add new employee information
Modify existing employee information
Delete employee information
Table Schema
The employee data is stored in a table named emp with the following schema:

## Table Schema

| Column    | Data Type | Description                      |
|-----------|-----------|----------------------------------|
| id        | Integer   | Primary key, auto-incremented    |
| name      | String    | Employee name, nullable          |
| email     | String    | Employee email, nullable         |
| address   | String    | Employee address, nullable       |
| department| String    | Employee department, nullable    |
