from flask import Flask,render_template,request
import pickle

import pandas as pd

with open('app/model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/',methods= ['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else :
        married = request.form['married']
        credit_history  = request.form['credit_history']
        applicantincome = request.form['applicantincome']
        loanamount = request.form['loanamount']
        loan_amount_term = request.form['loan_amount_term']
        input_data  = [married ,
        credit_history ,
        applicantincome ,
        loanamount ,
        loan_amount_term ]
        # df = pd.DataFrame([input],columns= ['married','credit_history', 'applicantincome', 'loanamount','loan_amount_term'])
        # print(df)


        output = model.predict([input_data ])
        print(output)
        if output[0] == 1:
            message   ="You're loan is accepted"
            status = "green"
        else:
            message   ="You're loan is refused"
            status = "red "
        return render_template("index.html",status = status, message=message, married=married,credit_history=credit_history, 
                               applicantincome=applicantincome, loanamount =loanamount,loan_amount_term= loan_amount_term)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

