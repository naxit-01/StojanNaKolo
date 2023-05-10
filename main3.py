

url = "https://abs-0.twimg.com/emoji/v2/svg/1f1fa-1f1e6.svg" # Nahraďte tuto adresu URL adresou SVG obrázku, který chcete stáhnout

import urllib.request
from io import BytesIO
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM


response = urllib.request.urlopen(url)
image_data = BytesIO(response.read())

drawing = svg2rlg(image_data)
buffer = BytesIO()
renderPM.drawToFile(drawing, buffer, fmt="jpg")
with open("output.png", "wb") as f:
    f.write(buffer.getbuffer())
prom = buffer.getbuffer()

print("end")