from flask import Flask,render_template,url_for,request
app=Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/contact')

def contact():
    return render_template('contact.html')

@app.route('/proj')

def proj():
    return render_template('proj.html')

@app.route('/skill')

def skill():
    return render_template('skill.html')

@app.route('/social')

def social():
    return render_template('social.html')

@app.route('/exp')

def exp():
    return render_template('exp.html')

@app.route('/edu')

def edu():
    return render_template('edu.html')

@app.route('/usercontact', methods=['GET','POST'])
def usercontact():
    if request.method=='POST':
       name= request.form["name"]
       email=request.form["email"]
       message=request.form['message']
       contact_detail=[name,email,message]
       return contact_detail 

if __name__=="__main__":
    app.run(debug=True)