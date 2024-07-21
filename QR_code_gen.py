import qrcode
import os

# Function to generate and save QR codes
def generate_qr_codes(names, output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for name in names:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(name)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image with the name as the filename
        img.save(os.path.join(output_dir, f'{name}.png'))

    print('QR codes generated and saved in the "{}" directory.'.format(output_dir))

# Read names from "Names.txt" file
file_path = 'Names.txt'
output_directory = 'QR_Codes'

try:
    with open(file_path, 'r') as file:
        names = [line.strip() for line in file]
    generate_qr_codes(names, output_directory)
except FileNotFoundError:
    print(f'Error: File "{file_path}" not found.')
except Exception as e:
    print(f'An error occurred: {e}')