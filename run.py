import json
import os
import shutil
import time
from moduletest import classify
from pan_int import icr_pan
from aadhar_int import icr_aadhaar
from dischargeSum import dis_sum

result_path = "imgsfolders"
listen_path = r"listen"
while True:

    if len(os.listdir(listen_path)) != 0:

        # Deleting older result
        if len(os.listdir(result_path)) != 0:
            for filename in os.listdir(result_path):
                shutil.rmtree(os.path.join(result_path, filename))

        # Call Main Function
        documents, result = classify(listen_path)
        print("result ---->", result)

        # JSON file
        f = open('all_bill.json', "r")

        # Reading from file
        data = json.loads(f.read())

        discharge_visit = False

        for cls in result['documents']:
            print("cls ----->", result['documents'][cls])
            txt_json = next(v for i, v in enumerate(data.values()) if i == int(cls)-1)
            # print("value ----->",txt_json)
            if result['documents'][cls] == "pan":
                res_pan = icr_pan(txt_json)
                print(res_pan)
            elif result['documents'][cls] == "aadhar":
                res_aadhar = icr_aadhaar(txt_json)
                print(res_aadhar)
            elif discharge_visit == False and result['documents'][cls] == "dischargesheet":
                print("cls ----->", cls)
                list_of_json = [txt_json]
                discharge_visit = True
                for q in range(int(cls)+1,len(result['documents'])):
                    print("q ----->", q)
                    if result['documents'][str(q)] == "dischargesheet":
                        txt_json = next(v for i, v in enumerate(data.values()) if i == int(q) - 1)
                        list_of_json.append(txt_json)
                    else:
                        break
                dis_sum(list_of_json)
                print("len list_of_json:",len(list_of_json))


        # Deleting the ran one
        for filename in os.listdir(listen_path):
            break

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
