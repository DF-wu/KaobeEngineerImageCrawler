import requests
from bs4 import BeautifulSoup
import os
def htmlPaserAndDownloader(CategoryTag,pathFix):

    url = 'https://kaobei.engineer/rankings/'+ CategoryTag
    tag = '.col-block a img'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')

    index = 0
    for img in soup.select(tag):
        index += 1
        img_data = requests.get(img.get('src')).content

        if not os.path.isdir(pathFix):
            os.mkdir(pathFix)
        with open( pathFix + '/' + 'top_{}.jpg'.format(index), 'wb') as handler:
            handler.write(img_data)
    print('file downloaded')
    print('done')

if __name__ == '__main__':
    print("Execute locally")