from flask import Flask, Blueprint, jsonify, request
import myapp
from ..models.book import Book

books = []
book_blueprint = Blueprint('book_blueprint', __name__)

@book_blueprint.route('/book', methods=['POST'])
def add_book():
    new_book = request.get_json()
    title = new_book.get('title')
    author = new_book.get('author')
    user_id = new_book.get('user_id')

    if title and author and user_id:
        id = len(books) + 1
        new_book_obj = Book(id, title, author, user_id)
        books.append(vars(new_book_obj))
        return jsonify({'id': id, 'title': title, 'author': author, 'user_id': user_id}), 201
    else:
        return jsonify({'error': 'Title, Author or User ID is missing'}), 400

@book_blueprint.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

@book_blueprint.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password