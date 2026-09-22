
import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

# Application title
st.title("🧮 Simple Calculator")
st.write("Select an operator and enter the required values.")

# Operator selection
operator = st.selectbox(
    "Select any operator:",
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)

# Addition
if operator == "Addition (+)":
    values = st.text_input(
        "Enter values separated by commas:",
        placeholder="10,20,30,40"
    )

    if st.button("Calculate Addition"):
        try:
            if values.strip() == "":
                st.warning("Please enter some numbers.")
            else:
                num_list = [
                    float(value.strip())
                    for value in values.split(",")
                ]

                result = sum(num_list)

                st.success(
                    f"Addition of all values = {result:g}"
                )

        except ValueError:
            st.error("Invalid input! Please enter numbers separated by commas.")

# Subtraction
elif operator == "Subtraction (-)":
    num1 = st.number_input(
        "Enter 1st Number:",
        value=0.0
    )

    num2 = st.number_input(
        "Enter 2nd Number:",
        value=0.0
    )

    if st.button("Calculate Subtraction"):
        result = num1 - num2

        st.success(
            f"Subtraction: {num1:g} - {num2:g} = {result:g}"
        )

# Multiplication
elif operator == "Multiplication (*)":
    values = st.text_input(
        "Enter values separated by commas:",
        placeholder="2,3,4"
    )

    if st.button("Calculate Multiplication"):
        try:
            if values.strip() == "":
                st.warning("Please enter some numbers.")
            else:
                num_list = [
                    float(value.strip())
                    for value in values.split(",")
                ]

                result = 1

                for number in num_list:
                    result = result * number

                st.success(
                    f"Multiplication of all values = {result:g}"
                )

        except ValueError:
            st.error("Invalid input! Please enter numbers separated by commas.")

# Division
elif operator == "Division (/)":
    num1 = st.number_input(
        "Enter 1st Number:",
        value=0.0
    )

    num2 = st.number_input(
        "Enter 2nd Number:",
        value=0.0
    )

    if st.button("Calculate Division"):
        if num2 != 0:
            result = num1 / num2

            st.success(
                f"You entered {num1:g} and {num2:g}. "
                f"After division, the total is = {result:.2f}"
            )
        else:
            st.error("You cannot divide by zero. Please try again.")

# Footer
st.divider()
st.caption("RDB Calculator | Built with Python and Streamlit")