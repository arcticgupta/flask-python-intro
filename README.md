# flask-python-intro

Requisites:
1. python 2.7 or higher(recommended)

virtualenv is a virtual Python environment builder. It helps a user to create multiple Python environments side-by-side. Thereby, it can avoid compatibility issues between the different versions of the libraries.

We want to avoid inconsistencies and hence our project will be made inside a virtual environment.

Make a virtual environment:
1. ```sudo apt-get install virtualenv```
2. ```mkdir flask_project```
3. ```cd flask_project```
4. Copy contents of github project into the ```flask_project``` directory.
5. ```virtualenv exvenv``` to create the environment inside the ```flask_project``` directory.
6. ```source exvenv/bin/activate``` to start the virtul environment.

The Flask Structure:
First, you need to install flask systemwide
```
sudo apt-get install python3-pip python3-dev nginx
sudo pip3 install virtualenv
```
Inside the flask_intro github project you'll find
1. app.py - controller for the project
2. static - images and other static resource
3. templates - HTML and other resources that can be rendered

Run the project:
1. ```cd flask_intro``` to enter the project
2. ```python app.py``` to start the server
3. ```localhost:5000``` to request the server in the browser.

Consructing the ```app.py``` file:
```
 from flask import Flask, render_template, url_for, request, redirect
```
To import the packages we will need in the project


```
app= Flask(__name__)
```
Flask constructor takes the name of current module (__name__) as argument.

```
return render_template('page2.html')
```
render_template renders the mentioned resource from the ```templates``` directory
```
@app.route('<path>')
```
This header tells the application which URL should call the associated function

```
@app.route('/login', methods=['GET', 'POST'])
```
Here, we define the type of requests that can be assocaited with the function

```
if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)
```
A Flask application is started by calling the run() method. However, while the application is under development, it should be restarted manually for each change in the code. To avoid this inconvenience ```app.debug``` is set to ```True```.The server will then reload itself if the code changes. It will also provide a useful debugger to track the errors if any, in the application.




