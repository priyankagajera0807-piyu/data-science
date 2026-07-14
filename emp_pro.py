import streamlit as st
import pandas as pd
import datetime
import os

# Page layout configurations
st.set_page_config(page_title="Employee Registry", page_icon="📝", layout="centered")

CSV_FILE = "employees.csv"

# Function to read data from CSV
def load_employee_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        # If the file does not exist, return an empty DataFrame with headers
        columns = ["Employee Name", "Designation", "DOB", "DOJ", "Gender", "Phone Number", "City"]
        return pd.DataFrame(columns=columns)

# Function to append details to the CSV file
def append_employee_to_csv(emp_dict):
    df = load_employee_data()
    new_row_df = pd.DataFrame([emp_dict])
    # Concatenate the new entry to the existing dataframe
    updated_df = pd.concat([df, new_row_df], ignore_index=True)
    updated_df.to_csv(CSV_FILE, index=False)

# Initialize Session State variables for Navigation and Storage
if "current_panel" not in st.session_state:
    st.session_state.current_panel = "registration"
if "latest_submission" not in st.session_state:
    st.session_state.latest_submission = {}

# --- PANEL 1: REGISTRATION FORM ---
if st.session_state.current_panel == "registration":
    st.title("📝 Employee Registration Form")
    st.write("Enter the employee details below to register and save them to the database.")
    st.write("---")
    
    with st.form("registration_form", clear_on_submit=True):
        name = st.text_input("1. Employee Name", placeholder="Enter full name")
        designation = st.text_input("2. Designation", placeholder="e.g. Systems Engineer")
        
        col1, col2 = st.columns(2)
        with col1:
            dob = st.date_input("3. Date of Birth (DOB)", min_value=datetime.date(1940, 1, 1))
        with col2:
            doj = st.date_input("4. Date of Joining (DOJ)")
            
        gender = st.radio("5. Gender", ["Male", "Female", "Other"], horizontal=True)
        phone = st.text_input("6. Phone Number", placeholder="e.g. +1 555-0199")
        city = st.text_input("7. City", placeholder="e.g. Chicago")
        
        # Form Submission Button
        submit_btn = st.form_submit_button("Submit Details")
        
        if submit_btn:
            # Field Validation
            if not name.strip() or not designation.strip() or not phone.strip() or not city.strip():
                st.error("⚠️ All fields are required! Please complete the form before submitting.")
            else:
                # Structure the data dict
                employee_record = {
                    "Employee Name": name.strip(),
                    "Designation": designation.strip(),
                    "DOB": dob.strftime("%Y-%m-%d"),
                    "DOJ": doj.strftime("%Y-%m-%d"),
                    "Gender": gender,
                    "Phone Number": phone.strip(),
                    "City": city.strip()
                }
                
                # 1. Save data directly to CSV file
                append_employee_to_csv(employee_record)
                
                # 2. Store latest entry to show on the next page
                st.session_state.latest_submission = employee_record
                
                # 3. Transition to viewing panel
                st.session_state.current_panel = "viewer"
                st.rerun()

# --- PANEL 2: DETAILS VIEWER & DATABASE ---
elif st.session_state.current_panel == "viewer":
    st.title("🖥️ Employee Profile Panel")
    st.success("🎉 Employee Registered and Saved to CSV Database Successfully!")
    st.write("---")
    
    # Grid split to show latest details card next to the full database summary
    col_details, col_db = st.columns([2, 3], gap="medium")
    
    with col_details:
        st.subheader("👤 Registered Details")
        latest = st.session_state.latest_submission
        
        with st.container(border=True):
            st.write(f"### {latest['Employee Name']}")
            st.caption(f"💼 {latest['Designation']}")
            st.write("---")
            st.write(f"📅 **DOB:** `{latest['DOB']}`")
            st.write(f"📆 **DOJ:** `{latest['DOJ']}`")
            st.write(f"⚧️ **Gender:** `{latest['Gender']}`")
            st.write(f"📞 **Phone:** `{latest['Phone Number']}`")
            st.write(f"📍 **City:** `{latest['City']}`")
            
        if st.button("🔄 Register Another", type="primary"):
            st.session_state.current_panel = "registration"
            st.session_state.latest_submission = {}
            st.rerun()
            
    with col_db:
        st.subheader("📁 CSV Records")
        # Load entire dataset from file
        df_all = load_employee_data()
        st.dataframe(df_all, use_container_width=True, hide_index=True)
        
        # Generate inline download button for the CSV file
        csv_download = df_all.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Updated CSV File",
            data=csv_download,
            file_name="employees.csv",
            mime="text/csv"
        )
