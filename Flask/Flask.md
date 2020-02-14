
Flask is a Python-based microframework used for developing small scale websites.  
Flask is very easy to make Restful API’s using python. 


## 1. request 
#### react to the data a client sends to the server
1.1 method [attr]: current request method ('POST', 'GET')  
1.2 form [attr]: access form data (data transmitted in a POST or PUT request)  

```
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method was GET or the credentials were invalid
    return render_template('login.html', error=error)
```

## 2. response
If a response object of the correct type is returned it’s directly returned from the view.  
If it’s a string, a response object is created with that data and the default parameters.  
If it’s a dict, a response object is created using jsonify.  

## 3. APIs with JSON
#### can turn dict to json
```
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }
```

## 4. Variable Rules
#### add variable sections to a URL
```
<variable_name> 
<converter:variable_name>     converter: string/ int/ float/ path(also accepts slashes) /uuid
```

## 5. HTTP Methods
#### Web applications use different HTTP methods when accessing URLs.
You should familiarize yourself with the HTTP methods as you work with Flask.  
By default, a route only answers to GET requests. 
```
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

## 6. Static Files
#### deal with CSS and JavaScript files
Just create a folder called static in your package or next to your module  
```
url_for('static', filename='style.css')
```

## 7. Rendering Templates
#### Generating HTML from within Python 
folder structure: Flask will look for templates in the **templates folder**.  
So if your application is a **module**, this folder is **next to that module**,  
if it’s a **package** it’s actually **inside your package**
```
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```
