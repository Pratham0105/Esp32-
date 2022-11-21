from flask import Flask, jsonify
app = Flask(__name__)

books_db=[
     {
        'name':'Secret',
        'price':275
    },
    {
        'name':'Doop Work',
        'price':300
    }
]

#retrive all the books
@app.route('/')
def home():
    return jsonify({'message':'welcome'})

@app.route('/on')
def on():
    return jsonify({'state':'1'})

@app.route('/off')
def off():
    return jsonify({'state':'0'})



if __name__=='__main__':
     app.run(debug=True)
