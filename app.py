from distutils.log import debug
from fileinput import filename
from flask import *  
app = Flask(__name__)  
  
@app.route('/')  
def main():  
    return render_template("homepage.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")
  
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename)  
        return render_template("acknowledgement.html", name = f.filename)  
  
if __name__ == '__main__':  
    app.run(debug=True)