from font2tri_lib import FontTriangulator

ft = FontTriangulator(r"C:\Windows\Fonts\simkai.ttf")

test_chars = ['中', '国', '字', 'A', 'O', '回', '明']

for char in test_chars:
    ft.run(char)