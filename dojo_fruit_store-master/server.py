from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    form_data={
        'straw':request.form.get('strawberry'),
        'rasp':request.form.get('raspberry'),
        'apple':request.form.get('apple'),
        'Fname':request.form.get('first_name'),
        'Lname':request.form.get('last_name'),
        'Sid':request.form.get('student_id')
    }
    print (f"Charging {form_data['Fname']} {form_data['Lname']} for {int(form_data['apple'])+int(form_data['rasp'])+int(form_data['straw'])}")
    print(request.form)
    return render_template("checkout.html",**form_data)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)