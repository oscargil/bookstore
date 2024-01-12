# Bookstore Inventory Management System

## Overview

This project is a simple inventory management system for a bookstore, allowing the owner to add, delete, and track the quantity of books in stock. The system includes a Django REST framework API for managing books and a microservice (service-notifier) for handling notifications related to stock levels.

## Features

- **Add Books**: Add new books to the inventory with details such as title, author, isbn, price and quantity.

- **Update Books info**: Update the details of a book, including quantity to track the stock.

- **Delete Books**: Remove books from the inventory when they are sold out.

- **Notification Service**: Integrates with the `service-notifier` microservice to receive notifications when books are running out of stock.

## Technologies Used

- Django
- Django REST framework
- Docker
- Swagger (API documentation)

## Getting Started

### Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <your_project_directory>
    ```

2. Build and run Docker container:

    ```bash
    docker-compose up --build
    ```

3. Access Swagger documentation at [http://localhost:8000/swagger/](http://localhost:8000/swagger/)


