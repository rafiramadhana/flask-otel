from flask import Flask

app = Flask(__name__)

@app.get("/books")
def get_books():
    return {
        "books": [
            "Petualangan Sherina",
            "Tenggelamnya Kapal van der Wijck",
            "Surat Cinta Untuk Starla"
        ],
    }

@app.post("/books/purchase")
def purchase_book():
    return {
        "purchase_id": 1,
        "book_name": "Tenggelamnya Kapal van der Wijck",
    }
