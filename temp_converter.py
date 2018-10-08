
import logging

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levename)s:%(message)s')



def doConversion():
    tempInFAsString = input('Enter the temperature in Farenheit: ')
    tempInF = float( tempInFAsString )
    tempInC = (tempInF - 32) * (5/9)
    logging.debug(tempInC)

for conversionCount in range( 3 ):
    doConversion()
