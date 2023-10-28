# FastAPI Todo Backend

A simple TODO backend built using FastAPI, SQLAlchemy, and Pydantic.

## Features

- Create, Retrieve, Update, and Delete (CRUD) operations for todos.
- Data validation using Pydantic.
- Asynchronous API endpoints.
- SQLite database integration using SQLAlchemy.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/caglarrkeskinn/TodoApp-FastApi
   cd TodoApp-FastApi
   ```

2. Setup a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

4. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server on `http://127.0.0.1:8000/`.

## Usage

The application provides the following endpoints:

- **POST /todos/**: Create a new todo.
- **GET /todos/**: List all todos with optional skip and limit parameters.
- **GET /todos/{todo_id}**: Retrieve a specific todo by ID.
- **DELETE /todos/{todo_id}**: Delete a specific todo by ID.
- **PUT /todos/{todo_id}**: Update a specific todo by ID.

You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Database

The backend uses an SQLite database by default, but this can be changed by updating the `DATABASE_URL` in `models.py`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
