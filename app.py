
from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://api.covid19india.org/state_district_wise.json')
    data = response.json()
    districts = []
    for area in data.keys(): 
        for district in data[area]['districtData'].keys():
            districts.append(district)

    return render_template("index.html", districts = districts)




@app.route("/select_district", methods=["POST"])
def select_district():
    district = request.form.get("district")
    response = requests.get('https://api.covid19india.org/state_district_wise.json')
    data = response.json()
    print(data)
   
    
    return render_template("selected_district.html", data = data)



# @app.route('/find-data')
# def find_data():
    
#     print (data)
#     return render_template('index.html' , data = data)


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')