import shutil

from moduletest_for_import import classifier, hospitalfinder
import json
import os
import time
from _csv import writer
from copy import deepcopy
from os.path import basename
import numpy as np
import cv2
import uuid
import requests
from pdf2image import convert_from_path

from PIL import Image
import cv2


def pdfapilocal(filename):
    # print('49')
    # print(str(request.files.getlist('file')))
    # print('52')
    # file1 = open(filename)
    # print(file1)
    if True:
        print('54')
        print(filename)
        # filename = secure_filename(filename)
        # if not os.path.isdir('/classification-API/incomings'):
        #     os.mkdir('/classification-API/incomings')
        random_id = str(uuid.uuid4())
        os.mkdir(BASE_IMGS_FOLDER + '/' + random_id)
        folder = BASE_IMGS_FOLDER + '/' + random_id
        root_path = "./extract"
        hospital_identified = 'none'
        ##pt.pytesseract.tesseract_cmd = "./tesseract/tesseract.exe"
        # path = "./listen/" + pdf_filename
        save_path = folder
        # file1[0].save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # eachfilepath = os.path.join(UPLOAD_FOLDER, filename)
        converting_to_image(filename, save_path, folder)
        resp = seggregator(save_path)
        # print(str(resp[0]))
        # print(str(resp[1]))
        # print(str(resp[2]))
        print('72')
        # print(resp[3])
        responses = {'hospital': resp[0], 'documents': resp[2]}
        # responses['counts'] = resp[3]
        print(type(responses))
        resplist = []
        # resplist.append(responses)
        # resplist.append(resp[3])
        # print(type(resp[3]))
        return responses
    else:
        print('error')
        errors[file1[0].filename] = 'File type is not allowed'
    return 'ok'


def change_resolution(input_image_path, output_image_path, basewidth, baseheight):
    # img = Image.open(input_image_path)
    # # baseheight = data["baseheight"]
    # # basewidth = data["basewidth"]
    # hpercent = (baseheight / float(img.size[1]))
    # wsize = int((float(img.size[0]) * float(hpercent)))
    # wpercent = (basewidth / float(img.size[0]))
    # hsize = int((float(img.size[1]) * float(wpercent)))
    # print(wsize, hsize)
    # img = img.resize((wsize, hsize), Image.ANTIALIAS)
    # img.save(output_image_path)
    image = cv2.imread(input_image_path, 1)
    resized_image = cv2.resize(image, (basewidth, baseheight))
    cv2.imwrite(output_image_path, resized_image)


def text_concat(json_data):
    text = " ".join([str(text.get('text')) for text in json_data])
    return text


def get_icr_data_from_image(filepath: str):
    """
    Passes the image url to IAIL cognitive services (ICR) and gets the interpreted data
    extracted from the image in the image url and returns a json data
    :param filepath:
            filepath of the image in local storage
    :type filepath: str
    :return: Interpreted data
    :rtype: dict
    """
    subscription_key = '665d4d9af50043ce91135e526a1f41ca'
    text_recognition_url = 'https://icr-prod-sh-1.cognitiveservices.azure.com/vision/v2.1/read/core/asyncBatchAnalyze?language=en'

    image_data = open(filepath, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color', 'language': 'en',
              'detectOrientation ': 'true'}
    response = requests.post(
        text_recognition_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    # operation_url = response.headers["Operation-Location"]

    analysis = {}
    poll = True
    while poll:
        response_final = requests.get(
            response.headers["Operation-Location"], headers=headers, params=params)
        analysis = response_final.json()
        time.sleep(1)
        # print('109')
        # print(analysis)
        if "recognitionResults" in analysis:
            poll = False
        if "status" in analysis and analysis['status'] == 'Failed':
            poll = False

    text_json = analysis['recognitionResults'][0].get("lines")
    # print(text_json)
    # print('119')
    # print(text_json)
    return text_json


def converting_to_image(file_name, save_path, folder):
    file_name_temp = []
    my_image_name = str(file_name).replace(".PDF", "").replace(".pdf", "")
    length_of_files_present = len(os.listdir(save_path))

    print(length_of_files_present)

    ##print("Started")
    ##my_image_name1 = my_image_name.split("\\")[-1]
    ##print(my_image_name1)
    doc_name = []
    import tempfile
    with tempfile.TemporaryDirectory() as tempdir:
        pages = convert_from_path(file_name, 300, output_folder=tempdir)
        print("Started Image Extraction....")
        no_of_pages = len(pages)
        print("pages : ", no_of_pages)
        for i in range(len(pages)):
            ##file_name_temp.append(str(my_image_name) + '-' + str(i) + '.jpeg')
            ##pages[i].save(save_path + str(i) + '.jpeg', 'JPEG')
            ##file_name_temp.append(save_path + str(i) + '.jpeg')
            filepath = os.path.join(folder, str(i + length_of_files_present) + ".jpg")
            pages[i].save(os.path.join(save_path, basename(folder + str(i + 1 + length_of_files_present) + '.jpg')),
                          'JPEG')
            img = cv2.imread(os.path.join(save_path, str(i + length_of_files_present) + '.jpg'))
            change_resolution(os.path.join(save_path, basename(folder + str(i + 1 + length_of_files_present) + ".jpg")),
                              os.path.join(save_path, basename(folder + str(i + 1 + length_of_files_present) + ".jpg")),
                              2300, 2700)
        #         print(img.shape)
        #         plt.figure(figsize=(10,15))
        #         plt.imshow(img)
        ##img_path = print(os.path.join(save_path,str(i) + '.jpeg'))
        ##file_name_temp.append(img_path)
        # text = get_icr_data_from_image(filepath)
        # text_json = text_concat(text)
        # print(text_json+'\n\n8989\n\n')
        # file_name_temp.append(img)
        # hospital, doc = classifier(text_json, 2)
        # doc_name.append(doc)
    print('completed imaging')
    # print(doc_name)
    ##file_name_temp.append(os.path.join(save_path,str(i) + '.jpeg'))
    # return hospital, doc


def seggregator(path, random_id):
    ###takes path of folder containing images as input and starts finding hospital first and docs next
    print('length:')
    print(len(os.listdir(path)))
    hospital_ = 'none'
    documents_indexes = []
    documents_indexes_dict = {}
    document_names = []
    documents = {}
    extracts = {}
    json_datas = {}
    try:
        for i in range(1, len(os.listdir(path)) + 1):
            # print('100 ' + str(i))
            filepath = os.path.join(path, basename(path + str(i) + ".jpg"))
            # print("filepath:",os.listdir(path),path)
            text = get_icr_data_from_image(filepath)
            json_datas[basename(filepath)] = text
            text_json = text_concat(text)

            # print(text_json + '\n\n8989\n\n')
            extracts[basename(filepath)] = text_json
            # extracts = {'1':"txtdata1",2:"tcxtdata2}
        print('189de')
        print(json_datas)
    except:
        print('1except')
        filepath = os.path.join(path, os.listdir(path)[0])
        text = get_icr_data_from_image(filepath)
        json_datas[basename(filepath)] = text
        text_json = text_concat(text)
        extracts[basename(filepath)] = text_json

    with open('all_bill.json', 'w') as f:
        json.dump(json_datas, f)
        # f.write(str(json_datas))

    with open("jsons_all_bill/"+str(random_id)+'.json', 'w') as f:
        json.dump(json_datas, f)

    for h in extracts:
        print('started hospitals')

        hospital_ = hospitalfinder(extracts[h])

        if hospital_ != 'none':
            break
    print('107: ' + hospital_)
    # finding hospital ends here
    counter = 0
    for j in extracts:
        # nums = []
        # filepath = os.path.join(folder, str(j) + ".jpeg")
        # text = get_icr_data_from_image(filepath)
        # text_json = text_concat(text)
        # print(text_json + '\n\n8989\n\n')
        print('197')
        print(random_id)
        print("j:", j)
        doc = classifier(extracts[j], 2, hospital_,j,random_id)
        # nums.append(str(j))
        documents_indexes.append(str(counter + 1) + ": ")
        documents_indexes.append(doc)

        documents_indexes_dict[str(counter + 1)] = doc  # here new code for dict

        document_names.append(doc)

        documents[basename(j)] = doc

        counter = counter + 1

    print("documents_indexes_dict: ", documents_indexes_dict)
    print("document_names: ", document_names)
    print("documents: ", documents)

    print('112: ' + hospital_)
    for i in range(len(document_names)):
        print(document_names[i] + '\n')
        print("sg dc:",document_names[i] + '\n')
        if document_names[i] == 'unknown':
            if len(document_names) - 1 > i > 0:
                if document_names[i - 1] == document_names[i + 1]:
                    # print('166')
                    # print(i-1)
                    # print(document_names[i-1])
                    # print(document_names[i+1])
                    # print(i+1)
                    # print('166')
                    document_names[i] = document_names[i - 1]
                    documents_indexes[2 * i + 1] = document_names[i - 1]
                    documents[basename(path + str(i + 1) + ".jpg")] = deepcopy(
                        documents[basename(path + str(i + 1) + ".jpg")])

    print(document_names)
    print(documents_indexes)
    unq, counts = np.unique(np.array(document_names), return_counts=True)
    frequencies = dict(zip(unq, counts))
    print(frequencies)

    """ old code
    ress = {'hospital': hospital_,
            'documents:': documents_indexes
            }
    """

    ress = {'hospital': hospital_,
            'documents': documents_indexes_dict
            }

    for i in range(1, len(os.listdir(path)) + 1):
        # print(os.path.join(path, imgname))
        # print(documents[basename(path + str(i) + ".jpg")])
        print("documents[0]:", list(documents.values())[0])
        try:
            old_imgname = os.path.join(path, basename(path + str(i) + ".jpg"))
            new_imgname = os.path.join(path, documents[basename(path + str(i) + ".jpg")] + str(i) + ".jpg")
        except:
            old_imgname = os.path.join(path, os.listdir(path)[0])
            new_imgname = os.path.join(path, list(documents.values())[0] + ".jpg")

        print(new_imgname, old_imgname)
        os.rename(old_imgname, new_imgname)
    print("check Folder: ", path)

    print('175')
    print(ress)
    with open("jsons_result/"+str(random_id)+'.json', 'w') as f:
        json.dump(ress, f)

    # print("final: ", documents_indexes_dict) #new code dict
    # print(documents)
    # with open("all_bill.json", 'w') as output:
    #     output.write(str(ress))

    return ress, documents, json_datas


path_to_watch = os.path.join("./listen")
def classify(path_to_watch):

    # before = dict([(f, None) for f in os.listdir(path_to_watch)])
    try:
        token = 1
        while token:
            print("1--->")
            # dircreate = str(uuid.uuid4())
            # BASE_IMGS_FOLDER = r"D:\SH-classificationdocs\icici_medical\portal"
            # MAIN_DIR = "listen"
            #
            # # pdf_filename = list(os.scandir(MAIN_DIR))[0].name
            # # print('193')
            # # print(pdf_filename)
            # folder = BASE_IMGS_FOLDER + '/' + dircreate
            # os.mkdir(BASE_IMGS_FOLDER + '/' + dircreate)
            # i = 0
            # for filename in os.listdir(path_to_watch):
            #
            #     print(filename)
            #     pathhere = MAIN_DIR + '/' +list(os.scandir(MAIN_DIR))[i].name
            #     print(pathhere)
            #     path = "./listen/" + pathhere
            #     #filepathhere = os.path.join(path_to_watch,filename)
            #
            #     converting_to_image(path,folder)
            #     i = i+1
            #
            #
            # token = 0
            # time.sleep(10)
            # after = dict([(f, None) for f in os.listdir(path_to_watch)])
            # added = [f for f in after if not f in before]
            # removed = [f for f in before if not f in after]
            if 1:
                # fileName = added

                # print("Added: ", ", ".join(added))
                # print(fileName[0])
                print("2--->")
                BASE_IMGS_FOLDER = r"imgsfolders"
                MAIN_DIR = "listen"
                # pdf_filename = list(os.scandir(MAIN_DIR))[0].name
                # claim_id = pdf_filename.split('.')[0]
                # os.mkdir(BASE_IMGS_FOLDER + '/' + claim_id)
                random_id = str(uuid.uuid4())
                os.mkdir(BASE_IMGS_FOLDER + '/' + random_id)
                folder = BASE_IMGS_FOLDER + '/' + random_id
                print("3--->")
                root_path = "./extract"
                hospital_identified = 'none'
                ##pt.pytesseract.tesseract_cmd = "./tesseract/tesseract.exe"
                # path = "./listen/" + pdf_filename
                save_path = folder
                # print('here 62')
                # print(pdf_filename,'/n')
                i = 0
                # converting_to_image(path, save_path)
                print("4--->")
                for filename in os.listdir(MAIN_DIR):
                    print("5--->")
                    print(filename)
                    eachfilepath = os.path.join(MAIN_DIR, filename)
                    print("6--->")
                    converting_to_image(eachfilepath, save_path, folder)
                    print("7--->")

                result, documents, json_datas = seggregator(save_path, random_id)
                token = 0
            # if removed:
            #     print("Removed: ", ", ".join(removed))
            # before = after
    except:

        print('2except')
        save_path = path_to_watch
        result, documents, json_datas = seggregator(save_path, random_id)
        originalfilepath = os.path.join(path_to_watch, os.listdir(path_to_watch)[0])
        BASE_IMGS_FOLDER = r"imgsfolders"
        targetfilepath = os.path.join(folder, os.listdir(path_to_watch)[0])
        shutil.copyfile(originalfilepath, targetfilepath)
    return documents, result

# remove : for result
# classify(path_to_watch)

"""
listen_path = r"listen"
while True:
    if len(os.listdir(listen_path)) != 0:
        # Classification code starts here
        for filename in os.listdir(listen_path):

            os.remove(os.path.join(listen_path, filename))
            print("Deleted ->", filename)
            time.sleep(1.0)

            if len(os.listdir(listen_path)) == 0:
                break
    else:
        print("No file found! recheck starts in 3 second...")
        time.sleep(3.0)
"""