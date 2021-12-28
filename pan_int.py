import re

def check_image_quality(rc_data):
    cnt = 0
    total = len(rc_data)
    for i in range(len(rc_data)):
        if rc_data[i]:
            cnt = cnt + 1
    confidence_level = (cnt / total) * 100
    confidence_level = round(confidence_level, 2)
    confidence_level = str(confidence_level) + "%"
    return confidence_level


def icr_pan(json_data):
    print("PAN ICR")

    pan_data = ["", "", "", ""]
    type_of_doc_flag = ""
    name_after_department = 0
    pan2_name_flag = 0
    pan2_father_name_flag = 0
    pan2_dob_flag = 0
    pan1_dob_flag = 0
    for i in range(len(json_data)):
        if str(json_data[i].get("text")).upper().__contains__("DEPARTMENT") and "PERMANENT" not in str(
                json_data[i + 2].get("text")).upper():
            if 'INDIA' not in str(json_data[i + 1].get("text")).upper():
                pan_data[0] = json_data[i + 1].get("text")
                name_after_department = 1

            for j in range(len(json_data)):
                if str(json_data[j].get("text")).upper().__contains__("OF") and str(
                        json_data[j].get("text")).upper().__contains__("INDIA") and str(
                        json_data[j].get("text")).upper().__contains__("GOVT"):
                    if name_after_department == 0:
                        # print("Full Name  :",json_data[j + 1].get("text"))
                        pattern = '[0-9]'
                        pan_data[0] = (re.sub(pattern, '', json_data[j + 1].get("text")))
                        # father_name = json_data[j + 2].get("text")
                    else:
                        pattern = '[0-9]'
                        pan_data[1] = (re.sub(pattern, '', json_data[j + 1].get("text")))
                        father_name = json_data[j + 1].get("text")
                        # print(father_name)

                    try:
                        if str(json_data[j + 2].get("text")).upper().replace(" ", "").isalpha():
                            pan_data[1] = (re.sub(pattern, '', json_data[j + 2].get("text")))
                            # print("Father Name :", pan_data[1])
                        else:
                            pan_data[1] = (re.sub(pattern, '', json_data[j + 3].get("text")))
                            # print("Father Name :", pan_data[1])
                    except IndexError:
                        pass
                    try:

                        if "/" not in str(json_data[j + 3].get("text")):
                            # print("DOB :", json_data[j + 4].get("text"))
                            pan_data[1] = pan_data[1] + " " + (re.sub(pattern, "", str(json_data[j + 3].get("text"))))
                            pan_data[2] = json_data[j + 4].get("text")
                            try:
                                if "Account" in str(json_data[j + 5].get("text")):
                                    # print("PAN Number :", json_data[j + 6].get("text"))
                                    pan_data[3] = json_data[j + 6].get("text")
                                else:
                                    # print("PAN Number :", json_data[j + 6].get("text"))
                                    pan_data[3] = json_data[j + 6].get("text")
                            except IndexError:
                                pass

                    except IndexError:
                        pass

                elif str(json_data[j].get("text")).__contains__("/") and str(json_data[j].get("text")).replace("/",
                                                                                                               "").replace(
                        " ", "").isdigit() and pan1_dob_flag == 0:
                    # print("DOB :", json_data[j].get("text"))
                    pan_data[2] = json_data[j].get("text").replace(" ", "")
                    pan1_dob_flag = 1
                elif "Account" in str(json_data[j].get("text")):
                    if str(json_data[j + 1].get("text")).__contains__("-"):
                        # print("PAN Number :", json_data[j + 2].get("text"))
                        pan_data[3] = json_data[j + 2].get("text")
                    else:
                        # print("PAN Number :", json_data[j + 1].get("text"))
                        pan_data[3] = json_data[j + 1].get("text")

                    # else:
                    #     print("PAN Number :", json_data[j + 1].get("text"))
            break

        elif str(json_data[i].get("text")).upper().__contains__("PERMANENT") and str(
                json_data[i].get("text")).upper().__contains__("ACCOUNT"):
            # print("Pan Number :",json_data[i+1].get("text"))
            pan_data[3] = json_data[i + 1].get("text")
            if 'NAME' not in json_data[i + 2].get("text").upper():
                pan_data[0] = json_data[i + 2].get("text")

            for j in range(len(json_data)):
                if pan2_name_flag == 0 and str(json_data[j].get("text")).upper().__contains__(
                        "NAME") and "FATHER" not in str(json_data[j].get("text")).upper():
                    for k in range(len(json_data)):
                        if abs(json_data[k].get("boundingBox")[1] - json_data[j].get("boundingBox")[7] < 35) and k > j:

                            pan_data[0] = json_data[k].get("text").lstrip()
                            # print(pan_data[0])
                            pan2_name_flag = 1
                            if json_data[k + 1].get("text").upper().isalpha():
                                pan_data[0] = (pan_data[0] + " " + json_data[k + 1].get("text")).lstrip()
                            break



                elif pan2_father_name_flag == 0 and str(json_data[j].get("text")).upper().__contains__("FATHER"):

                    for k in range(len(json_data)):
                        if abs(json_data[k].get("boundingBox")[1] - json_data[j].get("boundingBox")[7] < 35) and k > j:
                            pan_data[1] = json_data[k].get("text").lstrip()
                            # print(pan_data[1])
                            pan2_father_name_flag = 1
                            if json_data[k + 1].get("text").upper().isalpha():
                                pan_data[1] = (pan_data[1] + " " + json_data[k + 1].get("text")).lstrip()
                            break

                elif pan2_dob_flag == 0 and (str(json_data[j].get("text")).upper().__contains__("DATE") or str(
                        json_data[j].get("text")).upper().__contains__("BIRTH")):
                    for k in range(len(json_data)):
                        if json_data[k].get("boundingBox")[1] - json_data[j].get("boundingBox")[7] < 35 and (
                                str(json_data[k].get("text")).upper().__contains__("-") or str(
                                json_data[k].get("text")).upper().__contains__("/")) and k > j:
                            # print("DOB : ",json_data[k].get("text"))
                            pan_data[2] = json_data[k].get("text").lstrip()

                            pan2_dob_flag = 1
                            break
                elif pan2_dob_flag == 0 and str(json_data[j].get("text")).upper().__contains__("/") and str(
                        json_data[j].get("text")).upper().replace("/", "").replace(" ", "").isdigit():
                    pan_data[2] = json_data[j].get("text").lstrip()
                    pan2_dob_flag = 1
    if pan_data[1].upper().__contains__("PERMANENT") or pan_data[1].upper().__contains__("NUMBER") or pan_data[
        1].upper().__contains__("ACCOUNT"):
        pan_data[1] = ''
        if name_after_department == 1:
            pan_data[1] = father_name

    if pan_data[3].upper().isdigit():
        pan_data[3] = ''
    pan_json = {
        "full_name" : pan_data[0],
        "father_name" : pan_data[1],
        "dob" : pan_data[2],
        "pan_number" : pan_data[3]
    }

    print("ENDING PAN CARD ICR")

    return pan_json


