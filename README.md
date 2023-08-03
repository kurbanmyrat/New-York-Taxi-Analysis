# New York Taxi Spending Analysis

## Problem definition
Predict the average money spent on taxi rides for each region of New York per given day and hour.

This problem is a supervised regression problem. Supervised because we have the actual value of the value we’re trying to predict and regression because what we’re trying to predict is a continuous variable.

## Data cleaning
Negative total_amount values: removed them since they are likely faulty data points and there weren’t many of them.
Zero values for total_amount: Zero values are removed.
I decided to remove data points with a total_amount value higher than 200. Because, the average taxi_fare was ~$16 and there were only 1166 data points higher than $200.

## Feature engineering
I’ve added 3 sets of new features to the model. First set is time-based feature. These include, weekend and holiday boolean.

Second set is location-based information. We have Location IDs per region but there is a higher level abstraction for regions called Boroughs.

The last set is weather related data.

Here is a list of all features used in the final model: ['PULocationID', 'transaction_month', 'transaction_day', 'transaction_hour', 'transaction_week_day', 'weekend', 'is_holiday', 'Borough’, 'temperature', 'humidity', 'wind speed', 'cloud cover', 'amount of precipitation’, ‘total_amount’]

## Further steps

As you can see, the performance can be improved. These ways that wasn’t tried in this notebook:

limiting the regions included in this analysis. Removing the regions that do not normally get a lot of taxi traffic can be omitted. This might be a good action to take depending on the problem at hand. (If the goal is to service all of NYC no matter what, we should keep those data points)

hand selecting borough that should be included in the model. Again this should be decided based on the problem at hand and how this model is going to be used. But if the goal is solely to increase model performance, only including boroughs with the most transactions can increase the performance since likely most mistakes come from boroughs with fewer data points. Though this assumption should be checked before taking this action.


## Web Application

I have deployed the model on web application that I built with streamlit.

1.Firstly, to run the program, you need to cd into the folder that contains the files
>$ cd ../nyc_taxi_app.py

2.Enter on terminal to make a prediction through the trained model.
>streamlit run nyc_taxi_app.py 
to make a prediction through the trained model.

