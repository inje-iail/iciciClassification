from datetime import datetime
import json
import os
import re
import shutil
import time
from datetime import date

from moduletest import classify
from pan_int import icr_pan
from aadhar_int import icr_aadhaar, icr_aadhaar_back
# from dischargeSum import dis_sum
from Discharge_summary_seshu import run_dis_sum
from claim_form import claim_form_extract
from policy_id import policy_card
from Cheque import run

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
        print("data len",len(data))

        discharge_visit,claim_form_visit = False, False
        final = {}

        for cls in result['documents']:
            print("cls outer----->", result['documents'][cls])
            txt_json = next(v for i, v in enumerate(data.values()) if i == int(cls)-1)
            # print("value ----->",txt_json)
            if result['documents'][cls] == "cancelledcheque":
                res_cheque = run(txt_json)
                print(res_cheque)
                final["cancelledcheque"] = res_cheque
            if result['documents'][cls] == "pan":
                res_pan = icr_pan(txt_json)
                print(res_pan)
                final["pan"] = res_pan
            elif result['documents'][cls] == "aadhar":
                if "aadhar" in final.keys():
                    res_aadhar1 = icr_aadhaar(txt_json)
                    res_aadhar2 = icr_aadhaar_back(txt_json)
                    # print(res_aadhar)
                    res_aadhar = {
                        "front":res_aadhar1,
                        "back":res_aadhar2
                    }
                    final["aadhar"+str(cls)] = res_aadhar
                else:
                    res_aadhar1 = icr_aadhaar(txt_json)
                    res_aadhar2 = icr_aadhaar_back(txt_json)
                    # print(res_aadhar)
                    res_aadhar = {
                        "front": res_aadhar1,
                        "back": res_aadhar2
                    }
                    print(res_aadhar)
                    final["aadhar"] = res_aadhar
            elif discharge_visit == False and result['documents'][cls] == "dischargesheet" or result['documents'][cls] == "dischargesummary":
                print("cls ----->", cls)
                print("len of json1:", len(txt_json))
                list_of_json = [txt_json]
                discharge_visit = True
                for q in range(int(cls),len(result['documents'])):
                    print("q ----->", q)
                    if result['documents'][str(q)] == "dischargesheet" or result['documents'][str(q)] == "dischargesummary":
                        txt_json = next(v for i, v in enumerate(data.values()) if i == int(q))
                        list_of_json.append(txt_json)
                        print("len of json:", len(txt_json))

                res_dis_sum = run_dis_sum(list_of_json)
                print("len list_of_json:",len(list_of_json))

                final["discharge_summary"] = res_dis_sum

            elif claim_form_visit == False and result['documents'][cls] == "claimform":
                print("cls ----->", cls)
                print("len of json1:", len(txt_json))
                print("len(result['documents']) :",len(result['documents']))
                list_of_json = [txt_json]
                claim_form_visit = True
                for q in range(int(cls),len(result['documents'])):
                    print("q ----->", q)
                    if result['documents'][str(q)] == "claimform":
                        txt_json = next(v for i, v in enumerate(data.values()) if i == int(q))
                        list_of_json.append(txt_json)
                        print("len of json:", len(txt_json))

                res_claim_form_extract = claim_form_extract(list_of_json)
                print("len list_of_json:",len(list_of_json))

                final["claimform"] = res_claim_form_extract
            elif result['documents'][cls] == "policyidcard":
                if "policyidcard" in final.keys():
                    res_policyidcard = policy_card(txt_json)
                    print(res_policyidcard)
                    final["policyidcard"+str(cls)] = res_policyidcard
                else:
                    print("fiiiiii")
                    res_policyidcard = policy_card(txt_json)
                    print(res_policyidcard)
                    final["policyidcard"] = res_policyidcard



        with open("final.json", "w") as outfile:
            json.dump(final, outfile)


        #  summary result >>>>>>>>>>>>>>>>>>>>>>>>>>

        temp_summary = {
            "Hospital Name": {"discharge_summary": "hospital name", "claimform": "hospital_name"},
            "ROHINI ID": "",
            "Hospital Contact no": {"claimform": "hospital_mobile", "claimform": "hospital_telephone"},
            "Hospital Email id": "",
            "Hospital pincode": {"claimform": "hospital_pincode"},
            "Hospital city": {"claimform": "hospital_city"},
            "Hospital state": {"claimform": "hospital_state"},
            "Hospital Address": {"claimform": "hospital_address"},

            "Medical Practitioner Name": {"claimform": "treating_medical_practitioner","discharge_summary": "consultant"},
            "Doctor Contact no": {"claimform": "treating_medical_practitioner_Mobile_no"},
            "Clinical Specialization": {"discharge_summary": "Department Specialty"},

            "Date of Admission": {"discharge_summary": "date of admission", "claimform": "admission_date_time"},
            "Date of discharge": {"discharge_summary": "date of discharge", "claimform": "discharge_date_time"},
            "Length of stay in hospital": "",

            "ID Type": "",
            "Name as per ID": {"pan": "full_name", "aadhar": "name", "policyidcard": "name"},
            "DOB":{"aadhar": "dob", "pan": "dob", "claimform": "dob", "policyidcard": "DOB"},
            "Address as per ID": {"aadhar": "full_address"},
            "PAN number": {"pan": "pan_number"},
            "Adhaar number": {"aadhar": "aadhar number", "claimform": "claimant_aadhar_no"},
        }
        summary = {}
        summary_detail = {}
        temp_summary_detail = {}
        for fld in temp_summary:
            #ex dob
            if temp_summary[fld] != "":
                for doc2check in temp_summary[fld]:
                    print(fld,"-->",doc2check)
                    if doc2check in final and not fld in summary.keys():
                        print("___________>>>",doc2check)
                        if doc2check == "aadhar":
                            for fb in final[doc2check]:
                                print(">>>",fb,temp_summary[fld][doc2check])
                                if final[doc2check][fb][temp_summary[fld][doc2check]] != "" and not "ELECTRONICALLY" in final[doc2check][fb][temp_summary[fld][doc2check]].upper():
                                    temp_summary_detail[str(fld)] = doc2check
                                    summary[fld] = final[doc2check][fb][temp_summary[fld][doc2check]]
                                    break
                        else:
                            print("!>>>",doc2check,temp_summary[fld][doc2check])
                            if temp_summary[fld][doc2check] in list(final[doc2check].keys()) and final[doc2check][temp_summary[fld][doc2check]] != "":
                                temp_summary_detail[str(fld)] = doc2check
                                summary[fld] = final[doc2check][temp_summary[fld][doc2check]]
                                break
                    # else:
                    #     break

        for f in temp_summary:
            if not f in list(summary.keys()):
                summary[f] = ""

        # For Detailed Summary >>>>>>>>>>>>>>>>>>>>
        for fld in temp_summary:
            if temp_summary[fld] != "":
                summary_detail[fld] = []
                for doc2check in temp_summary[fld]:
                    print(fld,"11-->",doc2check)
                    if doc2check in final:
                        print("11___________>>>",doc2check)
                        if doc2check == "aadhar":
                            for fb in final[doc2check]:
                                print("11>>>",fb,temp_summary[fld][doc2check])
                                if temp_summary[fld][doc2check] in list(final[doc2check][fb].keys()) and final[doc2check][fb][temp_summary[fld][doc2check]] != "":
                                    summary_detail[fld].append({doc2check: final[doc2check][fb][temp_summary[fld][doc2check]]})

                        else:
                            print("!>>>",doc2check,temp_summary[fld][doc2check])
                            if temp_summary[fld][doc2check] in list(final[doc2check].keys()) and final[doc2check][temp_summary[fld][doc2check]] != "":
                                summary_detail[fld].append({doc2check: final[doc2check][temp_summary[fld][doc2check]]})
                                print("oo ", final[doc2check][temp_summary[fld][doc2check]])
                                print("list1:",summary_detail[fld])

        for fld in summary_detail:
            if summary_detail[fld] != []:
                summary_detail[fld].append({"Selected": temp_summary_detail[fld]})




        if "pan" in list(final.keys()) or "aadhar" in list(final.keys()):
            summary["ID Type"] = []
            if "pan" in list(final.keys()):
                summary["ID Type"].append("pan")
            if "aadhar" in list(final.keys()):
                summary["ID Type"].append("aadhar")
        if summary["Date of Admission"] != "" and summary["Date of discharge"] != "":
            if len(re.findall(r"\d{2}\/\d{2}\/\d{2,4}", summary["Date of Admission"])) == 1 and len(re.findall(r"\d{2}\/\d{2}\/\d{2,4}", summary["Date of discharge"])) == 1:
                summary["Date of Admission"] = re.findall(r"\d{2}\/\d{2}\/\d{2,4}", summary["Date of Admission"])[0]
                summary["Date of discharge"] = re.findall(r"\d{2}\/\d{2}\/\d{2,4}", summary["Date of discharge"])[0]

                if int(summary["Date of discharge"].split("/")[1]) > 12:
                    im = summary["Date of discharge"].split("/")[1]
                    nm = "0"+im[-1]
                    summary["Date of discharge"] = summary["Date of discharge"].replace(im, nm)

                if int(summary["Date of Admission"].split("/")[1]) > 12:
                    im = summary["Date of Admission"].split("/")[1]
                    nm = "0"+im[-1]
                    summary["Date of Admission"] = summary["Date of Admission"].replace(im, nm)

                try:
                    date_format = "%d/%m/%Y"
                    d1 = datetime.strptime(summary["Date of Admission"], date_format)
                    d0 = datetime.strptime(summary["Date of discharge"], date_format)
                    delta = d1 - d0
                    summary["Length of stay in hospital"] = str(delta.days) + " Days"
                    print("Length of stay in hospital",delta.days)
                except:
                    pass

            elif len(re.findall(r"\d{2}\-\d{2}\-\d{2,4}", summary["Date of Admission"])) == 1 and len(re.findall(r"\d{2}\-\d{2}\-\d{2,4}", summary["Date of discharge"])) == 1:
                summary["Date of Admission"] = re.findall(r"\d{2}\-\d{2}\-\d{2,4}", summary["Date of Admission"])[0]
                summary["Date of discharge"] = re.findall(r"\d{2}\-\d{2}\-\d{2,4}", summary["Date of discharge"])[0]

                if int(summary["Date of discharge"].split("-")[1]) > 12:
                    im = summary["Date of discharge"].split("-")[1]
                    nm = "0"+im[-1]
                    summary["Date of discharge"] = summary["Date of discharge"].replace(im, nm)

                if int(summary["Date of Admission"].split("-")[1]) > 12:
                    im = summary["Date of Admission"].split("-")[1]
                    nm = "0"+im[-1]
                    summary["Date of Admission"] = summary["Date of Admission"].replace(im, nm)

                try:
                    date_format = "%d-%m-%Y"
                    d1 = datetime.strptime(summary["Date of Admission"], date_format)
                    d0 = datetime.strptime(summary["Date of discharge"], date_format)
                    delta = d1 - d0
                    summary["Length of stay in hospital"] = str(delta.days) + " Days"
                    print("Length of stay in hospital",delta.days)
                except:
                    pass


        print(">>>>>>>>>")
        print("sum", summary)
        with open("summary.json", "w") as outfile:
            json.dump(summary, outfile)



        # generationg json for all result
        for filename in os.listdir("imageFolderJson"):
            os.remove(os.path.join("imageFolderJson", filename))
        for jsonres in final:
            with open("imageFolderJson/" +str(jsonres)+".json", "w") as outfile:
                json.dump(final[jsonres], outfile)
        with open("imageFolderJson/summary.json", "w") as outfile:
            json.dump(summary, outfile)
        with open("imageFolderJson/" + "final.json", "w") as outfile:
            json.dump(final, outfile)

        with open("imageFolderJson/summary_details.json", "w") as outfile:
            json.dump(summary_detail, outfile)
        print(">>>>>>>>>")
        print("sum", summary_detail)





        # Deleting the ran one
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
