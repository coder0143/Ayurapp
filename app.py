# df = {
#     "Medicines": [
#         {
#             "Name": None,
#             "Company": None,
#             "Year": None,
#             "Month": None,
#             "Pieces": None,
#             "MRP": None,
#         }
#     ]
# }

import streamlit as st 
import json 
import pandas as pd 

data = pd.read_csv("Data formatted.csv")

company_names = list(data["Company"].drop_duplicates())
medicine_names = list(data["Medicines"])
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
years = ['2024','2025','2026']

# Enter medcine name, month, year, get info
def show_med_data(med_name, month, year):
    with open('data.json','r') as f:
        df = json.load(f)
        for med in df['Medicines']:
            if med['Name'] == med_name and med['Month'] == month and med['Year'] == year:
                return med['Pieces'], med['MRP'], med['Company']

# Edit medicine pieces, mrp
def edit_med_data(med_name, company_name, month, year, new_pieces, new_mrp):
    with open('data.json','r') as read_file:
        df = json.load(read_file)
        for med in df['Medicines']:
            if med['Name'] == med_name and med['Company'] == company_name and med['Month'] == month and med['Year'] == year:
                med['Pieces'] = str(new_pieces)
                med['MRP'] = str(new_mrp)
        with open('data.json','w') as write_file:
            json.dump(df, write_file)

# Add new medicine
def add_new_med(med_name, company_name):
    new_row = pd.DataFrame({"Medicines": [med_name], "Company": [company_name]})
    data_mod = data._append(new_row, ignore_index=True)
    data_mod.to_csv("Data formatted.csv")
    with open('data.json','r') as read_file:
        df = json.load(read_file)
        for year in years:
            for month in months:
                df['Medicines'].append({
                    "Name": med_name,
                    "Company": company_name,
                    "Year": year,
                    "Month": month,
                    "Pieces": None,
                    "MRP": None
                })
        with open('data.json','w') as write_file:
            json.dump(df, write_file)
    
# Month end -> Generate report
# Generate report
    # Report generation: 
    # * Format: (Generate at month end)
    # Company name(Alphabetical) | Medicine | Stock | MRP | Amount 
    # Total : ()

# Month beginning -> update database


# Website
st.title(":blue[Medicine Database]")
st.markdown("## Password verification")
val = st.text_input("Enter password")
password = "abcd"
if val==password:
    # Medicine detatils
    st.markdown("## Get medicine details")
    med_name = st.selectbox("Medicine name", sorted(medicine_names))
    month = st.selectbox("Month",months)
    year = st.selectbox("Year", years)
    show = st.button("Submit")
    if show:
        pieces, mrp, company = show_med_data(med_name, month, year)
        st.write(f"Pieces: {pieces}")
        st.write(f"MRP: {mrp}")
        st.write(f"Company: {company}")

    # Edit medicine details
    st.markdown("## Edit medicine details")
    med_name_ed = st.selectbox("Medicine name ", medicine_names)
    company_name_ed = st.selectbox("Company name ", company_names)
    month_ed = st.selectbox("Month ",months)
    year_ed = st.selectbox("Year ", years)
    new_Pieces = st.number_input("Pieces ", step=1)
    new_MRP = st.number_input("MRP ", step=10)
    edit = st.button("Edit")
    if edit:
        edit_med_data(med_name_ed, company_name_ed, month_ed,year_ed,new_Pieces,new_MRP)

    # Add new medicine
    st.markdown("## Add new medicine")
    med_name_new = st.text_input("Medicine name  ")
    _ = st.selectbox("Check existing company names", company_names)
    company_name_new = st.text_input("Company name  ")
    add = st.button("Add")
    if add and (med_name_new not in medicine_names) and (company_name_new!=""):
        add_new_med(med_name_new, company_name_new)
        st.rerun()
    else:
        st.write("Medicine name already registered!")
    
    
