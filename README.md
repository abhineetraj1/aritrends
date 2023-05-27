# Aritrends

Open source python lib from file processing work. Instead of writing old multiline codes, just write one line code and complete your work quickly and efficently.

##  Installation

*	Install git command and python3.10 in your system.
*	Enter the following code in your terminal.

```
git clone https://github.com/abhineetraj1/aritrends
cd aritrends
pip3 install -r requirements.txt
```

## Command execution guide

### Convert Word file into pdf
This code will convert word file into pdf file
```
from aritrends import aritrends as w
w.convert("/path/to/folder/filename.docx")
```

### Convert multiple images to pdf
This code will convert multiple image file (*.png) to pdf
```
from aritrends import aritrends as w
list = ["/path/to/folder/image1.png","/path/to/folder/image2.png","/path/to/folder/image3.png"]
w.image2pdf(list)
```

### Generate qrcode
This will generate qrcode of input text.
```
from aritrends import aritrends as w
w.qrcode("Hello world !")
```

### Convert multiple files into zip
This code will compress all files into zip
```
from aritrends import aritrends as w
list = ["/path/to/folder/filename.exe","/path/to/folder/filename2.png","/path/to/folder/filename3.dart"]
w.zip(list)
```

### Write text on image file (*.png)
This code will save text on image.
```
from aritrends import aritrends as w
w.write_text_on_image("Hello World","/path/to/folder/filename.png",["Arial",35])
```

## Compress files to rar
This code will compress multiple files to *.rar
```
from aritrends import aritrends as w
list = ["/path/to/folder/filename.exe","/path/to/folder/filename2.png","/path/to/folder/filename3.dart"]
w.compress_to_rar(list, filename.rar)
```

## Compress files to 7z
This code will compress multiple files to *.7z
```
from aritrends import aritrends as w
list = ["/path/to/folder/filename.exe","/path/to/folder/filename2.png","/path/to/folder/filename3.dart"]
w.compress_to_7z(list, filename.7z)
```

## Programming language used
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>

## Developer

[@abhineetraj1](https://github.com/abhineetraj1)
