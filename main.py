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
    "Frequency":["Hertz","Kilohertz","Megahertz","Gigahertz"],
    "Fuel Econmy":[ "Kilometer per liter","Mile per US gallon","Mile per gallon",
              "Litre per 100 kilometres"],
    "Mass":["Kilogram","Tonne","Gram","Milligram","Microgram","Imperial ton","US ton",
              "Stone","Pound","Ounce"],
    "Plane Angle":["Degree","Radian","Arcsecond","Gradian","Milliradian",
              "Minute of arc"],
    "Pressure":["Bar","Pascal","Pound per square inch","Standard atmosphere","Torr"],
    "Speed":["Metre per second","Mile per hour","Foot per second","Kilometre per hour",
    "Knot"],
    "Temprature":["Degree Celsius","Fahrenheit","Kelvin"],
    "Time":["Second","Nanosecond","Microsecond","Millisecond","Minute","Hour","Day",
            "Week","Month","Year","Decade","Century"],
    "Volume" : ["Liter","US liquid gallon","US liquid quart","US liquid pint",
    "US legal cup","US fluid ounce","US tablespoon","US teaspoon","Cubic meter",
    "Milliliter","Imperial gallon","Imperial quart","Imperial pint","Imperial cup",
    "Imperial fluid ounce","Imperial tablespoon","Imperial teaspoon","Cubic foot",
    "Cubic inch"]
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
# Fuel Econmy Conversion Function
def fuel_econmy_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  fuel_econmy_dict : dict[str,float] = {
      "Kilometer per liter":1,
      "Mile per US gallon":2.35215,
      "Mile per gallon":2.82481,
      "Litre per 100 kilometres":100.0
  }
  primary_value:float=conversion_value/fuel_econmy_dict[from_unit]
  secondary_value:float=1.0
  if to_unit == "Litre per 100 kilometres":
    num : float = fuel_econmy_dict[from_unit]*100
    if conversion_value == 0.0:
      secondary_value = 0.0
    else:
      secondary_value = num/conversion_value
  elif from_unit == "Litre per 100 kilometres":
    num : float = conversion_value/100
    if conversion_value == 0.0:
      secondary_value = 0.0
    else:
      a = fuel_econmy_dict[to_unit]*100
      secondary_value = a/conversion_value
  else:
      try:
        secondary_value=primary_value*fuel_econmy_dict[conversion_unit]
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
# Mass Conversion Function
def mass_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  mass_dict : dict[str,float] = {
      "Kilogram":1.0,
      "Tonne":0.001,
      "Gram":1000.0,
      "Milligram":1e+6,
      "Microgram":1e+9,
      "Imperial ton":0.000984207,
      "US ton":0.00110231,
      "Stone":0.157473,
      "Pound":2.20462,
      "Ounce":35.274
  }
  primary_value:float=conversion_value/mass_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*mass_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Plane Angle Conversion Function
def plane_angle_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  plane_angle_dict : dict[str,float] = {
      "Degree":1.0,
      "Radian":0.0174533,
      "Arcsecond":3600.0,
      "Gradian":1.11111,
      "Milliradian":17.4533,
      "Minute of arc":60
  }
  primary_value:float=conversion_value/plane_angle_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*plane_angle_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Pressure Conversion Function
def pressure_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  pressure_dict : dict[str,float] = {
      "Bar":1.0,
      "Pascal":100000,
      "Pound per square inch":14.5038,
      "Standard atmosphere":0.986923,
      "Torr":750.062
  }
  primary_value:float=conversion_value/pressure_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*pressure_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Speed Conversion Function
def speed_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  speed_dict : dict[str,float] = {
      "Metre per second":1,
      "Mile per hour":2.23694,
      "Foot per second":3.28084,
      "Kilometre per hour":3.6,
      "Knot":1.94384
  }
  primary_value:float=conversion_value/speed_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*speed_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
#Temprature conversion function
def temprature_conversion(from_unit:int,conversion_unit:str,conversion_value:float):
  secondary_value:float=1.0
  if from_unit=="Degree Celsius":
    if conversion_unit=="Fahrenheit":
      dividing_factor : float = 9/5
      primary_value:float = conversion_value*dividing_factor
      secondary_value = primary_value+32 
    elif conversion_unit=="Kelvin":
      secondary_value = conversion_value+273.15
  elif from_unit=="Fahrenheit":
    if conversion_unit=="Degree Celsius":
      dividing_factor : float = 5/9
      primary_value:float = conversion_value-32
      secondary_value = primary_value*dividing_factor
    elif conversion_unit=="Kelvin":
      dividing_factor : float = 5/9
      primary_value : float = conversion_value-32
      middle_value : float = primary_value*dividing_factor
      secondary_value : float = middle_value+273.15
  elif from_unit == "Kelvin":
    if conversion_unit == "Degree Celsius":
      secondary_value = conversion_value-273.15
    elif conversion_unit == "Fahrenheit":
      dividing_factor : float = 9/5
      primary_value : float = conversion_value-273.15
      middle_value : float = primary_value*dividing_factor
      secondary_value = middle_value+32

  return secondary_value
# Time Conversion Function
def time_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  time_dict : dict[str,float] = {
      "Second":1.0,
      "Nanosecond":1e+9,
      "Microsecond":1e+6,
      "Millisecond":1000,
      "Minute":0.0166667,
      "Hour":0.000277778,
      "Day":1.1574e-5,
      "Week":1.6534e-6,
      "Month":3.8052e-7,
      "Year":3.171e-8,
      "Decade":3.171e-9,
      "Century":3.171e-10
  }
  primary_value:float=conversion_value/time_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*time_dict[conversion_unit]
  except:
    print("Unit Not Found Error!")
  return secondary_value
# Volume Conversion Function
def volume_conversion(from_unit:str,conversion_unit:str,conversion_value:float):
  volume_dict : dict[str,float] ={
    "Liter":1.0,
    "US liquid gallon":0.264172,
    "US liquid quart":1.05669,
    "US liquid pint":2.11338,
    "US legal cup":4.16667,
    "US fluid ounce":33.814,
    "US tablespoon":67.628,
    "US teaspoon":202.884,
    "Cubic meter":0.001,
    "Milliliter":1000,
    "Imperial gallon":0.219969,
    "Imperial quart":0.879877,
    "Imperial pint":1.75975,
    "Imperial cup":3.51951,
    "Imperial fluid ounce":35.1951,
    "Imperial tablespoon":56.3121,
    "Imperial teaspoon":168.936,
    "Cubic foot":0.0353147,
    "Cubic inch":61.0237
  }
  primary_value:float=conversion_value/volume_dict[from_unit]
  secondary_value:float=1.0
  try:
    secondary_value=primary_value*volume_dict[conversion_unit]
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
  "Fuel Econmy":fuel_econmy_conversion,
  "Mass":mass_conversion,
  "Plane Angle":plane_angle_conversion,
  "Pressure":pressure_conversion,
  "Speed":speed_conversion,
  "Temprature":temprature_conversion,
  "Time":time_conversion,
  "Volume":volume_conversion
}
# Use Markdown to use page heading and link text combo
st.markdown("""## Welcome to Python Unit Convertor by [Abdullah Shaikh](https://www.linkedin.com/in/abdullah-shaikh-29699b302/)""")
# Text which tells users about website
st.text("This is a simple web application built with Streamlit that allows you to convert between various units of measurement.")
category : str = st.selectbox("Select Category ",["Area","Data Transfer",
    "Digital Storage","Energy","Frequency","Fuel Econmy","Length","Mass","Plane Angle",
    "Pressure","Speed","Temprature","Time","Volume"])
from_unit= st.selectbox("Write Unit by from to convert value ",categories_unit_dict[category])
categories_unit_dict[category].remove(from_unit)
to_unit : str = st.selectbox("Write Unit in which to convert value ",categories_unit_dict[category])
conversion_value: float = float(st.number_input("Write Conversion value "))
converted_value : float = 1.0
converted_value = categories_functions[category](from_unit,to_unit,conversion_value)
if st.button("Convert Value"):
    st.write(f"{conversion_value} {from_unit} is {converted_value} {to_unit}")