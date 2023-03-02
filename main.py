import pandas as pd
import streamlit as st
import dill

loaded_model = dill.load(open('model/trained_model.joblib', 'rb'))
columns = ['town', 'flat_type', 'storey_range', 'floor_area_sqm', 'flat_model', 'remaining_lease']
town_list = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
       'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
       'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
       'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
       'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
       'TOA PAYOH', 'WOODLANDS', 'YISHUN']
flat_type_list = ['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM',
       'MULTI-GENERATION']
storey_range_list = ['07 TO 09', '01 TO 03', '13 TO 15', '10 TO 12', '04 TO 06',
       '19 TO 21', '16 TO 18', '22 TO 24', '25 TO 27', '28 TO 30',
       '34 TO 36', '46 TO 48', '31 TO 33', '37 TO 39', '43 TO 45',
       '40 TO 42', '49 TO 51']
flat_model_list = ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
       'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2',
       'Type S1', 'Type S2', 'Adjoined flat', 'Terrace', 'DBSS',
       'Model A-Maisonette', 'Premium Maisonette', 'Multi Generation',
       'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen']

# Header
st.set_page_config(page_title="HDB Price Predictor", page_icon="👋")
st.title("Hello, welcome to HDB price predictor!")
st.subheader('Home Qualities')
st.write('''Input the qualities of your desired home.''')
# Form
with st.form("my_form"):
       town_choice = st.selectbox(label='Select your favourite Town', options=town_list)
       flat_type_choice = st.selectbox(label='Select your favourite flat type', options=flat_type_list)
       storey_range_choice = st.selectbox(label='Select which floor you want to stay at', options=storey_range_list)
       floor_area_sqm = st.number_input('Select desired Floor Area Sqm', min_value=0, step=1)
       flat_model_choice = st.selectbox(label='Select a HDB Model', options=flat_model_list)
       remaining_lease = st.number_input(label='Remaining lease of choice', min_value=0, max_value=99)

       submitted = st.form_submit_button("Submit")
       if submitted:
              X = [[town_choice, flat_type_choice, storey_range_choice, floor_area_sqm, flat_model_choice, remaining_lease]]
              df = pd.DataFrame(X, columns = columns)
              results = loaded_model.predict(df)
              if results:
                     results = f'${int(results)}'
                     st.metric("Your dream home would be priced at:", results)

