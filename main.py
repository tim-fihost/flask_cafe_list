from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)



class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe's Location on Google's map",validators=[DataRequired(),URL()])
    opening = StringField('Open', validators=[DataRequired()])
    closing = StringField('Close',validators=[DataRequired()]) 
    coffee = SelectField('Coffee', choices=['✘','☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕']) 
    wifi = SelectField('Wifi', choices=['✘','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'] ) 
    power = SelectField('Power',choices=['✘',"🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        
        for row in csv_data:
            list_of_rows.append(row)
    
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/add', methods=['GET','POST'])
def add():
    cafe = CafeForm()
    cafe.validate_on_submit()
    with open('cafe-data.csv',mode='a', newline='',encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([cafe.cafe.data,
                         cafe.location.data,
                         cafe.opening.data,
                         cafe.closing.data,
                         cafe.coffee.data,
                         cafe.wifi.data,
                         cafe.power.data])
    return render_template('add.html',form = cafe)

if __name__ == '__main__':
    app.run(debug=True)


