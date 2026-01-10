# Import essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Lasso Regression model
filename = 'Batting-score-LassoReg-model.pkl'

# Fix for sklearn model version issues
with open(filename, 'rb') as f:
    regressor = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    temp_array = []

    if request.method == 'POST':
        # Batting team one-hot encoding
        batting_team = request.form['batting-team']
        teams = ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab',
                 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
                 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']
        temp_array += [1 if batting_team == team else 0 for team in teams]

        # Bowling team one-hot encoding
        bowling_team = request.form['bowling-team']
        temp_array += [1 if bowling_team == team else 0 for team in teams]

        # Venue one-hot encoding
        venues = ['M Chinnaswamy Stadium', 'Eden Gardens', 'Feroz Shah Kotla',
                  'MA Chidambaram Stadium, Chepauk', 'Punjab Cricket Association Stadium, Mohali',
                  'Wankhede Stadium', 'Sawai Mansingh Stadium', 'Rajiv Gandhi International Stadium, Uppal']
        venue = request.form['venue']
        temp_array += [1 if venue == v else 0 for v in venues]

        # Overs calculation: convert whole overs + balls to float
        overs_whole = int(request.form['overs_whole'])
        overs_balls = int(request.form['overs_balls'])
        overs = overs_whole + overs_balls / 6

        # Other numerical inputs
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])

        # Combine all features
        temp_array += [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

        # Convert to numpy array
        data = np.array([temp_array])

        # Prediction
        my_prediction = int(regressor.predict(data)[0])

        # Return result
        return render_template('result.html',
                               lower_limit=my_prediction - 10,
                               upper_limit=my_prediction + 5)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 5500)
