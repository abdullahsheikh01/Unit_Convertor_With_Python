# Python Unit Converter

This is a simple web application built with Streamlit that allows you to convert between various units of measurement.

## Features

* **Wide Range of Categories:** Convert units for Length, Area, Data Transfer, Digital Storage, Energy, Frequency, Fuel Economy, Mass, Plane Angle, Pressure, Speed, Temperature, Time, and Volume.
* **User-Friendly Interface:** Easily select categories and units using dropdown menus.
* **Instant Conversion:** Get your converted values with a click of a button.

## How to Use

1.  **Select a Category:** Choose the type of measurement you want to convert (e.g., Length, Temperature).
2.  **Choose "From" Unit:** Select the unit you want to convert from.
3.  **Choose "To" Unit:** Select the unit you want to convert to.
4.  **Enter Value:** Input the numerical value you want to convert.
5.  **Click "Convert Value":** The converted value will be displayed below the button.

## Code Explanation

The code uses Streamlit to create the web interface. It defines a dictionary `categories_unit_dict` to store the available units for each category. Conversion functions are defined for each category, which perform the necessary calculations. The `categories_functions` dictionary maps categories to their respective conversion functions.

## Author

This application was created by [Abdullah Shaikh](https://www.linkedin.com/in/abdullah-shaikh-29699b302/).

## Example

If you want to convert 10 meters to feet:

1.  Select "Length" from the category dropdown.
2.  Select "Metre" from the "Write Unit by from to convert value" dropdown.
3.  Select "Foot" from the "Write Unit in which to convert value" dropdown.
4.  Enter "10" in the "Write Conversion value" input.
5.  Click "Convert Value".

The result will display: "10 Metre is 32.8084 Foot".