import pandas as pd
import streamlit as st
import pickle

# Load the model
from PIL import Image


def tb(title):
    with open('models/tb_model.pkl', 'rb') as f:
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
            'Do you experience extreme and unexplained tiredness?',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var3 = 1
        elif option == "No":
            input_var3 = 0
        else:
            input_var3 = ""
        option = st.selectbox(
            'Have you had a productive cough lasting three weeks?:',
            ['', 'Yes', 'No'])
        if option == "Yes":
            input_var5 = 1
        elif option == "No":
            input_var5 = 0
        else:
            input_var5 = ""
        option = st.selectbox(
            'Do you experience recurring fever or profuse night sweats?',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var7 = 1
        elif option == "No":
            input_var7 = 0
        else:
            input_var7 = ""

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
            'Have you experienced sores in the mouth or any other part of the body?',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var4 = 1
        elif option == "No":
            input_var4 = 0
        else:
            input_var4 = ""

        option = st.selectbox(
            'Have you experienced significant and rapid weight loss?',
            ('', 'Yes', 'No'))
        if option == "Yes":
            input_var6 = 1
        elif option == "No":
            input_var6 = 0
        else:
            input_var6 = ""

    if st.button('Submit'):
        try:
            input_data = pd.DataFrame({
                'input_variable_1': [float(input_var1)],
                'input_variable_2': [input_var2],
                'input_variable_3': [input_var3],
                'input_variable_4': [input_var4],
                'input_variable_5': [input_var5],
                'input_variable_6': [input_var6],
                'input_variable_7': [input_var7]
                # ...
            })

            # Make a prediction using the loaded model
            prediction = model.predict(input_data)
            # Print the result
            if prediction == 1:
                st.write("Client is eligible for TB testing!")
            else:
                st.write("Client is not eligible for TB testing!")
            df = pd.read_csv("csv_files/tb screening results.csv")
            df_final = pd.concat([df, input_data])
            df_final.to_csv('csv_files/tb screening results.csv', index=False)

        except NameError as e:
            st.write("Please ensure all fields are filled")
        except ValueError as e:
            st.write("Please ensure all fields are filled!")
