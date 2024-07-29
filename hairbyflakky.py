import streamlit as st
import pandas as pd
import os
import base64

# Function to convert images to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Sample data for hairstyles and their corresponding image filenames
hairstyles = {
    "Braids": "braid.jpg",
    "Cornrows": "cornrows.jpg",
    "Box Braids": "box_braids.jpg",
    "Twists": "twists.jpg",
    "Weave": "weave.jpg",
    "Afro": "afro.jpg",
    "Locs": "locs.jpg",
    "Curls": "curl.jpg"
}

# Title of the app
st.title("HairByFlakky Salon Booking App")

# Display hairstyle images horizontally
st.header("Our Hairstyles")
image_folder = "images"

cols = st.columns(len(hairstyles))
for idx, (style, img) in enumerate(hairstyles.items()):
    img_path = os.path.join(image_folder, img)
    img_base64 = get_base64_image(img_path)
    cols[idx].image(f"data:image/jpeg;base64,{img_base64}", use_column_width=True)
    cols[idx].caption(style)

# Form for customer details
st.header("Book Your Favorite Hairstyle")

# Create a form for booking
with st.form(key='booking_form'):
    customer_name = st.text_input("Customer Name")
    phone_number = st.text_input("Phone Number")
    address = st.text_input("Address")
    hairstyle = st.selectbox("Choose Hairstyle", list(hairstyles.keys()))
    
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
