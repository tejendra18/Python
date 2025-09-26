#streamlit run calculator.py
#alternative: python -m streamlit run calcultor.py 
import streamlit as st

st.title("Simple Calculator")
# st.subheader("Perform basic arithmatic operations")
st.markdown("This is a simple calculator app built with Streamlit")

#Input fields for number
c1,c2 = st.columns(2)
fnum = c1.number_input("Enter the first number",value=0)
snum = c2.number_input("Enter the second number",value=0)

options=["Addition","Subtraction","Multiplication","Divivsion"]
choice= st.radio("select an operation",options)

button = st.button("Calculate")

result = 0
if button :
    if choice == "Addition":
        result=fnum + snum
    if choice == "Subtraction":
        result=fnum - snum
    if choice == "Multiplication":
        result=fnum * snum    
    if choice == "Divivsion":
        result=fnum / snum    
st.warning(f"Result is :{result}")


st.balloons()
st.snow()


 
