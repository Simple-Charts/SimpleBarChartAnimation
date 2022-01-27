from PIL import Image
import os
import cv2
from tqdm import tqdm

folder1 = 'C:/Users/****/Desktop/bca1'
folder2 = 'C:/Users/****/Desktop/bca2'
folder3 = 'C:/Users/****/Desktop/bca3'
folder4 = 'C:/Users/****/Desktop/bca4'

images = 3651
video_height = 1000
video_width = 1600
video_fps = 15

if not os.path.exists("image"):
    os.mkdir("image")
for i in tqdm(range(images)):
    image1 = Image.open(folder1 + "/image/img"+str(i).zfill(4)+".png")
    image2 = Image.open(folder2 + "/image/img"+str(i).zfill(4)+".png")
    image3 = Image.open(folder3 + "/image/img"+str(i).zfill(4)+".png")
    image4 = Image.open(folder4 + "/image/img"+str(i).zfill(4)+".png")

    image5 = Image.new('RGB', (image1.width * 2 , image1.height * 2))

    image5.paste(image1, (0, 0))
    image5.paste(image2, (image1.width, 0))
    image5.paste(image3, (0, image1.height))
    image5.paste(image4, (image1.width, image1.height))

    image5.save("image/img"+str(i).zfill(4)+".png")

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter('video.mp4', fourcc, fps = video_fps, frameSize = (video_width, video_height))
for i in tqdm(range(images)):
    img = cv2.imread('image/img%04d.png' % i)
    img = cv2.resize(img, (video_width, video_height))
    video.write(img)
video.release()