import os
import shutil
import time
from moduletest import classify

result_path = "imgsfolders"
listen_path = r"listen"
while True:

    if len(os.listdir(listen_path)) != 0:

        # Deleting older result
        if len(os.listdir(result_path)) != 0:
            for filename in os.listdir(result_path):
                shutil.rmtree(os.path.join(result_path, filename))

        classify(listen_path)
        for filename in os.listdir(listen_path):

            os.remove(os.path.join(listen_path, filename))
            print("Deleted ->", filename)
            time.sleep(1.0)

            if len(os.listdir(listen_path)) == 0:
                break
    else:
        print("No file found! recheck starts in 3 second...")
        time.sleep(3.0)

#static ip
#aws cred
