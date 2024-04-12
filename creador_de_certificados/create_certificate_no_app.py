from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import logging

def create_certificate_no_app_nt(names, certificate:str, output_folder:str):

    print('Creating your certificates...')

    for name in names:
        
        # Remove unwanted characters from the name
        name = name.replace('.', '').replace(',', '').replace(':', '').strip()

        name = name.upper()

        text_y_position = 450 #675 original webinar
        img = Image.open(certificate, mode='r')
        img_width = img.width

        # draw
        draw = ImageDraw.Draw(img)

        # font
        font_size = 110

        if len(name) > 30:
            font_size = font_size / 2
        elif len(name) > 20:
            font_size = font_size * 2/3

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

def create_certificate_no_app_aacc(names, certificate:str, output_folder:str):

    print('Creating your certificates...')

    for name in names:
        
        # Remove unwanted characters from the name
        name = name.replace('.', '').replace(',', '').replace(':', '').strip()

        name = name.upper()

        text_y_position = 450 #675 original webinar
        img = Image.open(certificate, mode='r')
        img_width = img.width

        # draw
        draw = ImageDraw.Draw(img)

        # font
        font_size = 150

        if len(name) > 30:
            font_size = font_size / 2
        elif len(name) > 20:
            font_size = font_size * 2/3

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

        # draw text for name in black color
        draw.text(((img_width - text_width) / 2, text_y_position), name, font=font)

        # save certificates in a folder
        output_path = f"{output_folder}/{name}.pdf"
        img.save(output_path)
        print(f"Saved certificate for {name} at {output_path}")