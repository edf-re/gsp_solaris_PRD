import streamlit as st

def main():

    with open('README.md', 'r') as f:
        text = f.read()

    st.markdown(text)

if __name__ == "__main__":
    main()