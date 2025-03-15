import streamlit as st

def main():
    st.title("Simple Calculator")
    st.write("Enter two numbers and choose an operation") 

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)

    operation = st.selectbox("Choose an operation!", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (*)":
                result = num1 * num2
                symbol = "*"
            elif operation == "Division (/)":
                if num2 != 0:
                    result = num1 / num2
                    symbol = "/"
                else:
                    st.error("Division by zero is not allowed.")
                    return
            st.success(f"The result of {num1} {symbol} {num2} is {result}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
