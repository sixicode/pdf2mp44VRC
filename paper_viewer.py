from pdf2image import convert_from_path
import os
import cv2

class paper_viewer():
    def __init__(self, doi):
        self.doi=doi
        pass

    # def get_available_url(self):
    #     res=os.popen('scihub -c')
    #     self.url_scihub=res[0]
    #     print(self.url_scihub)

    def download_pdf(self):
        try:
            # print(f'scihub -s {self.doi}')
            os.system(f'scihub -s {self.doi}')
        except:
            print('download error')
    
    def pdf2image(self):
        self.file_name=((self.doi).split('/')[1]).replace('/', '.', 2)
        pages = convert_from_path(f"pdf/{self.file_name}.pdf")
        self.num_page=len(pages)
        for i, page in enumerate(pages):
	        page.save(f"./pdf/{self.file_name+str(i)}.jpg", "JPEG")
        
    def image2mp4(self):
        # encoder(for mp4)
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        # output file name, encoder, fps, size(fit to image size)
        for i in range(self.num_page):
            video = cv2.VideoWriter(f'{self.file_name}{i}.mp4',fourcc, 20.0, (1240, 1360))
            img = cv2.imread(f'./pdf/{self.file_name}{i}.png')
            video.write(img)
            video.release()



doi='10.1126/science.1186799'
dl=paper_viewer(doi)
# dl.download_pdf()
dl.pdf2image()
dl.image2mp4()