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
import aritrends as w
w.convert("/path/to/folder/filename.docx")
```

### Convert multiple images to pdf
This code will convert multiple image file (*.png) to pdf
```
import aritrends as w
list = ["/path/to/folder/image1.png","/path/to/folder/image2.png","/path/to/folder/image3.png"]
w.image2pdf(list)
```

### Generate qrcode
This will generate qrcode of input text.
```
import aritrends as w
w.qrcode("Hello world !")
```

### Convert multiple files into zip
This code will compress all files into zip
```
import aritrends as w
list = ["/path/to/folder/filename.exe","/path/to/folder/filename2.png","/path/to/folder/filename3.dart"]
w.zip(list)
```

### Write text on image file (*.png)
This code will save text on image.
```
import aritrends as w
w.write_text_on_image("Hello World","/path/to/folder/filename.png",["Arial",35])
```

## Developer

[@abhineetraj1](https://github.com/abhineetraj1)
