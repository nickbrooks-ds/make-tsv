import os, hashlib, base64


def get_checksum(filename):
    # create an MD5 hash object
    md5_hash = hashlib.md5()

    # read the file
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)

    # get binary digest of hash
    md5_digest = md5_hash.digest()

    # encode in base64 and return
    md5_base64 = base64.b64encode(md5_digest).decode('utf-8')

    return md5_base64


BK_DIR = '/Users/nick/Documents/books'
PREFIX = 'https://raw.githubusercontent.com/nickbrooks-ds/make-tsv/main/books/'

# get the list of all books in the book directory
book_list = os.listdir(BK_DIR)

# remove the .DS_store file from the list (should it be there)
book_list.remove('.DS_Store')

# create tsv file and print header line to tsv
f = open('/Users/nick/Documents/books/books.tsv', 'x')
f.write('TsvHttpData-1.0\n')

# loop through the files and get the byte size for each file, get checksum, and print to file
for book in book_list:
    bookstats = os.stat(BK_DIR + '/' + book)
    bytes = bookstats.st_size
    checksum = get_checksum(BK_DIR + '/' + book)
    f.write(PREFIX + book + '\t' + str(bytes) + '\t' + checksum + '\n')



