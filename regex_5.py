# mahdi mohammadi khah 982011056

import re


def urls_finder(text):
    urls = re.findall(r'href="([^"]+)"', text)
    return urls


input_text = input()
urls = urls_finder(input_text)
print(f'Urls: {urls}')