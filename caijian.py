import os
from PIL import Image
import datetime
import matplotlib.pyplot as plt
def crop(image_read_dir, image_save_dir):
    img = Image.open(image_read_dir)  # 打开图像
    x, y = img.size
    img1 = img.crop((0, 0, x*0.5, y*0.55))
    img1.save(image_save_dir)

def main(image_read_dir, image_save_dir):

    for (root, dirs, files) in os.walk(image_read_dir):#os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
        for file in files:
            names = os.path.splitext(file)   ##os.path.splitext() 将文件名和扩展名分开
            if names[1] == '.png' or names[1] == '.jpg':  #判断如果是图片类型
                crop(os.path.join(image_read_dir, file), os.path.join(image_save_dir, file))
        break
#os.path.join(path, name)—连接目录和文件名，与os.path.split(path)相对。


if __name__ == '__main__':
    main()

