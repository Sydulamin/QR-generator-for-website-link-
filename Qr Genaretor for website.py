import qrcode
import random
import pandas as pd


df = pd.read_excel("weblink.xlsx")
data_new = []

for index, row in df.iterrows():
    for column in df.columns:
        cell_value = row[column]
        data_new.append(cell_value)

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


for data in data_new:
    filename = data + '.png'
    generate_qr_code(data, filename)
    print(f"QR code generated and saved as {filename}")


