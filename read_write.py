import cv2
# import os
# import sys

# cur_dir = os.path.dirname(sys.argv[0])  # 現在のディレクトリを取得
# file_path = os.path.join(cur_dir, 'image/cat.jpg')
img = cv2.imread("image/cat.jpg")
print(img.shape)


# print(cv2.__version__)
# img = cv2.imread(file_path)
# img = cv2.imread("image/cat.jpg", cv2.IMRESD_GRAYSCALE)

resize_img = cv2.resize(img, dsize=(768 // 2, 432 // 2))
cv2.imwrite("image/resize_cat.jpg", resize_img)

cv2.putText(
    img,
    text="CAT !!!",
    org=(100, 250),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=5,
    color=(255, 255, 0),
    thinkness=3,
    )
cv2.imshow("Image", img)

# cv2.waitKey(10000)  # 5000=5秒 10000=10秒

# cv2.imwrite(os.path.join(cur_dir, "write.jpg"), img)
