# Library Management API

This is a Flask-based REST API for managing a library system. It supports managing books and members, with operations like adding, retrieving, updating, and deleting records. Authentication is required using a predefined token.

---

## Features

### Books

- Add new books.
- Fetch books with optional search and pagination.
- Get, update, or delete a specific book by ID.

### Members

- Add new members.
- Fetch all members.
- Get, update, or delete a specific member by ID.

### Authentication

All routes require an `Authorization` header with a valid token.

---

## Prerequisites

- Python 3.7+
- Flask installed

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Set up Virtual Environment

Create and activate a virtual environment:

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The application will start at `http://127.0.0.1:5000`.

---

## API Endpoints

### **Books**

#### 1. Get All Books (with optional search and pagination)

- **URL:** `/books`
- **Method:** `GET`
- **Headers:**
  - `Authorization: secure-token`
- **Query Parameters:**
  - `q` (optional): Search term.
  - `page` (default: 1): Page number.
  - `per_page` (default: 5): Number of books per page.
- **Response:**
  ```json
  {
    "books": [
      {
        "id": 1,
        "title": "Book Title",
        "author": "Author Name",
        "year": 2024,
        "genre": "Fiction"
      }
    ],
    "total": 1
  }
  ```

#### 2. Add a New Book

- **URL:** `/books`
- **Method:** `POST`
- **Headers:**
  - `Authorization: secure-token`
- **Body:**
  ```json
  {
    "title": "Book Title",
    "author": "Author Name",
    "year": 2024,
    "genre": "Fiction"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Book Title",
    "author": "Author Name",
    "year": 2024,
    "genre": "Fiction"
  }
  ```

#### 3. Get, Update, or Delete a Specific Book

- **URL:** `/books/<book_id>`
- **Methods:** `GET`, `PUT`, `DELETE`
- **Headers:**
  - `Authorization: secure-token`
- **Response:**
  - `GET`: Book details.
  - `PUT`: Updated book details.
  - `DELETE`: Deletion confirmation.

### **Members**

#### 1. Get All Members

- **URL:** `/members`
- **Method:** `GET`
- **Headers:**
  - `Authorization: secure-token`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Member Name",
      "email": "email@example.com",
      "phone": "1234567890"
    }
  ]
  ```

#### 2. Add a New Member

- **URL:** `/members`
- **Method:** `POST`
- **Headers:**
  - `Authorization: secure-token`
- **Body:**
  ```json
  {
    "name": "Member Name",
    "email": "email@example.com",
    "phone": "1234567890"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Member Name",
    "email": "email@example.com",
    "phone": "1234567890"
  }
  ```

#### 3. Get, Update, or Delete a Specific Member

- **URL:** `/members/<member_id>`
- **Methods:** `GET`, `PUT`, `DELETE`
- **Headers:**
  - `Authorization: secure-token`
- **Response:**
  - `GET`: Member details.
  - `PUT`: Updated member details.
  - `DELETE`: Deletion confirmation.

---

## Authorization

The API requires an `Authorization` header with the value `secure-token`.

Example:

```bash
curl -H "Authorization: secure-token" http://127.0.0.1:5000/books
```

---

## Notes

- The `books` and `members` data are stored in memory and will reset when the application restarts.
- Modify the `TOKEN` variable in the code to change the API token.

---

## License

This project is open-source and available under the [MIT License](LICENSE).
