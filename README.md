# Certificate Creation Tool

## Overview
The Certificate Creation Tool is a collection of Python scripts designed to automate the generation of certificates for various purposes. It provides both command-line and graphical user interface (GUI) options for creating certificates. The tool allows users to overlay recipient names onto certificate templates, producing multiple individualized certificates in PDF format in seconds.

## Features
- **Multiple Options**: Choose between command-line interface (CLI) and graphical user interface (GUI) for certificate creation.
- **Customization**: Customize certificates by specifying sizes, and positions.
- **Batch Processing**: Generate certificates for multiple recipients at once by providing a list of names.
- **Error Handling**: Gracefully handle errors, such as missing font files or invalid input data, to ensure smooth execution.
- **Output Control**: Choose the output folder for saving generated certificates, allowing for easy organization and distribution.

## Repository Structure

- **certificates/**: The place where the certificates will be stored if using the command line.
- **creator_de_certificados/**: Stores Python scripts for certificate creation using the GUI or not. Also stores the script for the GUI. 
- **data/**: Contains CSV files with recipient data, the certificate template, and the fonts used.
- **notebooks/**: Stores a Jupyter notebook for demonstration.

## Usage
### Command-Line Interface (CLI)

1. Installation: Clone the repository and install the required dependencies:

```
git clone https://github.com/axcasas/creador-certificados.git
cd creador-certificados
pip install -r requirements.txt
```
2. **Customization**: Customize the certificate templates stored in the certificates/ folder.

3. **Data Preparation**: Prepare a CSV file containing the names of the certificate recipients under a column named nombre_apellido.

4. **Execution**: Run the appropriate Python script for certificate creation:
```
python create_certificate_no_app.py --data data/recipients.csv --template certificates/template.jpg --output output_folder
```
### Graphical User Interface (GUI)

1. **Installation**: Ensure all dependencies are installed as per the requirements.txt file.

2. **Execution**: Run the app.py script using Streamlit:
```
streamlit run streamlit_nt_app.py
```