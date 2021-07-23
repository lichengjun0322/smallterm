import datetime
import caijian
import Process
import saveexcel
import qushuiyin
import prework
from PIL import Image
image_read_dir = r'C:\Users\DELL\Desktop\test'   # 测试图片的路径
image_save_dir = r'C:\Users\DELL\Desktop\out'   # 裁剪图片的路径
text_dir = r'C:\Users\DELL\Desktop\out'         # 提取的文字保存的路径
save_name = 'test111.xls'       # Excel表保存的文件名

if __name__ == '__main__':
    begin = datetime.datetime.now()
    qushuiyin.main(image_read_dir)
    #caijian.main(image_read_dir,image_read_dir)
    Process.text_extraction(image_read_dir, text_dir)
    saveexcel.main(text_dir, save_name)
    print(datetime.datetime.now()-begin)