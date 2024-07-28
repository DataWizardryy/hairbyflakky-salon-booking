import streamlit as st
import pandas as pd
import os

# Sample data for hairstyles
hairstyles = [
    "Braids", "Cornrows", "Box Braids", "Twists", "Weave", "Afro", "Locs", "Curls"
]

# Title of the app
st.title("HairByFlakky Salon Booking App")

# Form for customer details
st.header("Book Your Favorite Hairstyle")

# Create a form for booking
with st.form(key='booking_form'):
    customer_name = st.text_input("Customer Name")
    phone_number = st.text_input("Phone Number")
    address = st.text_input("Address")
    hairstyle = st.selectbox("Choose Hairstyle", hairstyles)
    
    # Submit button
    submit_button = st.form_submit_button(label='Book Appointment')

# Handle form submission
if submit_button:
    if customer_name and phone_number and address:
        # Collect the input data
        booking_info = {
            "Customer Name": customer_name,
            "Phone Number": phone_number,
            "Address": address,
            "Hairstyle": hairstyle
        }

        # Display a success message
        st.success(f"Thank you, {customer_name}! Your appointment for {hairstyle} has been booked.")
        
        # Display the booking details
        st.write("Booking Details:")
        st.json(booking_info)

        # Filepath for the booking data
        data_file = "bookings.csv"

        # Check if the file exists, if not create it with headers
        if not os.path.exists(data_file):
            df = pd.DataFrame(columns=["Customer Name", "Phone Number", "Address", "Hairstyle"])
            df.to_csv(data_file, index=False)

        # Load existing data
        df = pd.read_csv(data_file)

        # Add new booking to the DataFrame
        new_booking = pd.DataFrame([booking_info])
        df = pd.concat([df, new_booking], ignore_index=True)

        # Save back to CSV
        df.to_csv(data_file, index=False)
    else:
        st.error("Please fill in all the fields.")
