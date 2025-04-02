# MUTUAL FUND APP REST API

This is a REST API built using FastAPI following the MVC (Model-View-Controller) pattern. It provides a robust and secure user management system, including features such as user registration, login, and JWT-based authentication for authorization. The API is designed to manage and integrate with a Mutual Fund API for fetching investment-related data.
The API follows modular URL routing, where each application or folder has its own specific URL setup, making it highly scalable and maintainable.   

## Features

- __User Registration:__ Allows users to create new accounts by providing basic credentials.
- __User Login & JWT Authentication:__ Secure user login with JWT token issuance for subsequent requests, ensuring safe and stateless communication.
- __Authorization:__ Ensures that protected routes require valid JWT tokens for access.
- __URL Routing:__ Modular URL routing based on app/folder structure, allowing easy management of different API components.
- __Mutual Fund API Integration:__ Seamless integration with an external mutual fund API to fetch real-time data and perform fund-related operations.
- __MVC Design Pattern:__ Separation of concerns using the MVC pattern, where Models manage the data, Views define the response structure, and Controllers handle the API logic.
- __Hourly Portfolio Update:__ User portfolio will be update hourly.

## Tech Stack

### Backend:
- Python
- FastAPI
- SQLlite
- JWT

### Data Storage:
- SQLlite

### User Authentication:
- JSON Web Tokens (JWT)

## API Reference

### User Authentication

- **POST** `/api/v1/users/register` - Register a new user.
- **POST** `/api/v1/users/login` - Login with an existing user.


### Funds (Bearer Token is required)

- **GET** `/api/v1/fund/fund-name` - Get all fund name for dropdown.
- **GET** `/api/v1/fund/open-scheme/mutual-fund?mutual_fund_family=selected_fund_name_from_dropdown Eg: mutual_fund_family=Aditya Birla Sun Life Mutual Fund` - Get all the open scheme funds of selected mutual_fund_family
- **POST** `/api/v1/fund/buy-fund` - Buy mutual fund.
- **GET** `/api/v1/fund/portfolio` - Get porfolio of the user who has logged in. 


## Installation

1. Clone the repository:
   ```sh
   https://github.com/Vina-y/mutual_fund.git
2. Install the requirements file:
    ```sh
   pip install -r requirements.txt
3. Set .env file :
    ```sh
   SECRET_KEY= set your own secret key
   DATABASE_URL = "sqlite://db.sqlite3"
   ALGORITHM = "HS256"
   RAPID_API_KEY = set ur own rapi api key by signinng in
   HOST = "latest-mutual-fund-nav.p.rapidapi.com"
4. Run project locally:
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
    
