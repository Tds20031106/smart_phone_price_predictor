from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression


app = Flask(__name__)


@app.route('/')
def default():
    return render_template('index.html')
  
@app.route('/predict')
def predict():
    return render_template('predict.html')
  
@app.route('/p', methods=["POST"])
def p():
  brand = request.form.get('brand')
  fiveg = request.form.get('5g')
  rom = request.form.get('rom')
  ram = request.form.get('ram')
  days = request.form['days']
      
  
  url = 'https://raw.githubusercontent.com/mannikdeep/usedmobile/main/main_price.csv'
  main = pd.read_csv(url)
  x = main.loc[:,'device_brand':'days_used']
  y = main['price']
  model = LinearRegression()
  model.fit(x,y)
  
  try:
    res = model.predict([[eval(brand), eval(fiveg), eval(rom), eval(ram), eval(days)]])
    res = "Upto Rs. "+ str(round(res[0],2))
    return render_template('predict.html', data = res)
  except:
    return render_template('predict.html', data = "Please Enter Valid Values")

@app.route('/contact')
def contact():
  return render_template('contact.html')
  

if __name__ == '__main__':
  app.run(debug=True)