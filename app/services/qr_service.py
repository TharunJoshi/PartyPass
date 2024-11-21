import qrcode
import os

def generate_qr_code(pub_name):
    qr_data = f"Pub: {pub_name}"
    qr_image = qrcode.make(qr_data)

    # Save the QR code as an image
    output_dir = "qr_codes"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{pub_name}.png")
    qr_image.save(file_path)
    return file_path

def validate_qr_code(pub_name, scanned_data):
    # Example logic to validate the QR code
    expected_data = f"Pub: {pub_name}"
    return scanned_data == expected_data
