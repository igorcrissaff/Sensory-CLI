from PIL import Image
import moondream

model = moondream.photon("moondream2")

image = Image.open("image.png")
result = model.caption(image, length="normal")
print(result["caption"])   