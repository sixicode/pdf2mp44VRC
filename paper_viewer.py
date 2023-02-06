from pdf2image import convert_from_path
import os
import cv2

class paper_viewer:
    def __init__(self, doi):
        self.doi=doi
        self.file_name=((self.doi).split('/')[1]).replace('/', '.', 2)

    # def get_available_url(self):
    #     res=os.popen('scihub -c')
    #     self.url_scihub=res[0]
    #     print(self.url_scihub)

    def download_pdf(self):
        try:
            file_list=os.popen('ls pdf')
            if f'{self.file_name}.pdf' in file_list:
                return
            # print(f'scihub -s {self.doi}')
            os.system(f'scihub -s {self.doi}')
        except:
            print('download error')
    
    def pdf2image(self):
        pages = convert_from_path(f"pdf/{self.file_name}.pdf")
        self.num_page=len(pages)
        for i, page in enumerate(pages):
	        page.save(f"./pdf/{self.file_name}{str(i)}.jpg", "JPEG")
        
    def image2mp4(self):
        if result_{self.file_name} in os.popen('ls'):
            pass
        else
            os.system(f'mkdir result_{self.file_name}')

        # encoder(for mp4)
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        # output file name, encoder, fps, size(fit to image size)
        
        for i in range(self.num_page):
            if f'result_{self.file_name}/{self.file_name}{i}.mp4' in os.popen(f'ls result_{self.file_name}'):
                continue
            img = cv2.imread(f'./pdf/{self.file_name}{i}.jpg')
            height, width, layers = img.shape
            size = (width, height)
            video = cv2.VideoWriter(f'result_{self.file_name}/{self.file_name}{i}.mp4',fourcc, 5.0, size)
            for i in range(10):
                video.write(img)
            video.release()