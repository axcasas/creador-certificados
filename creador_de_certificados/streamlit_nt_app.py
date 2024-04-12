import os
import streamlit as st
import zipfile
import tempfile
import base64
import pandas as pd
from pathlib import Path
from main import create_certificate_nt, create_certificate_aacc, clean_data

def main():
    logo = Path('data/logo_nt.png')
    st.sidebar.image(str(logo))
    st.sidebar.markdown("<h1 style='text-align: center;'>Creación de Certificados Asistencia NT</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("En esta interfaz gráfica pueden generar certificados de asistencia de manera sencilla en tan solo 3 pasos")
    st.sidebar.markdown("1. Subir tu archivo CSV")
    st.sidebar.markdown("2. Subir un template de certificado")
    st.sidebar.markdown("3. Generar y descargar tus certificados")

    st.title("Generador de Certificados de Asistencia --Neurotransmitiendo")

    # Step 1 File uploader for CSV file
    st.header("Paso 1: Subir Archivo CSV")
    st.markdown("Pueden conseguir su archivo CSV simplemente descargando el Google Sheets generado de las respuestas del Google Forms")
    csv_file = st.file_uploader("Subir archivo CSV", type=["csv"])

    # Step 2: Select certificate type
    st.header("Paso 2: Seleccionar Tipo de Certificado")
    certificate_type = st.radio("Seleccione el tipo de certificado:", ('Certificado de Asistencia NT', 'Certificado de Asistencia AACC'))

    # Step 3 File uploader for certificate template
    st.header("Paso 3: Subir Template (plantilla) de Certificafo en formato JPG")
    cert_template = st.file_uploader("Subir template de certificado (JPG)", type=["jpg"])

    if cert_template is not None:
        st.image(cert_template, caption='Tu template de certificado')

    # Step 4: Download Certificates (ZIP)
    st.header("Paso 4: Descargar Certificados")

    if csv_file and cert_template:
        # Display uploaded file details
        st.write("✅ Archivo CSV correctamente cargado:", csv_file.name)
        st.write("✅ Template de certificado (JPG) correctamente cargado:", cert_template.name)
        st.markdown("##### 🤓 ¡Todo listo para generar tus certificados! Haz clic en el siguiente botón:")

        # Button to generate certificates
        if st.button("Generar Certificados"):
            # Clean data
            cleaned_data = clean_data(csv_file)

            # Create certificates based on selected type
            with tempfile.TemporaryDirectory() as temp_dir:
                output_dir = temp_dir
                if certificate_type == 'Certificado de Asistencia NT':
                    create_certificate_nt(cleaned_data, cert_template, output_dir)
                elif certificate_type == 'Certificado de Asistencia AACC':
                    create_certificate_aacc(cleaned_data, cert_template, output_dir)

                # Provide download link for generated certificates
                st.markdown("##### 😃 ¡Listo! Ya puedes descargar tus certificados. El siguiente enlace descargará todos los certificados en formato PDF en un archivo ZIP:")
                st.markdown(get_download_link(output_dir), unsafe_allow_html=True)


def get_download_link(output_dir):

    """Generate a download link for a zip file containing all generated certificates."""
    cert_files = [f for f in os.listdir(output_dir) if f.endswith('.pdf')]
    if cert_files:
        # Create a temporary directory to store the zip file
        temp_dir = tempfile.mkdtemp()
        zip_filename = os.path.join(temp_dir, 'certificados.zip')
        
        # Create a zip file containing all certificate files
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for cert_file in cert_files:
                zipf.write(os.path.join(output_dir, cert_file), arcname=cert_file)

        # Read the zip file data
        with open(zip_filename, 'rb') as f:
            zip_data = f.read()

        # Encode the zip file data as base64
        zip_b64 = base64.b64encode(zip_data).decode('utf-8')

        # Provide download link for the zip file
        zip_link = f'<a href="data:application/zip;base64,{zip_b64}" download="certificates.zip">Download Certificates (ZIP)</a>'
        return zip_link
    else:
        return "Tus certificados aún no han sido generados."

if __name__ == "__main__":
    main()
