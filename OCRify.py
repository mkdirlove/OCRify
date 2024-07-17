import os
import json
import requests
import argparse

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

banner = f"""{bcolors.WARNING}
┏┓┏┓┳┓•┏  
┃┃┃ ┣┫┓╋┓┏ {bcolors.GREEN}{bcolors.BOLD}v1.0-dev{bcolors.ENDC}{bcolors.WARNING}
┗┛┗┛┛┗┗┛┗┫
         ┛{bcolors.ENDC}
{bcolors.BLUE}{bcolors.BOLD}Made with ❤️  by {bcolors.FAIL}@mkdirlove{bcolors.ENDC}{bcolors.GREEN}
"""
    
def ocr_space_file(filename, overlay=False, api_key='K89070197588957', language='eng'):
    """
    OCR.space API request with local file.

    :param filename: str - Path to your file.
    :param overlay: bool - Is OCR.space overlay required in your response. Defaults to False.
    :param api_key: str - OCR.space API key. Defaults to 'K89070197588957'.
    :param language: str - Language code to be used in OCR. Defaults to 'eng'.
                    List of available language codes can be found on https://ocr.space/OCRAPI
    :return: str - Parsed text from the response.
    """
    payload = {
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language,
    }
    with open(filename, 'rb') as f:
        response = requests.post(
            'https://api.ocr.space/parse/image',
            files={filename: f},
            data=payload
        )
    result = response.content.decode()
    result_json = json.loads(result)
    return result_json['ParsedResults'][0]['ParsedText']


def ocr_space_url(url, overlay=False, api_key='K89070197588957', language='eng'):
    """
    OCR.space API request with remote file.

    :param url: str - Image URL.
    :param overlay: bool - Is OCR.space overlay required in your response. Defaults to False.
    :param api_key: str - OCR.space API key. Defaults to 'K89070197588957'.
    :param language: str - Language code to be used in OCR. Defaults to 'eng'.
                    List of available language codes can be found on https://ocr.space/OCRAPI
    :return: str - Parsed text from the response.
    """
    payload = {
        'url': url,
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language,
    }
    response = requests.post(
        'https://api.ocr.space/parse/image',
        data=payload
    )
    result = response.content.decode()
    result_json = json.loads(result)
    return result_json['ParsedResults'][0]['ParsedText']


def main():
    os.system("clear")
    print(banner)
    parser = argparse.ArgumentParser(description='OCRify - A user-friendly command-line tool that extracts texts in images.')
    parser.add_argument('-f', '--filename', type=str, help='Path to the image file.')
    parser.add_argument('-u', '--url', type=str, help='URL of the image.')
    parser.add_argument('-o', '--output', type=str, help='Output text file.')

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    else:
        result = ""
        if args.filename:
            result = ocr_space_file(filename=args.filename)
        elif args.url:
            result = ocr_space_url(url=args.url)

        if result:
            if args.output:
                with open(args.output, 'w') as output_file:
                    output_file.write(result)
            else:
                print(result)


if __name__ == '__main__':
    main()
