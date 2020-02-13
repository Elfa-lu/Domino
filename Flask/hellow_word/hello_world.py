from flask import Flask, jsonify

# create an instance of this class.
## use __name__ when it’s started as application
## imported as module, the name will be the actual import name
app = Flask(__name__)

# route(): tell Flask what URL should trigger the function
@app.route('/')
def index():
#    return '<h1>Hello World</h1>'

# it will return a http content. So if i want return a json format, then we can use jsonify package
    return jsonify({"about": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True)

# remote method
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8888, debug=True)

# Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
