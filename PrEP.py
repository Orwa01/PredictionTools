import pandas as pd
import streamlit as st
import pickle

# Load the model
from PIL import Image


def prep(title):
    with open('models/prep_model.pkl', 'rb') as f:
        model = pickle.load(f)
    st.markdown(f"<h1 style='text-align: center; color: grey;'>FYJ {title} SCREENING TOOL</h1>", unsafe_allow_html=True)
    pepfar = Image.open('images/Pepfar-logo.png')
    nairobi = Image.open('images/Nairobi_City_Logo.png')
    kajiado = Image.open('images/kajiado logo.png')
    uon = Image.open('images/UoN Logo.jpg')
    usaid = Image.open('images/usaid logo.png')

    cols, cols1, cols2, cols3, cols4 = st.columns(5)
    with cols:
        st.image(pepfar)
    with cols1:
        st.image(usaid)
    with cols2:
        st.image(uon)

    with cols3:
        st.image(nairobi)
    with cols4:
        st.image(kajiado)

    # st.subheader('Please enter patient data ......')
    col1, col2, = st.columns(2)

    with col1:
        input_var1 = st.text_input('Age of client:')

        option = st.selectbox(
            'HIV status of your sexual partner:',
            ['', 'Positive', 'Negative', 'Unknown'])
        if option == "Positive":
            input_var5 = 1
        elif option == "Negative":
            input_var5 = 0
        elif option == "Unknown":
            input_var5 = 2
        else:
            input_var5 = ""
        option = st.selectbox(
            'Has client engaged in sex in exchange of money or other favors',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var7 = 1
        elif option == "No":
            input_var7 = 0
        else:
            input_var7 = ""
        option = st.selectbox(
            'Has client shared needles while engaging in intravenous drug use',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var9 = 1
        elif option == "No":
            input_var9 = 0
        else:
            input_var9 = ""
        option = st.selectbox(
            'Has client used Post Exposure Prophylaxis two times or more',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var11 = 1
        elif option == "No":
            input_var11 = 0
        else:
            input_var11 = ""
    with col2:
        option = st.selectbox(
            'Gender',
            ('', 'Male', 'Female'))
        if option == "Male":
            input_var2 = 1
        elif option == "No":
            input_var2 = 0
        else:
            input_var2 = ""
        option = st.selectbox(
            'HIV status of the client',
            ('', 'Positive', 'Negative', 'Unknown'))
        if option == "Positive":
            input_var4 = 1
        elif option == "Negative":
            input_var4 = 0
        elif option == "Unknown":
            input_var4 = 2
        else:
            input_var4 = ""

        option = st.selectbox(
            'Has client had sex without a condom or with a partner of unknown or positive HIVstatus',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var6 = 1
        elif option == "No":
            input_var6 = 0
        else:
            input_var6 = ""
        option = st.selectbox(
            'Has client had been diagnosed or treated for an STI',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var8 = 1
        elif option == "No":
            input_var8 = 0
        else:
            input_var8 = ""

        option = st.selectbox(
            'Has client had been forced to have sex against their will',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var10 = 1
        elif option == "No":
            input_var10 = 0
        else:
            input_var10 = ""
    if st.button('Submit'):
        try:
            input_data = pd.DataFrame({
                'input_variable_1': [float(input_var1)],
                'input_variable_2': [input_var2],
                'input_variable_4': [input_var4],
                'input_variable_5': [input_var5],
                'input_variable_6': [input_var6],
                'input_variable_7': [input_var7],
                'input_variable_8': [input_var8],
                'input_variable_9': [input_var9],
                'input_variable_10': [input_var10],
                'input_variable_11': [input_var11]
                # ...
            })

            # Make a prediction using the loaded model
            prediction = model.predict(input_data)
            # Print the result
            if prediction == 1:
                st.write("Client is eligible for PrEP!")
            else:
                st.write("Client is not eligible for PrEP!")
            df = pd.read_csv("csv_files/prep screening results.csv")
            df_final = pd.concat([df, input_data])
            df_final.to_csv('csv_files/prep screening results.csv', index=False)
        except NameError as e:
            st.write("Please ensure all fields are filled")
        except ValueError as e:
            st.write("Please ensure all fields are filled!")
