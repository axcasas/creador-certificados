from PIL import Image, ImageDraw, ImageFont
import pandas as pd 
from pathlib import Path
import logging

def clean_data(csv_file):
    """
    Clean and preprocess the data from a CSV file.

    Parameters:
        csv_file (str): Path to the CSV file containing the data.

    Returns:
        DataFrame: Cleaned DataFrame with renamed columns.

    This function reads the data from the specified CSV file into a DataFrame,
    renames the columns to standardized names, and returns the cleaned DataFrame.

    Note: Specify column name mappings according to the actual column names in your CSV file.
    """
    df = pd.read_csv(csv_file)

    df = df.rename(columns={
        'Correo electrónico. Por favor, asegurarse de que esté escrito correctamente.': 'mail',
        'APELLIDO/S, NOMBRE/S:': 'nombre_apellido'
    })
    return df

def create_certificate_nt(data, certificate_path: str, output_folder: str):
    """
    Create certificates for NT recipients.

    Parameters:
        data (DataFrame): DataFrame containing recipient names under the 'nombre_apellido' column.
        certificate_path (str): Path to the certificate template image file.
        output_folder (str): Path to the folder where generated certificates will be saved.

    Returns:
        None

    This function iterates through the recipient names extracted from the provided DataFrame,
    adds each name to the certificate template image, and saves the generated certificates as PDF files
    in the specified output folder.

    Note: Adjusted font size, font style, and text position for better certificate presentation.
    """

    logging.basicConfig(filename='certificate_creation.log', level=logging.ERROR)

    print('Creating your certificates...')

    # Extract names from the cleaned data
    names = data['nombre_apellido']

    for name in names:
        # Remove unwanted characters from the name
        name = name.replace('.', '').replace(',', '').replace(':', '').strip()
        name = name.upper()

        text_y_position = 430  # Adjusted position for text
        img = Image.open(certificate_path, mode='r')
        img_width = img.width

        # draw
        draw = ImageDraw.Draw(img)

        # font
        font_size = 110

        if len(name) > 30:
            font_size = font_size / 2
        elif len(name) > 20:
            font_size = font_size * 2 / 3

        # IMPORTANT
        # Set your own Font! If you get errors you can use the available fonts on your computer
        font_path = str(Path('data/Roboto-Medium.woff'))
        
        try:
            font = ImageFont.truetype(font_path, int(font_size))
        except Exception as e:
            logging.error(f"Error loading font file: {e}")
            print(f"Error loading font file: {e}")
            continue  # Skip this certificate and continue with the next one

        # text width
        text_width, _ = draw.textsize(name, font=font)

        # draw text for name in orange color
        draw.text(((img_width - text_width) / 2, text_y_position), name, font=font, fill='#de5602')

        # save certificates in a folder
        output_path = f"{output_folder}/{name}.pdf"
        img.save(output_path)
        print(f"Saved certificate for {name} at {output_path}")

def create_certificate_aacc(data, certificate_path: str, output_folder: str):
    """
    Create certificates for AACC recipients.

    Parameters:
        data (DataFrame): DataFrame containing recipient names under the 'nombre_apellido' column.
        certificate_path (str): Path to the certificate template image file.
        output_folder (str): Path to the folder where generated certificates will be saved.

    Returns:
        None

    This function iterates through the recipient names extracted from the provided DataFrame,
    adds each name to the certificate template image, and saves the generated certificates as PDF files
    in the specified output folder.

    Note: Adjusted font size, font style, and text position for better certificate presentation.
    """
        
    logging.basicConfig(filename='certificate_creation.log', level=logging.ERROR)

    print('Creating your certificates...')

    # Extract names from the cleaned data
    names = data['nombre_apellido']

    for name in names:
        # Remove unwanted characters from the name
        name = name.replace('.', '').replace(',', '').replace(':', '').strip()
        name = name.upper()

        text_y_position = 675  # Adjusted position for text
        img = Image.open(certificate_path, mode='r')
        img_width = img.width

        # draw
        draw = ImageDraw.Draw(img)

        # font
        font_size = 150

        if len(name) > 30:
            font_size = font_size / 2
        elif len(name) > 20:
            font_size = font_size * 2 / 3

        # IMPORTANT
        # Set your own Font! If you get errors you can use the available fonts on your computer
        font_path = str(Path('data/Montserrat-Regular.ttf'))
        
        try:
            font = ImageFont.truetype(font_path, int(font_size))
        except Exception as e:
            logging.error(f"Error loading font file: {e}")
            print(f"Error loading font file: {e}")
            continue  # Skip this certificate and continue with the next one

        # text width
        text_width, _ = draw.textsize(name, font=font)

        # draw text for name in black color
        draw.text(((img_width - text_width) / 2, text_y_position), name, font=font, fill=(0,0,0))

        # save certificates in a folder
        output_path = f"{output_folder}/{name}.pdf"
        img.save(output_path)
        print(f"Saved certificate for {name} at {output_path}")