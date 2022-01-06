import json
import os
import random
import re

from fuzzywuzzy import fuzz

from moduletest import get_icr_data_from_image, converting_to_image

def converti():
    BASE_IMGS_FOLDER = r"imgsfolders"
    MAIN_DIR = "listen"

    random_id = str(random.randint(300, 6000))
    os.mkdir(BASE_IMGS_FOLDER + '/' + random_id)
    folder = BASE_IMGS_FOLDER + '/' + random_id

    save_path = folder

    for filename in os.listdir(MAIN_DIR):
        print("5--->")
        print(filename)
        eachfilepath = os.path.join(MAIN_DIR, filename)
        print("6--->")
        converting_to_image(eachfilepath, save_path, folder)

# converti()

def jsonslist(img_dir):
    json_list = []
    for filename in os.listdir(img_dir):
        filepath = os.path.join(img_dir, filename)

        text = get_icr_data_from_image(filepath)
        json_list.append(text)

    with open(img_dir+"/jsonslist.json", "w") as outfile:
        json.dump(json_list, outfile)

    return json_list

# json_list = jsonslist(r"F:\iAssist_Projects\iciciClassification\imgsfolders\cbb785a2-1bf5-4937-bcce-6f82cb98c725")

def claim_form_extract(jsonpath):


    # JSON file
    try:
        f = open(jsonpath, "r")

        # Reading from file
        json_list = json.loads(f.read())
    except:
        json_list = jsonpath

    stopkey = {
        "treating_dr_details": [
            "Details of the patient",
            "admitted","Details of the patient",
            "admitted",
            "Nature of Injury/Illness:",
            "Nature of Injury/illness;",
            "Nature of injury/Illness:"
        ],
        "policy_no": [
            "Name of the Policyholder:", "Name","Card No","UHID"
        ],
        "uin_no": [
            "Issuance of this claim form is not to be taken as an admission of liability"
        ],
        "claim_no": [
            "Contact", "Description", "Loss/Event", "Mobile"
        ],
        "policyholder_name": [
            "Name of the Insured Person:", "insured", "Name" ,"Bank","number","Policy","Relationship"
        ],
        "patient/Insured_name": [
            "Card", "UHID","Address","Residential","Gender"
        ],
        "patient_card/uhid": [
            "Gender","Name","Group"
        ],
        "dob": [
            "Gender","age","Completed"
        ],
        "patient/Insured_current_address": [
            "Mobile"
        ],
        "patient/Insured_mobile_no": [
            "Email","Part","Claim","E-mail"
        ],
        "patient_email": [
            "Policy"
        ],
        "insured_person_aadhar_no": [
            "Claimant Details","PAN"
        ],
        "relationship_of_claimant_with_insured_person": [
            "Address","Policy","policy"
        ],
        "address_for_communication": [
            "Contact Details"
        ],
        "claiment_contact_no": [
            "Email Id", "Email id", "Email-id", "Email"
        ],
        "claiment_email_id": [
            "Aadhaar"
        ],
        "claimant_aadhar_no": [
            "insurance",
        ],
        "hospital_name": [
            "Address","Room"
        ],
        "hospital_address": [
            "treating Medical","Mobile no"
        ],
        "hospital_telephone": [
            "Mobile"
        ],
        "hospital_mobile": [
            "ROHINI","Hospital","Details"
        ],
        "rohini_id": [
            "Hospital","Type"
        ],
        "treating_medical_practitioner": [
            "Nature",
        ],
        "nature_of_injury/illness": [
            "treatment",
        ],
        "particulars_of_treatment": [
            "Date and time","Date","time"
        ],
        "admission_date_time": [
            "discharge","Discharge"
        ],
        "discharge_date_time": [
            "days","ICU","Sr No"
        ],
        "number_of_days_in_iCU_(if_any)": [
            "Maternal","Maternal Complication","UIN", "CIN"
        ],
        "maternal_complication_(if_any)": [
            "Reasons for admission",
        ],
        "claimant/insured_person's_name(as_per_bank_records": [
            "Claimant","bank","policy","Bank"
        ],
        "claimant/insured_person's_bank_account_no": [
            "bank","Bank","Name"
        ],
        "name_of_the_bank": [
            "Scanned","Branch","name"
        ],
        "branch_name:": [
            "Address","IFSC","Bank","bank"
        ],
        "bank_address": [
            "IFSC","FSC code"
        ],
        "IFSC_code": [
            "PAN","Pan","Policy","Nominee"
        ],
        "Name of the Insured Person/claimant/Nominee": [
            "Relation",
        ],
        "Relation with the Insured Person": [
            "Place", "Place:"
        ],
        "Place": [
            "Date","Signature"
        ],
        "Date": [
            "",
        ],
        "kyc_contact_no": [
            "PAN", "Pan", "KYC","IRDA", "Circular"
        ],
        "hos_details": [
            ""
        ]
    }

    present_keys = {
        "treating_dr_details":[
            "82. Details of the attending Medical Practitioner/ Doctor/ Treating Physician or Surgeon",
            "B2. Details of the attending Medical Practitioner/ Doctor/ Treating Physician or Surgeon",
            "Name of treating Medical Practitioner:",
        ],
        "policy_no": [
            "Current Policy No.:", "Policy No.:", "Policy No", "Policy No :", "C2. Policy Number"
        ],
        "uin_no": [
            "UIN No.", "UIN No"
        ],
        "claim_no": [
            "Claim Number (if allotted) .", "Claim Number (if allotted):", "Claim Number:", "Claim Number (if allotted) :",
            "Claim No. (If claim has already been registered with ICICI Lombard Health Care):",
            "C5. Claim Number (it allafter :"
        ],
        "policyholder_name": [
            "Name of the Policyholder:", "Name of the Policyholder", "Name of the Policy Holder", "Name of the Policy Holder:",
            "2. Name of the Proposer*:"
        ],
        "patient/Insured_name": [
            "Name of the Patient:","Name of the Patient","Name of Insured:"
        ],
        "patient_card/uhid": [
            "Card No./ UHID of the Patient:", "Card No./ UHID of the Patient","Card No./ UHID No."
        ],
        "dob": [
            "Date of birth:","Date of birth","Date of Birth:"
        ],
        "patient/Insured_current_address": [
            "Current residential address:", "Current residential address","Current Residential Address:"
        ],
        "patient/Insured_mobile_no": [
            "Mobile no.","Mobile No."
        ],
        "patient_email": [
            "Email:"
        ],
        "insured_person_aadhar_no": [
            "Aadhaar Card No. of Insured Person: _", "Aadhaar Card No. of Insured Person:", "Aadhaar Card No. of Insured Person",
            "Aadhar Card No of Insured Person:","Aadhaar No. of Policy Holder:","Aadhaar No. of Policy Holder"
        ],
        "relationship_of_claimant_with_insured_person": [
            "Relationship of claimant with Insured Person:", "Relationship of claimant with Insured Person",
            "Relationship with Proposer*:","Relationship with the Proposer*:"
        ],
        "address_for_communication": [
            "Address for communication"
        ],
        "claiment_contact_no": [
            "Contact Details: Mob._", "Contact Details: Mob.",
        ],
        "claiment_email_id": [
            "Email Id:", "Email Id", "Email id"
        ],
        "claimant_aadhar_no": [
            "Aadhaar Card No. of claimant:", "Aadhaar Card No. of claimant",
        ],
        "hospital_name": [
            "Name of the Hospital/ Nursing home:", "Name of the Hospital:", "Name of the Hospital",
            "Name of hospital where admitted"
        ],
        "hospital_address": [
            "Address of the Hospital","Address:"
        ],
        "hospital_telephone": [
            "Telephone no.:"
        ],
        "hospital_mobile": [
            "Mobile no.:"
        ],
        "rohini_id": [
            "ROHINI ID","ROHINI ID*:"
        ],
        "treating_medical_practitioner": [
            "Name of treating Medical Practitioner:", "Name of treating Medical Practitioner:_"
        ],
        "nature_of_injury/illness": [
            "Nature of Injury/Illness:", "Nature of Injury/illness;", 'Nature of Injury/illness:"', "Nature of injury/Illness:"
        ],
        "particulars_of_treatment": [
            "Particulars of treatment:",
        ],
        "admission_date_time": [
            "Date and time of admission:", "Date Of Admission"
        ],
        "discharge_date_time": [
            "Date and time of discharge:", "Date and time of discharge", "Date Of Discharge"
        ],
        "number_of_days_in_iCU_(if_any)" : [
            "Number of days in ICU (if any):",
        ],
        "maternal_complication_(if_any)" : [
            "Maternal Complication (if any):",
        ],
        "claimant/insured_person's_name(as_per_bank_records": [
            "Claimant /Insured Person's name(as per bank records:", "Claimant /Insured Person's name(as per bank records",
            "Claimant /Insured Person's name(as per bank records:", "Proposer (policy holder)/ Employee name* (as per bank records):",
            ". Proposer (policy holder)/ Employee name* (as per bank records):"
        ],
        "claimant/insured_person's_bank_account_no": [
            "Claimant /Insured Person's bank account no.:","Claimant /Insured Person's bank account no :","Bank account number of Policy Holder:",
            "Proposer/ policy holder Bank account no.:", ". Proposer/ policy holder Bank account no.:"
        ],
        "name_of_the_bank": [
            "Name of the bank:", "Name of the bank", "Name of the bank:", "Name of the Bank","Name of the Bank:"
        ],
        "branch_name:": [
            "Branch name:", "Branch name :","Branch Name:","Branch Name",". Branch name:"
        ],
        "bank_address": [
            "Address of the bank:",". Address of the bank:"
        ],
        "IFSC_code": [
            "IFSC code no. of the bank:", "FSC code no. of the bank:", "IFSC code no, of the bank:",
            "IFSC of the Bank:", ". IFSC code no. of the bank:"
        ],
        "Name of the Insured Person/claimant/Nominee": [
            "Name of the Insured Person/claimant/Nominee:", "Name of the Insured Person/claimant/Nominee:"
        ],
        "Relation with the Insured Person": [
            "Relation with the Insured Person: _","Relation with the Insured Person:", "Relation with the Insured Person"
        ],
        "Place": [
            "Place:", "Place :"
        ],
        "Date": [
            "Date:", "Date :"
        ],
        "kyc_contact_no": [
            "Mobile/ Contact No. ;", "Mobile/ Contact No. :", "Mobile/ Contact No.:"
        ],
        "hos_details" : [
            "B1. Details of the Hospital/ Nursing home in which treatment was taken"
        ]
    }

    result = {}
    visited = {}
    for v in present_keys:
        visited[v] = False
    for json_data in json_list:
        for i in range(len(json_data)):
            print(json_data[i].get("text"))
            listofunique = ["hospital_address"]
            for ext_fld in present_keys:
                # print("Extd :", ext_fld)

                # c_bb = json_data[i].get("boundingBox")
                # n_bb = json_data[i+1].get("boundingBox")
                # print(c_bb[2] , n_bb[0])

                # if ext_fld == "hos_details":




                if visited[ext_fld] == False and json_data[i].get("text") in present_keys[ext_fld] and ext_fld in listofunique:
                    print("iiiiiiii")
                    if ext_fld == "hospital_address":
                        ky_new = ""
                        ky = ext_fld
                        result[ky] = ""
                        brk_flag = False
                        for j in range(i + 1, len(json_data)):
                            txt2insert = json_data[j].get("text").lower()
                            for brk in stopkey[ext_fld]:
                                if brk in json_data[j].get("text"):
                                    brk_flag = True
                                    print("brked", brk)
                            if brk_flag:
                                break
                            for b in ["city", "state", "Pincode", "Telephone no"]:
                                if b in json_data[j].get("text").lower():
                                    ky = "hospital_" + b.lower()
                                    result[ky] = ""
                                    txt2insert = txt2insert.upper().replace(b.upper(),"").strip(":-. ,")
                                    j_flag = True
                                    break
                            # if j_flag:
                            #     ky =
                            print("---'''",ky,json_data[j].get("text"))
                            result[ky] = result[ky] + " " + txt2insert




                elif visited[ext_fld] == False and json_data[i].get("text") in present_keys[ext_fld]:

                    result[ext_fld] = ""
                    b_flag = False
                    for j in range(i+1, len(json_data)):
                        for b in stopkey[ext_fld]:
                            if b in json_data[j].get("text"):
                                b_flag = True
                        if b_flag or json_data[j].get("text") in present_keys[ext_fld]:
                            break
                        else:
                            result[ext_fld] = result[ext_fld] + json_data[j].get("text") + " "
                            visited[ext_fld] = True



                    if ext_fld == "treating_dr_details":
                        print("yes treating_dr_details")
                        dr_details = result[ext_fld]
                        if "Name" in dr_details:
                            dr_details = result[ext_fld].replace("Name","")
                        if "Qualification" in dr_details:
                            result["treating_medical_practitioner"] = dr_details.split("Qualification")[0].strip(": -")
                            dr_details = dr_details.split("Qualification")[1].strip(": -")
                        if "Registration no" in dr_details:
                            result["treating_medical_practitioner_Qualification"] = dr_details.split("Registration no")[0].strip(": -")
                            dr_details = dr_details.split("Registration no")[1].strip(".: -")
                        if "Telephone no" in dr_details:
                            result["treating_medical_practitioner_registration_no"] = dr_details.split("Telephone no")[0].strip(".: -")
                            dr_details = dr_details.split("Telephone no")[1].strip(".: -")
                        if "Mobile no" in dr_details:
                            result["treating_medical_practitioner_Telephone_no"] = dr_details.split("Mobile no")[0].strip(".: -")
                            dr_details = dr_details.split("Mobile no")[1].strip(": -")
                            result["treating_medical_practitioner_Mobile_no"] = dr_details.strip(".: -")







                            # if visited[ext_fld] == False and json_data[i].get("text") in present_keys[ext_fld] and c_bb[2] < n_bb[0]:
                        result[ext_fld] = ""

                #     result[ext_fld] = json_data[i+1].get("text")
                #     visited[ext_fld] = True
                #     break

                else:
                    for eackkey in present_keys[ext_fld]:
                        if visited[ext_fld] == False and json_data[i].get("text").startswith(eackkey) and (len(eackkey)+2) < len(json_data[i].get("text")):
                            # txt = json_data[i].get("text").split(eackkey)
                            # if len(txt[0]) .startswith('Python') eackkey in json_data[i].get("text")
                            result[ext_fld] = json_data[i].get("text").replace(eackkey,"").strip(" .:,[]")
                            visited[ext_fld] = True

                            b_flag = False
                            for j in range(i + 1, len(json_data)):
                                for b in stopkey[ext_fld]:
                                    if b in json_data[j].get("text"):
                                        b_flag = True
                                if b_flag or json_data[j].get("text") in present_keys[ext_fld]:
                                    break
                                else:
                                    result[ext_fld] = result[ext_fld] + " " + json_data[j].get("text")
                                    visited[ext_fld] = True

                            if ext_fld == "hospital_address":
                                print("yes hospital_address")
                                print(result[ext_fld])
                                hos_detail = result[ext_fld]
                                if "City" in hos_detail:
                                    result["hospital_address"] = hos_detail.split("City")[0].strip("-: .")
                                    hos_detail = hos_detail.split("City")[1].strip("-: .")
                                if "State" in hos_detail:
                                    result["hospital_city"] = hos_detail.split("State")[0].strip("-: .")
                                    hos_detail = hos_detail.split("State")[1].strip("-: .")
                                if "Pincode" in hos_detail:
                                    result["hospital_state"] = hos_detail.split("Pincode")[0].strip("-: .")
                                    hos_detail = hos_detail.split("Pincode")[1].strip("-: .")
                                    print(hos_detail)
                                    result["hospital_pincode"] = hos_detail
                                    visited["hospital_pincode"] = True
                                if "Telephone" in hos_detail:
                                    txtt = hos_detail.split("Telephone")
                                    result["hospital_pincode"] = txtt[0].strip("-: .")
                                    result["hospital_telephone"] = txtt[1].strip("-: .")
                                    visited["hospital_telephone"]=True



                            break



    # with open(jsonpath.replace("\jsonslist.json", "")+"/result.json", "w") as outfile:
    #     json.dump(result, outfile)

    # Standardization of Final Output
    if "hospital_address" in list(result.keys()) and not "hospital_pincode" in list(result.keys()):
        regex = "\d{5,6}"
        match = re.findall(regex, result["hospital_address"])
        if len(match) == 1:
            result["hospital_pincode"] = match[0]

    states = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
     "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
     "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
     "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh",
     "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
    if "hospital_address" in list(result.keys()):
        for state in states:
            choice =  result["hospital_address"].lower().split(" ")
            print("fuzzzz",fuzz.partial_token_sort_ratio(state.lower(), choice))
            if state.lower() in result["hospital_address"].lower():
                result["hospital_state"] = state
            elif fuzz.ratio(state.lower(), choice) > 70:
                result["hospital_state"] = state
                print("yes  ",result["hospital_state"])
                break

    print("###########################")
    for q in result:
        print(q, "--->", result[q])
    print("###########################")
    for q in visited:
        if visited[q] == False:
            print(q, "--->", visited[q])

    return result


# claim_form_extract(r"F:\iAssist_Projects\iciciClassification\imgsfolders\cbb785a2-1bf5-4937-bcce-6f82cb98c725\jsonslist.json")

