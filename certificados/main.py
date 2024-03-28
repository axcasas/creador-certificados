from PIL import Image, ImageDraw, ImageFont
import pandas as pd 

def clean_data(csv_file):
    df = pd.read_csv(csv_file)

    df = df.rename(columns={
        'Correo electrónico. Por favor, asegurarse de que esté escrito correctamente.': 'mail',
        'APELLIDO/S, NOMBRE/S:': 'nombre_apellido'
    })
    return df

def create_certificate(data, certificate_path: str, output_folder: str):
    print('Creating your certificates...')

    # Extract names from the cleaned data
    names = data['nombre_apellido']

    for name in names:
        # Remove unwanted characters from the name
        name = name.replace('.', '').replace(',', '').replace(':', '').strip()
        name = name.upper()

        text_y_position = 430 # 450 original nt helvetica, 675 original webinar aacc
        img = Image.open(certificate_path, mode='r')
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
        font = ImageFont.truetype('Roboto-Medium.woff', int(font_size))

        # text width
        text_width, _ = draw.textsize(name, font=font)

        # draw text for name in orange color
        draw.text(((img_width - text_width) / 2, text_y_position), name, font=font, fill='#de5602')

        # save certificates in a folder
        output_path = f"{output_folder}/{name}.pdf"
        img.save(output_path)
        print(f"Saved certificate for {name} at {output_path}")
