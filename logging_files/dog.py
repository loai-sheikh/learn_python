import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s    %(levelname)s   %(message)s')

handler = logging.FileHandler('logging_files/dog.log')
handler.setFormatter(formatter)
logger.addHandler(handler)


class dog:
      def __init__(self, name):
            self.name = name
            logger.info(f"doggo {name} created!")