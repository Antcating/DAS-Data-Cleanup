import os 
import datetime

from config import PATH
from log.main_logger import logger as log


def deleting_old_files():
    today_date = datetime.datetime.now()
    delete_before = today_date - datetime.timedelta(days=3)

    for data_dir in os.listdir(PATH):
        if os.path.isdir(os.path.join(PATH, data_dir)):
            log.info(f"Checking {data_dir}")
            if datetime.datetime.fromtimestamp(
                os.path.getmtime(
                    os.path.join(PATH, data_dir))
                    ) < delete_before:
                if ".completed" in os.listdir(os.path.join(PATH, data_dir)):
                    os.system(f"rm -rf {os.path.join(PATH, data_dir)}")
                    log.info(f"Deleting {data_dir}")
                else:
                    log.warning(f"Skipping {data_dir}, .completed not found")
            else:
                log.info(f"Skipping {data_dir}, too new")


if "__main__" == __name__:
    deleting_old_files()
    log.info("Done!")