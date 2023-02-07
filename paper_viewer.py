from pdf2image import convert_from_path
import os
import cv2

class paper_viewer:
    def __init__(self, doi1, doi2, page):
        self.doi1=doi1
        self.doi2=doi2
        # self.file_name=((self.doi).split('/')[1]).replace('/', '.', 2)
        self.file_name=doi2
        self.page=int(page)
    # def get_available_url(self):
    #     res=os.popen('scihub -c')
    #     self.url_scihub=res[0]
    #     print(self.url_scihub)

    def download_pdf(self):
        try:
            file_list=os.popen('ls pdf').read()
            if f'{self.file_name}.pdf' in file_list:
                return
            # print(f'scihub -s {self.doi}')
            os.system(f'scihub -s {self.doi}')
        except Exception as e:
            print('download error')
            print(e)
    
    def pdf2image(self):
        if f'{self.file_name}{self.page}.jpg' in os.popen('ls pdf').read():
            return
        pages = convert_from_path(f"pdf/{self.file_name}.pdf")
        # self.num_page=len(pages)
        # page.save(f"./pdf/{self.file_name}{str(self.page)}.jpg", "JPEG")
        for i, page in enumerate(pages):
            if i==self.page:
	            page.save(f"./pdf/{self.file_name}{str(i)}.jpg", "JPEG")
        
    def image2mp4(self):
        if f'result_{self.file_name}' in os.popen('ls').read():
            pass
        else:
            os.system(f'mkdir result_{self.file_name}')

        if f'result_{self.file_name}/{self.file_name}{self.page}.mp4' in os.popen(f'ls result_{self.file_name}').read():
            return
        else:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            img = cv2.imread(f'./pdf/{self.file_name}{self.page}.jpg')
            height, width, layers = img.shape
            wh_ratio=1.777 # value from 1920/1080
            height_video=int(width/wh_ratio)
            size = (width, height_video)
            video = cv2.VideoWriter(f'result_{self.file_name}/{self.file_name}{self.page}.mp4',fourcc, 5.0, size)
            # num_img=int(height/(height_video/2))-1
            # for i in range(num_img):
            i=0
            while (i+1)*int(height_video/2)<height:
                if i*int(height_video/2)+height_video>height:
                    partial_img=img[0:width, height-height_video:height]
                else:
                    partial_img=img[0:width, (i)*int(height_video/2):(i)*int(height_video/2)+height_video]
                for j in range(5):
                    video.write(partial_img)
                i=i+1
            video.release()