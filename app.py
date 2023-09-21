from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
        {

        'id': 1,
        'title': 'Data Analyst',
        'location': 'Chattanooga, Tennessee',
        'salary': '$60,000-$80,000'    
    },
    {
        'id': 2,
        'title': 'Site Reliability Engineer',
        'location': 'Remote, USA',
        'salary': '$70,000-$90,000'
    },
    {
        'id':3,
        'title': 'Frontend Engineer',
        'location': 'Remote, USA',
        'salary': '$80,000-$100,000'
    },
    {
        'id':4,
        'title': 'Backend Engineer',
        'location': 'Nashville, Tennessee',
        'salary': '$80,000-$100,000'
    }

]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)