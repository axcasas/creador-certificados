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
                if certificate_type == 'NT Certificate':
                    create_certificate_nt(cleaned_data, cert_template, output_dir)
                elif certificate_type == 'AACC Certificate':
                    create_certificate_aacc(cleaned_data, cert_template, output_dir)

                # Provide download link for generated certificates
                st.markdown("##### 😃 ¡Listo! Ya puedes descargar tus certificados. El siguiente enlace descargará todos los certificados en formato PDF en un archivo ZIP:")
                st.markdown(get_download_link(output_dir), unsafe_allow_html=True)