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
- **Request:**
  ```json
  http://127.0.0.1:5000/books?q=mockingbird&page=1&per_page=5
  ```
- **Response:**
  ![image](https://github.com/user-attachments/assets/81ae8f71-3c3b-43a7-864d-176bfa988481)


#### 2. Add a New Book

- **URL:** `/books`
- **Method:** `POST`
- **Headers:**
  - `Authorization: secure-token`
- **Body:**
  ```json
  {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960,
    "genre": "Fiction"
  }
  ```
- **Response:**
  ![image](https://github.com/user-attachments/assets/182615b6-afcb-4cf4-8ef2-b9b0219164f9)


#### 3. Get, Update, or Delete a Specific Book

- **URL:** `/books/<book_id>`
- **Methods:** `GET`, `PUT`, `DELETE`
- **Headers:**
  - `Authorization: secure-token`
- **Response:**
  - `GET`: Book details.
    ![image](https://github.com/user-attachments/assets/e6580bf3-8cac-4da7-b88c-307207721f33)

  - `PUT`: Updated book details.
    ![image](https://github.com/user-attachments/assets/1be619d2-bf04-466f-a163-94a9f708de8f)

  - `DELETE`: Deletion confirmation.
    ![image](https://github.com/user-attachments/assets/f6cb9621-2522-482e-8c8c-3a5967c787a3)


### **Members**

#### 1. Get All Members

- **URL:** `/members`
- **Method:** `GET`
- **Headers:**
  - `Authorization: secure-token`
- **Response:**
  ![image](https://github.com/user-attachments/assets/104ebb1f-941b-4ecd-9c8a-7323e4b51ba6)

#### 2. Add a New Member

- **URL:** `/members`
- **Method:** `POST`
- **Headers:**
  - `Authorization: secure-token`
- **Body:**
  ```json
   {
      "name": "Alice Smith",
      "email": "alice@example.com",
      "phone": "9876543210"
  }
  ```
- **Response:**
  ![image](https://github.com/user-attachments/assets/abaeb123-61fb-47ed-96d6-67a16795923d)


#### 3. Get, Update, or Delete a Specific Member

- **URL:** `/members/<member_id>`
- **Methods:** `GET`, `PUT`, `DELETE`
- **Headers:**
  - `Authorization: secure-token`
- **Response:**
  - `GET`: Member details.
    ![image](https://github.com/user-attachments/assets/328766b1-3044-4f16-b17d-3dea7a1f778d)

  - `PUT`: Updated member details.
    ![image](https://github.com/user-attachments/assets/1cbafa19-30dc-4e95-acb8-f42f5aa8afad)

  - `DELETE`: Deletion confirmation.
    ![image](https://github.com/user-attachments/assets/4fdb7855-5de0-4aa4-9dd2-ad4616d9fc60)


---

## Authorization

The API requires an `Authorization` header with the value `secure-token`. We have added a token in the header named Authorization with the value of the field as mentioned in the code. This mocks authorization feature.

---

## Notes

- The `books` and `members` data are stored in memory and will reset when the application restarts.
- Modify the `TOKEN` variable in the code to change the API token.

---

## License

This project is open-source and available under the [MIT License](LICENSE).
