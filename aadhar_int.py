import pandas as pd
import re

def remove_dates(date_data):

    date_data = re.sub(r'(\d)\s+(\d)', r'\1\2', date_data)
    date_data = re.sub(r'\d{2}/\d{2}/\d{2,4}', '', date_data)
    numbers = re.findall('[0-9]+', date_data)
    for num in numbers:
        if len(num)>=4:
            date_data = re.sub(num, '', date_data)
    date_data = date_data.lstrip().rstrip()

    #print(date_data, date_data[4])
    return date_data

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

def icr_aadhaar(json_data):
    aadhar_data = ["", "", "", "", "", "", "", ""]
    pincode = []
    aadhar_text = ""
    temp = []
    index = 0
    address_to =[]
    add_var =[]
    address_flag=0
    to_flag =""
    add_flag = ""
    father_flag = 0
    temp_name = ""
    print("starting Aadhaar ICR")
    data = pd.DataFrame(json_data)
    data['text'] = data.text.str.replace("  ", " ")

    for text in data.text:
        aadhar_text = aadhar_text + " " + text.replace(" ","")

    numbers = re.findall('[0-9]+', aadhar_text)

    for num in numbers:
        if len(num) == 6:
            pincode.append(num)
    pincode = list(dict.fromkeys(pincode))
    # for pin in pincode:
    #
    #     try:
    #         app = create_app()
    #         df_pin = pd.read_csv(app.config['DATASET_PATH'] + "/" + app.config['PINCODE'], encoding="ISO-8859-1").applymap(str)
    #         cols = ["Pincode", "City", "StateName"]
    #         proper_pin = df_pin[cols]
    #         match_pin = proper_pin[proper_pin['Pincode'].str.match(pin)]
    #         final_city = match_pin["City"].iloc[0].title()
    #         final_state = match_pin["StateName"].iloc[0].title()
    #         # print(final_state)
    #         aadhar_data[6] = final_state.upper().lstrip()
    #         aadhar_data[5] = final_city.upper().lstrip()
    #         aadhar_data[7] = pin
    #
    #     except IndexError:
    #         pass


    for i in range(len(json_data)):
            # print(str(json_data[i].get("text")))
            if str(json_data[i].get("text")).replace(" ","").isdigit() and len(str(json_data[i].get("text")).replace(" ","")) == 12:
                # print("Aadhar Number :",json_data[i].get("text"))
                aadhar_data[0] = json_data[i].get("text").lstrip()
                # break
            elif str(json_data[i].get("text")).upper().__contains__("DOB") or str(json_data[i].get("text")).upper().__contains__("YEAR") or str(json_data[i].get("text")).upper().__contains__("DO8"):
                if str(json_data[i].get("text")).upper().__contains__("DOB") or str(json_data[i].get("text")).upper().__contains__("DO8"):
                    # print("DOB :",str(json_data[i].get("text")).split("DOB")[1].replace(":","").replace(" ",""))
                    try:
                        aadhar_data[1] =re.split("DOB|DO8",str((json_data[i].get("text"))))[1].replace(":","").replace(" ","")

                        if aadhar_data[1].replace("/", "").replace(" ", "").isdigit():
                            aadhar_data[1] = str(
                                (json_data[i].get("text")).split("DOB")[1].replace(":", "").replace(" ", ""))
                        else:
                            aadhar_data[1] = str(
                                (json_data[i].get("text")).split("DOB")[2].replace(":", "").replace(" ", ""))

                    except IndexError:
                        pass
                else:
                    # print("DOB :", (str(json_data[i].get("text")).replace(" ","")[-4:]))
                    aadhar_data[1]= (str((json_data[i].get("text")).replace(" ","")[-4:]))

                if str(json_data[i -1].get("text")).upper().__contains__("ADDRESS"):
                    if str(json_data[i -1].get("text")).upper().isdigit():
                        print("Name :",json_data[i - 3].get("text"))
                        aadhar_data[2]= json_data[i - 3].get("text").replace("Father","").replace(":","").lstrip()
                    else:
                        print("Name :", json_data[i - 2].get("text"))
                        aadhar_data[2]= json_data[i - 2].get("text").replace("Father","").replace(":","").lstrip()
                else:
                    if str(json_data[i - 1].get("text")).upper().isdigit():
                        print("Name :", json_data[i - 2].get("text"))
                        aadhar_data[2]= json_data[i - 2].get("text").replace("Father","").replace(":","").lstrip()
                    else:
                        print("Name :", json_data[i - 1].get("text"))
                        aadhar_data[2]= json_data[i - 1].get("text").replace("Father","").replace(":","").lstrip()
            elif str(json_data[i].get("text")).upper().__contains__("FATHER") and father_flag == 0:
                if str(json_data[i - 1].get("text")).replace(" ", "").replace(".", "").replace(":", "").isalpha():
                    temp_name = json_data[i - 1].get("text")
                    father_flag = 1
            elif str(json_data[i].get("text")).upper().__contains__("ADDRESS") and 'MAIL' not in str(json_data[i].get("text")).upper() and address_flag == 0:
                add_flag = "YES"
                address_flag = 1



                for k in range(len(json_data)):
                    if (k > i and abs(json_data[k].get('boundingBox')[1] - json_data[i].get('boundingBox')[7]) < 180 and \
                        abs(json_data[k].get('boundingBox')[0] - json_data[i].get('boundingBox')[6]) < 180):
                        temp.append(json_data[k].get("text"))

            elif str(json_data[i].get("text")).upper().__contains__("TO") and address_flag == 0:
                to_flag = "YES"


                for k in range(len(json_data)):
                    if (k > i and abs(json_data[k].get('boundingBox')[1] - json_data[i].get('boundingBox')[7]) < 250 and \
                        abs(json_data[k].get('boundingBox')[0] - json_data[i].get('boundingBox')[6]) < 100):
                        address_to.append(json_data[k].get("text"))
                        if (str(json_data[k].get("text")).upper().replace(" ", "").isdigit() and len(
                                str(json_data[k].get("text")).replace(" ", "")) > 8) or str(
                            json_data[k].get("text")).upper().__contains__("RET"):
                            #print(address_to)
                            address_flag = 1
                            break
    if father_flag == 1:
         aadhar_data[2]=temp_name
    if to_flag =="YES":
        add_var = address_to
    elif add_flag == "YES":
        add_var=temp
    elif add_flag == "YES" and to_flag == "YES":
        add_var=temp
    print("add_var :", add_var)

    for i in range(len(add_var)):
        if i == 0 or i == 1:
            aadhar_data[3] = aadhar_data[3]+" "+add_var[i].upper()


        else:
            aadhar_data[4] = (aadhar_data[4] + " " + add_var[i]).upper()

    aadhar_data[3]=remove_dates(aadhar_data[3])
    #aadhar_data[4] = re.sub(r'[0-9]+', '', aadhar_data[4])
    aadhar_data[4] = remove_dates(aadhar_data[4])
    aadhar_image_quality=check_image_quality(aadhar_data)

    aadhar_json={
        "aadhar number" : aadhar_data[0],
        "dob" : aadhar_data[1],
        "name" : aadhar_data[2],
        "address line 1" : aadhar_data[3],
        "address line 2" : aadhar_data[4],
        "city" : aadhar_data[5],
        "state" : aadhar_data[6],
        "pincode" : aadhar_data[7]
    }

    return aadhar_json

def icr_aadhaar_back(json_data):
    aadhar_data = ["", "", "", "", "", "", "", ""]
    pincode = []
    aadhar_text = ""
    temp=[]
    index=0
    to_flag = ""
    address_flag = 0

    print("starting Aadhaar Back ICR")

    data = pd.DataFrame(json_data)
    data['text'] = data.text.str.replace("  ", " ")

    for text in data.text:
        aadhar_text = aadhar_text + " " + text

    numbers = re.findall('[0-9]+', aadhar_text)

    for num in numbers:
        if len(num) == 6:
            pincode.append(num)
    pincode = list(dict.fromkeys(pincode))
    # print(pincode)
    # app = create_app()
    # for pin in pincode:
    #
    #     try:
    #         df_pin = pd.read_csv(app.config['DATASET_PATH'] + "/" + app.config['PINCODE'], encoding="ISO-8859-1").applymap(str)
    #         cols = ["Pincode", "City", "StateName"]
    #         proper_pin = df_pin[cols]
    #         match_pin = proper_pin[proper_pin['Pincode'].str.match(pin)]
    #         final_city = match_pin["City"].iloc[0].title()
    #         final_state = match_pin["StateName"].iloc[0].title()
    #         # print(final_state)
    #         aadhar_data[6] = final_state.upper().lstrip()
    #         aadhar_data[5] = final_city.upper().lstrip()
    #         aadhar_data[7] = pin
    #
    #
    #
    #     except IndexError:
    #         pass


    for i in range(len(json_data)):

        ###########################################################################################################################
        if str(json_data[i].get("text")).upper().__contains__("ADDRESS") and address_flag==0:

            for k in range(len(json_data)):
                if (k > i and abs(json_data[k].get('boundingBox')[1] - json_data[i].get('boundingBox')[7]) < 180 and \
                        abs(json_data[k].get('boundingBox')[0] - json_data[i].get('boundingBox')[6]) < 180):
                    temp.append(json_data[k].get("text"))


            break






    for i in range(len(temp)):
        if i==0:
            aadhar_data[3]=temp[i]
        else:
            aadhar_data[4] = aadhar_data[4]+" "+temp[i]
    aadhar_data[3]=aadhar_data[3].lstrip().rstrip()
    aadhar_data[4]=remove_dates(aadhar_data[4])
    aadhar_data[4] = aadhar_data[4].lstrip().rstrip()

    aadhar_json = {
        "aadhar number": '',
        "dob": '',
        "name": '',
        "address line 1": aadhar_data[3],
        "address line 2": aadhar_data[4],
        "city": aadhar_data[5],
        "state": aadhar_data[6],
        "pincode": aadhar_data[7]
    }

    return aadhar_json
