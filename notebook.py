# This is a Marimo notebook
# Email: 23f2000275@ds.study.iitm.ac.in

# Cell 1: Import and define slider
import marimo

__generated_with = "0.3.2"
app = marimo.App()

# Define slider for interactive control
slider = app.slider(start=1, stop=10, value=5, label="Select a multiplier")

# Output the widget to the UI
app.display(slider)

# Cell 2: Use slider value to calculate result

# Data flows from slider to result
value = slider.value  # Dependency on slider from previous cell
result = value * 3    # Simple computation

# Comment: result is computed based on the slider
result

# Cell 3: Show dynamic markdown based on result

# This markdown will update when the slider is changed
app.markdown(f"### Multiplied value is **{result}**")

# Comment: markdown reacts to changes in the slider -> result
