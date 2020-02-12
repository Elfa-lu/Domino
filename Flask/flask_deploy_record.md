

```
C:\Users\elfa>d:
D:\>cd WashU
D:\WashU>mkdir Flask_test
D:\WashU>cd Flask_test

# make use of virtual environment
# folder venv is created (Include, Lib, Source)
D:\WashU\Flask_test>py -3 -m venv venv

# activate venv
D:\WashU\Flask_test>venv\Scripts\activate.bat

(venv) D:\WashU\Flask_test>pip install flask

# create folder templates, and put index.html into it
(venv) D:\WashU\Flask_test>mkdir templates

# put script.py into the project folder
# put model.pkl into the project folder

(venv) D:\WashU\Flask_test>set FLASK_APP=script.py
(venv) D:\WashU\Flask_test>run flask
 * Serving Flask app "script.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
 # open the URL and submit the form.
 # get the result in template/result.html
```
