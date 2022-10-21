import imp
import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub

book = epub.read_epub('books/213d36.epub')
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return ''.join(text)

texts = {}
for c in items:
    texts[c.get_name()] = chapter_to_str(c)

with open('test.txt', mode='w') as my_file:
    text = my_file.write((str(texts)).upper())
