# Importing Streamlit
import streamlit as st
# Setting up web page
st.set_page_config(
    page_title="Python Unit Convertor",
    page_icon="logo.png"
)
# Categories Unit
categories_unit_dict : dict = {
    "Length":["Nautical Mile","Kilometre","Metre","Centimetre","Micrometre","Centimetre",
            "Nanometre","Mile","Yard","Foot","Inch"],
    "Area":["Square Kilometre","Square Metre","Square Mile","Square Yard",
            "Square Foot","Square Inch","Hectare","Acre"],
    "Data Transfer": ["Bit per Second (bps)","Kilobit per Second (Kbps)",
                      "Megabit per Second (Mbps)","Gigabit per Second (Gbps)",
                      "Terabit per Second (Tbps)","Byte per Second (Bps)","Kilobyte per Second (KBps)",
                      "Megabyte per Second (MBps)","Gigabyte per Second (GBps)",
                      "Terabyte per Second (TBps)"],
    "Digital Storage":["byte", "bit", "Kilobit", "Kibibit", "Megabit", "Mebibit",
                       "Gigabit", "Gibibit", "Terabit", "Tebibit", "Petabit", "Pebibit",
                       "Kilobyte", "Kibibyte", "Megabyte", "Mebibyte", "Gigabyte",
                        "Gibibyte","Terabyte", "Tebibyte", "Petabyte", "Pebibyte"
                        ],
    "Energy":["Joule","Kilojoule","Gram calorie","Kilocalorie","Watt hour",
              "Kilowatt-hour","Electronvolt","British Thermal Unit","US Therm",
              "Foot-pound"],
    "Frequency":["Hertz","Kilohertz","Megahertz","Gigahertz"]
}
# Area Conversion Function
def area_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  area_dict : dict[str,float] = {
      "Square Kilometre":1.0,
      "Square Metre":1000000.0,
      "Square Mile":0.386102,
      "Square Yard":1196000,
      "Square Foot":10760000,
      "Square Inch":1550000000,
      "Hectare":100,
      "Acre":247.105
  }
  primary_value:float=conversion_value/area_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*area_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Data Transfer  Conversion Function
def data_transfer_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  data_transfer_dict: dict[str, float] = {
    "Bit per Second (bps)": 1.0,
    "Kilobit per Second (Kbps)": 0.001,
    "Megabit per Second (Mbps)": 0.000001,
    "Gigabit per Second (Gbps)": 0.000000001,
    "Terabit per Second (Tbps)": 0.000000000001,
    "Kilobyte per Second (KBps)": 0.000125,
    "Kilobibit per Second":0.000976563,#
    "Megabyte per Second (MBps)": 0.000000125,
    "Gigabyte per Second (GBps)": 0.000000000125,
    "Terabyte per Second (TBps)": 0.000000000000125,
}

  primary_value:float=conversion_value/data_transfer_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*data_transfer_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Digital Storage Conversion Function
def digital_storage_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  data_storage_dict: dict[str, float] = {
    "byte":1.0,
    "bit":8.0,
    "Kilobit":0.008,
    "Kibibit":0.0078125,
    "Megabit":8e-6,
    "Mebibit":7.6294e-6,
    "Gigabit":8e-9,
    "Gibibit":7.4506e-9,
    "Terabit":8e-12,
    "Tebibit":7.276e-12,
    "Petabit":8e-15,
    "Pebibit":7.1054e-15,
    "Kilobyte":0.001,
    "Kibibyte":0.000976563,
    "Megabyte":1e-6,
    "Mebibyte":9.5367e-7,
    "Gigabyte":1e-9,
    "Gibibyte":9.3132e-10,
    "Terabyte":1e-12,
    "Tebibyte":9.0949e-13,
    "Petabyte":1e-15,
    "Pebibyte":8.8818e-16
}

  primary_value:float=conversion_value/data_storage_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*data_storage_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Energy Conversion Function
def energy_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  energy_dict : dict[str,float] = {
      "Joule":1.0,
      "Kilojoule":0.001,
      "Gram calorie":0.239006,
      "Kilocalorie":0.000239006,
      "Watt hour":0.000277778,
      "Kilowatt-hour":2.7778e-7,
      "Electronvolt":6.242e+18,
      "British Thermal Unit":0.000947817,
      "US Therm":9.4804e-9,
      "Foot-pound":0.737562
  }
  primary_value:float=conversion_value/energy_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*energy_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Frequency Conversion Function
def frequency_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  frequency_dict : dict[str,float] = {
      "Hertz":1.0,
      "Kilohertz":0.001,
      "Megahertz":1e-6,
      "Gigahertz":1e-9
  }
  primary_value:float=conversion_value/frequency_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*frequency_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Length Conversion Function
def length_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  length_dict : dict[str,float] = {
      "Nautical Mile":1.0,
      "Kilometre":1.852,
      "Metre":1852.0,
      "Centimetre":185200.0,
      "Micrometre":1852000000.0,
      "Nanometre":1852000000000.0,
      "Mile":1.15078,
      "Yard":2025.37,
      "Foot":6076.12,
      "Inch":72913.4,
  }
  primary_value:float=conversion_value/length_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*length_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Categories Functions
categories_functions : dict = {
  "Length":length_conversion,
  "Area":area_conversion,
  "Data Transfer":data_transfer_conversion,
  "Digital Storage":digital_storage_conversion,
  "Energy":energy_conversion,
  "Frequency":frequency_conversion,
}
# Use Markdown to use page heading and link text combo
st.markdown("""## Welcome to Python Unit Convertor by [Abdullah Shaikh](https://www.linkedin.com/in/abdullah-shaikh-29699b302/)""")
# Text which tells users about website
st.text("This unit convertor allows you to")
# 
category : str = st.selectbox("Select Category ",["Area","Data Transfer",
    "Digital Storage","Energy","Frequency","Length"])
from_unit= st.selectbox("Write Unit by from to convert value ",categories_unit_dict[category])
categories_unit_dict[category].remove(from_unit)
to_unit : str = st.selectbox("Write Unit in which to convert value ",categories_unit_dict[category])
conversion_value: float = float(st.number_input("Write Conversion value "))
converted_value : float = 1.0
converted_value = categories_functions[category](from_unit,to_unit,conversion_value)
if st.button("Convert Value"):
    st.write(f"{conversion_value} {from_unit} is {converted_value} {to_unit}")