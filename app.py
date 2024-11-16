# import streamlit as st
# import pathlib
# # File to store user credentials
# USER_FILE = "users.txt"

# page_bg_image = """
# <style>
# [data-testid=""stAppViewContainer]{
# background-color:" #40E0D0";
# opacity: 0.8;
# background: repeating-linear-gradient(to right, #000000, #40E0D0);
# }

# """
# st.markdown(page_bg_image,unsafe_allow_html=True)
# # Save user data to a file
# def save_user_data(username, password, email):
#     with open(USER_FILE, "a") as file:
#         file.write(f"{username},{password},{email}\n")

# # Check if user credentials are correct
# def check_user_credentials(username, password):
#     try:
#         with open(USER_FILE, "r") as file:
#             users = file.readlines()
#         for user in users:
#             stored_username, stored_password, _ = user.strip().split(",")
#             if stored_username == username and stored_password == password:
#                 return True
#         return False
#     except FileNotFoundError:
#         return False

# # Signup page
# def signup():
#     st.subheader("Please fill in the details below to create a new account.")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     email = st.text_input("Email")
    
#     if st.button("Sign Up"):
#         if username and password and email:
#             save_user_data(username, password, email)
#             st.success("User registered successfully!")
#         else:
#             st.error("Please fill in all fields.")

# # Login page
# def login():
#     st.subheader("Enter your credentials to log in.")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     if st.button("Login"):
#         if check_user_credentials(username, password):
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.rerun()  # Refresh the page to show the home page after login
#         else:
#             st.error("Incorrect username or password.")

# # Home page after login
# def home():
#     st.title("Welcome to ChatSphere!")
#     st.write(f"Hi, {st.session_state.username}! Welcome to the ChatSphere!")
    
#     if st.button("Sign Out"):
#         st.session_state.logged_in = False
#         st.session_state.username = None
#         st.rerun()  # Refresh the page to log out

# # Main function to control page flow
# def main():
#     if 'logged_in' not in st.session_state:
#         st.session_state.logged_in = False
    
    
#     if not st.session_state.logged_in:
#         st.title("Welcome to ChatSphere!")
#         st.write("Please login or register to continue.")
    
#     # If logged in, show the home page, otherwise show login/signup forms
#     if st.session_state.logged_in:
#         home()  # Show home page
#     else:
#         # Selectbox for login or signup (visible only when logged out)
#         action = st.selectbox("Choose an option", ["Login", "Sign Up"])

#         if action == "Sign Up":
#             signup()
#         elif action == "Login":
#             login()

# if __name__ == "__main__":
#     main()
import streamlit as st
import pathlib

# File to store user credentials
USER_FILE = "users.txt"

# Set the background gradient and text styles
page_bg_image = """
<style>
[data-testid="stAppViewContainer"]{
    background-color: #40E0D0;
    background: linear-gradient(to right, #4A90E2, #50C878); /* Soft Blue to Mint Green Gradient */
    opacity: 0.9;
}

h1 {
    color: white !important;
}

h3 {
    color: white !important;
}

# .stTextInput, .stTextArea {
#     background-color: white;
#     color: black;
#     # border-radius: 1px;
# }

.stButton button {
    background-color: #008CBA;
    color: white;
    border-radius: 5px;
}

.stTextInput input, .stTextArea textarea {
    color: black;
}
</style>
"""
st.markdown(page_bg_image, unsafe_allow_html=True)

# Save user data to a file
def save_user_data(username, password, email):
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password},{email}\n")

# Check if user credentials are correct
def check_user_credentials(username, password):
    try:
        with open(USER_FILE, "r") as file:
            users = file.readlines()
        for user in users:
            stored_username, stored_password, _ = user.strip().split(",")
            if stored_username == username and stored_password == password:
                return True
        return False
    except FileNotFoundError:
        return False

# Signup page
def signup():
    st.subheader("Please fill in the details below to create a new account.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    
    if st.button("Sign Up"):
        if username and password and email:
            save_user_data(username, password, email)
            st.success("User registered successfully!")
        else:
            st.error("Please fill in all fields.")

# Login page
def login():
    st.subheader("Enter your credentials to log in.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if check_user_credentials(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()  # Refresh the page to show the home page after login
        else:
            st.error("Incorrect username or password.")

# Home page after login
def home():
    st.title("Welcome to ChatSphere!")
    st.write(f"Hi, {st.session_state.username}! Welcome to the ChatSphere!")
    
    if st.button("Sign Out"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()  # Refresh the page to log out

# Main function to control page flow
def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        st.title("Welcome to ChatSphere!")
        st.write("Please login or register to continue.")
    
    # If logged in, show the home page, otherwise show login/signup forms
    if st.session_state.logged_in:
        home()  # Show home page
    else:
        # Selectbox for login or signup (visible only when logged out)
        action = st.selectbox("Choose an option", ["Login", "Sign Up"])

        if action == "Sign Up":
            signup()
        elif action == "Login":
            login()

if __name__ == "__main__":
    main()
