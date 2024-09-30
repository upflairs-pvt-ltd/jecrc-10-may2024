from flask import Flask,render_template ,url_for ,request
import joblib 
import pandas as pd 
df = pd.read_csv('models\label_data.csv')
std_scaler = joblib.load('models\std_scaler.lb')
model = joblib.load('models\kmeans.lb')

app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000/
def home():
    return render_template('homepage.html')

@app.route('/inputdata')  # http://127.0.0.1:5000/inputdata 
def inputdata():
    return render_template('input.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        # data = request.form 
        # print(data)
        # return data 

        N = int(request.form['N'])
        P = int(request.form['P'])
        h = int(request.form['h'])
        k = int(request.form['k'])
        ph = int(request.form['ph'])
        r = int(request.form['r'])
        t = int(request.form['t'])

# N	P	K	temperature	humidity	ph	rainfall
        unseen_data = [[N,P,k,t,h,ph,r]] 
        transformed_data = std_scaler.transform(unseen_data)
        cluster_no = model.predict(transformed_data)[0]
        filter_cluster_data = df[df['cluster_no'] == cluster_no]
        crops = list(filter_cluster_data['label'].unique())
        return render_template('output.html',suggested_crops=crops)  

if __name__ == "__main__": 
    app.run(debug=True)
 