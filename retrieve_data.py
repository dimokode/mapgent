import os
from dotenv import load_dotenv
from dataStorage import Datastorage

from logger2 import Logme


load_dotenv()

CONTENT_DIR = os.getenv('CONTENT_DIR')

logme = Logme(fn='inference.log', root_logger_name='inference')
main_logger = logme.create()


def get_data_by_permalink(permalink) -> dict:
    permalink = str(permalink)
    main_logger.info(f'Permalink: {permalink}')

    path_to_extracted_data = os.path.join(CONTENT_DIR, permalink, 'extracted.json')
    if(os.path.exists(path_to_extracted_data)):
        ds = Datastorage(CONTENT_DIR, logger=main_logger)
        ds.permalink = permalink
        if data:= ds.load_json('extracted.json'):
            main_logger.info('extracted.json found and loaded')
            return data
    else:
        main_logger.info(f'Retrieve data from internet')
        print('Retrieve data from internet')
        return {}


if __name__ == "__main__":
    data = get_data_by_permalink(244474102223)
    print(data)