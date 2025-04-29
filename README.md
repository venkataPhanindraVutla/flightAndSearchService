# Flight And Search Service

## Overview

This service provides flight search functionality and is part of a larger microservices architecture.

## Related Services

This project is part of a larger microservices architecture. Each service in the ecosystem plays a crucial role in the overall functionality. Explore the related services:

### 🔗 [FlightsAndSearchService](https://github.com/venkataPhanindraVutla/flightAndSearchService)
### 🔗 [EmailReminderService](https://github.com/venkataPhanindraVutla/EmailReminderService)
### 🔗 [Auth_Service](https://github.com/venkataPhanindraVutla/Auth_Service)
### 🔗 [TicketBookingService](https://github.com/venkataPhanindraVutla/TicketBookingService)
### 🔗 [API_Gateway](https://github.com/venkataPhanindraVutla/API_Gateway)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/venkataPhanindraVutla/flightAndSearchService
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    ```

   Activate the virtual environment:

   - **On Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Configuration**:

    - Create a `.env` file in the root directory of the project.
    - Add the following environment variables to your `.env` file, replacing the placeholders with your actual database credentials:

      ```plaintext
      DB_HOST=your_local_host
      DB_PORT=3306
      DB_NAME=database
      DB_USER=your_username
      DB_PASSWORD=your_password
      ```

      **Note:** Ensure that these environment variables are correctly set, as the application relies on them to connect to your database.

## Running the Server

1. **Run the FastAPI server**:

    ```bash
    python -m uvicorn main:app --reload
    ```

2. **Access the API**:

   The server will start at `http://127.0.0.1:8000`. You can view the automatically generated interactive API docs at: `http://127.0.0.1:8000/docs`

## Database Design

- **Tables:**
    - Airplane
    - Flight
    - Airport
    - City

- **Relationships:**
    - A Flight belongs to an Airplane, but one airplane can be used in multiple flights.
    - A city has many airports, but an airport belongs to one city.
    - One airport can have many flights, but a flight belongs to one airport.

### Table Schemas

- **City:**
    - `id`, `name`, `created_at`, `updated_at`

- **Airport:**
    - `id`, `name`, `address`, `city_id`, `created_at`, `updated_at`
    - Relationship: City has many Airports, and Airport belongs to a City (one-to-many).

- **Airplane:**
    - `id`, `model_number`, `capacity`, `created_at`, `updated_at`

- **Flight:**
    - `id`, `flight_number`, `departure_airport_id`, `arrival_airport_id`, `airplane_id`, `departure_time`, `arrival_time`, `price`, `created_at`, `updated_at`
    - Relationships:
        - Flight belongs to one Airplane (one-to-many).
        - Flight belongs to one Departure Airport (one-to-many).
        - Flight belongs to one Arrival Airport (one-to-many).

## Service-Specific Configuration

- **Database Configuration**:
    - The service uses environment variables from the `.env` file for database configuration. Ensure the `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, and `DB_PASSWORD` variables are correctly set.

## Tech Stack

- **Python**: Programming language.
- **FastAPI**: Web framework.
- **Uvicorn**: ASGI server.
- **SQLAlchemy**: ORM for database interaction.
- **PostgreSQL/MySQL (or other SQL databases)**: Database system.
- **Pydantic**: Data validation and settings management.
- **python-dotenv**: Loading environment variables from `.env` files.