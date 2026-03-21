import re

number_lines = int(input())

pattern = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'

for _ in range(number_lines):
    barcode = input()
    match = re.match(pattern, barcode)
    if match:
        barcode_group = re.findall(r'\d+', barcode)
        if barcode_group:
            print(f'Product group: {"".join(barcode_group)}')
        else:
            print(f'Product group: 00')
    else:
        print(f'Invalid barcode')