
import streamlit as st

def app():
    st.title("Find the Largest Number")
    
    # Add input boxes for the numbers
    number1 = st.number_input("Enter the first number:",step=1,value=None)
    number2 = st.number_input("Enter the second number:",step=1,value=None)
    number3 = st.number_input("Enter the third number:",step=1,value=None)

    # Add a button to calculate the largest number
    if st.button("Find the Largest Number"):
        # Calculate the largest number
        largest_number = max(number1, number2, number3)
        # Display the result
        st.write("The largest number is:", largest_number)

app()
