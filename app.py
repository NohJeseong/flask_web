from flask import Flask, render_template
from data import Articles
import pymysql

db_connection = pymysql.connect(
	user    = 'root',
        passwd  = '1234',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
    	charset = 'utf8'
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home',methods=['GET','POST'])
def index():
    name = "Noh Jeseong"
    return render_template('index.html',data=name)

@app.route('/articles',methods=['GET','POST'])
def articles():
    # list_data = Articles()
    cursor = db_connection.cursor()
    sql = 'SELECT * FROM list;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    return render_template('articles.html',data = topics)

# @app.route('/detail/<ids>')
# def detail(ids):
#     ids =int(ids)-1
#     list_data = Articles()
#     return render_template('detail.html',data = list_data[ids])

@app.route('/detail/<ids>')
def detail(ids):
    # list_data=Articles()
    cursor = db_connection.cursor()
    sql = f'SELECT * FROM list WHERE id={int(ids)};'
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    # for data in list_data:
    #     if data['id'] == int(ids):
    #         article = data
    return render_template('article.html',data = topic)

if __name__ == '__main__':
    app.run(debug=True)