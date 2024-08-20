import qrcode
from PIL import Image

def create_qr_code(data, output_file):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code
    qr_img.save(output_file)
    print(f"QR code saved to {output_file}")

def main():
    # Accept user input
    input_data = input("Enter a URL or image file path: ")

    # Determine whether the input is a URL or an image
    if input_data.startswith("http://") or input_data.startswith("https://"):
        output_file = "qrcode.png"
        create_qr_code(input_data, output_file)
    else:
        try:
            img = Image.open(input_data)
            img.show()  # Display the image (optional)
            output_file = "qrcode_from_image.png"
            create_qr_code(input_data, output_file)
        except Exception as e:
            print(f"Error: {e}. Please provide a valid URL or image file path.")

if __name__ == "__main__":
    main()
