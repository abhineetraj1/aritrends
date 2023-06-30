from docx2pdf import convert
import qrcode
import zipfile
from datetime import datetime
from PIL import Image
import webbrowser
import py7zr
import rarfile
import os
import PyPDF2

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
    def compress_to_7z(file_paths, output_path):
        with py7zr.SevenZipFile(output_path + '.7z', 'w') as archive_7z:
            for file_path in file_paths:
                archive_7z.write(file_path, os.path.basename(file_path))
    @staticmethod
    def compress_to_rar(file_paths, output_path):
        with rarfile.RarFile(output_path + '.rar', 'w') as archive_rar:
            for file_path in file_paths:
                archive_rar.write(file_path, os.path.basename(file_path))
    @staticmethod
    def show_credits():
        print("This project is developed by Abhineet Raj (GitHub: @abhineetraj1).")
    @staticmethod
    def merge_pdfs(filenames, output_filename):
        merged_pdf = PyPDF2.PdfFileMerger()
        try:
            # Merge all PDF files
            for filename in filenames:
                with open(filename, 'rb') as file:
                    merged_pdf.append(file)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return
        except PyPDF2.PdfReadError:
            print(f"Error: Invalid PDF file '{filename}'.")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        try:
            # Save the merged PDF to the output file
            with open(output_filename, 'wb') as output_file:
                merged_pdf.write(output_file)
        except Exception as e:
            print(f"An error occurred while saving the merged PDF: {e}")
            return
        print(f"Merged PDFs saved to '{output_filename}'.")

print("Welcome to file processing library.\nType 'aritrends.show_credits()' or 'aritrends.open_github()' for more information")
