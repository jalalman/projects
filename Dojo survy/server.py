from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/result",methods=['POST'])

def print_res():
    form_data = {
            'name': request.form.get('name'),
            'location': request.form.get('location'),
            'lang': request.form.get('lang'),
            'gender': request.form.get('Gender'),
            'jobs': request.form.getlist('jobs'),
            'text': request.form.get('comment')
        }
    return render_template("result.html",**form_data)

if __name__== "__main__":
    app.run(debug=True)