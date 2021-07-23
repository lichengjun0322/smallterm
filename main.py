import datetime
import caijian
import Process
import saveexcel
import qushuiyin
import prework
from PIL import Image
image_read_dir = r'C:\Users\DELL\Desktop\test'   # 测试图片的路径
image_save_dir = r'C:\Users\DELL\Desktop\aftercut'   # 裁剪图片的路径
text_dir = r'C:\Users\DELL\Desktop\out'         # 提取的文字保存的路径
save_name = 'test112.xls'       # Excel表保存的文件名


if __name__ == '__main__':
    begin = datetime.datetime.now()
    qushuiyin.main(image_read_dir)
    time1 = datetime.datetime.now()
    print("**********去水印完成**********,共用时：",time1-begin)
    caijian.main(image_read_dir,image_save_dir)
    time2 = datetime.datetime.now()
    print("**********裁剪图片完成**********,共用时：",time2-time1)
    Process.text_extraction(image_save_dir, text_dir)
    time3 = datetime.datetime.now()
    print("**********提取文字完成**********,共用时：", time3 - time2)
    saveexcel.main(text_dir, save_name)
    time4 = datetime.datetime.now()
    print("**********导入表格完成**********,共用时：", time4 - time3)
    print("共用时：",time4-begin)