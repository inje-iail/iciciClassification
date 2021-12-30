import os
from pdf2image import convert_from_path
import pyzbar.pyzbar as pyzbar
import requests
import time
import json
import re
import cv2
import fuzzywuzzy.fuzz
import imutils
import PyPDF2
import pandas as pd


def interpret_hdfc(z, s, text_json):
    result = {}
    result["bank_name"] = "HDFC BANK"
    for i in range(len(z)):
        if ("Please sign above" in z[i] or "sign above" in z[i] or "Please" in z[i]) and ("Payable" not in z[i - 1]) and \
                z[i - 1].replace(" ", "").strip().isalpha():
            result["name"] = z[i - 1]

        if "IFSC" in z[i]:
            result["ifsc"] = z[i].split("IFSC")[-1].strip(" . , : ;")

        if "A/C" in z[i].upper() and "NO" in z[i].upper():
            if (len(z[i + 1].replace(" ", "").strip()) == 13 or len(z[i + 1].replace(" ", "").strip()) == 14) and z[
                i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif (len(z[i + 2].replace(" ", "").strip()) == 13 or len(z[i + 2].replace(" ", "").strip()) == 14) and z[
                i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_sbi(z, s, text_json):
    result = {}
    result["bank_name"] = "STATE BANK OF INDIA"
    for i in range(len(z)):

        if "Please sign above" in z[i]:
            if "Payable" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&", "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&", "").strip().isalpha():
                result["name"] = z[i - 2]

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if "A/c" in z[i] and "No" in z[i]:
            if len(z[i + 1].strip()) == 11 and z[i + 1].strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].strip()) == 11 and z[i + 2].strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 11 and z[i].replace(" ",
                                                                     "").strip().isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_icici(z, s, text_json):
    result = {}
    result["bank_name"] = "ICICI BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        #         elif "CODE" in z[i].upper():
        #             result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if "A/c" in z[i] and "No" in z[i]:
            if len(z[i + 1].replace(" ", "").strip()) == 12 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 12 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 12 and z[i].replace(" ",
                                                                     "").strip().isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_andhra(z, s, text_json):
    result = {}
    result["bank_name"] = "ANDHRA BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if "A/c" in z[i] and "No" in z[i]:
            if len(z[i + 1].replace(" ", "").strip()) == 15 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 15 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 15 and z[i].replace(" ",
                                                                     "").strip().isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_baroda(z, s, text_json):
    result = {}
    result["bank_name"] = "BANK OF BARODA"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            elif "Payable" not in z[i - 3] and "PROPRIETOR" not in z[i - 3] and z[i - 3].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 3]
            if "name" in result.keys() and result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if "A/c" in z[i] and "No" in z[i]:
            if len(z[i + 1].replace(" ", "").strip()) == 14 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 14 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 14 and z[i].replace(" ",
                                                                     "").strip().isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_punjab(z, s, text_json):
    result = {}
    result["bank_name"] = "PUNJAB NATIONAL BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].strip() != "GAL" and len(
                    z[i - 1]) > 3:
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].strip() != "GAL" and len(
                    z[i - 2]) > 3:
                result["name"] = z[i - 2]
            elif "Payable" not in z[i - 3] and "PROPRIETOR" not in z[i - 3] and z[i - 3].strip() != "GAL" and len(
                    z[i - 3]) > 3:
                result["name"] = z[i - 3]
            if "name" in result.keys() and result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]
    try:
        pattern = re.compile('[0-9]{13}[0-9]?[0-9]?[0-9]?')
        result['account_no'] = pattern.findall(s)[0]
    except:
        pass
    return result


def interpret_uco(z, s, text_json):
    result = {}
    result["bank_name"] = "UCO BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].strip() != "GAL" and z[
                i - 1].replace(" ", "").replace("&", "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].strip() != "GAL" and z[
                i - 2].replace(" ", "").replace("&", "").strip().isalpha():
                result["name"] = z[i - 2]
            elif "Payable" not in z[i - 3] and "PROPRIETOR" not in z[i - 3] and z[i - 3].strip() != "GAL" and z[
                i - 3].replace(" ", "").replace("&", "").strip().isalpha():
                result["name"] = z[i - 3]
            if "name" in result.keys() and result["name"].islower():
                result["name"] = ""

        if "IFSC" in z[i].upper():
            result["ifsc"] = z[i].split("IFSC")[-1].strip(" . , : ;")

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]
    try:
        pattern = re.compile('[0-9]{14}')
        result['account_no'] = pattern.findall(s)[0]
    except:
        pass

    return result


def interpret_federal(z, s, text_json):
    result = {}
    result["bank_name"] = "FEDERAL BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "PAYABLE" not in z[i - 1].upper() and "PROPRIETOR" not in z[i - 1] and "AUTHORISED" not in z[
                i - 1] and "SIGNATORY" not in z[i - 1] and z[i - 1].strip() != "GAL" and z[i - 1].replace(" ",
                                                                                                          "").replace(
                "&", "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "PAYABLE" not in z[i - 2].upper() and "PROPRIETOR" not in z[i - 2] and "AUTHORISED" not in z[
                i - 2] and "SIGNATORY" not in z[i - 3] and z[i - 2].strip() != "GAL" and z[i - 2].replace(" ",
                                                                                                          "").replace(
                "&", "").strip().isalpha():
                result["name"] = z[i - 2]
            elif "PAYABLE" not in z[i - 3].upper() and "PROPRIETOR" not in z[i - 3] and "AUTHORISED" not in z[
                i - 2] and "SIGNATORY" not in z[i - 3] and z[i - 3].strip() != "GAL" and z[i - 3].replace(" ",
                                                                                                          "").replace(
                "&", "").strip().isalpha():
                result["name"] = z[i - 3]
            if "name" in result.keys() and result["name"].islower():
                result["name"] = ""

        if "IFSC" in z[i].upper():
            result["ifsc"] = z[i].split("IFSC")[-1].strip(" . , : ;")

        if "A/c" in z[i] and "No" in z[i]:
            if len(z[i].split("No")[-1].strip(" . : ;")) == 14:
                result["account_no"] = z[i].split("No")[-1].strip(" . : ;")
            elif len(z[i + 1].replace(" ", "").strip()) == 14 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 14 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 14 and z[i].replace(" ",
                                                                     "").strip().isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0].upper() == "FOR":
            result["name"] = z[i]

    return result


def interpret_union(z, s, text_json):
    result = {}
    result["bank_name"] = "UNION BANK"
    for i in range(len(z)):

        if "PLEASE SIGN ABOVE" in z[i].upper() and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].strip() != "GAL" and z[
                i - 1].replace(" ", "").replace("&", "").strip().isalpha() and len(z[i - 1]) <= 25:
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].strip() != "GAL" and z[
                i - 2].replace(" ", "").replace("&", "").strip().isalpha() and len(z[i - 2]) <= 25:
                result["name"] = z[i - 2]
            elif "Payable" not in z[i - 3] and "PROPRIETOR" not in z[i - 3] and z[i - 3].strip() != "GAL" and z[
                i - 3].replace(" ", "").replace("&", "").strip().isalpha() and len(z[i - 3]) <= 25:
                result["name"] = z[i - 3]
            if "name" in result.keys() and result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if "A/c" in z[i] and "No" in z[i]:
            if len(z[i].split("No")[-1].strip(" . : ;")) == 15:
                result["account_no"] = z[i].split("No")[-1].strip(" . : ;")
            elif len(z[i + 1].replace(" ", "").strip()) == 15 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 15 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 15 and z[i].replace(" ",
                                                                     "").strip().isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_axis(z, s, text_json):
    result = {}
    result["bank_name"] = "AXIS BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if "A/C" in z[i].upper() and "NO" in z[i].upper():
            if len(z[i + 1].replace(" ", "").strip()) == 15 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 15 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 15 and z[i].strip().replace(" ",
                                                                             "").isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_canara(z, s, text_json):
    result = {}
    result["bank_name"] = "CANARA BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFSC" in z[i].upper():
            result["ifsc"] = z[i].split("IFSC")[-1].strip(" . , : ; - ")
        elif "IFS" in z[i].upper():
            result["ifsc"] = z[i].split("IFS")[-1].strip(" . , : ; - ")
        elif "1FSC" in z[i].upper():
            result["ifsc"] = z[i].split("1FSC")[-1].strip(" . , : ; - ")

        if "ACC" in z[i].upper() and "NO" in z[i].upper():
            if len(z[i + 1].replace(" ", "").strip()) == 14 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 14 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 14 and z[i].strip().replace(" ",
                                                                             "").isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_bandhan(z, s, text_json):
    result = {}
    result["bank_name"] = "BANDHAN BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if "ACC" in z[i].upper() and "NO" in z[i].upper():
            if len(z[i + 1].replace(" ", "").strip()) == 14 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 14 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 14 and z[i].strip().replace(" ",
                                                                             "").isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]
    return result


def interpret_baroda_gujarat(z, s, text_json):
    result = {}
    result["bank_name"] = "BARODA GUJARAT GRAMIN BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFSC" in z[i].upper():
            result["ifsc"] = z[i].split("IFSC")[-1].strip(" . , : ; - ")
        elif "IFS" in z[i].upper():
            result["ifsc"] = z[i].split("IFS")[-1].strip(" . , : ; - ")
        elif "1FSC" in z[i].upper():
            result["ifsc"] = z[i].split("1FSC")[-1].strip(" . , : ; - ")

        if "ACC" in z[i].upper() and "NO" in z[i].upper():
            if len(z[i + 1].replace(" ", "").strip()) == 14 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 14 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 14 and z[i].strip().replace(" ",
                                                                             "").isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_idfc(z, s, text_json):
    result = {}
    result["bank_name"] = "IDFC FIRST BANK"
    for i in range(len(z)):

        if "Please sign above" in z[i] and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if "ACC" in z[i].upper() and "NO" in z[i].upper():
            if len(z[i + 1].replace(" ", "").strip()) == 11 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 11 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 11 and z[i].strip().replace(" ",
                                                                             "").isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_indusind(z, s, text_json):
    result = {}
    result["bank_name"] = "INDUSIND BANK"
    for i in range(len(z)):

        if ("Please sign above" in z[i] or "sign above" in z[i]) and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFSC" in z[i].upper():
            result["ifsc"] = z[i].split("IFSC")[-1].strip(" . , : ; - ")
        elif "IFS" in z[i].upper():
            result["ifsc"] = z[i].split("IFS")[-1].strip(" . , : ; - ")
        elif "1FSC" in z[i].upper():
            result["ifsc"] = z[i].split("1FSC")[-1].strip(" . , : ; - ")
        elif "FSC" in z[i].upper():
            result["ifsc"] = z[i].split("FSC")[-1].strip(" . , : ; - ")

        if "ACC" in z[i].upper() and "NO" in z[i].upper():
            if len(z[i + 1].replace(" ", "").strip()) == 12 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 12 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 12 and z[i].strip().replace(" ",
                                                                             "").isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_kotak_mahindra(z, s, text_json):
    result = {}
    result["bank_name"] = "KOTAK MAHINDRA BANK"
    for i in range(len(z)):

        if ("Please sign above" in z[i] or "sign above" in z[i]) and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFSCY" in z[i].upper():
            result["ifsc"] = z[i].split("IFSCY")[-1].strip(" . , : ; - ")
        elif "IFSC" in z[i].upper():
            result["ifsc"] = z[i].split("IFSC")[-1].strip(" . , : ; - ")
        elif "IFS" in z[i].upper():
            result["ifsc"] = z[i].split("IFS")[-1].strip(" . , : ; - ")
        elif "1FSC" in z[i].upper():
            result["ifsc"] = z[i].split("1FSC")[-1].strip(" . , : ; - ")
        elif "FSC" in z[i].upper():
            result["ifsc"] = z[i].split("FSC")[-1].strip(" . , : ; - ")

        if "ACC" in z[i].upper() and "NO" in z[i].upper():
            if len(z[i + 1].replace(" ", "").strip()) == 10 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 10 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 10 and z[i].strip().replace(" ",
                                                                             "").isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_rbl(z, s, text_json):
    result = {}
    result["bank_name"] = "RBL BANK"
    for i in range(len(z)):

        if ("Please sign above" in z[i] or "sign above" in z[i]) and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if "ACC" in z[i].upper() and "NO" in z[i].upper():
            if len(z[i + 1].replace(" ", "").strip()) == 12 and z[i + 1].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 1].replace(" ", "").strip()
            elif len(z[i + 2].replace(" ", "").strip()) == 12 and z[i + 2].replace(" ", "").strip().isnumeric():
                result["account_no"] = z[i + 2].replace(" ", "").strip()

        if len(z[i].replace(" ", "").strip()) == 12 and z[i].strip().replace(" ",
                                                                             "").isnumeric() and "account_no" not in result.keys():
            result["account_no"] = z[i].replace(" ", "").strip()

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def interpret_mahanagar(z, s, text_json):
    result = {}
    result["bank_name"] = "THE MAHANAGAR CO-OP BANK"
    for i in range(len(z)):

        if ("Please sign above" in z[i] or "sign above" in z[i]) and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]
    try:
        pattern = re.compile('[0-9]{15}')
        result['account_no'] = pattern.findall(s)[0]
    except:
        pass
    return result


def interpret_hsbc(z, s, text_json):
    result = {}
    result["bank_name"] = "HSBC BANK"
    for i in range(len(z)):
        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]
    try:
        pattern1 = re.compile('[0-9]{3}\s?\-?\s?[0-9]{6}\s?\-?\s?[0-9]{3}')
        result['account_no'] = pattern1.findall(s)[0]
    except:
        pass
    try:
        pattern2 = re.compile('\([A-Z\s]*\)')
        name = pattern2.findall(s)[0]
        name = name.replace('(', '')
        name = name.replace(')', '')
        result['name'] = name
    except:
        pass

    return result


def interpret_vmcb(z, s, text_json):
    result = {}
    result["bank_name"] = "The Vaijapur Merchant's Co-op. Bank"
    for i in range(len(z)):

        if ("Please sign above" in z[i] or "sign above" in z[i]) and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
            if result["name"].islower():
                result["name"] = ""

        if "IFS CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        elif "IFSC CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")
        #         elif "CODE" in z[i].upper():
        #             result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    try:
        pattern1 = re.compile('[0-9]{15}')
        result['account_no'] = pattern1.findall(s)[0]
    except:
        pass
    return result


def interpret_karnataka(z, s, text_json):
    result = {}
    result["bank_name"] = "KARNATAKA BANK"
    for i in range(len(z)):

        if ("Please sign above" in z[i] or "sign above" in z[i]) and "name" not in result.keys():
            if "Payable" not in z[i - 1] and "PROPRIETOR" not in z[i - 1] and z[i - 1].replace(" ", "").replace("&",
                                                                                                                "").strip().isalpha():
                result["name"] = z[i - 1]
            elif "Payable" not in z[i - 2] and "PROPRIETOR" not in z[i - 2] and z[i - 2].replace(" ", "").replace("&",
                                                                                                                  "").strip().isalpha():
                result["name"] = z[i - 2]
        #             if result["name"].islower():
        #                 result["name"] = ""

        if "IFSC" in z[i].upper():
            result["ifsc"] = z[i].upper().split("IFSC")[-1].strip(" . , : ; - ")
        elif "IFS" in z[i].upper():
            result["ifsc"] = z[i].upper().split("IFS")[-1].strip(" . , : ; - ")
        elif "CODE" in z[i].upper():
            result["ifsc"] = z[i].upper().split("CODE")[-1].strip(" . , : ; - ")

        if ("ACC" in z[i].upper() or "A/C" in z[i].upper()) and "NO" in z[i].upper():
            account_no = z[i + 1]
            account_no = account_no.replace(' ', '')
            if account_no.isnumeric():
                result['account_no'] = account_no

        if z[i].replace(" ", "").replace("&", "").strip().isalpha() and z[i].strip().split()[0] == "FOR":
            result["name"] = z[i]

    return result


def getCheque(pdf_path):
    pdf = PyPDF2.PdfFileReader(pdf_path, "rb")
    file_base_name = pdf_path.replace('.pdf', '')
    pages = pdf.getNumPages()
    pageNum = -1
    for i in range(pages):
        p = pdf.getPage(i)

        w = int(float(p.mediaBox.getWidth()) * 0.352)
        h = int(float(p.mediaBox.getHeight()) * 0.352)

        if w > h and w / h > 2:
            print("Page ", i + 1)
            print(w, h, w / h)
            pageNum = i

    if pageNum == -1:
        return True, ""

    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(pdf.getPage(pageNum))

    with open('uploads\\{0}_subset.pdf'.format(file_base_name), 'wb') as f:
        pdfWriter.write(f)
        f.close()

    return False, "uploads\\" + file_base_name + "_subset.pdf"


def list_str(s):
    mystr = ""
    for ele in s:
        mystr = mystr + ele + " "
    return mystr


def geti(text_j):
    return text_j.get("text")


def getb(text_j):
    return text_j.get("boundingBox")


def get_micr(text_json):
    micr_identified = False
    micr_no = ""
    micrs_bb = []

    for i in range(len(text_json) - 1, -1, -1):
        # for i in range(int(len(text_json)/3),len(text_json)):

        if re.match("[0-9\s\/\'\:\"]+", geti(text_json[i])) and len(geti(text_json[i])) > 12:
            micr_no = geti(text_json[i])
            micrs_bb = text_json[i].get("words")
            break

    i = 0
    text = micr_no
    micr_list = []
    print('MICR BB', micrs_bb)
    while i < len(micrs_bb):

        micr_f = ""

        firstTym = True
        try:
            while i < len(micrs_bb):

                ibb = micrs_bb[i]["boundingBox"]
                nibb = micrs_bb[i + 1]["boundingBox"]

                if abs(ibb[2] - nibb[0]) <= 13:
                    if firstTym:
                        micr_f = micrs_bb[i]["text"]
                        firstTym = False

                    micr_f = micr_f + micrs_bb[i + 1]["text"]
                    i += 1
                if abs(ibb[2] - nibb[0]) > 13:
                    if micr_f == "":
                        micr_f = micrs_bb[i]["text"]
                    break
                # micr_f = micr_f + micrs_bb[i]["text"]
            micr_list.append(micr_f)
        except:
            pass

        i += 1

    temp_str_micrlist = list_str(micr_list).replace("'", "").replace('"', '')
    if len(temp_str_micrlist) < 9:
        micr_list = []

    micr_no = ""
    for i in micr_list:
        no = i.replace("'", "").replace('"', "")

        if len(no) > 8:

            if ":" in no[-1] and "1" in no[-2]:
                micr_no = no[0:-2]
            elif ":" in no[-1] and not "1" in no[-2]:
                micr_no = no.replace(":", "")
            else:
                micr_no = no

    if len(micr_no) > 9:
        if ":" in micr_no:
            temp_micr = micr_no.split(":")
            micr_no = temp_micr[0]
            if len(micr_no) == 10:
                if "4" in micr_no[-1] or "1" in micr_no[-1]:
                    micr_no = micr_no[:-1]
        if "0" in micr_no[-1] or "4" in micr_no[-1]:
            micr_no = micr_no[:-1]
        else:
            micr_no = micr_no[-9:]
    if micr_list == []:
        micr_list = text.split(" ")

    if micr_no == "" and micr_list != []:
        new_micr_list = []
        searchable = False
        for m in micr_list:
            if ":" in m:
                new_micr_list.append(m)
                searchable = True
                break
            else:
                new_micr_list.append(m)

        if searchable:
            try:
                micr_no = list_str(new_micr_list).replace(" ", "")
                if ":" in micr_no[-1] and "1" in micr_no[-2]:
                    micr_no = micr_no[0:-2].replace("'", "").replace('"', '')
                elif ":" in micr_no[-1] and not "1" in micr_no[-2]:
                    micr_no = micr_no.replace(":", "")

                if len(micr_no) > 9:
                    if "4" in micr_no[-1]:
                        micr_no = micr_no[:-1]
                    micr_no = micr_no[-9:]
            except:
                pass
    return micr_no


def run(text_json, name=''):
    s = ""
    z = []
    name_present = False
    for i in range(len(text_json)):
        s = s + " " + text_json[i].get("text")
        z.append(text_json[i].get("text"))

        # print(text_json[i].get("text"))
        # print(text_json[i].get("boundingBox"))

        if fuzzywuzzy.fuzz.ratio(name, text_json[i].get("text")) > 80:
            name_present = True
    print(z)
    print("#############################")
    print(s)
    result = {}
    if "HDFC BANK" in s:
        print("HDFC")
        result = interpret_hdfc(z, s, text_json)
    if "AXIS BANK" in s:
        print("AXIS")
        result = interpret_axis(z, s, text_json)
    if "FEDERAL BANK" in s:
        print("FEDERAL")
        result = interpret_federal(z, s, text_json)
    if "ICICI Bank" in s:
        print("ICICI")
        result = interpret_icici(z, s, text_json)
    if "Andhra Bank" in s:
        print("ANDHRA")
        result = interpret_andhra(z, s, text_json)
    elif "State Bank Of India" in s:
        print("SBI")
        result = interpret_sbi(z, s, text_json)
    elif "Bank of Baroda" in s:
        print("BARODA")
        result = interpret_baroda(z, s, text_json)
    elif "UCO Bank" in s:
        print("UCO")
        result = interpret_uco(z, s, text_json)
    elif "Union Bank" in s:
        print("UNION")
        result = interpret_union(z, s, text_json)
    elif "punjab" in s and "national" in s and "bank" in s:
        print("PUNJAB")
        result = interpret_punjab(z, s, text_json)
    elif "Canara" in s or "canara" in s:
        print("Canara")
        result = interpret_canara(z, s, text_json)
    elif "Bandhan" in s:
        print("Bandhan")
        result = interpret_bandhan(z, s, text_json)
    elif "Baroda" in s and "Gujarat" in s and "Gramin" in s:
        print("Baroda Gujarat Gramin")
        result = interpret_baroda_gujarat(z, s, text_json)
    elif "IDFC" in s:
        print("IDFC Bank")
        result = interpret_idfc(z, s, text_json)
    elif "Indusind" in s or "IndusInd" in s or "Indus" in s:
        print("IndusInd Bank")
        result = interpret_indusind(z, s, text_json)
    elif "Kotak Mahindra" in s or "Kotak" in s or "Mahindra" in s:
        print("Kotak Mahindra Bank")
        result = interpret_kotak_mahindra(z, s, text_json)
    elif "RBL" in s:
        print("RBL Bank")
        result = interpret_rbl(z, s, text_json)
    elif "Mahanagar" in s or "Co-Op" in s:
        print("The Mahanagar Co-Op Bank")
        result = interpret_mahanagar(z, s, text_json)
    elif "Hongkong" in s or "Sanghai" in s:
        print("HSBC Bank")
        result = interpret_hsbc(z, s, text_json)
    elif "Vaijapur" in s or "Merchant's" in s:
        print("VMCB Bank")
        result = interpret_vmcb(z, s, text_json)
    elif "KARNATAKA" in s:
        print("KARNATAKA BANK")
        result = interpret_karnataka(z, s, text_json)

    ls = ["name", "ifsc", "bank_name", "account_no"]

    for l in ls:
        if l not in result.keys():
            result[l] = ""

    if name:
        if fuzzywuzzy.fuzz.ratio(name, result["name"]) > 80:
            name_present = True
    else:
        if result["name"]:
            name_present = True
        else:
            name_present = False

    result["name_present"] = name_present
    micr_no = get_micr(text_json)
    result["micr_code"] = micr_no
    return result