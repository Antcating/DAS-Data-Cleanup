import os
import datetime

from config import PATH, NASPATH
from log.main_logger import logger as log


def deleting_old_files():
    if os.path.exists(os.path.join(NASPATH, "last")):
        with open(os.path.join(NASPATH, "last"), "r", encoding='utf-8') as f:
            last_timestamp = float(f.readlines()[0].strip())
    last_timestamp -= 86400 * 3

    for data_dir in sorted(os.listdir(PATH)):
        if os.path.isdir(os.path.join(PATH, data_dir)):
            print(os.path.getmtime(os.path.join(PATH, data_dir)), last_timestamp)
            if last_timestamp > datetime.datetime.strptime(data_dir, "%Y%m%d").timestamp():
                log.info(f"Deleting {data_dir}")
                if os.name == "nt":
                    # Delete dir in Windows
                    os.system(f"rmdir /s /q {os.path.join(PATH, data_dir)}")
                elif os.name == "posix":
                    # Delete dir in Linux
                    os.system(f"rm -rf {os.path.join(PATH, data_dir)}")
            else:
                log.info("Skipping %s, too new", data_dir)

if "__main__" == __name__:
    deleting_old_files()
    log.info("Done!")