import os
import json
from typing import Union, List, Dict
# from logger import logger, get_logger

class Datastorage:

    def __init__(self, content_dir, logger=None):
        self.CONTENT_DIR = content_dir
        self._permalink = None
        self.logger = logger
        # self.permalink = str(permalink)

    @property
    def permalink(self):
        return self._permalink
    
    @permalink.setter
    def permalink(self, value):
        self._permalink = str(value)


    def mkdir(self, permalink = None):
        if permalink:
            self.permalink = permalink
        os.makedirs(os.path.join(self.CONTENT_DIR, self.permalink), exist_ok=True)



    def load_content(self, filename: str) -> str:
        try:
            path_to_file = os.path.join(self.CONTENT_DIR, self.permalink, filename)
            with open(path_to_file, mode='r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return None
        



    def saveContent(self, filename: str, content: str) -> bool:
        permalink = self.permalink
        logger = self.logger.get_logger(permalink)
        try:
            path_to_file = os.path.join(self.CONTENT_DIR, self.permalink, filename)
            if os.path.exists(path_to_file):
                print(f"{path_to_file} found")
                logger.info(f"{path_to_file} found")
                path_to_newfile = os.path.join(self.CONTENT_DIR, self.permalink, f"bak_{filename}")
                try:
                    os.rename(path_to_file, path_to_newfile)
                    logger.info(f"File {filename} was successfully renamed to bak_{filename}")
                except Exception as exc_info:
                    logger.error(exc_info)
            with open(path_to_file, mode='w', encoding='utf-8') as file:
                file.write(content)

            # logger.info(f'{filename} / ok')
        except Exception as exc_info:
            # logger.error(exc_info)
            return False
        

    def save_json(self, filename: str, obj: dict={}, replace=False) -> bool:
        permalink = self.permalink
        # logger = self.logger.get_logger(permalink)
        logger = self.logger.get_logger(permalink)
        try:
            path_to_file = os.path.join(self.CONTENT_DIR, permalink, filename)
            if os.path.exists(path_to_file) and not replace:
                try:
                    logger.warn('File already exists')
                except Exception:
                    print('File already exists')
                finally:
                    return

            with open(path_to_file, mode='w', encoding='utf-8') as file:
                json.dump(obj, file, ensure_ascii=False, indent=4)

            # logger.info(f'{filename} / ok')
        except Exception as exc_info:
            logger.error(exc_info)
            return False
        
    
    def load_json(self, filename: str) -> Union[List, Dict]:
        permalink = self.permalink
        path_to_file = os.path.join(self.CONTENT_DIR, permalink, filename)

        with open(path_to_file, mode='r', encoding='utf-8') as file:
            return json.load(file)