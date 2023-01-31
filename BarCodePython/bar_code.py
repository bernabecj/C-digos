import barcode
from barcode import Code128

def generate_barcode(data):
    code = Code128(data)
    code.save("barcode")
    print("Barcode generated!")

if __name__ == '__main__':
    data = "1234-5678-9012"
    generate_barcode(data)