from flask import Flask,jsonify,request
import csv 
all_books=[]
with open('articles.csv',encoding="utf8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_books=data[1:]
liked=[]
disliked=[]
did_not_read=[]
app=Flask(__name__)

@app.route('/get-book')
def get_book():
    return jsonify({
        'data':all_books[0],
        'status':'success'
    })

@app.route('/liked-books',methods=['POST'])
def liked_book():
    book=all_books[0]
    all_books=all_books[1:]
    liked.append(book)
    return jsonify({
        'status':'success'
    })
@app.route('/disliked-books',methods=['POST'])
def disliked_book():
    book=all_books[0]
    all_books=all_books[1:]
    disliked.append(book)
    return jsonify({
        'status':'success'
    })
@app.route('/did-not-read-books',methods=['POST'])
def did_not_read_book():
    book=all_books[0]
    all_books=all_books[1:]
    did_not_read.append(book)
    return jsonify({
        'status':'success'
    })

@app.route("/popular-books")
def popular_books():
    book_data = []
    for book in output:
        _d = {
            "id": book[0],
            "authorRegion": book[9],
            "authorCountry": book[10] or "N/A",
            "contentType": book[11],
            "url": book[12],
            "title": book[13]
        }
        book_data.append(_d)
    return jsonify({
        "data": book_data,
        "status": "success"
    }), 200

@app.route("/recommended-books")
def recommended_books():
    all_recommended = []
    for liked_book in liked_books:
        output = get_recommendations(liked_book[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    book_data = []
    for recommended in all_recommended:
        _d = {
             "id": book[0],
            "authorRegion": book[9],
            "authorCountry": book[10] or "N/A",
            "contentType": book[11],
            "url": book[12],
            "title": book[13]
        }
        book_data.append(_d)
    return jsonify({
        "data": book_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()
