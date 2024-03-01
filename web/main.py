from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model_hosp = pickle.load(open('hosp_model.obj', 'rb'))
model_icu = pickle.load(open('icu_model.obj', 'rb'))
model_death = pickle.load(open("death_model.obj", "rb"))

age_groups = {
    '1': '0-9 years',
    '2': '10-19 years',
    '3': '20-29 years',
    '4': '30-39 years',
    '5': '40-49 years',
    '6': '50-59 years',
    '7': '60-69 years',
    '8': '70-79 years',
    '9': '85+ years'
}

gender_labels = {
    '0': "Female",
    '1': "Male"
}

confirmed_labels = {
    '0': "No",
    '1': "Yes"
}

condition_labels = {
    '0': "No",
    '1': "Yes"
}


def get_percentage(prediction):
    return str(round(prediction[0, 1] / (prediction[0, 0] + prediction[0, 1]) * 100, 4))[0:5]


@app.get('/')
def display_form():
    return render_template('covid_form.html')


@app.post('/result')
def process_form():
    gender = request.form['gender']
    condition = request.form['condition']
    age = request.form['age']
    lab_confirmed = request.form['confirmed']
    hosp_probability = model_hosp.predict_proba(pd.DataFrame(
        {"age_group": [int(age)], "medcond_yn": [int(condition)], "current_status": [int(lab_confirmed)],
         "sex": [int(gender)]}))
    icu_probability_1 = model_icu.predict_proba(
        pd.DataFrame({"age_group": [int(age)], "medcond_yn": [int(condition)], "current_status": [int(lab_confirmed)],
                      "sex": [int(gender)], "hosp_yn": [0]}))
    icu_probability_2 = model_icu.predict_proba(
        pd.DataFrame({"age_group": [int(age)], "medcond_yn": [int(condition)], "current_status": [int(lab_confirmed)],
                      "sex": [int(gender)], "hosp_yn": [1]}))
    death_probability_1 = model_death.predict_proba(
        pd.DataFrame({"age_group": [int(age)], "medcond_yn": [int(condition)], "current_status": [int(lab_confirmed)],
                      "sex": [int(gender)], "hosp_yn": [0], "icu_yn": [0]}))
    death_probability_2 = model_death.predict_proba(
        pd.DataFrame({"age_group": [int(age)], "medcond_yn": [int(condition)], "current_status": [int(lab_confirmed)],
                      "sex": [int(gender)], "hosp_yn": [1], "icu_yn": [0]}))
    death_probability_3 = model_death.predict_proba(
        pd.DataFrame({"age_group": [int(age)], "medcond_yn": [int(condition)], "current_status": [int(lab_confirmed)],
                      "sex": [int(gender)], "hosp_yn": [1], "icu_yn": [1]}))


    return render_template('result.html', age=age_groups[age], gender=gender_labels[gender],
                           condition=condition_labels[condition],
                           lab_confirmed=confirmed_labels[lab_confirmed],
                           hosp_probability=get_percentage(hosp_probability),
                           icu_probability_1=get_percentage(icu_probability_1),
                           icu_probability_2=get_percentage(icu_probability_2),
                           death_probability_1=get_percentage(death_probability_1),
                           death_probability_2=get_percentage(death_probability_2),
                           death_probability_3=get_percentage(death_probability_3))


if __name__ == '__main__':
    app.run(port=8000, debug=True)
