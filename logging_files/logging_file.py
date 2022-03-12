import logging
import dog

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s    %(levelname)s   %(message)s')
handler = logging.FileHandler('logging_files/driver.log')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("script start")

logger.debug("creating dogs")
for i in range(10):
      d = dog.dog("woofy" + str(i))