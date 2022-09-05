from flask import Flask,jsonify,request
import csv 
all_articles=[]
with open('articles.csv',encoding="utf8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]
liked=[]
disliked=[]
did_not_read=[]
app=Flask(__name__)

@app.route('/get-article')
def get_article():
    return jsonify({
        'data':all_articles[0],
        'status':'success'
    })

@app.route('/liked-articles',methods=['POST'])
def liked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked.append(article)
    return jsonify({
        'status':'success'
    })
@app.route('/disliked-articles',methods=['POST'])
def disliked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    disliked.append(article)
    return jsonify({
        'status':'success'
    })
@app.route('/did-not-read-articles',methods=['POST'])
def did_not_read_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    did_not_read.append(article)
    return jsonify({
        'status':'success'
    })

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            "id": article[0],
            "authorRegion": article[9],
            "authorCountry": article[10] or "N/A",
            "contentType": article[11],
            "url": article[12],
            "title": article[13]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
             "id": article[0],
            "authorRegion": article[9],
            "authorCountry": article[10] or "N/A",
            "contentType": article[11],
            "url": article[12],
            "title": article[13]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()
