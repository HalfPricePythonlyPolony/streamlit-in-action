import streamlit as st

# Put the detailed, GitHub-flavored Markdown into the widget tooltip itself.
# Note: tooltips are shown only when label_visibility="visible".
quantity = st.sidebar.radio(
    "Select a quantity",
    ["Mass", "Length", "Time"],
    help="""
    ## What does this selector do?

    Choose the physical quantity you want to convert. The app will show unit
    choices and conversion controls for the selected quantity.

    ### Supported quantities
    - **Mass** — mass units (kg, g, lb, oz, etc.)
    - **Length** — distance units (m, cm, mm, in, ft, etc.)
    - **Time** — time units (s, min, h, etc.)

    ### Examples
    - Convert `5 kg` → `lb` to compare weights.
    - Convert `2.5 h` → `min` to see smaller time units.

    ### Tips
    - Pick the quantity first, then enter the value and choose source/target units.
    - This text supports GitHub-flavored Markdown (bold, italics, lists, code, and links).

    If you'd prefer this information always visible, move it out of the tooltip
    (for example with `st.markdown(...)` above the selector) or place it in the
    sidebar using `st.sidebar.markdown(...)`.
    """,
    label_visibility="visible",
)

st.title("Unit :blue[Converter] :train:")

input_num = float(st.text_input("value to convert", "1.0"))
units = ["Kilograms", "Pounds", "Ounces"]

from_unit_col, to_unit_col = st.columns(2)
from_unit = from_unit_col.selectbox("from", units)
to_unit = to_unit_col.selectbox("to", units, 1)

if st.button("Convert"):
    pass# ...conversion logic goes here...

