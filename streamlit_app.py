import pickle
from re import X
import streamlit as st
file = "laptop_pred.pkl"
md = pickle.load(open(file,'rb'))
def main():
        st.title("Laptop price prediction")
        st.write("check out this for refrence code [link](https://storage.googleapis.com/true-eye-360908.appspot.com/index.html)")
        Inches = st.text_input('Inches')
        Ram = st.text_input('Ram')
        Weight = st.text_input('Weight')
        CPU = st.text_input('CPU')
        COMPANY = st.text_input('COMPANY')
        MEMORY = st.text_input('MEMORY')
        GPU = st.text_input('GPU')
        if st.button('Predict'):
            prediction = md.predict([[Inches,Ram,Weight,CPU,COMPANY,MEMORY,GPU]])
            output = round(100*prediction[0])
            st.success("you can purchase laptop for {}".format(prediction))
if __name__=='__main__':
    main()