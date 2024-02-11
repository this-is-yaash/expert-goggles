# import the necessary packages
import pytesseract
import cv2

file_type = input("File type? ")
file_loc = input("Location? ")

if file_type.lower() == "i" or "image":
	# load the input image and convert it from BGR to RGB channel
	# ordering}
	image = cv2.imread(file_loc)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	# use Tesseract to OCR the image
	text = pytesseract.image_to_string(image)
	print(text)
else:
	print("Check again")	
