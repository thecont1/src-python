import nbformat
from nbconvert import PythonExporter

# Specify path and notebook filename
source_path = "/Users/home/DEV/scaler/python/public/namma-metro-ridership-tracker/"
filename = "ridership.ipynb"

# Load the notebook
with open(source_path+filename) as f:
    notebook = nbformat.read(f, as_version=4)

# Convert the notebook to a Python script
exporter = PythonExporter()
script, _ = exporter.from_notebook_node(notebook)

# Save the script
with open("./your_script.py", 'w') as f:
    f.write(script)
