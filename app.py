from flask import *  
from extractor import crack
import json

app = Flask(__name__, static_url_path='/static')  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  

@app.route('/api', methods=['POST'])
def extract_data():
    if request.method == 'POST':
        string_data = request.data.decode('utf-8')
        # Parse string as JSON
        json_data = json.loads(string_data)
        image = json_data['image']
        result=crack(image)
        if result[-1] == 'X':
            result = result[:-1]
        data = {
            'output': result
        }
        return jsonify(data)
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        name=f.filename
        f.save("static/"+name)       
        result=crack(name)

        return render_template("success.html", name = name,result=result,ad="/static/"+name)  
  
if __name__ == '__main__':  
    app.run(debug = True, port=5050, threaded=True) 