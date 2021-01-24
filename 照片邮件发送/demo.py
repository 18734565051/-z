'''
功能：
前置摄像头拍照
发送email邮箱
'''
from email.mime.image import MIMEImage  # 附件
from email.mime.text import MIMEText  # 内容
from email.mime.multipart import MIMEMultipart

import time
import smtplib  # 发送邮件
import cv2  # 拍照  pip install opencv-python


# 思路
# 1、调用摄像头拍照保存图片
# 2、构造email响应数据
# 3、发送email

class ImageEmail(object):
    def __init__(self, path):
        self.path = path
        self.sender = '***@163.com'
        self.receiver = '***@qq.com'
        self.Authorization_code = '***'  # 授权码
        self.host = '***'
        self.port = 25

    def getimage(self):
        # cv2.namedWindow('camera')
        # 电脑
        cap = cv2.VideoCapture(0)
        # count = 0
        # while True:
        ret, frame = cap.read()
        cv2.imwrite(self.path + '/person.jpg', frame)
        # count += 1
        cap.release()

    def set_email(self):
        msg = MIMEMultipart('mixed')  # 添加附件
        # 标题
        msg['Subject'] = '送给你'
        msg['From'] = self.sender
        msg['To'] = self.receiver
        # 邮件正文内容
        text = '请接受'
        text_plain = MIMEText(text, 'plain', 'utf-8')  # 转码
        msg.attach(text_plain)
        # 附件
        sendImagedata = open(self.path + '/person.jpg', 'rb').read()
        image = MIMEImage(sendImagedata)
        # msg.attach(image)

        # 修改图片名字
        image['Content-Disposition'] = 'attachment; filename = "my.png"'
        msg.attach(image)
        return msg.as_string()

    def send_email(self, msg):
        smtp = smtplib.SMTP()
        smtp.connect(self.host)
        smtp.login(self.sender, self.Authorization_code)
        smtp.sendmail(self.sender, self.receiver, msg)
        time.sleep(2)
        smtp.quit()


if __name__ == '__main__':
    path = r"C:\Users\Lenovo\Desktop\images"
    e_m = ImageEmail(path)
    e_m.getimage()
    content = e_m.set_email()
    e_m.send_email(content)
