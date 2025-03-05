import streamlit as st
import datetime
import requests
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
user_pickup_datetime = st.date_input('What is your pickup datetime ?')
user_pickup_longitude = st.number_input('What is your pickup longitude (between -74.3 and -73.7) ?')
user_pickup_latitude = st.number_input('What is your pickup latitude (between 40.5 and 40.9) ?')
user_dropoff_longitude = st.number_input('What is your dropoff longitude (between -74.3 and -73.7) ?')
user_dropoff_latitude = st.number_input('What is your dropoff latitude (between 40.5 and 40.9) ?')
user_passenger_count = st.number_input('How many passengers (max : 8) ?')

params = {
    'pickup_datetime' : user_pickup_datetime.strftime('%Y-%m-%dT%H:%M'),
    # 'pickup_datetime' : pd.Timestamp("2013-07-06 17:18:00", tz='UTC'),
    'pickup_longitude' : user_pickup_longitude,
    'pickup_latitude' : user_pickup_latitude,
    'dropoff_longitude' : user_dropoff_longitude,
    'dropoff_latitude' : user_dropoff_latitude,
    'passenger_count' : int(user_passenger_count)
    }


# params_ok = {'pickup_datetime':datetime.strftime('%Y-%m-%dT%H:%M')
#     # pd.Timestamp("2013-07-06 17:18:00", tz='UTC'),
#              'pickup_longitude':-73.950655,
#              'pickup_latitude':40.783282,
#              'dropoff_longitude':-73.984365,
#              'dropoff_latitude':40.769802,
#              'passenger_count':1,
#              }

# st.write(requests.get(url, params_ok).json())

response = requests.get(url, params=params)

if st.button('prediction ?'):
    # print is visible in the server output, not in the page
    print('prediction asked!')
    st.write('prediction is', response.json())
else:
    st.write('I was not clicked 😞')
