from pdf2image import convert_from_path
import os

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
        pages = convert_from_path("./pdf/" + self.doi)
        for i, page in enumerate(pages):
	        page.save(f"./pdf/{file_name+str(i)}.jpg", "JPEG")


doi='10.1126/science.1186799'
dl=paper_viewer(doi)
# dl.download_pdf()
dl.pdf2image()