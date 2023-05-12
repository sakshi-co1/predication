from flask import Flask, render_template, request, url_for
import pickle
from flask.templating import Environment
import sklearn
app = Flask(__name__)

# model = pickle.load(('model/model_pickle','rb'))
prediction = ""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-report')
def prediction():
    return render_template('prediction.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/prediction', methods=['GET','POST'])

def predict():
    if request.method == 'POST':
        
        with open('./model/model_pickle','rb') as f:
            model = pickle.load(f)
        # model("Malaise,Swelled Lymph Nodes,Phlegm")
        # hb = int(request.form['hb'])
        # mcv = int(request.form['MCV'])
        # mchc = int(request.form['MCHC'])

        prediction = model("Malaise,Swelled Lymph Nodes,Phlegm")

#         if prediction[0]=='Microcytic':
#             diet_plan = '''Microcytic anemia: Increase intake of iron-rich foods such as lean red meat, poultry, fish, beans, lentils, tofu, and dark green leafy vegetables like spinach and kale.
# Include foods that are high in vitamin C such as citrus fruits, strawberries, and kiwi to help your body better absorb iron.
# Avoid drinking tea or coffee with meals as they can inhibit the absorption of iron.
# Consider taking an iron supplement as recommended by your doctor.'''
#         elif prediction[0] == 'Macrocytic':
#             diet_plan = '''Macrocytic anemia: Increase intake of foods rich in vitamin B12 such as lean meat, fish, poultry, dairy products, and fortified breakfast cereals.
# Include more folate-rich foods like dark green leafy vegetables, citrus fruits, and fortified breakfast cereals.'''
#         else:
#             diet_plan = '''Normocytic anemia: Eat a balanced and varied diet that includes lean protein, whole grains, fruits, and vegetables.
# Include foods that are rich in iron, vitamin B12, and folate to support healthy red blood cell production.
# Limit processed foods and sweets, which can be low in nutrients and contribute to inflammation.'''

        return render_template('prediction.html',prediction_text=prediction)
    return render_template('prediction.html')

if __name__=='__main__':
    app.run(debug=True)

