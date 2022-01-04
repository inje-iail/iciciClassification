import itertools
import json
import os
import cv2
from copy import deepcopy
from pdf2image import convert_from_path
#from Discharge_summary_keywords import Headings,Exception_Headings, Ending_page_text, others_exception
from Dis_sum_keywords import Headings, Exception_Headings, Ending_page_text, others_exception
#from interpretation import get_icr_data_from_image
from fuzzywuzzy import fuzz
import sys
#sys.path.append(r"D:/discharge summary and fir/interpretation")
from moduletest import get_icr_data_from_image



def converting_to_image(file_name):
    file_name_temp = []
    my_image_name = str(file_name).replace(".PDF", "").replace(".pdf", "")

    pages = convert_from_path(file_name, 400)  ##
    print("Started Image Extraction....")
    no_of_pages = len(pages)
    for i in range(len(pages)):
        pages[i].save(os.path.join(save_path, str(i) + '.jpeg'), 'JPEG')
        img = cv2.imread(os.path.join(save_path, str(i) + '.jpeg'))

        file_name_temp.append(img)
        ##file_name_temp.append(os.path.join(save_path,str(i) + '.jpeg'))
    return no_of_pages, file_name_temp


# ###    HOS-4312, HOS-1866, HOS-3890(PRS), HOS-2262, HOS-0067, HOS-5175, HOS-2061
#
# main_path = r"C:\Users\iail_\Documents\Seshu\shantam_working_project\31-50\Top 31 - 50 Providers\Top 31 - 50 Providers\Claim Data - Top 31 - 50 Downloaded files_29-Jun-21"
# # main_path = r"C:\Users\iail_\Documents\Irshad sent pdf's\Sample Cases_17 Mar'21\Yashoda - Sec'bad"
# main_path = os.path.join(main_path, "N15601_Aakash Healthcare Private Limited")
# path = os.path.join(main_path, "220100586629.pdf")
#
# res_path = main_path
#
# pdf_name = path.split('\\')[-1]
# pdf_name = pdf_name.split('.')[0]
# print(pdf_name)
# if not os.path.exists(os.path.join(res_path, pdf_name)):
#     os.mkdir(os.path.join(res_path, pdf_name))
#     save_path = os.path.join(res_path, pdf_name)
#     no_of_pages, file_name_temp = converting_to_image(path)

others = []

def check_HOS(listofjson, Headings):
    check_flag = 0
    json_data = list(itertools.chain.from_iterable(listofjson))


    for hos in Headings.keys():
        # print(hos)
        matched_hos = []
        for i in range(len(json_data)):
            # print("yyyy",i)

            #             if str(json_data[i].get("text")).lower().__contains__(str(hos).lower()) and \
            #             len(str(json_data[i].get("text")).lower()) == len(str(hos).lower()):
            if str(json_data[i].get("text")).lower().__contains__(str(hos).lower()) and \
                    fuzz.ratio(str(hos).lower(), str(json_data[i].get("text")).lower()) > 80:   # need to change condition
                # print(fuzz.ratio(str(hos).lower(), str(json_data[i].get("text")).lower()))
                # print(hos)
                headings = [x.lower() for x in Headings[hos]]
                # print(headings)
                check_flag = 1
                matched_hos.append(hos)
                print("matched_hospitals = ", matched_hos)
                break
        if check_flag == 1:
            break
    if check_flag == 0:
        for hos in Headings:
            # print("**************", hos, "**************")
            # print(str(hos), " = ", Headings[hos], "\n")
            # others.append(Headings[hos])
            for each_head in Headings[hos]:
                # print(each_head)
                others.append(each_head)
        hos = others
        if hos == others:
            headings = None

    return hos, headings


def Dis_summary(listofjson, hos):

    first_page_keys = []  #modified by seshu 21-sep
    rep_gate = 0

    hos = hos

    if hos == others:
        gate = 0
    else:
        gate = 1

    Keys = [] #Keywords
    Vals = [] #Results

    last_key = "" #last key encountered
    last_val = ""
    # last_key_check = 0

    prev = "ignore"
    out_count = 0
    check_discharge = 0
    end_page = 0
    miss_match = 0

    for k in range(len(listofjson)):  # len(os.listdir(save_path))):##len(os.listdir(save_path))):
        # print(i)
        #out_count = out_count + 1       ## checking condition so cominting this

        # filepath = os.path.join(save_path, str(k) + ".jpg")
        # img = cv2.imread(filepath)
        # # print("original image dimentions = ",img.shape)
        # img = cv2.resize(img, (3365, 4640))
        # print("reshaped image dimentions = ",img.shape)
        # if k == index:

        # print(filepath)
        json_data = listofjson[k]

        start_dict = {}
        count_dict = {}

        final = {}
        temp = []
        # prev = "ignore"

        #  first and endpoint are flags for exception words and ending words
        first = 0
        endpoint = 0
        last_key_check = 0

        # Headings = [x.lower() for x
        flag = False
        # for a in range(len(json_data)):  ## small changes needed in this loop
        #     if (str(json_data[a].get('text')).lower().__contains__('overview health claim form')) and \
        #             str(json_data[a].get('text')).lower().__contains__("details of the amount claimed"):
        #         miss_match = 1
        #         break
        # if miss_match == 1:
        #     miss_match = 0
        #     continue
        for a in range(len(json_data)):
            if miss_match == 0 and \
                    (str(json_data[a].get('text')).lower().__contains__('overview health claim form') or
                    str(json_data[a].get('text')).lower().__contains__("details of the amount claimed") or
                    str(json_data[a].get("text")).upper().__contains__("AADHAAR CARD AND PAN CARD ARE REQUIRED FOR ALL CLAIMS") or
                    # str(json_data[a].get("text")).lower().__contains__("fir attached") or
                    # str(json_data[a].get("text")).lower().__contains__("fir no") or
                    str(json_data[a].get("text")).upper().__contains__("CLAIM SETTLEMENTS")):
                miss_match = 1
                break

            if (str(json_data[a].get("text")).lower().__contains__("discharge summary") or str(
                    json_data[a].get('text')).lower().__contains__('death summary')) and \
                    len(json_data[a].get("text")) <= 30:
                check_discharge = 1
                # print(json_data[a].get("text"))
                end_page = 1

            if end_page == 1:
                if str(json_data[a].get("text")).lower().__contains__("in- patient bill") or \
                        str(json_data[a].get("text")).lower().__contains__("payer payable") or \
                        str(json_data[a].get("text")).lower().__contains__("bill details") or \
                        str(json_data[a].get("text")).lower().__contains__("break up details") or \
                        str(json_data[a].get("text")).upper().__contains__("MEDICAL RECORD") or \
                        str(json_data[a].get('text')).lower().__contains__('final bill') or \
                        str(json_data[a].get('text')).lower().__contains__('breakup bill') or \
                        str(json_data[a].get("text")).lower().__contains__("inpatient detail running bill") or \
                        str(json_data[a].get("text")).upper().__contains__("BILL SUMMARY") or \
                        str(json_data[a].get("text")).upper().__contains__("INTERIM RUNNING BILL") or \
                        str(json_data[a].get("text")).lower().__contains__("Provisional Bill - Details") or \
                        str(json_data[a].get("text")).upper().__contains__("TO WHOM SO EVER IT MAY CONCERN") or \
                        str(json_data[a].get("text")).upper().__contains__("DRAFT BILL SUMMARY") or \
                        str(json_data[a].get('text')).lower().__contains__('interim bill of supply') or  \
                        str(json_data[a].get('text')).lower().__contains__('laboratory report') or \
                        str(json_data[a].get('text')).lower().__contains__('ip bill breakup details') or \
                        str(json_data[a].get('text')).lower().__contains__('inpatient bill (summary)') or \
                        str(json_data[a].get('text')).lower().__contains__('radiodiagnosis report'):
                    end_page = 2
        if end_page == 2:
            break

        if check_discharge == 0:
            out_count = 0
            continue

        if miss_match == 1:
            miss_match = 0
            continue

        if check_discharge == 1:
            out_count = out_count + 1

            for i in range(len(json_data)):
                if gate == 1:

                    if first_page_keys != []:
                        for each_key in first_page_keys:
                            if fuzz.ratio(str(each_key).lower(),
                                          str(json_data[i].get("text")).lower().split(':')[0]) > 90:
                                print("1st_page_keys = ", str(json_data[i].get("text")))
                                rep_gate = 1
                                break
                        if rep_gate == 1:
                            rep_gate = 0
                            continue

                    if i > 10:
                        for end_word in Ending_page_text[str(hos)]:
                            if str(json_data[i].get("text")).lower().__contains__(str(end_word).lower()):
                                # print("end page keywords = ", json_data[i].get("text"), "\n")
                                endpoint = 1
                                break
                        if endpoint == 1:
                            endpoint = 0
                            break

                    for j in Headings[str(hos)]:
                        # for j in headings:

                        if str(json_data[i].get("text")).lower().__contains__(':') and \
                                fuzz.ratio(str(j).lower(), str(json_data[i].get("text")).lower().split(':')[0]) > 90:#70:
                            # print("ratio = ", fuzz.ratio(str(j).lower(), str(json_data[i].get("text")).lower().split(':')[0]))
                            #if Exception_heading != []:
                            for a in Exception_Headings[str(hos)]:
                                if fuzz.ratio(str(a).lower(),str(json_data[i].get("text")).lower().split(':')[0]) > 85:
                                    # print("match0")
                                    first = 1
                                    break

                            if first == 1:
                                first = 0
                                continue      ## changed break to continue

                            # print(json_data[i].get("text"))
                            if str(json_data[i].get("text")).lower().split(':')[1] == "":
                                # print(json_data[i].get("text").split(':')[0])
                                final[prev] = temp
                                prev = json_data[i].get("text")
                                temp = []
                                flag = True
                                break
                            if str(json_data[i].get("text")).lower().split(':')[1] != "":
                                # print(json_data[i].get("text").split(':')[1])
                                final[prev] = temp
                                prev = json_data[i].get("text").split(':')[0]
                                temp = []
                                temp.append(json_data[i].get("text").split(':')[1])
                                flag = True
                                break

                            # break
                        elif fuzz.ratio(str(j).lower(), str(json_data[i].get("text")).lower()):
                            if fuzz.ratio(str(j).lower(), str(json_data[i].get("text")).lower()) > 90:#70:
                                # print("ratio1 = ", fuzz.ratio(str(j).lower(), str(json_data[i].get("text")).lower()))  # len(str(json_data[i].get("text")).lower().split(':')[0]) <= len(j) + 15:
                                # if Exception_heading != []:
                                for a in Exception_Headings[str(hos)]:
                                    if fuzz.ratio(str(a).lower(), str(json_data[i].get("text")).lower()) > 90:
                                        # print("match1")
                                        first = 1
                                        break

                                if first == 1:
                                    first = 0
                                    continue         ## changed break to continue

                                count_dict[j] = 0 if j not in count_dict else deepcopy(
                                    count_dict[j] + 1)  ## should be clarified by venky
                                count_ = str(count_dict[j]) if count_dict[j] != 0 else ""
                                # print("count = ", count_)
                                ##start_dict[j + count_] = i
                                # if str(j) == str(json_data[i].get("text")):
                                # print(json_data[i].get("text"))
                                final[prev] = temp
                                # prev = json_data[i].get("text")
                                prev = str(j + count_)
                                temp = []
                                flag = True
                                break


                elif gate == 0:

                    for j in hos:
                        # for j in headings:

                        if str(json_data[i].get("text")).lower().__contains__(':') and \
                                fuzz.ratio(str(j).lower(), str(json_data[i].get("text")).lower().split(':')[0]) > 85:#70:
                            # print("ratio = ",
                            #       fuzz.ratio(str(j).lower(), str(json_data[i].get("text")).lower().split(':')[0]))
                            # if Exception_heading != []:
                            for a in others_exception:
                                if fuzz.ratio(str(a).lower(), str(json_data[i].get("text")).lower().split(':')[0]) > 85:
                                    # print("match0")
                                    first = 1
                                    break

                            if first == 1:
                                first = 0
                                break

                            # print(json_data[i].get("text"))
                            if str(json_data[i].get("text")).lower().split(':')[1] == "":
                                # print(json_data[i].get("text").split(':')[0])
                                final[prev] = temp
                                prev = json_data[i].get("text")
                                temp = []
                                flag = True
                                break
                            if str(json_data[i].get("text")).lower().split(':')[1] != "":
                                # print(json_data[i].get("text").split(':')[1])
                                final[prev] = temp
                                prev = json_data[i].get("text").split(':')[0]
                                temp = []
                                temp.append(json_data[i].get("text").split(':')[1])
                                flag = True
                                break

                            # break
                        elif fuzz.ratio(str(j).lower(), str(json_data[i].get("text")).lower()):
                            if fuzz.ratio(str(j).lower(), str(json_data[i].get("text")).lower()) > 85:#70:
                                # print("ratio1 = ", fuzz.ratio(str(j).lower(), str(json_data[i].get(
                                #     "text")).lower()))  # len(str(json_data[i].get("text")).lower().split(':')[0]) <= len(j) + 15:

                                for a in others_exception:
                                    if fuzz.ratio(str(a).lower(), str(json_data[i].get("text")).lower()) > 90:
                                        # print("match1")
                                        first = 1
                                        break

                                if first == 1:
                                    first = 0
                                    break

                                count_dict[j] = 0 if j not in count_dict else deepcopy(
                                    count_dict[j] + 1)  ## should be clarified by venky
                                count_ = str(count_dict[j]) if count_dict[j] != 0 else ""
                                # print("count = ", count_)
                                ##start_dict[j + count_] = i
                                # if str(j) == str(json_data[i].get("text")):
                                # print(json_data[i].get("text"))
                                final[prev] = temp
                                # prev = json_data[i].get("text")
                                prev = str(j + count_)
                                temp = []
                                flag = True
                                break

                if flag:
                    flag = False
                    continue
                temp.append(json_data[i].get("text"))

            # print("out_count = ", out_count)
            final[prev] = temp
            # print(len(final))

            in_count = 0
            # print("final keys started")

            for key in final.keys():
                if out_count > 1:
                    new_val = ""
                    if key == last_key:
                        # print("last_key = ", last_key)
                        print(last_val)
                        # if type(last_val) == list:
                        #     final[key] = ' '.join(map(str, last_val))
                        #     new_val = final[key]
                        # else:
                        #     new_val = last_val
                        if type(last_val) == list:                                  #Updated by shantam
                            new_val = ' '.join(map(str, last_val))
                        else:
                            new_val = last_val

                        if type(final[key]) == list:
                            new_val = new_val + ' '.join(map(str, final[key]))
                        else:
                            new_val = new_val + final[key]

                        print(key + " -> " + str(new_val))
                        Keys.append(key)
                        Vals.append(new_val)
                        in_count = in_count + 1
                        if in_count == len(final):
                            print(key, len(final))
                            last_key_check = 1
                            break
                            # prev = key
                    #                     last_key = key
                    #                     #print("Ending = ", last_key)
                    #                     last_val = str(new_val)
                    #                     continue

                    elif key != last_key:
                        in_count = in_count + 1
                        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        # print(key + " -> " + str(final[key]))
                        Keys.append(key)
                        Vals.append(final[key])
                print("out_count = ", out_count)
                if out_count == 1:
                    in_count = in_count + 1
                    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    # print(key + " -> " + str(final[key]))
                    Keys.append(key)
                    Vals.append(final[key])
                    first_page_keys.append(key)  #modified by seshu 21-sep
            if last_key_check == 1:
                prev = key
                last_key = key
                # print("Ending = ", last_key)
                if type(last_val) == list:
                    last_val = ' '.join(map(str, last_val))
                last_val = str(new_val)

            if in_count == len(final) and last_key_check == 0:
                prev = key
                last_key = key
                # print("Ending = ", last_key)
                if type(final[prev]) == list:
                    last_val = ' '.join(map(str, final[prev]))
                    # last_val = str(final[prev])
                else:
                    print()

    result = {}

    for i in range(len(Keys)):
        if Vals[i] != []:
            result[Keys[i]] = Vals[i]

    return result, json_data

# save_path = r"F:\iAssist_Projects\iciciClassification\listen"
def run_dis_sum(save_path):
    # save_path = r"C:\Users\iail_\Documents\Seshu\shantam_working_project\31-50\Top 31 - 50 Providers\Top 31 - 50 Providers\Claim Data - Top 31 - 50 Downloaded files_29-Jun-21\N0070_Krishna Institute of Medical Sciences Ltd\220202021628"
    ##save_path = r"D:\DS_work_Inje\discharge sum\110100112090-1_Verified_2-Pharmacy missing"


    hos, headings = check_HOS(save_path, Headings)
    print(hos)

    if hos == others:
        result, text_json = Dis_summary(save_path, hos)

    elif hos == hos:
        result, text_json = Dis_summary(save_path, hos)

    print(result)

    final = {}

    for key in result.keys():
        key_final = key.lower().replace(".", "").replace(":", "").strip()
        if type(result[key]) == list:
            result[key] = ' '.join(map(str, result[key]))

        if key_final.strip() in ["reg no", "registration no", "registration number", "regno", 'reg no ','op number','opd no','reg  no', 'hospital no','op no', "mci regno",'hh no']:    ## 'admission no', 'umr no'
            final["registration no"] = result[key].replace("Name", "")

        elif key_final in ["f date of admission with time","date of admission with time","admission date /time",'Admission', "adm date", "admission date",'d.o.a', 'admn dt',"date of admission",'admission date & time','date of admission',"doa", "admn date", "admitted on", "admdate", "admit date", "admission date/time", "admission datetime", "admitted","admission dt / tm","admitted date","admission dt"]:
            if "date of admission" not in final.keys():
                final["date of admission"] = result[key].replace(":", "").strip()

        elif key_final in ["date of discharge with time","date of discharge with time","discharge date / time",'discharge', 'discharge dt','discharge date & time','discharge date','d.o.d', "dod",'date of discharge','date of procedure/ operation',"discharge dt","discharge dt ", "discharge date",   "discharge summary date", "discharged on", "discharged date", "discharge date/time", "discharge datetime", "disdate",'Date and Time of Discharge,' "date and time of discharge","discharge dt / tm","dischargeon","discharge date time", "discharge"]: #"discharged"   ##  'discharge type',
            final["date of discharge"] = result[key].replace(":", "").strip()

        elif key_final in ["dos", "surgrey date", "date of surgery"]:
            final["date of surgery"] = result[key].replace(":", "").strip()

        elif key_final in ['primary consultant',"consultant", "consultant(s)",'atten physician','consultant in charge','name of Consultant','doctor name','doctors who attended on the patient',"name of consultant", "consultation", "consultations", "primary consultant",'asst surgeon',"surgeons/consultants", "consultant name", "attending physicians", "referral consultant name", "name of surgeon", "attending consultants", "associate consultant", "admitting doctor", "primary consultant",'any special consultation', "treating doctor", "consultant doctor", "doctor", "treating doctor(s)",'admitting consultant',"atten. physician","under doctor","doctor",'dis doctor',
                           "attending","consultant doctor name"]:
            if "consultant" not in final.keys():
                final["consultant"] = result[key].replace("Category", "")

        elif key_final in ['admn no','admission no']:
            final['admn no'] = result[key].replace(":", "").strip()

        elif key_final in ["uhid",'jhid','uhid | old uhid','uhid/i', "lhid | old uhid", "uhid/ip","patient uhid",'uid','uid no']:
            if "uhid" not in final.keys():
                final["uhid"] = result[key].replace(":", "").strip()

        elif key_final in ["telephone no / mobile no","patient contact",'phone no ', 'contact no',"mobile", "mob no", "mobile no", "contact no", "mobile no/landline no", "phone no","phone",'tel number']:
            final["mobile"] = result[key]

        elif key_final in ["apatient's name*","patient's name","patient name", "name",'patient',"name", 'name of patient','patient/relative signature',"patient", "name of the patient",'head of department','name of the patient',"name ","|name of patient"]:  #'baby details',
            final["patient name"] = result[key].replace(":", "").strip()

        elif key_final in ["age", "age(as of today)", "age/gender", "age/sex", "gender/age", "gender / age","age/ sex","age / sex",'age / gender', 'age(as per today)', "age /sex"]:  #
            if "age" not in final.keys():
                if result[key].__contains__("/"):
                    # if result[key].split("/")[0]
                    final["age"] = result[key].split("/")[0]
                    final["gender"] = result[key].split("/")[1]
                else:
                    final["age"] = result[key].replace(":", "").strip()   #final["age"] = result[key]

        elif key_final in ["h mlc no*","mrd", "mrd#", 'mr no','mrdno',"mrd no", "mr no", "mr no / ip no",'mrdno ',"ipno",'mr number', 'umr no']: #'episode no'
            final["mrd"] = result[key].replace(":", "").strip()

        elif key_final in ["gender", "sex", "sox","sex "]:
            if "gender" not in final.keys():
                final["gender"] = result[key]

        elif key_final in ["room/bed no","bed", 'bed no','bed no ','ward / room/ bed', "ward/bed no", 'bed no', "war/room/bed", "bed no - ward", "ward / bed", "room no", "ward/bed", "bed details","bed category"]: #,'bed category',  ##  "ward/floor",  "ward no", "ward info", "ward", 'ssn no',
             final["bed no"] = result[key]

        ## newly added by seshu

        elif key_final in ["ward/floor", "ward no", "ward info", "ward"]:  # ,'bed category',  "bed details", "bed category"
             final["ward"] = result[key]

        elif key_final in ["c ipd no","ipd no","ip no",'i p no',"patient id", "patient no", "in patient no", "patient no ", "patient identifier", "ipd no", "ipnc", "ipno", 'ipid']:
            final["patient id"] = result[key].replace(":", "").strip()

        elif key_final in ["address",'address of the patient', "address of the patient", "location", "location name","house","patient address"]:  #'pincode',
            final["address"] = result[key].replace(":", "").strip()

        # elif key_final in ['diet advice','normal diet',"discharging status",'post operative advice','discharge advice','advice at discharge', "advice",'nursing discharge advice', "discharge advice", "specific advice",'advise on discharge ', "advise on discharge", "advice on discharge", "rehab / prevention / any other advice", 'physiotherapy','advise on discharge']:  #'advice on discharge',"recommendation",
        #     final["advice"] = result[key]

        # elif key_final in ["drugs allergies", "drug allergies", "drug allergy", "allergies", "allergic drug", "history of drug allergy"]:
        #     final["allergies"] = result[key]

        # elif key_final in ["diagnosis",'diagn','pre of diagnosis','riagnosis','diagnosis and co-morbidities','final diagnosis at the time of discharge','final diagnosis','diagnosis description','provisional diagnosis', "final diagnosis", "discharge diagnosis", "diagnosis with icd code", "diagnoses", "diagnosis at discharge", "final diagnosis at time of discharge", "provisional diagnosis","diagnosis & co-morbidities", "diagnosis1"]:
        #     if "diagnosis" not in final.keys():
        #         final["diagnosis"] = result[key]

        # elif key_final in ["history", 'case history',"medical history", "medical history of the patient","history of presenting illness","medical history & presenting complaints","presenting complaints",'maternal history ','social / family history','brief history', "present medical history & examination findings"]:
        #     final["history"] = result[key]

        # elif key_final in ["medicine on admission", "medication on admission", "medications administered", "admission notes", "medication administered",'medications',  "medicines given in ward"]:
        #     final["medicine on admission"] = result[key]

        # elif key_final in ["treatment given", "treatment given in ward", "treatment given with dates"]:
        #     final["treatment given"] = result[key]

        # elif key_final in ["past history", "past medical / surgical history", "past medical history", "previous evaluation", "past medical and sx history", "past medical history", "past med/surg hx", "past surgical history", "pediatric history", "significant past medical and surgical history if any", "brief history of illness-past", "obstertic/menstrual/marital history", "relevant past history and Investigations", "any significant medical history", "past medical and surgical history",'brief history of illness',"relevant past history and Investigation"]:
        #     final["past history"] = result[key]
        #
        # elif key_final in ["personal history", "history of present illness", "present history", "persoonal/social history", "present illness", "history of presenting complaint", "summary of present illness", "brief history of illness", "brief history of illness-present", "admission complaint and brief history of present illness", "history of current illness"]:
        #     final["personal history"] = result[key]
        #
        # elif key_final in ["family history", "personal/family history", "personal / family history", "family and social history", "family history if significant /relevant to diagnosis or treatment", "social / family history"]:
        #     final["family history"] = result[key]
        #
        # elif key_final in ["clinical examination", "presenting symptoms & clinical findings", "clinical finding ", "clinical finding", "clinical examination – physical examination – systemic examination",'clinical examination at the time of admission',"presenting symptoms & clinical findings", "clinical findings", "clinical examination at the time of admission", "local examination at time of discharge", "systemic examination", "local examination", "clinical examination findings","clinical summary","clinical profile", "examination findings", "clinical history and examination"]:
        #     final["clinical examination"] = result[key]

        elif key_final in ["investigations","investigations (detailed report with the patient)", "laboratory investigations", "investigation", "investigation results", "investigation(s)", "hospital course & investigations", "other investigation result", "other investigation results", "investigation advice", "other investigation", "other investigations", "investigations done", "investigation reports", "summary of investigation", "lab results", "significant/supportive investigations", "relevant/supportive investigations", "special investigations", "summary of key investigations during hospitalisation", "investigation report", "pertinent investigative data", "investigation result", 'special investigatio', "summary of key investigations", "investigation done","investigations (detailed report with the patient)", "investigation data", "other investigations report"]:
            final["investigations"] = result[key]

        # elif key_final in ["discharge medication", "discharge medications", "medications", "medication", "current medication", "medication on discharge", "treatment on discharge", "prescription detail on discharge", "treatment advice", "discharge prescription", "treatment advised", "sos medications", "treatment advised at discharge"]:  ##  "medicines given in ward", "treatment given", "discharge medications",
        #     final["discharge medication"] = result[key]

        # elif key_final in ["plan on discharge", "important highlights of discharge summary", "prognosis on discharge"]:
        #     final["plan on discharge"] = result[key]

        # elif key_final in ["course in the hospital & discussion", "course in hospital", "course in the hospital and discussion", "course in the hospital", "course in the hospital/summary", "course in The hospital & discussion", "summary of hospital course", "hospital course", "course of stay in hospital", "course of stay in hospital and medication", 'clinical course', "course in hospital including complications if any", "post op/ clinical course", "post operative course", "clinical course and event", "preop course", "procedures/treatment and course during hospitalization", "course at hospital", "coiurse of hosp", "course of hosp", "course in the ward", "course in the ward / icu", "course and managment", "course during stay", "course of hospitalisation", "course in the hospital stay"]:  ## "post op treatment",  "course and managment"
        #     final["course in hospital"] = result[key]

        # elif key_final in ["condition on discharge", "condition at discharge", "condition of the patient on discharge", "discharge condition", "condition of patient", "condition at the time of discharge", "patient condition on discharge"]:
        #     final["condition on discharge"] = result[key]

        # elif key_final in ["condition of the patient on admission"]:
        #     final["condition on admission"] = result[key]

        # elif key_final in ['history of presenting complaint',"presenting complaints", "presenting symptoms", "chief complaints", "chief complaints on admission", "presenting complaints with duration and reason for admission", 'Chief complaint(s)']:
        #     final["presenting complaints"] = result[key]

        # elif key_final in ["procedure performed", "procedure done",'surgery / procedure performed', "surgery/procedure performed", "procedure / surgery done",'presentation','present complaints with duration and reason for admission', "procedure", "major procedure", "surgery/procedures", "surgery/procedure notes", "procedure or operative procedure if any", "surgery", "details of procedure/operation", "procedures/surgeries", "procedure notes", "name of the procedure", "name of surgery", "surgical procedure", "treatment during hospitalisation", "operation details", "procedure done", "operative procedure and date", "operative title and date", "procedure performed(if any)", "surgery / procedure","procedure and surgery","surgery/(if any)/course in the","operations/ procedures","operative findings ","procedure done ","details of procedure/operation", 'surgery / procedure performed', "surgical/therapeutic procedures"]:
        #     final["procedure performed"] = result[key]

        # elif key_final in ["physical examination", "systemic examination", "physical examination at admission", "physical systemic examination", "operative notes", "post operative period", "physical findings", "physical examination(at the time of admission)", "physical activity", "general physical & systemic examination", "findings", "physical examiniation"]:  # "findings", "general examination", "general examination ",
        #     if "physical activity" not in final.keys():
        #         final["physical examination"] = result[key]

        elif key_final in ["reason for admission", 'admitting complaints',"complaints and reasons for admission", "chief complaints and history", "complaints and findings"]:
            final["reason for admission"] = result[key]

        # elif key_final in ["on examination", "local examination", "examination",'discharge examination']:
        #     final["on examination"] = result[key]

        # elif key_final in ['general examination','significant medications given',"general examination "]:
        #     final['general examination'] = result[key]

        # elif key_final in ["follow up", 'followup','follow-up',"follow up on", "follow up date", "follow-up advice", "follow up advice", "next follow up", "follow up appointment","review","next appointment","follow up visit instructions","review","follow-up instructions","review on", "follow up after 2 weeKks"]:
        #     final["follow up"] = result[key]

        # elif key_final in ["instructions",'precautions', "patient instructions",'any significant surgical history', 'general instructions to patient',"any other instructions",'special instruction','special instructions',"emergency visit instructions"]:
        #     final["instructions"] = result[key]

        # elif key_final in ["discharge recommendations", "recommendations at discharge", "recommendations",'review','recommedations','preventive plan of','preventive plan of care','when to obtain urgent care']:
        #     final["discharge recommendation"] = result[key]            ## added by seshu

        ##  added by Injee
        # elif key_final in ["antenatal period"]:
        #     final["antenatal period"] = result[key]

        # elif key_final in ["admission details"]:
        #     final["admission details"] = result[key]

        # elif key_final in ["caesarean details"]:
        #     final["caesarean details"] = result[key]

        # elif key_final in ["postoperative period"]:
        #     final["postoperative period"] = result[key]

        # elif key_final in ["baby details"]:
        #     final["baby details"] = result[key]

        # elif key_final in ["aig", "miot", "aries maternity hospital", "sparsh", "sailaja multispeciality hospitals", "aims"]:
        #     final["hospital name"] = hos #if hos not others #result[key]

        elif key_final in ["name of department", "department name"]:
            final["department name"] = result[key]

        elif key_final in ["head of department"]:
            final["department head"] = result[key]

        elif key_final in ["b department/specialty"]:
            final["Department Specialty"] = result[key]

        final["hospital name"] = hos



    c=1
    for key in final.keys():
        print(c)
        c=c+1
        print(key + " -> " + str(final[key]))
        # print(key + " -> " + ' '.join(map(str, result[key])))

    with open("Interpretation.json", "w") as outfile:
        json.dump(final, outfile)
    return final

# print(run_dis_sum(save_path))
# print(result["ignore"])

# json_data = []
# for i in range(len(text_json)):
#     if

# ' '.join(map(str, s))


