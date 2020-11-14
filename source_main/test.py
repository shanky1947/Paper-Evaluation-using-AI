from PIL import Image
img = Image.open(r"C:\Users\shash\Desktop\AI\mine2.jpeg")
top=130
bottom=220
for i in range(0,4):
    area = (30, top, 1200, bottom)
    cropped_img = img.crop(area)
    top=top+90
    bottom=bottom+90
    im1 = cropped_img.save(r"C:\Users\shash\Desktop\AI\new"+str(i)+".jpeg")