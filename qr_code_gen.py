import qrcode

url = input("Enter the url: ").strip()
name = input("Enter the name: ").strip()
location = f"C:\\Users\\Dell\\Desktop\\{name}.png"

img = qrcode.make(url)
img.save(location)

print("QR code generated successfully.")