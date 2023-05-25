from docx2pdf import convert
import qrcode
import zipfile
from datetime import datetime
from PIL import Image
import webbrowser

def rnm():
    return datetime.now().strftime("%Y%m%d%H%M%S")

class aritrends:
    @staticmethod
    def docx2pdf(filename):
        try:
            convert(filename, rnm()+".pdf")
        except Exception as e:
            print(e)
    @staticmethod
    def zip(file_list):
        try:
            with zipfile.ZipFile(rnm()+".zip", "w") as z:
                for file in file_list:
                    z.write(file)
        except Exception as e:
            print(e)
    @staticmethod
    def image2pdf(file_list):
        try:
            images = [Image.open(file).convert("RGB") for file in file_list]
            images[0].save(rnm()+".pdf", save_all=True, append_images=images[1:])
        except Exception as e:
            print(e)
    @staticmethod
    def generate_qrcode(text):
        try:
            qrcode.make(text).save(rnm()+".png")
        except Exception as e:
            print(e)
    @staticmethod
    def open_github():
        webbrowser.open("http://github.com/abhineetraj1")
    @staticmethod
    def show_credits():
        print("This project is developed by Abhineet Raj (GitHub: @abhineetraj1).")

print("Welcome to file processing library.\nType 'aritrends.show_credits()' or 'aritrends.open_github()' for more information")
