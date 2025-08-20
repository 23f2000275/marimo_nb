# This is a Marimo notebook
# Email: 23f2000275@ds.study.iitm.ac.in

# Cell 1: Import and define slider
# Email: your.email@example.com

import marimo

app = marimo.App()

# Cell 1: Create slider widget
slider = app.slider(
    label="Select a multiplier",
    start=1,
    stop=10,
    value=5,
)

# Display the slider widget
app.display(slider)
# Cell 2: Use slider value to compute a result

# Data flow: this depends on slider's current value
multiplier = slider.value
result = multiplier * 3

result
# Cell 3: Dynamic markdown output reacting to slider

app.markdown(f"### Multiplied value is **{result}**")
