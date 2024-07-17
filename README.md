<h1 align="center">
  <br>
  <a href="https://github.com/mkdirlove/OCRify"><img src="https://github.com/mkdirlove/OCRify/blob/main/logo.png" alt="OCRify"></a>
  <br>
  Process images with OCR.space API.
  <br>
</h1>

#### Installation

Copy-paste this into your terminal:

```sh
git clone https://github.com/mkdirlove/OCRify.git
```
```
cd OCRify
```
```
python3 OCRify.py
```
or
```
python3 OCRify.py -h
```
#### Usage
``` 
┏┓┏┓┳┓•┏  
┃┃┃ ┣┫┓╋┓┏ v1.0-dev
┗┛┗┛┛┗┗┛┗┫
         ┛
Made with ❤️  by @mkdirlove

usage: OCRify.py [-h] [-f FILENAME] [-u URL] [-o OUTPUT]

OCRify - Process images with OCR.space API.

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Path to the image file.
  -u URL, --url URL     URL of the image.
  -o OUTPUT, --output OUTPUT
                        Output text file.

```
#### Example

Using local file as input
```
python3 OCRify.py --filename sample.png --output result.txt
```

Using url as input
```
python OCRify.py --url http://i.imgur.com/31d5L5y.jpg --output result.txt
```
