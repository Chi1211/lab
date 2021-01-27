import glob, os
from PIL import Image  # chạy lệnh cài đặt thư viện: pip install Pillow==2.2.2

licenseDict = {} # Lưu các nhãn trong file class.txt
charDict = {}    # Lưu nội dung của các files gán nhãn key = “tên file”, value= nội dung các nhãn
storeDict = '../chars/'
path = './dataset/license/'

def delete_file_in_folder(folder):
    # code xóa files trong thư mục
    pass
def preProcess():
    listCharsReady = []
    for key in licenseDict:
        chars = licenseDict[key]
        imgPath = key
        img = Image.open(imgPath)
        dw, dh = img.size
        for char in chars:
            dirChar = storeDict + charDict[int(char[0])]
            # Xóa file cũ, chỉ xóa 1 lần đầu
            if char[0] not in listCharsReady:
                delete_file_in_folder(dirChar)
                listCharsReady.append(char[0])
            # Lấy tọa độ ký tự
            dataCoordinate = char[1:]
            x, y, w, h = map(float, dataCoordinate)
            left = int((x-w / 2) * dw)
            right = int((x + w / 2) * dw)
            top = int((y - h / 2) * dh)
            bottom = int((y + h / 2) * dh)
            if left < 0:
                l = 0
            if right > dw - 1:
                right = dw - 1
            if top < 0:
                top = 0
            if bottom > dh - 1:
                bottom = dh - 1
            # Crop ký tự trên biển số
            cropImg = img.crop((left,top,right,bottom))
            # Tạo thư mục cho ký tự nếu thư mục chưa tồn tại
            if not os.path.exists(dirChar):
                os.makedirs(dirChar)
            # Tạo chỉ số cho file hình 
            numFileChar = len(os.listdir(dirChar)) + 1
            # Thư mục và file hình sẽ lưu
            imgPathSave = dirChar +'/'+ charDict[int(char[0])]+'_'+str(numFileChar)+'.jpg'
            # Tiến hành lưu file
            cropImg.save(imgPathSave, 'JPEG')
print(charDict)
print(licenseDict['5498.jpg'])

