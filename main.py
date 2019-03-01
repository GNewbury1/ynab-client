import os
import base64
import logging
import logging.handlers
import ynab.objects.transaction

logger = logging.getLogger('YNABPython')
logger.setLevel(logging.DEBUG)

fh = logging.handlers.SysLogHandler(address = '/dev/log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

def connect_api():
    if not os.path.isfile('./config/access.conf'):
        logger.debug('Api Key not found. Getting user to enter it')
        apikey = input('Please enter your YNAB API key: ')
        apikeyEncoded = base64.b64encode(apikey)
        f = open('.config/access.conf', 'w')
        f.write()
        f.close()
    else:
        f = open('./config/access.conf', 'r')
        apikeyEncoded = f.read()
        f.close()
        apiKey = base64.b64decode(apikeyEncoded)

def main():
    #api = connect_api()
    trans = ynab.objects.transaction.transaction('01/01/19','test','category:test','0.00','1.00','test')
    print(trans.to_dict())

if __name__ == '__main__':
    main()
