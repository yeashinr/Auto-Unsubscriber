import imapclient
import getpass
import requests
from bs4 import BeautifulSoup
import pyzmail

impObj = imapclient.IMAPClient('imap.gmail.com', ssl = True)
password = getpass.getpass()
impObj.login('yeashinr@gmail.com', password)
impObj.select_folder('[Gmail]/Spam', readonly = True)
UIDs = impObj.search(['FROM', 'noreply@r.grouponmail.ca'])
obj =impObj.fetch(UIDs,['BODY[]'])
message = pyzmail.PyzMessage.factory(obj[12472][b'BODY[]'])

if message.text_part == None:
    aa = message.html_part.get_payload().decode(message.html_part.charset)
    soup = BeautifulSoup(aa, 'lxml')
    print(soup.prettify())



# #print(obj)
# for msgNum in UIDs:
#     message = pyzmail.PyzMessage.factory(UIDs[msgNum][b'BODY[]'])
#     print(message)




