import imapclient
import getpass

impObj = imapclient.IMAPClient('imap.gmail.com', ssl = True)
password = getpass.getpass()
impObj.login('yeashinr@gmail.com', password)
impObj.select_folder('[Gmail]/Spam', readonly = True)
UIDs = impObj.search(['FROM', 'noreply@r.grouponmail.ca'])
print(UIDs)
