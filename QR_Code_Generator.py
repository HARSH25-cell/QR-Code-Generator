import qrcode
def generate_qr(data, filename="qr_code.png"):
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,  # size of the QR Code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # size of each box in pixels
        border=4  # border in boxes
    )
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the image
    img.save(filename)
    print(f"QR Code saved as {filename}")
def main():
    print("QR Code Generator")
    user_data = input("Enter text or URL to encode: ")
    filename = input("Enter filename to save (with .png): ") or "qr_code.png"
    
    generate_qr(user_data, filename)
if __name__ == "__main__":
    main()