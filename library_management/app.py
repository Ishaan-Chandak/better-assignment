from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

books = []
members = []

TOKEN = "secure-token"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        print(token)
        if not token or token != TOKEN:
            return jsonify({"message": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route("/books", methods=["GET", "POST"])
@token_required
def handle_books():
    if request.method == "POST":
        book = request.json
        book["id"] = len(books) + 1
        for b in books:
            if b['title'] == book['title'] and b['author'] == book['author'] and b['year'] == book['year'] and b['genre'] == book['genre']:
                return "Book already exist", 202
        books.append(book)
        return jsonify(book), 201

    query = request.args.get("q", "").lower()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))
    
    filtered_books = []
    for book in books:
        if query in book["title"].lower() or query in book["author"].lower():
            filtered_books.append(book)

    paginated_books = filtered_books[(page-1)*per_page: page*per_page]
    
    return jsonify({"books": paginated_books, "total": len(filtered_books)}), 200

@app.route("/books/<int:book_id>", methods=["GET", "PUT", "DELETE"])
@token_required
def handle_book(book_id):
    book = None
    for b in books:
        if b["id"] == book_id:
            book = b
            break

    if not book:
        return jsonify({"message": "Book not found"}), 404

    if request.method == "GET":
        return jsonify(book), 200

    if request.method == "PUT":
        updated_data = request.json
        book.update(updated_data)
        return jsonify(book), 200

    if request.method == "DELETE":
        books.remove(book)
        return jsonify({"message": "Book deleted"}), 200

@app.route("/members", methods=["GET", "POST"])
@token_required
def handle_members():
    if request.method == "GET":
        return jsonify(members), 200

    if request.method == "POST":
        member = request.json
        for m in members:
            if m['name'] == member['name'] and m['email'] == member['email'] and m['phone'] == member['phone']:
                return "Member already exist", 202
        member["id"] = len(members) + 1
        members.append(member)
        return jsonify(member), 201


@app.route("/members/<int:member_id>", methods=["GET", "PUT", "DELETE"])
@token_required
def handle_member(member_id):
    member = None
    for m in members:
        if m["id"] == member_id:
            member = m
            break

    if not member:
        return jsonify({"message": "Member not found"}), 404

    if request.method == "GET":
        return jsonify(member), 200

    if request.method == "PUT":
        updated_data = request.json
        member.update(updated_data)
        return jsonify(member), 200

    if request.method == "DELETE":
        members.remove(member)
        return jsonify({"message": "Member deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)