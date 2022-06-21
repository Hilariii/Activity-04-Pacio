import cv2

x = int(input("Enter 1 if Fixed & Enter 2 if Provide: "))

if (x == 1 ):
	filePath='zh.jpg'
	img = cv2.imread(filePath, 1)
	cv2.imshow("Zeus & Hades", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
elif (x == 2):
	filePath = str(input("Enter filePath: "))
	Color = int(input("Enter 1 for color, 0 for Grayscale, -1 for Unchanged: "))
	
	if (Color == 1 or Color == 0 or Color == -1):
		img = cv2.imread(filePath,Color) 
		cv2.imshow("TITLE", img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	else:
		print ("Invalid Input")
		exit()
else:
	print ("Invalid Input")