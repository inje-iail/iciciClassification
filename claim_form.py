import json
import os
import random

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

# json_list = jsonslist(r"F:\iAssist_Projects\iciciClassification\imgsfolders\d306b672-8bf4-4343-bfda-255c2ae97d41")

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
            "admitted"
        ],
        "policy_no": [
            "Name of the Policyholder:", "Name","Card No","UHID"
        ],
        "uin_no": [
            "Issuance of this claim form is not to be taken as an admission of liability"
        ],
        "claim_no": [
            "Contact", "Description", "Loss/Event"
        ],
        "policyholder_name": [
            "Name of the Insured Person:", "insured", "Name" ,"Bank","number","Policy"
        ],
        "patient/Insured_name": [
            "Card", "UHID","Address","Residential"
        ],
        "patient_card/uhid": [
            "Gender"
        ],
        "dob": [
            "Gender","age","Completed"
        ],
        "patient/Insured_current_address": [
            "Mobile"
        ],
        "patient/Insured_mobile_no": [
            "Email","Part","Claim"
        ],
        "patient_email": [
            "Policy"
        ],
        "insured_person_aadhar_no": [
            "Claimant Details","PAN"
        ],
        "relationship_of_claimant_with_insured_person": [
            "Address"
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
            "Address",
        ],
        "hospital_address": [
            "treating Medical","Telephone"
        ],
        "hospital_telephone": [
            "Mobile"
        ],
        "hospital_mobile": [
            "ROHINI"
        ],
        "rohini_id": [
            "Hospital"
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
            "Claimant",
        ],
        "claimant/insured_person's_bank_account_no": [
            "bank","Bank","Name"
        ],
        "name_of_the_bank": [
            "Scanned","Branch","name"
        ],
        "branch_name:": [
            "Address","IFSC","Bank"
        ],
        "bank_address": [
            "IFSC","FSC code"
        ],
        "IFSC_code": [
            "PAN","Pan","Policy"
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
            "PAN", "Pan", "KYC"
        ],
    }

    present_keys = {
        "treating_dr_details":[
            "82. Details of the attending Medical Practitioner/ Doctor/ Treating Physician or Surgeon",
            "B2. Details of the attending Medical Practitioner/ Doctor/ Treating Physician or Surgeon"
        ],
        "policy_no": [
            "Current Policy No.:", "Policy No.:", "Policy No", "Policy No :"
        ],
        "uin_no": [
            "UIN No.", "UIN No"
        ],
        "claim_no": [
            "Claim Number (if allotted) .", "Claim Number (if allotted):", "Claim Number:", "Claim Number (if allotted) :",
            "Claim No. (If claim has already been registered with ICICI Lombard Health Care):"
        ],
        "policyholder_name": [
            "Name of the Policyholder:", "Name of the Policyholder", "Name of the Policy Holder", "Name of the Policy Holder:"
        ],
        "patient/Insured_name": [
            "Name of the Patient:","Name of the Patient","Name of Insured:"
        ],
        "patient_card/uhid": [
            "Card No./ UHID of the Patient:", "Card No./ UHID of the Patient"
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
            "Relationship of claimant with Insured Person:", "Relationship of claimant with Insured Person"
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
            "Name of the Hospital/ Nursing home:", "Name of the Hospital:", "Name of the Hospital"
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
            "ROHINI ID"
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
            "Claimant /Insured Person's name(as per bank records:"
        ],
        "claimant/insured_person's_bank_account_no": [
            "Claimant /Insured Person's bank account no.:","Claimant /Insured Person's bank account no :","Bank account number of Policy Holder:"
        ],
        "name_of_the_bank": [
            "Name of the bank:", "Name of the bank", "Name of the bank:", "Name of the Bank","Name of the Bank:"
        ],
        "branch_name:": [
            "Branch name:", "Branch name :","Branch Name:","Branch Name"
        ],
        "bank_address": [
            "Address of the bank:"
        ],
        "IFSC_code": [
            "IFSC code no. of the bank:", "FSC code no. of the bank:", "IFSC code no, of the bank:",
            "IFSC of the Bank:"
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
    }

    result = {}
    visited = {}
    for v in present_keys:
        visited[v] = False
    for json_data in json_list:
        for i in range(len(json_data)):
            print(json_data[i].get("text"))
            for ext_fld in present_keys:
                # print("Extd :", ext_fld)

                # c_bb = json_data[i].get("boundingBox")
                # n_bb = json_data[i+1].get("boundingBox")
                # print(c_bb[2] , n_bb[0])

                if visited[ext_fld] == False and json_data[i].get("text") in present_keys[ext_fld]:

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

                            # if ext_fld == "hospital_address":
                            #     print("yes hos add----")
                            #     hos_ilist = {"hospital_city": ["City", "city"],
                            #                  "hospital_state": ["State"],
                            #                  "hospital_pincode": ["Pincode"], }
                            #     temptxt = ""
                            #     nb_flag = False
                            #     for j in range(i + 1, len(json_data)):
                            #         print("yes hos add:", json_data[j].get("text"))
                            #         for b in stopkey[ext_fld]:
                            #             if b in json_data[j].get("text"):
                            #                 nb_flag = True
                            #                 print("Flag found")
                            #         if nb_flag or json_data[j].get("text") in present_keys[ext_fld]:
                            #             print("Flag break")
                            #             break
                            #         else:
                            #             for nw in range(0, len(hos_ilist)):
                            #                 print("yes hos 1:", list(hos_ilist.values())[nw])
                            #                 for ni in list(hos_ilist.values())[nw]:
                            #                     if ni in json_data[j].get("text"):
                            #                         if ni in hos_ilist["hospital_city"]:
                            #                             result[ext_fld] = temptxt
                            #                             temptxt = ""
                            #                         else:
                            #                             result[list(hos_ilist.keys())[nw-1]] = temptxt
                            #                             temptxt = ""


                            break

    print("###########################")
    for q in result:
        print(q, "--->", result[q])
    print("###########################")
    for q in visited:
        if visited[q] == False:
            print(q, "--->", visited[q])

    # with open(jsonpath.replace("\jsonslist.json", "")+"/result.json", "w") as outfile:
    #     json.dump(result, outfile)
    return result


# claim_form_extract(r"F:\iAssist_Projects\iciciClassification\imgsfolders\d306b672-8bf4-4343-bfda-255c2ae97d41\jsonslist.json")
