import streamlit as st
from pages import home, search

# Streamlit app
def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ['Home', 'Search'], index=0)

    if selection == 'Home':
        home.home()
    elif selection == 'Search':
        search.search()

if __name__ == '__main__':
    main()

