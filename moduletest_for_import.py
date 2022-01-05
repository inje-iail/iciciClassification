def hospitalfinder(txt: str):
    print('122 \n\n')
    # print(txt)
    print(txt)
    print("\n\n138")
    commonvar = txt.lower().replace(" ", "")
    hospital_local = 'none'
    if txt.lower().replace(" ", "").__contains__('nanavati'):
        hospital_local = 'nanavati'
    elif txt.lower().replace(" ", "").__contains__('medanta') or txt.lower().replace(" ", "").__contains__('medantha'):
        hospital_local = 'medanta'
    elif txt.lower().replace(" ", "").__contains__('07aaabb0018m1z2') or txt.lower().replace(" ", "").__contains__(
            '07aaabbo018m1z2') or 'maxsuperspecialityhospital,patparganj' in txt.lower().replace(" ", ""):
        hospital_local = 'maxpatparganj'
    elif txt.lower().replace(" ", "").__contains__('07aaatd5283g1zr') or (
            'maxhealthcare' in commonvar and 'saket' in commonvar) or (
            'maxsuperspeciality' in commonvar and 'saket' in commonvar):
        hospital_local = 'maxsaket'
    elif txt.lower().replace(" ", "").__contains__('09aaccc4239q1z6') or txt.lower().replace(" ", "").__contains__(
            '09aaccc4239q126'):
        hospital_local = 'maxvaishali'
    elif commonvar.__contains__('06aaaca6671n1ze') or commonvar.__contains__(
            '06aaaca6671nize') or commonvar.__contains__('06aaaca667in1ze') or commonvar.__contains__(
        'ogaaaca6671nize'):
        hospital_local = 'maxgurgaon'
    elif commonvar.__contains__('maxsuperspecialityhospital,shalimarbagh'):
        hospital_local = 'maxshalimarbagh'
    elif txt.lower().replace(" ", "").__contains__('07aaatg2183j22n') or txt.lower().replace(" ", "").__contains__(
            '07aaatg2183j2zn') or 'otaaatg2193122n' in commonvar:
        hospital_local = 'max'
    elif txt.lower().replace(" ", "").__contains__('deenanath') or txt.lower().replace(" ", "").__contains__(
            'deenanathmangeshkar'):
        hospital_local = 'deenanath'
    elif txt.lower().replace(" ", "").__contains__('astermim'):
        hospital_local = 'aster'
    elif txt.lower().replace(" ", "").__contains__('blksuperspeciality') or 'info@blk' in commonvar or (
            'blk' in commonvar and 'passionforlife' in commonvar):
        hospital_local = 'blk'
    elif txt.lower().replace(" ", "").__contains__('g.kuppuswamy'):
        hospital_local = 'gknaidu'
    elif txt.lower().replace(" ", "").__contains__('prshospital'):
        hospital_local = 'prs'
    elif txt.lower().replace(" ", "").__contains__('amritainstituteofmedical'):
        hospital_local = 'amrita'
    elif txt.lower().replace(" ", "").__contains__('07aaaci2398n1z4') or txt.lower().replace(" ", "").__contains__(
            '07aaacl2398n1z4') or txt.lower().replace(" ", "").__contains__('07aaac12398n1z4') or txt.lower().replace(
        " ", "").__contains__(
        '07aaac12398n124') or "Kindly send final approval as per policy T & C of the patient according to Room Rent Capping".lower() in txt.lower() or "So that there should not be any deductions at the time of settlement of the Claim".lower() in txt.lower():
        hospital_local = 'indraprasthaapollo'
    elif txt.lower().replace(" ", "").__contains__('sirgangaramhospital'):
        hospital_local = 'sirgangaram'
    elif txt.lower().replace(" ", "").__contains__("kokilaben") or txt.lower().replace(" ", "").__contains__(
            "dhirubhaiambani"):
        hospital_local = 'kokilaben'
    elif txt.lower().replace(" ", "").__contains__("yashodahospital") and 'ghaziabad' not in commonvar:
        hospital_local = 'yashoda'
    elif commonvar.__contains__('yashodasuperspeciality') and 'ghaziabad' not in commonvar:
        hospital_local = 'yashodasuperspecialityhospital'
    elif txt.lower().replace(" ", "").__contains__("29aagcm5933r2zk"):
        hospital_local = 'manipalbengaluru'

    elif commonvar.__contains__('fortisescorts'):
        hospital_local = 'fortisescorts'
    elif txt.lower().replace(" ", "").__contains__('36aaaca5443n3zh') or "36AAACA5Final".lower() in txt.lower().replace(
            " ", ""):
        hospital_local = 'apollohyd'
    elif txt.lower().replace(" ", "").__contains__('27aaaca5443n2zh') or commonvar.__contains__(
            'apollohospitalsnavimumbai') or "27aaaca5443n" in txt.lower().replace(" ", ""):
        hospital_local = 'apollonavimumbai'
    elif txt.lower().replace(" ", "").__contains__('33aaaca5443n3zn') or commonvar.__contains__('33aaaca5443n32n'):
        hospital_local = 'apollochennai'
    elif txt.lower().replace(" ", "").__contains__('19aaeca5407e1zy') or "wwwapollogleneaglesin" in txt.lower().replace(
            ".", "") or '19aaeca5407eizy' in txt.lower() or commonvar.__contains__(
        'pollogleneagleshospitals') or commonvar.__contains__('19MACCA5-107E1ZY'):
        hospital_local = 'apollogleneagleskolkata'
    elif txt.lower().replace(" ", "").__contains__('29aabci5313c1zz') or txt.lower().replace(" ", "").__contains__(
            '29aabc15313c1zz') or (commonvar.__contains__('bc15313c1zz') and commonvar.__contains__('karnataka')) or (
            commonvar.__contains__('bci5313c1zz') and commonvar.__contains__('karnataka')) or (
            commonvar.__contains__('29aabc1531') and commonvar.__contains__('karnataka')) or (
            'bc15313' in commonvar and 'bangalore' in commonvar):
        hospital_local = 'apollobanglore'
    elif commonvar.__contains__('21aaaca5443n3zs'):
        hospital_local = 'apollobhubaneshwar'
    elif txt.lower().replace(" ", "").__contains__('36aabca7322f1z1') or txt.lower().replace(" ", "").__contains__(
            '36aabca7322f121') or 'aighospitals' in commonvar:
        hospital_local = 'aighospitals'
    elif txt.lower().replace(" ", "").__contains__('06aafca0130m1z1') or txt.lower().replace(" ", "").__contains__(
            '06aafca0130m121'):
        hospital_local = 'artemis'

    elif txt.lower().replace(" ", "").__contains__('miot'):
        hospital_local = 'miotinternational'
    elif txt.lower().replace(" ", "").__contains__('rubyhallclinic') or txt.lower().replace(" ", "").__contains__(
            '27aaaci7904g1zn'):
        hospital_local = 'ruby'
    elif txt.lower().replace(" ", "").__contains__('06aadcb0899g1zn') or txt.lower().replace(" ", "").__contains__(
            'asianinstituteofmedicalsciences'):
        hospital_local = 'asian'
    elif txt.lower().replace(" ", "").__contains__('sarvodayahospital'):
        hospital_local = 'sarvodaya'
    elif txt.lower().replace(" ", "").__contains__('hindujanationalhospital'):
        hospital_local = 'hinduja'
    elif txt.lower().replace(" ", "").__contains__('sriramachandrahospital') or txt.lower().replace(" ",
                                                                                                    "").__contains__(
        '33aaats2283d2zs'):
        hospital_local = 'sriramachandra'
    elif txt.lower().replace(" ", "").__contains__('fortis') and txt.lower().replace(" ", "").__contains__('mohali'):
        hospital_local = 'fortismohali'
    elif txt.lower().replace(" ", "").__contains__('fortis') and txt.lower().replace(" ", "").__contains__('jindal'):
        hospital_local = 'fortisjindal'
    elif txt.lower().replace(" ", "").__contains__('jupiterhospital') or txt.lower().replace(" ", "").__contains__(
            '27aabcji982e1zn'):
        hospital_local = 'jupiter'
    elif 'krishnainstituteofmedicalsciences' in commonvar or '36aacck2540g1zu' in commonvar or '36aacck2540glzu' in commonvar or '36aacck2540gizu' in commonvar:
        hospital_local = 'KIMSsecunderabad'
    elif 'kimstrivandrum' in commonvar:
        hospital_local = 'KIMStrivandrum'
    elif 'carenampally' in commonvar:
        hospital_local = 'carenampally'
    elif '36aabca7624c1z2' in commonvar or 'carehospitals,banjarahills' in commonvar:
        hospital_local = 'carebanjara'
    elif 'parashospital' in commonvar:
        hospital_local = 'parasgurgaon'
    elif 'hiranandanihospital' in commonvar or '27aaath0960n2zf' in commonvar or '27aaath0960n22f' in commonvar:
        hospital_local = 'hiranandani'
    elif 'www.rfhospital.org' in commonvar:
        hospital_local = 'relaince'
    elif 'fortishospital' in commonvar and 'shalimarbagh' in commonvar:
        hospital_local = 'fortisshalimar'
    elif ('fortis' in commonvar and 'mulund' in commonvar) or (
            'myfortishealthcare.com' in commonvar and 'mumbai' in commonvar):
        hospital_local = 'fortismulund'
    elif 'fortis' in commonvar and 'gurugram' in commonvar:
        hospital_local = 'fortisgurugram'
    elif txt.lower().replace(" ", "").__contains__(
            'fortismemorial') or 'fortisnxt/takecare' in commonvar or 'fortishospital' in commonvar or 'myfortishealthcare.com' in commonvar:
        hospital_local = 'fortis'
    elif 'christianmedicalcollege' in commonvar:
        hospital_local = 'christianmedicalcollege'
    elif 'continentalhospital' in commonvar:
        hospital_local = 'continentalhospital'
    elif 'srminstitute' in commonvar:
        hospital_local = 'SIMS'
    elif 'akashhealthcare' in commonvar:
        hospital_local = 'aakash'
    elif 'bhailalamin' in commonvar or 'baghospital' in commonvar:
        hospital_local = 'bhailalamin'
    elif 'kailashhospital' in commonvar or 'kailashhealthcare' in commonvar:
        hospital_local = 'kailashhospital'
    elif ('maxsuper' in commonvar and 'mohali' in commonvar) or '03aacch151881zg' in commonvar:
        hospital_local = 'maxmohali'
    elif 'mazumdarshawmedical' in commonvar:
        hospital_local = 'narayanahrudayalaya'
    elif 'rajivgandhicancerinstitute' in commonvar:
        hospital_local = 'rajivgandhicancerinstitute'
    elif 'rainbowchildren' in commonvar:
        hospital_local = "rainbowchildren'smedicare"
    elif 'sribalaji' in commonvar and 'actionmedicalinstitute' in commonvar:
        hospital_local = 'sribalaji'
    elif (
            'yashoda' in commonvar and 'hospital' in commonvar and 'researchcentre' in commonvar and 'nehrunagar' in commonvar) or (
            'yashodahospital' in commonvar and 'nehrunagar' in commonvar):
        hospital_local = 'yashodaghaziabad'
    elif 'caritashospital' in commonvar:
        hospital_local = "caritashospital"
    elif 'kovaimedical' in commonvar:
        hospital_local = "kovaimedicalcenter"
    elif 'sriramakrishnahospital' in commonvar:
        hospital_local = "sriramakrishnahospital"
    elif 'kimskollam' in commonvar:
        hospital_local = "kimskollam"
        # elif txt.lower().replace(" ", "").__contains__('kims'):
        #     hospital_local = 'kims'
    elif 'nsmemorial' in commonvar or 'nsmimskollam' in commonvar:
        hospital_local = 'nsmemorialinstituteofmedicalscience'
    elif 'tuliphospital' in commonvar or 'tulipmultispeciality' in commonvar:
        hospital_local = 'tuliphospital'
    elif 'jaypeehospital' in commonvar or '09aaccj9811dlzm' in commonvar:
        hospital_local = 'jaypeehospital'
    elif 'sparshsuper' in commonvar:
        hospital_local = 'sparshhospital'
    elif 'gghospital' in commonvar:
        hospital_local = 'GGHospital'
    elif 'rajagiri' in commonvar and 'hospital' in commonvar:
        hospital_local = 'rajagirihospital'
    elif 'royalcaresuperspeciality' in commonvar:
        hospital_local = 'royalcare'
    elif ('deep' in commonvar and 'hospital' in commonvar and 'lampoflife' in commonvar) or (
            'deepnursinghome' in commonvar):
        hospital_local = "deephospital"
    elif 'babymhospital' in commonvar or 'babymemorialhospital' in commonvar:
        hospital_local = 'babymemorialhospital'
    elif ('noblehospitals' in commonvar and 'hadapsar,pune' in commonvar) or 'care@noblehospitalspune' in commonvar:
        hospital_local = 'noblehospitalspune'
    elif 'venkateshwarhospitals' in commonvar or '07aacaa1301klzb' in commonvar:
        hospital_local = "venkateshwarhospitalsdelhi"
    elif 'hospitalamritdhara' in commonvar or 'amritdhara.my.hospital' in commonvar:
        hospital_local = "amritdharahospital"
    elif 'www.saideephospital.com' in commonvar or 'info@saideephospital.com' in commonvar:
        hospital_local = 'saideephealthcare'
    elif 'kongunadhospital' in commonvar or '33aabck4270g' in commonvar:
        hospital_local = "kongunadhospitals"
    elif 'skhospitals@yahoo.co' in commonvar or 'skhospital' in commonvar:
        hospital_local = "skhospital"
    elif 'sutpattom' in commonvar or '32aabct6646b2' in commonvar:
        hospital_local = 'sutpattomhospital'
    elif 'holycrosshospital' in commonvar or 'www.holycrosskottiyam.org' in commonvar or 'admin@holycrosskottiyam.org' in commonvar:
        hospital_local = "holycrosshospital"
    elif 'jubileememorial' in commonvar or 'jubileehospital@hotmail' in commonvar:
        hospital_local = "jubileememorial"
    elif '32aaatl1070d2za' in commonvar or '4842403877' in commonvar:
        hospital_local = "lisiehospital"
    elif 'contact@msrmh.com' in commonvar or ('ramaiah' in commonvar and 'memorialhospital' in commonvar):
        hospital_local = "ramaiahmemorial"
    elif 'poonahospital' in commonvar or 'www.poonahospital.org' in commonvar:
        hospital_local = "poonahospital"
    elif 'billrothhospitals.com' in commonvar or 'www.billrothhospitals' in commonvar:
        hospital_local = "billrothhospital"
    elif 'amalainstitute' in commonvar or '914872304000' in commonvar:
        hospital_local = "amalahospital"
    elif 'ananthapuri' in commonvar or 'u85110kl1992ptc006645' in commonvar:
        hospital_local = "ananthapurihospitals"
    elif 'jehangir' in commonvar or 'info@jehangirhospital.com' in commonvar:
        hospital_local = "jehangirhospital"
    elif 'satgurupratapsingh' in commonvar or 'info@spshospitals.com' in commonvar:
        hospital_local = "satgurupratapsinghhospitals"
    elif 'sreegokulam' in commonvar or 'www.sgmc.in' in commonvar:
        hospital_local = "sreegokulammedicalcentre"
    elif 'metrospecialityhospital' in commonvar or '06aadcm5528m' in commonvar:
        hospital_local = "metrohospital"
    elif 'noorulislaminstitute' in commonvar or 'www.nimshospital' in commonvar:
        hospital_local = "NIMS"
    elif "bombayhospital" in commonvar:
        hospital_local = "bombayhospital"
    elif "kghospital" in commonvar or 'govindaswamynaidumedicaltrust' in commonvar:
        hospital_local = 'kghospital'
    elif "kalingainstituteofmedicalscience" in commonvar or 'pradyumnabalmemorial' in commonvar:
        hospital_local = "kalingainstituteofmedicalscience"
    elif "batrahospital" in commonvar or "batrahospitaldelhi" in commonvar:
        hospital_local = "batrahospital"
    elif "kailashhospitals" in commonvar or 'kailash.gnoida' in commonvar:
        hospital_local = "kailashhospitals"
    elif 'dayanandmedicalcollege' in commonvar:
        hospital_local = "dayanandhospital"
    elif 'psghospitals' in commonvar or 'psghospitalspeelameducoimbatore' in commonvar or 'www.psghospitals.com' in commonvar:
        hospital_local = "psghospital"
    elif 'fortishospitalnoida' in commonvar:
        hospital_local = "fortisnoida"
    elif 'lakeshoregloballifecare' in commonvar or 'lakeshorehospital' in commonvar or 'www.lakeshorehospital.com' in commonvar:
        hospital_local = "lakeshorehospital"
    elif 'bhagwanmahaveerjainhospital' in commonvar or 'www.bmjh.org' in commonvar:
        hospital_local = "bhagwanmahaveer"
    elif 'narayananethralaya' in commonvar or 'yourfaithshallhealyou' in commonvar:
        hospital_local = "narayananethralayahospital"
    elif 'ckbirlahospitals' in commonvar or '19aaatt4227c1zo' in commonvar:
        hospital_local = "ckbirlahospital"
    elif (
            'gangamedicalcentre' in commonvar or 'srs@gangahospital.com' in commonvar) or 'gangamedicalcentre' in commonvar and (
            'mettupalayamroad,coimbatore' in commonvar):
        hospital_local = "ganga"
    elif 'themissionhospitaldurgapur' in commonvar or 'www.themissionhospital.com' in commonvar or 'aunitofdugapurmedicalcentre' in commonvar:
        hospital_local = "themissionhospital"
        # elif 'prshospital' in commonvar or 'www.prshospital.com' in commonvar or 'aahcpFinal' in commonvar:
        #     hospital_local = "prs"
    elif 'columbiaasiareferralhospital' in commonvar or 'wwww.columbiaindiahospitals.com' in commonvar or '29aaccc2943f1zs' in commonvar:
        hospital_local = "columbiaasiahospital"
    elif 'breachcandyhospital' in commonvar or 'www.breachcandyhospital' in commonvar or 'info@breachcandyhospital' in commonvar:
        hospital_local = "breachcandyhospital"
    elif 'kamakshimemorialhospital' in commonvar:
        hospital_local = "dr.kamakshimemorialhospital"
    elif 'bellevueclinic' in commonvar or '03322872321' in commonvar:
        hospital_local = "bellevueclinic"
    elif "woodlandsmultispeciality" in commonvar or 'woodlandhospital.in' in commonvar:
        hospital_local = "woodlandhospital"
    elif 'caseno.:hsh' in commonvar or 'caseno:hsh' in commonvar or 'caseno.hsh' in commonvar:
        hospital_local = "holyspirithospital"
    elif 'starhospitals' in commonvar or '36aaacu8638b' in commonvar or '040-44777777' in commonvar:
        hospital_local = "starhospital"

    elif 'jaypeehospital' in commonvar or '09aaccj9811dlzm' in commonvar:
        hospital_local = 'jaypeehospital'

    elif 'globalhospitals' in commonvar or 'globalhospital' in commonvar or '+912267670121' in commonvar or 'www.globalhospitalsindia.com' in commonvar:
        hospital_local = 'globalhospital'
    elif '09aagcm9435l1zu' in commonvar or 'apollomedics' in commonvar or 'apollomedicssuperspecialityhospitals' in commonvar:
        hospital_local = 'apollomedicshospitals'
    elif 'humancaremedicalcharitabletrust' in commonvar or 'delhi.manipalhospitals.com' in commonvar or '001-49674967' in commonvar:
        hospital_local = 'manipaldelhi'
    elif 'astercmihospital' in commonvar or 'www.asterbangalore.com' in commonvar or '29aaccd7912k1zd' in commonvar:
        hospital_local = 'astercmibangalore'
    elif 'wockhardthospitals' in commonvar or '8108181081' in commonvar or 'www.wockhardthospitals.com' in commonvar or '27aaacw3342g1zh' in commonvar:
        hospital_local = 'wockhardthospital'
    elif 'qrghealthcity' in commonvar or '06aaacq2238d1zw' in commonvar or 'www.qrghealthcity.com' in commonvar:
        hospital_local = 'qrghealthcityhospital'
    elif 'marsleevamedicity' in commonvar or '32aabtp0809p1zg' in commonvar or '@marsleevamedicity.com' in commonvar:
        hospital_local = 'marsleevamedicity'

    else:
        hospital_local = "none"

    print('147: ' + hospital_local)
    return hospital_local


def classifier(txt: str, c: int, hosp: str,j,randomid):
    if hosp == 'nanavati':
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "operationnotes", "investigations", "courseinhospital",
                               "conditionatdischarge", "dietadvice", "followupdate", "medications", "adviceondischarge",
                               "admittingconsultant", "departmentname", "drugallergy", "history"],
            "billdetails": ["patientbill(details)", "i.p.no.", "ipno", "billno", "total"],
            "admissionnote": [],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia", "address"
                                               "uidai", "uldal"],
            "policy": [],
            "labreport": ["departmentoflaboratorymedicine", "reportstage", "labno", "sampledate"],
            "cashless": ["cashlessauthorizationrequestnote", "tobefilledbytheinsured", "tobefilledbythetreatingdoctor",
                         "insuredcardidno", "declaration+"],
            "authorizationletter": ["authorizationletter", "finalsanctionedamount", "hospitalagreedtariff",
                                    "finalapprovedamount"],
            "prescription": [],
            "policyidcard": ["cardno", "validfrom", "validto", "icicilombardhealthcarecard"],
        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "hospitalagreedtariff", "claimform", "declarationbythepatient",
                               "teslamri"],
            "billdetails": ["dischargesummary", "submissionofclaimpapers", "relation", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "transport", "licence", "drive", "starhealth", "hospitalisation", "manager",
                          "bill", "medicine", "doctor", "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", ],
            "labreport": ["admissiondate", "checklistfortpadispatch", "dischargesummary", "conditionatdischarge",
                          "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],

        }
    elif hosp == 'medanta':
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "foremergencyandambulance", "followup", "attendingpractitioner",
                               "adviceondischarge", "conditionatdischarge", "encounterid", "dischargemedication",
                               "medicalhistory", "presentingcomplaints", "courseinhospital", "surgeriesinthepast",
                               "localexamination",
                               "radiologyresults", "whentoobtainurgentcare", "followupappointment",
                               "courseinthehospital"],
            "billsummary": ["attendingdoctor", "hsncode", "admittingdoctor",
                            "billoutstanding", "visitingconsultantcharges"],
            "billdetails": ["billno", "qty", "patientid", "billofsupply", "gstin", "admittingdoctor", "ipdno",
                            "subtotal", "creditbill", "patientshare"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia", "address"
                                               "uidai", "uldal"],
            "policy": ["uhid", "policy"],
            "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "clinical", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilledbytreating", "tobefilled", "nameofthetratingdoctor",
                         "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "approvalisgiven", "claimnumber",
                                    "approvedamountinrs", "corporatename", "alapproveddate",
                                    "approvedamountinwords", "hospitalagreedtariff", "totalauthorizedamount"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }

        absent = {

            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "claimform", "declarationbythepatient", "teslamri"],
            "billsummary": ["dischargesummary", "subtotal"],
            "billdetails": ["dischargesummary", "relation", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", "findings"],
            "labreport": ["admissiondate", "financialcounselingsheet", "dischargesummary", "conditionatdischarge",
                          "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability", "sanctioned", "approvalisgiven"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],

        }
    elif hosp == 'maxsaket' or hosp == 'maxpatparganj' or hosp == 'max' or hosp == 'maxvaishali' or hosp == 'maxgurgaon' or hosp == 'maxshalimarbagh' or hosp == 'maxmohali':
        present = {
            "billsummary": ["finalbillsummary", "maxid", "finalbillofsupplyinpatient-summary", "ipid"],
            "dischargesheet": ["dischargesummary", "underwent", "conditionatdischarge", "history",
                               "dischargemedication", "followingmedication", "forappointment", "incaseyourequire",
                               "operationdetails", "pastmedical", "pastsurgical", "operativefindings",
                               "medicationondischarge", "incaseofemergency", "reportbackto", "courseofhospital",
                               "internalmedicine",
                               "doctornote", "adviceondischarge", "showed", "revealed", "treatmentreceived",
                               "adviceondischarge", "optedfor", "instructionatdischarge", "caseofemergency",
                               "formedicalser", "followupadvice", "courseinhospital", "majormedicationused",
                               "dateofadmission", "dateandtimeofdischarge", "reportbacktoyour", "incaseofany", "ssnno",
                               "pleasecontact", "investigation", "profile", "incaseofrequire"],
            "billdetails": ["finalbillofsupplyinpatientbill(detailed)", "qty", "price", "itemname", "amount(rs",
                            "totalamount",
                            "subtotal"],
            "coveringletter": ["coveringletter", "ipid", "maxid", "finalbillsummary"],
            "aadhar": ["uniqueidentification", "enrollmentno", "youraadharno", "uniqueidentification",
                       "governmentofindia", "yearofbirth", "dob"],
            "cashless": ["cashless", "tobefilledbytheinsured/patient", "tobefilledbytreatingdoctor/hospital",
                         "nottobefaxed/scanned", "declarationbythepatient", "hospitaldeclaration"],
            "authorizationletter": ["authorizationletter", "finalsanctionedamount", "alrequesteddate", "alnumber",
                                    "termsandconditionsofauthorization", "alapproveddate", "hospitalagreedtariff"],
            "labreport": ["laboratoryinvestigationreport", "labid", "reportingdate", "collectiondate"],
            "pan": ["incometax", "govtofindia", "govt.ofindia", "permanentaccountnumber"],
            "policyidcard": ["healthcarecard", "tollfree"],
        }
        absent = {
            "billsummary": ["subtotal", "healthcarecard", "detailed", "creditbillchecklist", "coveringletter",
                            "knowyourcustomer",
                            "knowyourcustomer"],
            "dischargesheet": ["coveringletter", "creditbillchecklist", "qty", "healthcarecard", "alapproveddate",
                               "knowyourcustomer", 'itemname'],
            "aadhar": ["subtotal", "qty", "knowyourcustomer", "healthcarecard", "creditbillchecklist", "amount",
                       "summary", "final", "incometax"],
            "billdetails": ["finalbillsummary", "nonadmissibleitemslist", "healthcarecard", "creditbillchecklist",
                            "coveringletter",
                            "finalbillofsupplyinpatient-summary", "healthcarecard"],
            "coveringletter": ["dischargesummary", "subtotal", "healthcarecard", "creditbillchecklist"],
            "cashless": ["incometax", "subtotal", "courseofhospital", "healthcarecard", "creditbillchecklist",
                         "courseinhospital", "labresults"],
            "pan": ["uniqueidentification", "enrollmentno", "youraadharno", "healthcarecard"],
            "labreport": ["subtotal", "coveringletter", "finalbillsummary", "healthcarecard", "creditbillchecklist"],
            "authorizationletter": ["requestforcashless", "healthcarecard", "creditbillchecklist"],
            "policyidcard": ["total", "discharge", "authorization", "creditbillchecklist"]
        }

    elif hosp == 'deenanath':
        present = {
            "billsummary": ["patientfinal", "tpaco", "refno", "netbillamount", "grossamount", "bill-provisional",
                            "in-patientfinalbill-provisional",
                            "visitnumber"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "attendingpractitioner", "dischargedate", "allergicdrugs",
                               "admissiondate", "followup", "ensuringappointment", "dateofdischarge",
                               "hospitaldeclaration", "intraoperativenotes", "medicinesgiveninward",
                               "clinicalcourseandevents",
                               "dischargediagnosis", "dateofaadmission", "dateofdischarge", "treatmentondischarge",
                               "incaseofemergency",
                               "findings", "adviceondischarge", "pendingresult", "conditionatdischarge",
                               "emergencyroom",
                               "dischargemedication", "dischargerecommendation"],
            "billdetails": ["billofsupplyinpatientbill", "netbillamount", "payeramount", "paymentmode" "summary",
                            "billdate", "signatureofaccountant", "amountinwords",
                            "gstin", "subtotal", "admincharges" "procedurecharge", "nursingcarecharge", "expirydate",
                            "qty",
                            "quantity", "batchno",
                            "signatureofcashier", "billdate", "amounttopay", "amountcollected", "investigationcharge",
                            "consultationcharge", "partytotal", "consumable", "unitprice", "mrp"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "department", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policy": ["uhid", "policy", "renewalendorsement", "endorsementno"],
            "labreport": ["report", "p.h.diagnosticcentre", "departmentof", "laboratorymedicine", "methodused",
                          "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "hospitaldeclaration", "tobefilled", "nameofthetratingdoctor",
                         "declaration", "authorizedamount", "agreedtariff", "authorizationsummary",
                         "authorizationremarks", "approvedamount", "corporateidentity",
                         "documentstobeprovidedbythehospital", "qualification", "expectedcostofinvestigation",
                         "costofimplants",
                         "expectedcostofhospitalization", "authorizedsignatory", "registrationnumberwithstate",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }

        absent = {
            "billsummary": ["quantity", "unit", "whomsoever"],
            "aadhar": ["incometax", "report", "test", "depart", "whomsoever", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "p.h.diagnosticcentre", "subtotal", "whomsoever", "hospitaldeclaration",
                               "claimform", "cashlessauthorization", "approved(enhancement", "authorizedamount",
                               "declarationbythepatient", "teslamri", "documentstobeprovided"],
            "billdetails": ["dischargesummary", "relation", "whomsoever", "mandatorypasthistory", "bill-provisional"],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "whomsoever", "clinical", "billsummary",
                    "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "whomsoever", "uidai", "uldal"],
            "panaadhar": ["laboratory", "diagnosis", "prescription", "starhealth", "hospitalisation", "manager", "bill",
                          "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", "requestforcashless"],
            "labreport": ["admissiondate", "historyofpresent", "dischargesummary", "conditionatdischarge",
                          "detailsofpatientadmitted", "incaseofemergency",
                          "billsummary", "tobefilled", "cashless", "approximateestimate"],
            "cashless": ["claimnumber", "selfdeclaration", "relation",
                         "admissionofliability", "authorizedamount", "authorisedamount"
                , "deductionreason"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "notes", "ipprogressnote", "attendingpractitioner", "claimform",
                             "corseandevents"],
            "policyidcard": [],

        }

    elif hosp == 'aster':
        present = {

            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "uhid", "ipno", "diagnosis", "history", "investigations",
                               "interpretation",
                               "crossconsultation", "departmentof", "laboratorymedicine", "methodused", "testname",
                               "scans&laboratory",
                               "scanno", "report", "radiologist", "mri", "observations",
                               "reportedon", "reportedby", "adviceondischarge", "courseinthehospital", "investigation",
                               "laboratory", "ultrasoundfor", "courseinhospital", "medication", "findings",
                               "adviceondischarge", "pendingresult", "conditionatdischarge",
                               "dischargemedication", "dischargerecommendation"],
            "consolidatedbill": ["consolidatedbill", "admitdate", "lessexcessamount", "dischargedate"],
            "billsummary": ["patientbill(summary)", "i.p.no", "billno", "debit(rs"],
            "billdetails": ["billofsupplyinpatientbill", "billinggroup", "netbillamount", "payeramount",
                            "paymentmode" "summary",
                            "billdate", "preparedby", "printedby", "signatureofaccountant", "amountinwords",
                            "gstin", "subtotal", "admincharges" "procedurecharge", "nursingcarecharge",
                            "expirydate",
                            "qty", "netamount", "totalamount", "totalformedicines",
                            "quantity", "batchno", "medicines", "bedcharges"
                                                                "signatureofcashier", "billdate", "amounttopay",
                            "amountcollected", "investigationcharge",
                            "consultationcharge", "partytotal", "consumable", "unitprice", "mrp"],
            "pharmacybillstatement": ["pharmacybillstatement", "pharmacyissues", "drugdescription", "pharmacyreturns"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],

            "labreport": ["diagnosticreport", "labno", "laboratoryservices", "testreport",
                          "dateandtimeofsamplecollection", "servicename"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],

            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "advancereceipt": ["advancereceipt", "doa", "paymentmodedetails"],
            "policy": ["policy", "periodofinsurance"],
        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["diagnostic", "nursesrecord", "physician'srecord", "laboratoryservice",
                               "medicationsprescribed", "tobefilledbytreatingdoctor", "detailsofpatientadmitted",
                               "hospitaldeclaration", "billsummary", "detailsofpatientadmitted",
                               "filledbytreatingdoctor", "paidamount", "claimform", "declarationbythepatient",
                               "teslamri"],
            "consolidatedbill": ["bill(details)", "pharmacybillstatement", "pharmacyreturns"],
            "billsummary": ["labno", "patientbill(details)", "pharmacyreturns", "pharmacybillstatement",
                            "advancereceipt"],
            "billdetails": ["consolidatedbill", "nursesrecord", "drugdescription", "pharmacyreturns",
                            "pharmacybillstatement", "testreport", "patientbill(summary)", "dischargesummary",
                            "advancereceipt", "relation", "mandatorypasthistory", ],
            "pharmacybillstatement": ["consolidatedbill", "patientbill(details)", "bill(details)"],
            "admissionnote": [],
            "pan": ["discharge", "prescription", "medication", "declaration", "qualification", "hrctchest", "radiology",
                    "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "cardiac", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "prescription", "medication", "starhealth", "hospitalisation", "manager",
                          "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "requestforcashless", "authorizationsummary", "totalbillamount",
                       "departmentofradiology", "hrctchest",
                       "invoice", "advancereceipt", "doa", "interpretation", "liverfunction"],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "dischargesummary", "tobefilled", "paymentreceipt", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],
            "advancereceipt": ["consolidatedbill", "billofsupply"],

        }
    elif hosp == 'blk':
        present = {
            "aadhar": ["youraadhaarno.", "address", "proofofidentity", "enrolmentno", "governmentofindia", "uidai",
                       "uldal"],
            "dischargesheet": ['dischargesummary', "reasonforadmission", "systemicexamination", "courseinhospital",
                               "investigation(s)", "dietaryadvice", "follow-upadvice", "uhid", "ipno",
                               'provisionaldiagnosis', 'investigationresults', 'kindlycallincase', 'dietaryadvise',
                               'procedureperformed', 'adviceondischarge', 'courseinthehospital', 'admissiondate',
                               'presentingcomplaints', 'significantmedicalhistory', 'generalexamination',
                               'physicalexamination'],
            "billsummary": ["inpatientbill(summary)", "in-patientbill(summary)", "gstin", "grossamount",
                            "finalapprovedamount",
                            "netamountinwords"],
            "billdetails": ["billofsupply(detailed)", "in-patientbill(details)", "bedcharge", "totalfor",
                            "totalforconsultation",
                            "itemname", "itemamount", "unit", "totalforbedcharge", "rate", "qty", "preparedby",
                            "printedby"],
            "admissionnote": [],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "department", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "uidai", "uldal"],

            "labreport": ["laboratoryservices", "blkradiology", "imaginginstitute", "sampledate", "labno",
                          "endofreport"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetreatingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration", "anyauthorizedtpa/insurance"
                                                                                 "natureofillness",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],

            "authorizationletter": ["cashlessauthorizationletter", "claimnumber", "authorizationdetails",
                                    "totalauthorizedamount", "alapproveddate", "alrequesteddate", "authorizedremarks",
                                    "authorizationsummary"],
            "prescription": [],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "policy": ["renewalendorsement", "suminsured", "periodofinsurance", "sectorclassification",
                       "nomineedetailsforproposer", "appointeedetails"],

        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ['counselingsummary', 'alapproveddate', "qty", "in-patient(details)",
                               "in-patient(summary)"],
            "billsummary": ['counselingsummary', 'dischargesummary', 'in-patientbill(details)'],
            "billdetails": ['counselingsummary', 'dischargesummary', 'in-patientbill(summary)'],
            "admissionnote": [],
            "pan": ["discharge", "laboratoryservices", "hrctchest", "radiology", "findings", "clinical", "billsummary",
                    "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "transport", "licence", "drive", "starhealth", "hospitalisation", "manager",
                          "bill", "medicine", "doctor",
                          "method", "personaldetails", "voteridcard", "taxidentification", "contactdetails",
                          "detailsofrelatedperson", "remarks"],
            "policy": [],
            "labreport": [],
            "cashless": ["claimnumber", "centralkycregistry", "customer(kyc)application", "relation",
                         "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": [],
            "policyidcard": [],

        }
    elif hosp == 'kims' or hosp == 'kimskollam' or hosp == 'kimstrivandrum':
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "attendingpractitioner", "dischargedate", "allergicdrugs",
                               "admissiondate", "followup", "ensuringappointment", "dateofdischarge",
                               "dischargediagnosis", "conditionatdischarge",
                               "findings", "adviceondischarge", "pendingresult", "conditionatdischarge",
                               "dischargemedication", "dischargerecommendation"],
            "billsummary": ["billsummary", "dischargedate", "mrno", "refno"],
            "billdetails": ["billofsupplyinpatientbill", "cptcode", "netbillamount", "payeramount",
                            "paymentmode" "summary",
                            "billdate", "signatureofaccountant", "amountinwords",
                            "gstin", "subtotal", "admincharges" "procedurecharge", "nursingcarecharge", "expirydate",
                            "qty",
                            "quantity", "batchno",
                            "signatureofcashier", "billdate", "amounttopay", "amountcollected", "investigationcharge",
                            "consultationcharge", "partytotal", "consumable", "unitprice", "mrp"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],

            "labreport": ["report", "departmentof", "medicationcpoe", "radiology", "treatmentplan",
                          "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "policy": ["uhid", "policy"],
        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "gstno", "hospitaldeclaration", "claimform", "declarationbythepatient",
                               "teslamri"],
            "billsummary": ["cptcode"],
            "billdetails": ["dischargesummary", "billsummary", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "laboratory", "radiology", "findings", "clinical", "billsummary",
                    "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", "requestforcashless", "rejectionofcashless"],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],

        }
    elif hosp == 'gknaidu':
        present = {
            "billsummary": ["billsummary", "ipno", "opno", "dischstatus", "depositbalance"],
            "deathsummary": ["deathsummary", "opno", "ipno", "presentingcomplaints", "medicationsgiven",
                             "courseinhospital", "declareddead", "causeofdeath"],
            "billofsupply": ["finalbillofsupply", "adm/dischsts", "insuranceapprovalamount"],
            "statementofcharge": ["statementofchargedetails", "ipno", "opno", "creditcompany"],
            "consolidateddispensarybill": ["consolidateddispensarybill", "ipno", "opno", "gstin"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "serum", "presentingcomplaints", "attendingpractitioner",
                               "emergencysymptoms", "dischargedate", "allergicdrugs",
                               "admissiondate", "followup", "ensuringappointment", "dateofdischarge",
                               "hospitaldeclaration", "investigations", "medicationsgiven",
                               "thesemedicationaretobe", "dischargemedicines", "ipno", "opno",
                               "findings", "advice", "pendingresult", "conditionatdischarge",
                               "dischargerecommendation"],
            "billdetails": ["billofsupplyinpatientbill", "netbillamount", "payeramount", "paymentmode" "summary",
                            "billdate", "signatureofaccountant", "amountinwords",
                            "gstin", "subtotal", "admincharges" "procedurecharge", "nursingcarecharge", "expirydate",
                            "qty",
                            "quantity", "batchno",
                            "signatureofcashier", "billdate", "amounttopay", "amountcollected", "investigationcharge",
                            "consultationcharge", "partytotal", "consumable", "unitprice", "mrp"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],

            "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "tobefilled", "noobjectiontoany", "tobefilledbytrating", "authorization",
                         "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "prescription": ["prescription", "opno", "ipno", "gstin"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "policy": ["uhid", "policy"],
        }

        absent = {
            "billsummary": ["deathsummary", "prescription", "dischargesummary", "deathsummary", "billofsupply",
                            "statementofcharge", "consolidateddispensarybill"],
            "billofsupply": ["billsummary", "prescription", "deathsummary", "dischargesummary", "statementofcharge",
                             "consolidateddispensarybill"],
            "statementofcharge": ["billsummary", "prescription", "deathsummary", "dischargesummary", "billofsupply",
                                  "consolidateddispensarybill"],
            "deathsummary": ["billsummary", "billofsupply", "prescription", "statementofcharge",
                             "consolidateddispensarybill", "dischargesummary"],
            "consolidateddispensarybill": ["billsummary", "deathsummary", "prescription", "dischargesummary",
                                           "billofsupply", "statementofcharge"],
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["deathsummary", "gstin", "memono", "consolidateddispensarybill", "billsummary",
                               "deathsummary", "tobefilledby", "hospitaldeclaration", "claimform",
                               "declarationbythepatient",
                               "teslamri"],
            "billdetails": ["dischargesummary", "billsummary", "billofsupply", "statementofcharge", "prescription",
                            "deathsummary", "consolidateddispensarybill", "relation", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", "requestforcashless"],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["billsummary", "dischargesummary", "billofsupply", "statementofcharge", "deathsummary",
                             "consolidateddispensarybill"],
            "policyidcard": [],

        }
    elif hosp == 'prs':
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "admittingdoctor", "attendingpractitioner", "dischargedate",
                               "allergicdrugs",
                               "admissiondate", "followup", "ensuringappointment", "dateofdischarge",
                               "otherinvestigationresults", "emergencycontact"
                                                            "dischargediagnosis",
                               "findings", "adviceondischarge", "pendingresult", "conditionatdischarge",
                               "dischargemedication", "dischargerecommendation"],
            "billsummary": ["creditbill", "ipno", "billno", "patientnumber", "refdate", "billtotal"],
            "billdetails": ["ipbillbreakupdetails", "ipno", "billno", "admission"],

            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],

            "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "incaseofaccident", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "policy": ["uhid", "policy"],
        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "creditbill", "ipbreakup", "claimform", "declarationbythepatient",
                               "teslamri"],
            "admissionnote": [],
            "billsummary": ["ipbillbreakup", "ipreceiptvoucher"],
            "billdetails": ["creditbill", "ipreceiptvoucher"],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", "requestforcashless"],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "policyidcard": [],

        }
    elif hosp == 'amrita':
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "drugallergies", "thyroidpanel", "cbcwbc", "dateofdischarge",
                               "dischargingstatus",
                               "medicineonadmission", "haemogram", "liverfunctiontest", "familyhistory",
                               ",hepaticfunctionpanel", "pre-opserology", "hem-panel", "urineanalysis",
                               "clinicalexamination", "investigation", "dischargemedication",
                               "planondischarge", "contentofthedischarge", "courseinthehospital", "discussion",
                               "investigations"],
            "billsummary": ["inpatientcollection", "summaryoftransactions", "totalamountdueinwords", "billdate"],
            "billdetails": [],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policy": ["uhid", "policy"],
            "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetreatingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration", "noobjectiontoanytpa"
                                                                                 "natureofillness",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "claimform", "declarationbythepatient", "teslamri"],
            "billsummary": [],
            "billdetails": ["dischargesummary", "relation", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", ],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "declaration", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],

        }
    elif hosp == 'indraprasthaapollo':
        present = {

            "billsummary": ["billofsupply", "billno", "billingtype", "amount"],
            "billdetails": ["ipno", "qty", "reftarif", "subtotal", "medicalservices", "otcharge", "otconsumable", "tab",
                            "hsn",
                            "otpharmacy", "professionalcharges", "roomrent", "wardpharmacy", "billno"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
        }
        absent = {
            "billsummary": ["qty", "deptsubtotal"],
            "billdetails": ["billofsupply", "specialization"],
            "cashless": ["qty", "deptsubtotal", "billsupply"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary'],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
        }
    elif hosp == 'sirgangaram':
        present = {
            "billdetails": ["interimrunningdatewiseitemisedbill", "qty", "price", "orderitem", "netpayable", "charge"],
            "dischargesheet": ["dischargesummary", "diagnosis", "clinicalhistory", "physicalexamination",
                               "admissioninvestigation", "procedures",
                               "followup", "dischargeadvice", "homecareservice"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],

            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
        }
        absent = {
            "billdetails": ["dischargesummary"],
            "dischargesheet": ["interimrunningdatewiseitemisedbill"],
            "cashless": ["qty", "deptsubtotal", "interimrunningdatewiseitemisedbill"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary', 'charge', "hospital"],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
        }
    elif hosp == 'kokilaben':
        present = {
            "billdetails": ["amount", "subtotal", "qty", "billno", "billdate", "speciality"],
            "billsummary": ["attendingdoctor", "admn.date"],
            "dischargesummary": ["dischargesummary", "practitioner", "treatmentondischarge", "admittedfor",
                                 "instructionstopatient",
                                 "urgentcareadvice", "signature", "dischargedate", "patientresponse",
                                 "medicationondischarge", "surgery/procedure", "pasthistory", "investigations"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
        }
        absent = {
            "billdetails": ["dischargedate"],
            "billsummary": ["dischargedate", "subtotal"],
            "dischargesummary": ['subtotal'],
            "cashless": ["subtotal", "dischargesummary", "attendingdoctor", "speciality"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary'],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
        }
    elif hosp == 'yashoda' or hosp == 'yashodasuperspecialityhospital':
        present = {

            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "billsummary": ["billofsupply", "creditfromicicilombard", "consultant", "paidamount",
                            "patientbill(summary)", "billno"],
            "billdetails": ["description", "qty", "indentno", "value", "expdate", "totalfor",
                            "chargedamount", "ipno", "subtotal", "patientbill(detail)"],
            "authorizationletter": ["cashlessauthorizationletter", "alapproveddate", "alrequesteddate",
                                    "non-packagecase", "initialapproved", "hospitalagreedtariff", "claimnumber"],
            "dischargesummary": ["dischargesummary", "mg/dl", "gms", "dateofadmission", "dateofdischarge", "diagnosis",
                                 "pasthistory", "chiefconsultant", "investigations", "examination", "absolutecounts",
                                 "forreviewvisists",
                                 "summaryofhospitalcourse", "review", "peripheralsmear",
                                 "tinyanteriorabdominalwalldefect",
                                 "recommendationsatdischarge", "adviseatthetimeofdischarge", "conditionondischarge",
                                 "incaseoffever",
                                 "dischargemedication", "inumbilicalregionwithherniation", "operativefindings",
                                 "leftminiperc",
                                 "livershowsmildlyaltered", "opdwithpriorappointment", "incaseofemergency"],
            "policyidcard": ["policyno", "icicilombardhealthcarecard", "validupto"],
            "labreport": ["departmentoflaboratorymedicine", "specimentype", "diagno", "diag.no", "studydate",
                          "samplecollecteddate"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
        }
        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "cashless": ["cashlessauthorizationletter", "knowyourcustomer", "alapproveddate"],
            "authorizationletter": ["termsandcondistionofauthorization", "supportoftheclaim"],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "centralkyc", "applicationform", "proofof", "starhealth", "hospitalisation",
                          "manager", "bill", "medicine", "doctor", "discharge",
                          "method"],
            "labreport": ["dischargesummary"],
            "billsummary": ["subtotal"],
            "billdetails": ["consultant"],
            "policyidcard": [],
            "dischargesummary": ["billofsupply", "claimform", "creditfromicicilombard", "subtotal"],
        }
    elif hosp == 'manipalbengaluru' or hosp == 'manipaldelhi':
        present = {
            "billsummary": ["inpatientinterimbillofsupply", "inpatientno", "netpayable", "netamount"],
            "billdetails": ["inpatientinterimbillofsupplydetail", "subtotal", "qty", "price", "billno",
                            "statementofbill", "billcumreceipt", "unit"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "dischargesheet": ["dischargesummary", "pasthistory", "physicalexamination", "medicaldischargedate",
                               "therapeuticprocedures", "courseoftreatment",
                               "conditionondischarge", "furtheradviceondischarge", "seekmedicalhelp"],
        }
        absent = {
            "billsummary": ["subtotal", "inpatientinterimbillofsupplydetail", "qty"],
            "billdetails": ["yoursfaithful", "enclosures"],
            "cashless": ["qty", "deptsubtotal", "billsupply"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary'],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
            "dischargesheet": ["inpatientinterimbillofsupply", "netpayable", "inpatientinterimbillofsupplydetail",
                               "qty",
                               ]
        }
    elif hosp == 'fortis' or hosp == 'fortisescorts' or hosp == 'fortisshalimar' or hosp == 'fortismohali' or hosp == 'fortismulund' or hosp == 'fortisgurugram' or hosp == "fortisbanglore" or hosp == "fortisnoida":
        present = {
            "billsummary": ["summaryrunningbill", "netpayableamount", "refundamount", "individualcredit", "roomrent",
                            "admissioncharges"],
            "billdetails": ["detailrunningbill", "particulars", "amount", "payable", "interimbill", "finalbilling",
                            "quantity", "qty",
                            "orderitem", "expirydate", "batchno"],
            "dischargesummary": ["dischargesummary", "courseinthehospital", "treatmentgiven", "followup",
                                 "proceduredone", "adviseondischarge",
                                 "dischargeinstructions", "adviceondischarge", "dischargeadvice", "medicationsgiven",
                                 "investigation",
                                 "followupadvice", "whentoobtainurgentcare", "doctorteam", "courseinhospital",
                                 "treatmentprovidedtome",
                                 "medicationgiven", "diagnosis", "chiefcomplaints", "presentillness", "medicalhistory",
                                 "allergytomedication", "findingsonexamination"],
            "progressnotes": ["progressnotes", "medications&investigations", "d.o.a.", "doa", "d.oa"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "declarationbythepatient", "agreetosign",
                         "hospitaldeclaration",
                         "wehavenoobjection", "claimform", "detailsofprimaryinsured", "detailsofinsurancehistory"
                                                                                      "natureofillness",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "alapproveddate", "alrequesteddate",
                                    "non-packagecase", "initialapproved", "hospitalagreedtariff", "claimnumber"],
            "policyidcard": ["policyno", "icicilombardhealthcarecard", "validupto", "validfrom", "corporatename"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "dob", "uidai", "uldal",
                       "uniqueindentification", "authorityofindia", "uniqueindentificationauthority", "meraaadhaar",
                       "meripehachaan"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "labreport": ["testreportstatus", "biologicalreferenceinterval", "clinicalinformation", "reported"]
        }
        absent = {
            "billsummary": ["detailrunningbill", "orderitem", "qty", "quantity"],
            "billdetails": ["detailsummarybill", "declarationbythepatient", "agreetosign"],
            "dischargesummary": ["detailrunningbill", "authorizationletter", "agreedtariff", "summaryrunningbill",
                                 "examinationsheet", "declarationbypatient", "agreetosign",
                                 "paymenttohospitalisgoverned"],
            "progressnotes": ["detailrunningbill", "summaryrunningbill", "dischargesummary"],
            "cashless": ["agreedtariff", "particularsoftransaction", "rationcard",
                         "incaseofmaternitybenefits"],
            "authorizationletter": [],
            "policyidcard": [],
            "aadhar": ['incometax', "accountnumber", 'bill', 'dischargesummary'],
            "pan": ['aadhar', 'enrollment', 'bill', 'dischargesummary'],
            "panaadhar": ['bill', 'dischargesummary', 'queryletterforenhancement', 'nameoftheinsured'],
            "labreport": [],
        }
    elif hosp == 'apollogleneagleskolkata':
        present = {
            "dischargesummary": ["dischargesummary", "uhid", "history", "familyandsocialhistory", "forenquiry",
                                 "adviceondischarge", "chiefcomplaint", "wasadmitted", "wasdischarged", "oninspection",
                                 "emergencyservice", "courseinthehospital", "mg/dl", "diagnosis",
                                 "historyofpresentillness", "physicalexamination", "pleasecallemergency",
                                 "ifyouhaveanyofthefollowingsymptoms",
                                 "treatmentsummary", "dischargemedication", "dischargeexamination",
                                 "dischargeprescription",
                                 "conditionatdischarge", "follow-upinstruction", "emergencycare", "reviewdetails"],
            "billsummary": ["finalinterimbill", "billofsupply", "billingtype", 'billestimate', 'approxestimation',
                            'managementcharges'],
            "billdetails": ["subtotal", "aliascode", "ipno", "qty", "billno", "total"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
        }
        absent = {
            "dischargesummary": ["finalinterimbill", "billofsupply", "subtotal", "aliascode", "qty"],
            "billsummary": ["aliascode", "qty"],
            "billdetails": ["finalinterimbill"],
            "cashless": ["qty", "finalinterimbill", "billofsupply"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary'],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
        }
    elif hosp == 'apollohyd' or hosp == 'apollonavimumbai' or hosp == 'apollochennai' or hosp == "apollomedicshospitals":
        present = {
            "dischargesummary": ["dischargesummary", "pasthistory", "familyandsocialhistory", "adviceondischarge",
                                 "courseinthehospital", "diagnosis", "historyofpresentillness", "physicalexamination",
                                 "pleasecallemergency", "ifyouhaveanyofthefollowingsymptoms",
                                 "treatmentsummary", "dischargemedication", "dischargeexamination",
                                 "conditionatdischarge", "follow-upinstruction", "emergencycare", "reviewdetails"],
            "billsummary": ["finalinterimbill", "billofsupply", "billingtype", 'billestimate', 'approxestimation',
                            'managementcharges'],
            "billdetails": ["subtotal", "aliascode", "ipno", "qty", "billno"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
        }
        absent = {
            "dischargesummary": ["finalinterimbill", "billofsupply", "subtotal", "aliascode", "qty"],
            "billsummary": ["aliascode", "qty"],
            "billdetails": ["finalinterimbill", "specialization"],
            "cashless": ["qty", "finalinterimbill", "billofsupply"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary'],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
        }

    elif hosp == 'apollobanglore':
        present = {
            "dischargesummary": ["dischargesummary", "pasthistory", "familyandsocialhistory", "adviceondischarge",
                                 "courseinthehospital", "diagnosis", "historyofpresentillness", "physicalexamination",
                                 "treatmentsummary", "dischargemedication", "dischargeexamination",
                                 "clinicalexamination"
                                 "conditionatdischarge", "follow-upinstruction", "emergencycare", "reviewdetails",
                                 "dischargeadvice", "followup", "yourpostdischarge", "follow-upcall",
                                 "pleaseexpectadischarge"],
            "billsummary": ["finalinterimbill", "billofsupply", "billingtype", "36aaaca5443n3zh",
                            "totalinterimbillamounttilldate", "outstandingamount", ],
            "billdetails": ["subtotal", "aliascode", "ipno", "qty", "billno"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
        }
        absent = {
            "dischargesummary": ["finalinterimbill", "billofsupply", "subtotal", "aliascode", "qty"],
            "billsummary": ["aliascode", "qty"],
            "billdetails": ["finalinterimbill", "specialization", "totalinterimbillamounttilldate", "departmentname"],
            "cashless": ["qty", "finalinterimbill", "billofsupply"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary'],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
        }
    elif hosp == 'apollobhubaneshwar':
        present = {
            "dischargesummary": ["dischargesummary", "pasthistory", "familyandsocialhistory", "adviceondischarge",
                                 "courseinthehospital", "diagnosis", "historyofpresentillness", "physicalexamination",
                                 "treatmentsummary", "dischargemedication", "dischargeexamination",
                                 "conditionatdischarge", "follow-upinstruction", "emergencycare", "reviewdetails",
                                 "g/dl", "keepthereportscarefully", "visittoourhospital"],
            "billsummary": ["finalinterimbill", "billofsupply", "billingtype", "interimbillamounttilldate"],
            "billdetails": ["subtotal", "aliascode", "ipno", "lpno", "qty", "billno", "abovedatesindicatedasdate",
                            "timeoftheentry"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
        }
        absent = {
            "dischargesummary": ["finalinterimbill", "billofsupply", "subtotal", "aliascode", "qty", "billno"],
            "billsummary": ["aliascode", "qty"],
            "billdetails": ["finalinterimbill", 'specialization'],
            "cashless": ["qty", "finalinterimbill", "billofsupply"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary'],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
        }
    elif hosp == 'aighospitals':

        present = {
            'billdetails': ['qty', 'rate', 'slipno', 'netamount', 'totalamt', 'address', 'grossamount', 'finalbill',
                            'admittedunder'],
            'dischargesummary': ['dischargesummary', 'pastmedicalhistory', 'conditionatthetimeofadmission', 'diagnosis',
                                 'recommendationsatdischarge', 'dateofdischarge''currentmedication', 'dischargetype',
                                 'conditionatdischarge', 'dischargemedications', 'dateofadmission',
                                 'incaseofmedicalemergency'],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
        }

        absent = {
            'billdetails': ['dischargesummary'],
            'dischargesummary': ['amt', 'qty'],
            "cashless": ["qty", "deptsubtotal", "billsupply"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary'],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
        }

    elif hosp == 'artemis':
        present = {
            "authorizationletter": ["termsandcondistionofauthorization", "cashlessauthorizationletter", "claimnumber",
                                    "consultantname", "supportoftheclaim", 'authorizationlettertothehospital',
                                    'alapproveddate', 'hospitalagreedtariff', 'finalapprovedamount'],
            "billdetails": ['date', 'qty', 'total', 'baserate', 'subtotal'],
            "dischargesummary": ['dischargesummary', 'followupadvice', 'followupappointment', 'presentingcomplaint',
                                 'difficultinbreathing', 'refusingtotakefeeds',
                                 'historyofpresentingcomplaint', 'hospitalcourse', 'admissiondate', 'dischargetype',
                                 'thereisbluish',
                                 'medicationgiven', 'conditionatdischarge', 'followupappointment',
                                 'withclinicalhistory', 'referencevalues', 'specimentype'
                , 'rbccount', 'interpretationofresults', 'instrumentinterpretation', 'inthesamplebythismethod',
                                 'secondspecimentype',
                                 'cutoffsfordiagnosing', 'goalsintreatment',
                                 'validationspecimen', 'finalaftervalidation', 'absoluteneutro', 'followupadvise',
                                 'respiratoryrate',
                                 'incaseofemergency', 'reportimmediatelyinemergency', 'adviceondischarge',
                                 'complaintsof',
                                 'discolourationofextremities',"impression","observations"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "labreport": ["medicalreport","laboratory","antibiotic","normalrange","specimentype","reportrange"],
        }
        absent = {

            'billdetails': ['authorizationletter', 'specimentype', 'parkmediclaiminsurance'],
            'dischargesummary': ['authorizationletter'],
            "cashless": ["qty", "deptsubtotal", "billsupply"],
            "aadhar": ['incometax', 'permanent'],
            "pan": ['enroll', 'aadhar'],
            "panaadhar": ['billofsupply', 'qty', 'dischargesummary'],
            "policyidcard": [],
            "authorizationletter": ["requestforcashless"],
            "labreport": [],
        }


    elif hosp == 'miotinternational':
        present = {
            'billsummary': ['ipfinalbill', 'totalamount', 'grosstotal', 'netpayable', 'lesswriteoff',
                            'breakupdetailsforpackage',
                            "ipfinal.bill","particulars"],
            'billdetails': ['breakupdetail', 'qty', 'coderef'],
            'dischargesummary': ['diagnosis', 'pastmedicalhistory', 'dischargemedication', 'adviceondischarge',
                                 'impression', 'operationdetails', 'courseinthehospital', 'examinationfindings',
                                 'incaseoflowcounts',
                                 'foremergencyadminissues',
                                 'chiefcomplaintsonadmission', 'conditionofthepatientonadmission', 'localexamination',
                                 'investigations', 'dischargesummary', 'dateofsurgery', 'chiefcomplaintsonadmission',
                                 'menstrualhistory',

                                 "dischargesummary", "hepaticfunction", "attendingpractitioner", "dischargedate",
                                 "allergicdrugs", "courseduringhospitalization", "repeatedinvestigations",
                                 "admissiondate", "followup", "ensuringappointment", "dateofdischarge",
                                 "hospitaldeclaration", "feverwithchills", "cvsexamination", "homeadvice",
                                 "whatcaretotake", "indoorno",
                                 "dischargediagnosis", "complaintsonadmission", "abdomenexamination", "restcourse",
                                 "findings", "adviceondischarge", "pendingresult", "conditionatdischarge",
                                 "dischargemedication", "dischargerecommendation", "treatmentadvice", "followup",
                                 "dateofadmission", "operationnote", "treatmentgiven", "semiliquid",
                                 "dischargecard", "dischargeticket", "doa", "specialinvestigation", "treatmentgiven",
                                 "treatmentadvised", "capidreview", "investigations", "blood", "treatmentised", "dod",
                                 "pasthistory","thefollowingtissuesamplesweresent","bed-sidescreening","impression","dailythreetimessteriledressing",
                                 "woundcareprotocol","precautions"
                                 ],
            'authorizationletter': ['authorizationletter', 'alrequesteddate', 'alnumber', 'initialapproved',
                                    'finalapproved', 'hospitalagreed', 'non-packagecase', 'hospitalagreedtariff'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", "urine",
                          "testdone"],
        }
        absent = {
            'billsummary': ['qty', ],
            'billdetails': ['ipfinalbill', 'totalamount'],
            'dischargesummary': ['ipfinalbill', 'breakupdetail', 'authorizationletter', 'non-packagecase',

                                 "billsummary", "cashlessauthorization", "claimform", "declarationbythepatient",
                                 "teslamri", "advancereceived", "admissioncard", "deposit", "haemogramreport",
                                 "staffisqualified", "employeeno", "empcode", "detailedbill", "policynumber",
                                 "registrationcharges", "ipfinalbill", "finalbill", "conditionsofreporting"
                                 ],
            'authorizationletter': ['qty', 'breakupdetail', 'ipfinalbill', ],
            'aadhar': ['qty', 'total', 'income', 'bill'],
            'pan': ['aadhar', 'qty', 'total', 'bill'],
            'panaadhar': ['qty', 'total', 'bill', 'dischargesummary'],
            'policyidcard': ['bill', 'total'],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless", "policy", "dischargecard", "onephotocopy",
                          "courseduring", "dischargecard",
                          "undertakingfor", "familycommunication", "continuationsheet", "receiptno",
                          "initialassessment",
                          "billcumreceipt", "claimno", "lossdate", "riskassumption", "statethat", "attendance",
                          "total:", "empcode", "government","terms&conditions","conditionsofreporting"],

        }
    elif hosp == 'ruby':
        present = {
            'billsummary': ['summarybill', 'roomandnursingcharges', 'totalbillamount', 'amountpayable',
                            'amounttorefund'],
            'billdetails': ['detailedbreakup', 'nameofthedrug', 'mfr', 'batchno', 'qty', 'detailsofmedicine', 'rate',
                            'primarycode', 'nos(unit)'],
            'dischargesummary': ['dischargesummary', 'keyinvestigationsduringhospitalization', 'laboratory',
                                 'diagnosisatthetimeofdischarge', 'presentcomplaints', 'keyfindings',
                                 'pastmedicalandsurgicalhistory', 'specialinvestigation', 'courseinthehospital',
                                 'treatmentduringhospitalisation', 'physiotherapy', 'adviceondischarge',
                                 'treatmentondischarge', 'adviceondischarge', 'courseinthehospital'],
            'authorizationletter': ['authorizationletter', 'alrequesteddate', 'alnumber', 'initialapproved',
                                    'finalapproved', 'hospitalagreed'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'billsummary': ['detailedbreakup', 'detailsofmedicine'],
            'billdetails': ['summarybill'],
            'dischargesummary': ['summarybill', 'detailedbreakup'],
            'authorizationletter': ['qty', 'summarybill'],
            'aadhar': ['permanentaccountnumber', 'incometax', 'customeridentitycard', 'total', 'summarybill'],
            'pan': ['aadhar', 'customeridentitycard', 'total', 'summarybill'],
            'panaadhar': ['bill', 'customeridentitycard'],
            'policyidcard': ['bill'],
        }
    elif hosp == 'asian':
        present = {
            'authorizationletter': ['authorizationletter', 'documentstobeprovidedbythehospital', "surgeon'scertificate",
                                    'alrequesteddate', 'alnumber', 'initialapproved', 'isapprovedat',
                                    'finalapproved', 'hospitalagreed'],
            'dischargesummary': ['dischargesummmary', 'uhid', 'diagnosis', 'physicalfindings', 'investigation',
                                 'hospitalcourse', 'conditionatdischarge', 'dischargeadvice', 'preventivestrategies',
                                 'underdoctor', 'doctor.unit', 'nextappointment'],
            'billsummary': ['draftbillsummary', 'grossamt', 'netamount', 'depositamount'],
            'billdetails': ['qty', 'rate', 'slipno', 'gstn', 'servicecode', 'billno', 'provisionalbill'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'authorizationletter': ['qty'],
            'dischargesummary': ['qty', 'counsellingsheet', 'grossamount', 'provisionalbil'],
            'billsummary': ['qty'],
            'billdetails': ['billsummary'],
            "aadhar": ['billsummary', 'incometax', 'qty', 'dischargesummary', 'authorisationletter'],
            "pan": ['billsummary', 'aadhar', 'qty', 'dischargesummary', 'authorisationletter'],
            "panaadhar": ['dischargesummary'],
            "policyidcard": ['billsummary', 'aadhar', 'qty', 'dischargesummary', 'authorisationletter'],
        }

    elif hosp == 'sarvodaya':
        present = {
            'authorizationletter': ['authorizationletter', 'documentstobeprovidedbythehospital', "surgeon'scertificate",
                                    'alrequesteddate', 'alnumber', 'initialapproved',
                                    'finalapproved', 'hospitalagreed'],
            'billdetails': ['rate', 'qty', 'total', 'billamount', 'servicename(notes)', 'subtotal'],
            'billsummary': ['salessummary', 'totalmedicine', 'totalconsumable', 'netpurchased', 'category', 'expiry'],
            'dischargesummary': ['dischargesummary', 'finaldiagnosis', 'presentingcomplaints',
                                 'evaluationandmanagement', 'dischargecondition',
                                 'examinations', 'courseinhospital', 'conditionatdischarge',
                                 'treatmentadviceondischarge', 'conditionatdischarge'
                , 'investigation', 'diet', 'followupafter'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }

        absent = {
            'authorizationletter': ['salessummary', 'qty'],
            'billdetails': ['salessummary'],
            'billsummary': ['rate', 'qty'],
            'dischargesummary': ['salessummary', 'qty'],
            "aadhar": ['income', 'bill', 'amount', 'total', 'qty', 'salessummary'],
            "pan": ['aadhar', 'bill', 'amount', 'total', 'qty', 'salessummary'],
            "panaadhar": ['bill', 'amount', 'total', 'qty', 'salessummary'],
            "policyidcard": ['bill', 'amount', 'total', 'qty', 'salessummary', 'aadhar', 'pan'],
        }
    elif hosp == 'hinduja':
        present = {
            'billsummary': ['bill(summary)', 'billamount', 'billofsupply'],
            'dischargesummary': ['dischargesummary', 'finaldiagnosis', 'chiefcomplaints', 'treatmentondischarge',
                                 'toobtainurgentcare',
                                 'oobtainurgentcare', 'exactdateofonsetofsymptoms',
                                 'clinicalcoursepriortohospitalization',
                                 'treatmentgivenduringstay', 'moderateinfection', 'whentoseekmedicalcare',
                                 'followupadvice',
                                 'additionaladvice', 'departmentofgeneralsurgery',
                                 'admissiondate', 'conditionatdischarge', 'prescriptiondetailondischarge',
                                 'historyofpresentillness'],
            'billdetails': ['detailedstatement', 'cgst', 'sgst', 'syringe', 'disposable', 'billofsupply', 'qty', 'rate',
                            'bonewax',
                            'dissectingtools', 'kitpressuremonitoring', 'surgiwear', 'gownsurgical', 'cottonroll',
                            'bathprotect',
                            'sterilewater', 'syringewithneedle', 'charge',
                            'saccode', 'billamount', 'netamount', 'foodservices', 'fulldaymeal', 'facemask',
                            'disposablebriefs'
                            'plasticapron', 'vesselsealingdevice', 'endotrachealtube', 'ventilatorcircuit',
                            'abdominalbelt', 'paraglass'],
            'authorizationletter': ['authorizationletter', 'documentstobeprovidedbythehospital', "surgeon'scertificate",
                                    'alrequesteddate', 'alnumber', 'initialapproved',
                                    'finalapproved', 'hospitalagreed'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'billsummary': ['rate', 'qty', 'detailedstatement'],
            'dischargesummary': ['bill(summary)', 'qty'],
            'billdetails': ['bill(summary)', 'dischargesummary'],
            'authorizationletter': ['bill(summary)', 'dischargesummary'],
            'aadhar': ['incometax', 'bill', 'discharge', 'rate'],
            'pan': ['aadhar', 'bill', 'discharge', 'authorization', 'rate'],
            'panaadhar': ['bill', 'discharge', 'authorization', 'rate'],
            'policyidcard': ['bill', 'discharge', 'authorization', 'rate'],
        }
    elif hosp == 'sriramachandra':
        present = {
            'billdetails': ['inpatientbilldetail', 'qty', 'amount', 'tax', 'billno'],
            'dischargesummary': ['dischargesummary', 'dischargestatus', 'appointment', 'physicalexaminnation',
                                 'position', 'findings', 'procedure', 'problemencountered', 'conditionatdischarge',
                                 'dischargeadvice'],
            'authorizationletter': ['authorizationletter', 'documentstobeprovidedbythehospital', "surgeon'scertificate",
                                    'alrequesteddate', 'alnumber', 'initialapproved',
                                    'finalapproved', 'hospitalagreed'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "labreport": ["testname", "biologicalreferenceinterval", "biologicalreference", "bloodbank",
                          "cellantibodyscreen",
                          "virology", "testparameters", "realtimepcrtechnology", "testdescription",
                          "microbiologyresult",
                          "histopathology", "finalimpression", "testmethod", "microbiologyresult", "natureofspecimen"]

        }
        absent = {
            'billdetails': ['dischargesummary'],
            'dischargesummary': ['billdetail'],
            'authorizationletter': [],
            "aadhar": ['incometax', 'dischargesummary'],
            "pan": ['aadhar'],
            "panaadhar": ['dischargesummary', 'billdetail', 'result', 'bloodbank', 'finalimpression', 'histopathology'],
            "policyidcard": ['dischargesummary', 'billdetail'],
            "labreport": ["incometax", "dischargesummary", ]
        }
    elif hosp == 'jupiter':
        present = {
            'authorizationletter': ['authorizationletter', 'documentstobeprovidedbythehospital', "surgeon'scertificate",
                                    'alrequesteddate', 'alnumber', 'initialapproved',
                                    'finalapproved', 'hospitalagreed'],
            'billsummary': ['groupwisedetail', 'billinggroupname', 'billamount', 'netamount'],
            'billdetails': ['finalbill-details', 'finalbill-medicinewisedetail', 'rate', 'expiry', 'qty', 'servicedate',
                            'servicecode', 'servicename'],
            'dischargesummary': ['dischargesummary', 'admittingdoctor', 'complaints', 'pasthistory',
                                 'systemicexamination', 'hospitalcourse', 'proceduredetails', 'treatmentadvice'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'authorizationletter': [],
            'billsummary': ['qty', 'expiry'],
            'billdetails': ['billinggroupname'],
            'dischargesummary': ['billinggroupname', 'qty', 'expiry'],
            'aadhar': ['income'],
            'pan': ['aadhar'],
            'panaadhar': [],
            'policyidcard': []

        }
    elif hosp == 'fortisjindal':
        present = {
            'billdetails': ['quantity', 'amount', 'provisionaldetail', 'consumable', 'charges', 'thisisaninterimbill',
                            'timeoffinalbilling', 'totalamount', 'totalpayable', 'netpayable'],
            'authorizationletter': ['authorizationletter', 'documentstobeprovidedbythehospital', "surgeon'scertificate",
                                    'alrequesteddate', 'alnumber', 'initialapproved',
                                    'finalapproved', 'hospitalagreed'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'billdetails': [],
            'authorizationletter': [],
            'aadhar': ['income'],
            'pan': ['aadhar'],
            'panaadhar': [],
            'policyidcard': []

        }
    elif hosp == 'KIMSsecunderabad':
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "attendingpractitioner", "dischargedate", "allergicdrugs",
                               "admissiondate", "followup", "ensuringappointment", "dateofdischarge",
                               "dischargediagnosis", "conditionatdischarge", "consultant", "chiefcomplaints",
                               "presenthistory", "pasthistory",
                               "findings", "adviceondischarge", "pendingresult", "conditionatdischarge",
                               "dischargeadvice", "followup", "emergencyplanofcare"
                                                              "dischargemedication", "dischargerecommendation"],
            "billsummary": ["billsummary", "dischargedate", "mrno", "refno"],
            "billdetails": ["billofsupplyinpatientbill", "cptcode", "netbillamount", "payeramount",
                            "paymentmode", "rate", "amount",
                            "billdate", "signatureofaccountant", "amountinwords",
                            "gstin", "subtotal", "admincharges" "procedurecharge", "nursingcarecharge", "expirydate",
                            "qty",
                            "quantity", "batchno",
                            "signatureofcashier", "billdate", "amounttopay", "amountcollected", "investigationcharge",
                            "consultationcharge", "partytotal", "consumable", "unitprice", "mrp"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],

            "labreport": ["report", "departmentof", "medicationcpoe", "radiology", "treatmentplan",
                          "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
            "policy": ["uhid", "policy"],
        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "gstno", "hospitaldeclaration", "claimform", "declarationbythepatient",
                               "teslamri"],
            "billsummary": ["cptcode"],
            "billdetails": ["dischargesummary", "billsummary", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "laboratory", "radiology", "findings", "clinical", "billsummary",
                    "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", "requestforcashless", "rejectionofcashless"],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],

        }
    elif hosp == 'carenampally':
        present = {
            'billsummary': ['provisionalbillsummary', 'amount', 'regno', 'billno'],
            'billdetails': ['provisionalbilldetails', 'qty', 'servicename', 'servicedate'],
            'dischargesheet': ['dischargesummary', 'diagnosis', 'reasonforadmission', 'keyexamination',
                               'courseinhospital', 'investigationdetails', 'dischargemedication', 'followedby',
                               'followup'],
            'pharmacybill': ['consolidatedpharmacybill', 'itemdescription', 'amount', 'qty'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "policyidcard": ["customeridentitycard", "customeridno"],

        }
        absent = {
            'billsummary': ['consolidatedpharmacybill', 'provisionalbilldetails', 'dischargesummary'],
            'billdetails': ['provisionalbillsummary', 'consolidatedpharmacybill', 'dischargesummary'],
            'dischargesheet': ['consolidatedpharmacybill', 'provisionalbillsummary', 'provisionalbilldetails'],
            'pharmacybill': ['dischargesummary', 'provisionalbilldetails', 'provisionalbillsummary'],
            'aadhar': ['incometax', 'permanentaccountnumber', 'discharge', 'amount'],
            'pan': ['aadhar', 'discharge', 'amount'],
            'panaadhar': ['discharge', 'amount', 'qty'],
            'cashless': [],
            'authorizationletter': [],
            'policyidcard': []
        }
    elif hosp == 'carebanjara':
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "hepaticfunction", "attendingpractitioner", "dischargedate",
                               "allergicdrugs", "incaseof", "patientappointment",
                               "admissiondate", "followup", "ensuringappointment", "dateofdischarge",
                               "hospitaldeclaration",
                               "dischargediagnosis",
                               "findings", "adviceondischarge", "pendingresult", "conditionatdischarge",
                               "dischargemedication", "dischargerecommendation"],
            "billdetails": ["billofsupplyinpatientbill", "netbillamount", "payeramount", "paymentmode" "summary",
                            "billdate", "signatureofaccountant", "amountinwords",
                            "gstin", "subtotal", "admincharges" "procedurecharge", "nursingcarecharge", "expirydate",
                            "qty",
                            "quantity", "batchno",
                            "signatureofcashier", "billdate", "amounttopay", "amountcollected", "investigationcharge",
                            "consultationcharge", "partytotal", "consumable", "unitprice", "mrp"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policy": ["uhid", "policy"],
            "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "claimform", "declarationbythepatient", "teslamri"],
            "billdetails": ["dischargesummary", "relation", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", ],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],

        }
    elif hosp == 'parasgurgaon':
        present = {
            'billdetails': ['patientbill(detail)', 'billno', 'services', 'rate', 'qty', 'amount'],
            'dischargesheet': ['dischargesummary', 'adviceondischarge', 'onexamination', 'investigations',
                               'treatmentreceived', 'conditionatdischarge', 'diagnosis', 'admittingcomplaints',
                               'historyofpresentillness', 'pastmedicalhistory', 'familyhistory', 'drugallergy',
                               'generalexamination(atthetimeofadmission)', 'courseinthehospital', 'findings',
                               'conditionatthetimeofdischarge', 'dischargeadvice', 'followup', 'urgentcare'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'billdetails': ['dischargesummary', 'authorizationletter', 'agreedtariff'],
            'dischargesheet': ['patientbill(detail)'],
            'aadhar': ['incometax', 'permanent', 'discharge', 'rate', 'patientbill'],
            'pan': ['aadhar', 'discharge', 'patientbill'],
            'panaadhar': ['discharge', 'patientbill'],
            'cashless': ['sanctionedamount'],
            'authorizationletter': [],
            'policyidcard': [],
        }
    elif hosp == 'hiranandani':
        present = {
            'billdetails': ['billdetails', 'qty', 'rate', 'billnumber', 'billdate'],
            'dischargesheet': ['dischargesummary', 'diagnosis', 'casehistory', 'examinationfinding', 'allergies',
                               'investigations',
                               'treatmentgiven', 'courseinward', 'treatmentadvised', 'adviceondischarge',
                               'preventiveaspects', 'followupadvice', 'toobtainurgent'],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'billdetails': ['dischargesummary'],
            'dischargesheet': ['billdetails'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'relaince':
        present = {
            "billdetails": ['subtotal', 'amount', 'qty', 'rate'],
            "dischargesheet": ['dischargesummary', 'diagnosisdescription', 'presentingcomplaints',
                               'courseinthehospital', 'significantevents', 'conditionatthetimeofdischarge',
                               'urgentcareinstruction', 'incaseofobservation', 'dischargeadvice', 'followup',
                               'homemedication', 'allergies', 'history', 'examination', 'proceduresummary',
                               'labfinding', 'urgentcareinstruction', 'physicalactivity'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            "billdetails": [],
            "dischargesheet": ['authorizationletter', 'sanctionedamount'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'christianmedicalcollege':
        present = {
            'billdetails': ['in-patient', 'particulars', 'code', 'billnumber', 'total', 'qty'],
            'dischargesheet': ['dischargesummary', 'diagnosis', 'history', 'onexamination', 'investigation',
                               'operationdone', 'operativefindings', 'discussion', 'recommendation',
                               'thissummaryhasnotbeen', 'collectyourfinalreport'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'billdetails': ['dischargesummary'],
            'dischargesheet': ['in-patient'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'continentalhospital':
        present = {
            'billdetails': ['inpatientfinalbill', 'qty', 'code', 'subtotal', 'total'],
            'dischargesheet': ['dischargesummary', 'reasonforadmission', 'admissiondate', 'dischargedate',
                               'diagnosisatdischarge', 'hospitalcourse', 'keytestresult', 'labresults',
                               'medicationatdischarge'
                , 'patientinstructions', 'followupappointment'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'billdetails': ['dischargesummary'],
            'dischargesheet': ['inpatientfinalbill', 'qty'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'SIMS':
        present = {
            'dischargesheet': ['dischargesummary', 'historyofpresentillness', 'pastmedicalhistory'
                , 'onexamination', 'localexamination', 'courseinhospital', 'procedurenote',
                               'medication', 'review'],
            'billsummary': ['finalbill', 'netamount', 'totalbill', 'address'],
            'billdetails': ['breakupbill-final', 'orderdetails', 'qty', 'servicetotal'
                            ],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'dischargesheet': ['bill-final', 'qty', ],
            'billsummary': ['dischargesummary', 'breakupbill'],
            'billdetails': ['finalbill', 'dischargesummary'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'aakash':
        present = {
            'dischargesheet': ['dischargesummary', 'admissiondate', 'dischargesate', 'diagnosis', 'complains',
                               'reasonsforadmission'
                , 'pastmedicalhistory', 'courseofstay', 'dischargeadvice', 'conditionondischarge', ],
            'billsummary': ['interiminpatientbill(summary)', 'ipno', 'servicename', 'patientamt'
                , 'companyamt', 'billamount'],
            'billdetails': ['interiminpatientbill(detailed)', 'qty', 'itemname', 'itemcode'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'dischargesheet': ['interiminpatientbill', 'qty', 'authorization', 'initialapproved'],
            'billsummary': ['interiminpatientbill(detailed)', 'itemname', 'itemcode', 'dischargesummary'],
            'billdetails': ['dischargesummary', 'interiminpatientbill(summary)'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'bhailalamin':
        present = {
            'dischargesheet': ['dischargesummary', 'treatmentgiven', 'patientconditionondischarge', 'adviseondischarge',
                               'followupadvice'
                , 'treatingconsultant', 'admittingdoctor', 'medicalofficer', 'urgentcare', 'mrno'],
            'billsummary': [],
            'billdetails': ['charge', 'qty', 'rate', 'billno', 'total', 'amount'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'dischargesheet': ['interiminpatientbill', 'qty', 'authorization', 'initialapproved'],
            'billsummary': ['interiminpatientbill(detailed)', 'itemname', 'itemcode', 'dischargesummary'],
            'billdetails': ['dischargesummary', 'interiminpatientbill(summary)'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'kailashhospital':
        present = {
            'billsummary': ['billforapproval', 'amount', 'charges', 'billno'
                                                                    'providername', 'panno'
                , 'total'],
            'billdetails': ['billforapproval', 'amount', 'charges', 'billno'
                , 'rate', 'qty', 'unit', 'mrp', 'packing', 'batchno'
                , 'total', 'detailedbreakup'],
            'dischargesheet': ['dischargesummary', 'dateofdischarge', 'doctorincharge'
                , 'casesummary', 'operationdone', 'finaldiagnosis', 'treatmentgiven'
                , 'investigation', 'adviceatdischarge', 'nextfollowup'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            'billsummary': ['detailedbreakup', 'dischargesummary', 'mrp', 'particular'],
            'billdetails': ['dischargesummary', 'adviceatdischarge'],
            'dischargesheet': ['billforapproval'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'narayanahrudayalaya':
        present = {
            'billdetails': ['billno', 'qty', 'mrp', 'amount', 'package', 'particulars', 'total', 'charges'],
            'dischargesheet': ['dischargesummary', 'finaldiagnosis', 'pastmedicalhistory', 'admissionreason'
                , 'systemicexamination', 'gastrointestinalsystem', 'operationandprocedure',
                               'findings', 'surgeons', 'courseinhospital', 'medicationatdischarge', 'followupdetail',
                               'emergencymanagement', 'careteamdetail'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno"],

        }
        absent = {
            'billdetails': [],
            'dischargesheet': [],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'rajivgandhicancerinstitute':
        present = {
            'dischargesheet': ['diagnosis', 'presentadmission', 'comorbidities',
                               'presentcomplaint', 'history', 'rgciinvestigation',
                               'treatmentatrgci', 'briefsummaryofthecase', 'labservicesinvestigation',
                               'proposedtreatmentplan'
                , 'treatmentgivenduringhospitalization', 'adviceondischarge', 'attentionfortreatment', 'painmedication'
                , 'morbiditymedication', 'revisitschedule', 'discharge', 'summary'],
            'billsummary': ['summarybill', 'amount', 'description', 'rent', 'charge', 'total', 'receipt'],
            'billdetails': ['detailedbill', 'amount', 'charge', 'rent', 'unit', 'particulars',
                            'date', 'qty', 'expirydate', 'discount'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],

        }
        absent = {
            'dischargesheet': ['qty', 'amount', "cashlessauthorization"],
            'billsummary': ['detailedbill', 'authorizationletter', 'discharge',
                            'initialapproved', 'cashlessauthorization', 'qty', 'particulars', 'refunddetail'],
            'billdetails': ['summarybill', 'cashlessauthorization', 'authorizationletter'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == "rainbowchildren'smedicare":
        present = {
            'billsummary': ['provisionalbill(summary)', 'amount', 'billno', 'patientname'],
            'billdetails': ['provisionalbill(detail)', 'amount', 'qty', 'charges', 'total', 'billno'],
            'dischargesheet': ['dischargesummary', 'diagnosis', 'history', 'investigation', 'indication',
                               'operativefindings', 'advice'
                , 'operativenotes', 'incaseofemergency', 'maternalhistory', 'examination'
                , 'procedurenotes', 'postoperativemanagement'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],
        }
        absent = {
            'dischargesheet': ['provisionalbill', 'qty'],
            'billdetails': ['provisionalbill(summary)'],
            'billsummary': ['provisionalbill(detail)', 'operationtheatreconsumables'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'sribalaji':
        present = {
            'billsummary': ['particulars', 'charges', 'economy', 'billofsupply', 'grossamount'],
            'billdetails': ['patientbill(details)', 'rate', 'qty', 'totalfor', 'billno',
                            'amount', 'uhid'],
            'dischargesheet': ['dischargesummary', 'medicalhistory', 'diagnosis'
                , 'presentingcomplaints', 'previousinvestigation', 'pasthistory'
                , 'timeofadmission', 'courseduringhospital', 'treatmentgiven', 'investigation'
                , 'incaseofemergency', 'admissiondate', 'dateofdischarge'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],
        }
        absent = {
            'billsummary': ['rate', 'qty', 'patientbill(detail', 'dischargesummary'],
            'billdetails': ['billofsupply', 'dischargesummary'],
            'dischargesheet': ['rate', 'grossamt'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'yashodaghaziabad':
        present = {
            'billsummary': ['creditprovisionalbill', 'particulars', 'amount'],
            'billdetails': ['creditprovisionalbill(detail', 'billno', 'particulars', 'rate'],
            'dischargesheet': ['dischargesummary', 'diagnosis', 'operativeprocedure'
                , 'chiefcomplaint', 'pastmedical', 'familyhistory',
                               'systemicexamination', 'localexamination', 'treatmentgivenduringhospitalization'
                , 'operation', 'adviceondischarge', 'nutritionaladvice', 'followupplan', 'incase'],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],
        }
        absent = {
            'billsummary': ['provisionalbill(detail', 'dischargesummary', 'rate'],
            'billdetails': ['servicetax', 'dischargesummary'],
            'dischargesheet': ['provisionalbill', 'billamount'],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'caritashospital':
        present = {
            "billsummary": ['billnumber', 'dischargebill', 'charges', 'billamount'],
            "dischargesheet": ["dischargesummary", 'diagnosis', 'dischargemedication',
                               'investigationdone', 'courseandmanagement', "investigations",
                               "presentinghistory", "onexamination", "treatmentsummary"
                , "whentoseekurgentcare"],
            "billdetails": ["splitup", "rate", "qty", "amount", "exp.date"],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],
        }
        absent = {
            "billsummary": ['qty', "dischargesummary"],
            "dischargesheet": ["dischargebill", "qty"],
            "billdetails": ["dischargebill"],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],

        }
    elif hosp == 'nsmemorialinstituteofmedicalscience':
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "billsummary": ["billsummary", "qty", "amount", "netamount", "admission"],
            "billdetails": ["rate", "qty", "price", "medicinename", "billdetails", "itemname", "billno"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "dischargesheet": ["dischargesummary", "physicalexamination", "courseinthehospital", "diagnosis",
                               "adviceondischarge", "followup",
                               "instructions"],
            "clinicalnotes": ["clinicalnotes", "procedure", "prescribesmedicine"],
            "cashless": ["policypart", "cashless", "authorization", "tobefilled", "nameofthetreatingdoctor",
                         "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],
            "labreport": ["testdate", "reportdate/time", "mrno", "patientname", "age", "gender", "referredby", "ipward",
                          "testdesciption", "observedvalue", "biologicalreferenceintervalandunits",
                          "pathology", "biochemistry"],
        }
        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "billsummary": ["billdetails", "clinicalnotes"],
            "billdetails": ["dischargebill", "dischargesummary", "icici", "relation", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["hospitalagreedtariff", "clinicalnotes", "claimform", "declarationbythepatient",
                               "teslamri"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "policyidcard": ["laboratory", "transport", "licence", "drive", "manager",
                             "bill", "medicine", "method"],
            "clinicalnotes": ["billdetails", "dischargebill"],
            "labreport": ["checklistfortpadispatch", "dischargesummary", "identitycard", "conditionatdischarge",
                          "clinicalnotes",
                          "detailsofpatientadmitted", "billsummary", "cashless"],
        }
    elif hosp == 'kovaimedicalcenter':
        present = {
            "billsummary": ['billnumber', 'dischargebill', 'charges', 'billamount'],
            "dischargesheet": ["dischargesummary", 'diagnosis', 'dischargemedication',
                               'investigationdone', 'courseandmanagement', "investigations", "management", "advice",
                               "medication", "followup"
                                             "presentinghistory", "onexamination", "treatmentsummary"
                , "whentoseekurgentcare"],
            "billdetails": ["splitup", "rate", "qty", "amount", "exp.date"],
            "aadhar": ["youraadhaarno.", "proofofidentity", 'incaseofobservation', "enrolmentno", "governmentofindia",
                       "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],
            "labreports": ["radiology", "impression", "scanreport", "liver", "kidney"],
        }
        absent = {
            "billsummary": ['qty', "detailbill", "cashlessauthorization"],
            "dischargesheet": ["dischargebill", "qty", "cashlessauthorization"],
            "billdetails": ["dischargebill", "cashlessauthorization"],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
            "labreports": ["servicedetailbill", "dischargesummary"]
        }
    elif hosp == 'amalahospital':
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "billsummary": ["paymentrequestforfinalbil", "remarks"],
            "billdetails": ["charges", "paymentdetails", "credit"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "dischargesheet": ["dischargesummary", "medicationsadministered", "conditionatthetimeofdischarge",
                               "follow-up",
                               "procedureperformed", "investigation", "review", "preparedby"],
            "authorizationletter": ["queryletterforcashlessauthorization", "claimintimationno", "hospitalname",
                                    "address"],
            "labreport": ["mriscanreport", "name", "referredby", "age", "sex", "date", "scanno"],
            "cashless": ["policypart", "cashless", "tobefilled", "nameofthetreatingdoctor", "declaration",
                         "qualification",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "policycard": ["customeridno", "policyno", "corporatename",
                           "relationship", "validfrom", "officecode",
                           "emergencyhelplineno"],
        }
        absent = {"aadhar": ["incometax", "depart", "permanentaccountnumber", ],
                  "billsummary": ["inpatientpaymentdetails"],
                  "billdetails": ["paymentrequestforfinalbill", "dischargesummary", "impression", "provideddate",
                                  "signature"],
                  "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary",
                          "youraadhaarno.",
                          "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
                  "dischargesheet": ["house", "dist", "requestforfinal", "actualamount", "creditamount",
                                     "creditdetails",
                                     "signature", "inpatientpaymentdetails", "customeridno", "policyno",
                                     "corporatename"],
                  "authorizationletter": ["requestforcashless"],
                  "labreport": ["patientdetails", "finalbill", "inpatientpaymentdetails", "actualamount",
                                "dischargesummary"],
                  "cashless": ["claimnumber", "relation", "admissionofliability"],
                  "policycard": ["laboratory", "transport", "licence", "drive", "hospitalisation", "manager",
                                 "bill", "medicine", "method", "dischargesummary",
                                 "conditionatthetimeofdischarge"],
                  }
    elif hosp == "kongunadhospitals":
        present = {
            "billsummary": ["hospiatalservicesestimate", "summary", "ipdno", "patientname", "contactno", "address",
                            "mrno",
                            "doctor", "hospitalservicesdetails", "medicines",
                            "netamountrecievable"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber",
                                    "authorizationisvalidforadmissionupto",
                                    "nameofinsurancecompany", "nameoftpa", "proposername",
                                    "relationwithproposer"],
            "dischargesheet": ["dischargesummary", "mrno", "patientname", "department", "address", "dateofadmission",
                               "dateofdischarge", "dischargetype", "admissionunit", "diagnosis",
                               "management", "reasonforadmission", "investigationreports", "treatmentgiven",
                               "courseduringstay", "vitalsondischarge", "dischargeadvise",
                               "whenandhowtobtainurgentmedicalcare"],
            "labreport": [
                "patientname", "doctor", "labno", "ipdno", "department"
                , "randombloodsugar",
                "samplecollection", "reporttype", "departmentofct", "hrct", "technique",
                "departmentofhaematology", "departmentofbiochemistry", "departmentofmicrobiology"],
            "billdetail": ["provisionalbill", "ipdno", "patientname", "contactno", "address", "panelname", "billno",
                           "billdate", "mrno", "doctor", "admissiondate", "date",
                           "particulars", "rate", "qty", "disc.", "taxableamt", "netamount", "admissioncharges",
                           "laboratory", "radiology", "medicines&consumables", "covidtreatment",
                           "othercharges", "qty", "rate", "gst"],

            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetreatingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "policycard": ["customeridno", "policyno", "corporatename", "name", "dateofbirth", "empid", "age", "gender",
                           "relationship", "validfrom", "officecode",
                           "emergencyhelplineno"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"]
        }
        absent = {
            "billsummary": ["provisionalbill", "dischargesummary", "management",
                            "frequency", "treatmentchart", "tablet", "qty"],
            "authorizationletter": ["requestforcashless"],
            "dischargesheet": ["provisionalbill", "laboratory", "radiology", "medicines&consumables", "covidtreatment",
                               "othercharges", "hospiatalservicesestimate", "netamountrecievable",
                               ],
            "labreport": ["provisionalbill", "checklistfortpadispatch", "dischargesummary", "conditionatdischarge",
                          "detailsofpatientadmitted", "treatmentchart", "frequency",
                          "billsummary", "cashless", "gst"],
            "billdetail": ["hospiatalservicesestimate", "treatmentchart", "frequency",
                           "hospitalservicesdetails", "investigationreport"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "policycard": ["laboratory", "transport", "licence", "treatmentchart", "frequency", "drive",
                           "hospitalisation", "manager",
                           "bill", "medicine", "method", "investigationreport"],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"]
        }
    elif hosp == "satgurupratapsinghhospitals":
        present = {
            "authorizationletter": ["claimnumber", "cashlessauthorizationletter", "authorizationdetails"
                                                                                  "initialapprovalamount"],
            "dischargesheet": ["dischargesummary", "admissiondatetime"],
            "billsummary": ["interimpatientbill", "servicename", "patientamt", "companyamt"],
            "billdetail": ["interimpatientbill", "detailed", "itemname", "itemcode", "datetime", "qty", "price",
                           "patientamt", "companyamt", "(detailed)"],
            "cashless": ["requestforcashlesshospitalisationforhealthinsurance", "policypart",
                         "tobefilled", "nameofthetreatingdoctor", "declaration", "wehavenoobjection"
                                                                                 "qualification",
                         "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration", "declarationbythepatient"
                                                                                 "iagreetoallow", "natureofillness",
                         "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory", "hospitalseal"
                                                                             "roomtype"],
            "policycard": ["customeridno", "policyno", "corporatename", "dateofbirth", "empid",
                           "relationship", "validfrom", "officecode",
                           "emergencyhelplineno"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal",
                       "dob", "yearofbirth", "uniqueidentificationauthorityofindia", "aadhaar", "india"],
            "labreport": ["diagnosticsreport", "orderdate", "reportdate", "ultrasound",
                          "facility", "hrctchestscan", "impression"],
            "prescription": ["prescription", "medication", "prescriptionno"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
        }
        absent = {
            "authorizationletter": ["requestforcashlesshospitalisationforhealthinsurance", "policypart"],
            "dischargesheet": ["interimpatientbill", "detailed", "servicename", "patientamt", "companyamt", "itemcode"],
            "billsummary": ["detailed", "itemname', 'itemcode", "price", "dischargesummary", "dischargedatetime"],
            "billdetail": ["summary", "servicename", "dischargedatetime"],
            "cashless": ["claimnumber", "relation", "admissionofliability", "admissiondatetime"],
            "policycard": ["laboratory", "transport", "licence", "drive", "manager",
                           "bill", "medicine", "method", "dischargesummary"],
            "aadhar": ["incometax", "depart", "permanentaccountnumber", "dischargesummary"],
            "labreport": ["interimpatientbill", "dischargesummary", "prescription", "queryonpreauthorization",
                          "starhealthandalliedinsurancecoltd.", "nameoftheinsured", "nameoftheemployee",
                          "relationshipwithemployee", "dateofadmission", "nameofpolicy", "dateofdischarge",
                          "medication",
                          "observation", "modifiedby"],
            "prescription": ["interimpatientbill", "discharge summary"],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
        }
    elif hosp == "ananthapurihospitals":
        present = {
            "billsummary": ["inpatientinvoicesummary", "customer", "patientnumber", "billtype", "billdate",
                            "description", "billtotal", "patientpayable",
                            "preparedby", "checkedby"],
            "billdetail": ["ipbillbreakupdetails", "billtype", "billdetail",
                           "description", "grossamt",
                           "billtotal", "patientpayable",
                           "preparedby", "checkedby"],
            "dischargesheet": ["dischargesummary", "mobileno", "phoneno", "bloodbank", "microbiology"
                                                                                       "testname"
                , "dateofdischarge", "admittingdoctor", "advice",
                               "foremergency", "clinicalpathology", "bio-chemistry",
                               "qualification", "physicalexamination", "courseinthehospital",
                               "adviseondischargetime", "otherinvestigationresults",
                               "biochemistry", "heamatology", "approvedby"],
            "cashless": ["policypart", "cashless", "tobefilled", "nameofthetreatingdoctor",
                         "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "policycard": ["customeridno", "corporatename"
                , "validfrom", "officecode",
                           "emergencyhelplineno"],
            "prescription": ["doctorsmedicationorder", "prescription", "drug", "startdate", "dose", "frequency",
                             "route", "nursingmedicationadministration", ],
            "labreport": ["investigationreport", "investigation"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
        }
        absent = {
            "billsummary": ["ipbillbreakupdetails", "rate", "grossamt"],
            "billdetail": ["inpatientinvoicesummary", "dischargesummary"],
            "dischargesheet": ["inpatientinvoicesummary", "ipbillbreakupdetails", "billtype", "billdetail", "billtotal",
                               "doctorsmedicationorder", "prescription", ],
            "cashless": ["claimnumber", "relation", "admissionofliability", "queryonpreauthorization"],
            "policycard": ["laboratory", "transport", "licence", "drive", "hospitalisation", "manager",
                           "bill", "medicine", "method"],
            "prescription": ["inpatientinvoicesummary", "ipbillbreakupdetails", "billtotal", "patientpayable",
                             "dischargesummary", "testname", "roomcategory"],
            "labreport": ["inpatientinvoicesummary", "ipbillbreakupdetails", "billtotal", "dischargesummary",
                          "policypart",
                          "queryonpreauthorization"],
            "aadhar": [],
            "pan": [],
        }
    elif hosp == "omegahospitals":
        present = {
            "billdetails": ["ipdetailedbill", "billno", "admissionno", "billdate", "admitteddt", "umrno",
                            "dischargedate", "employeeno", "services", "investigation",
                            "hospitalservices", "qty", "rate", "servicecd"],
            "dischargesheet": ["dischargesummary", "consultant", "presenthistory", "pasthistory", "onexamination",
                               "courseinthehospital", "patientrecieved",
                               "conditionondischarged", "dischargeadvice", "preventiveplanofcare", "followup",
                               "transcribedby", "residentdoctor"],
            "cashless": ["cashless",
                         "requestforcashlesshospitalisationforhealthinsurance", "nameofthetreatingdoctor",
                         "declaration",
                         " doyouhaveafamilyphysician", "thepatientsdeclaration", "intheeventofunauthorizedrecovery",
                         "tobefilledbytreating", "costofimplants", "expectedcostofhospitalization",
                         "hospitaldeclaration",
                         "relevantcriticalfindings", "durationofpresentillness", "natureofillness",
                         "noobjectiontoanyauthorizedtpa", "detailsofpatientadmitted", "mandatorypasthistory",
                         "authorizationtostarhealth", "roomtype", "declarationbythepatient", "hospitaldeclaration"],
            "policycard": ["customeridno", "corporatename", "relationship", "validfrom", "officecode", "p.no",
                           "personalandcaring", "emergencyhelplineno"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal",
                       "yearofbirth", "uniqueidentificationauthorityofindia", "unique", "identity", "authority"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber",
                                    "authorizationisvalidforadmissionupto",
                                    "nameofinsurancecompany", "nameoftpa", "proposername",
                                    "relationwithproposer"],

        }
        absent = {
            "billdetails": ["dischargesummary", "presenthistory", "pasthistory", "onexamination", "courseinthehospital",
                            "patientrecieved", "conditionondischarged", "dischargeadvice", "preventiveplanofcare"],
            "dischargesheet": ["ipdetailedbill", "billno", "billdate", "servicecd"],
            "authorizationletter": ["requestforcashless"],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "cashless": ["claimnumber", "relation", "admissionofliability", "interimsummary",
                         "provisionalbill"],
            "policycard": ["laboratory", "transport", "licence", "drive", "manager",
                           "bill", "medicine", "method", "investigationreport"],
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ]
        }
    elif hosp == "jehangirhospital":
        present = {
            "billsummary": ["billofsupplyprovisional", "gross", "netamt", "bilamount", "billto",
                            "patientregn.no", "visit", "services", "billestimate"
                                                                   "servicestotal", "counselingpersonname"],
            "billdetail": ["billdetail", "qty", "gross", "moudiscount", "conc", "net"],
            "dischargesheet": ["dischargesummary", "chiefcompliants", "admissiondt", "dischargedt", "operationnotes",
                               "surgeon", "followup", "specialinstructions",
                               "medicationduringhospitalization", "courseinhospital", "historyofpresentillness"
                                                                                      "generalexamination",
                               "systemicexamination", "medicationsduringhospitalization"
                                                      "clinicalbiochemistry", "haematology", "treatmentondischarge",
                               "contactnumberincaseofemergency", "followupinstructions"],
            "cashless": ["requestforcashlesshospitalisationformedicalinsuracepolicy", "detailsofthirdpartadministrator",
                         "policypart", "cashless", "authorization", "tobefilled", "nameofthetreatingdoctor",
                         "declaration", "hospitaldeclaration", "iagreetoallow", "ihearebywarrant",
                         "documentstobeprovided"
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype", "incaseofaccident", "deatilsofpatientadmitted"],
            "policycard": ["customeridno", "policyno", "corporatename",
                           "validfrom", "officecode", "emergencyhelplineno", "personalandcaring"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal", "dob"
                                                                                                                  "goverment"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "labreport": ["obstgrowthscan", "growthparameters", "impression", "testname", "labcustomerno",
                          "labcustomerno.", "samplecollected", "samplerevd", "reportedon", "processedat",
                          "rdrpgene"
                , "emergencyassessmentrecord", "functionalassessment", "provisionaldiagnosis",
                          "obstgrowthscan", "allergicto", "labno.", "labno",
                          "initialassessmentcovid", "temp", "resprate", "bp", "growthparameters"
                                                                              "anomalies", "heartsounds",
                          "intravenousinfusiontherapy"
                          "perabdomen", "bowelsounds", "kidney",
                          "cns", "cgs", "fuctionalassessment",
                          "capabilitytoperformroutineactivity"],
            "prescription": ["prescription", "administrationrecord", "allergicto", "dose", "drugname", "frequency",
                             "indicationofsosdrugs", "drname", "startdate",
                             ],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia", "dob", "goverment", "year"
                                                                   "uidai", "uldal"],
        }
        absent = {
            "billsummary": ["billdetail", "rate", "dischargesummary", "testname", "gipsa", "obstgrowthscan"],
            "billdetail": ["billofsupplyprovisional", "dischargesummary", "testname", "queryonauthorizationletter"
                                                                                      "nameoftheinsured", "cashless",
                           "customeridno", "nameoftheinsured-patient"],
            "dischargesheet": ["billofsupplyprovisional", "billdetail", "bilamount", "billto", "servicestotal",
                               "qty", "billestimate", "hospitaldeclaration", "iagreetoallow", "ihearebywarrant",
                               "documentstobeprovided",
                               "gross", "moudiscount", "net", 'testname'],
            "cashless": ["claimnumber", "relation", "admissionofliability", "queryonauthorizationletter"
                                                                            "nameoftheinsured", "weaddcare"],
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "labreport": ["billofsupplyprovisional", "dailyassessmentcovid", "gross", "netamt", "servicestotal",
                          "billdetail", "qty", "billestimate", "morning", "evening", "afternoon"
                                                                                     "services", "prescription",
                          "administrationrecord", "dischargesummary"
                                                  "indicationofsosdrugs""sign", "queryonauthorizationletter"
                                                                                "nameoftheinsured", "authorization",
                          "policynumber"],
            "prescription": ["billdetail", "billofsupplyprovisional", "billdetail", "bilamount", "billto",
                             "obstgrowthscan", "findings", "growthparameters", "impression", "testname", "onmyown"
                                                                                                         "dateofdischarge",
                             "clarification", "rejection"],
            "policycard": ["laboratory", "transport", "licence", "drive", "manager",
                           "bill", "medicine", "method", "emergencyassessmentrecord", "medicationchartingsheet",
                           "dailyassessmentcovid", "treatmentadvised", "dischargesummary"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
        }
    elif hosp == "kasturbahospitalmanipal":
        present = {
            "billsummary": ["inpatientcreditbill", "admission", "no.ofdayscategory", "grossamt", "no.ofdays", "days"
                                                                                                              "hospitalno"],
            "dischargesheet": ["dischargesummary", "dateadmitted", "datedischarged", "finaldiagnosis",
                               "compliantsonreporting", "physicalfindingsofexamination", "therapeutic Procedure",
                               "coursesoftreatmentinthehospital", "conditionondischarge", "furtheradviceondischarge"],
            "prescription": ["provisionaldiagnosis", "desiredresults", "medications", "rehabilitativeadvice",
                             "medicationsandtreatmentchart", "medications",
                             "fluids", "ecno", "medicationorder", ],
            "billdetails": ["ipchargesdetails", "ipbillno", "depositdetails", "admittingdocumentationcharges",
                            "centralsterilesupplydepart", "consultationcharges", "generalstoreissues"
                                                                                 "netgeneralstoreissues",
                            "investigationbiochemistry", "investigationbloodbank", "subtotal",
                            "investigationclinicallab", "investigationecg",
                            "investigationmicrobiology", "investigationradiology", "materialsbloodbank",
                            "medicinecharges", "oncopharmacy", "issuetotal", "satpharmacy",
                            "netmedicinecharges", "procedurecardiac", "procedurecharges", "sub-consultationcharges",
                            "otmaterials&drugs", "netotmaterials&drugs"],
            "cashless": ["cashless", "requestforcashlesshospitalisationforhealthinsurance",
                         "nameofthetreatingdoctor", "declaration", " doyouhaveafamilyphysician",
                         "thepatientsdeclaration", "intheeventofunauthorizedrecovery",
                         "tobefilledbytreating", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration", "relevantcriticalfindings",
                         "durationofpresentillness", "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory", "authorizationtostarhealth"
                                                                             "roomtype", "declarationbythepatient",
                         "hospitaldeclaration"],
            "policycard": ["customeridno", "corporatename",
                           "relationship", "validfrom", "officecode",
                           "emergencyhelplineno"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
        }
        absent = {
            "billsummary": ["dischargesummary", "physicalfindingsofexamination", "conditionondischarge",
                            "furtheradviceondischarge", "rehabilitativeadvice", "generalstoreissues",
                            "netgeneralstoreissues", "ipchargesdetails", "ipbillno", "subtotal", "netmedicinecharges",
                            "netotmaterials&drugs"],
            "dischargesheet": ["inpatientcreditbill", "no.ofdayscategory", "grossamt", "rehabilitativeadvice",
                               "medicationsandtreatmentchart", "ipchargesdetails"],
            "billdetails": ["inpatientcreditbill", "admissiondischarge", "no.ofdayscategory", "grossamt",
                            "dischargesummary", "datedischarged", "finaldiagnosis", "remarks", "particulars",
                            "coursesoftreatmentinthehospital",
                            "conditionondischarge", "furtheradviceondischarge", "rehabilitativeadvice"],
            "prescription": ["billdetail", "billofsupplyprovisional", "billdetail", "bilamount", "billto",
                             "obstgrowthscan", "findings", "growthparameters", "impression", "testname", "onmyown",
                             "dateofdischarge", "clarification", "rejection"],

            "cashless": ["claimnumber", "relation", "admissionofliability", "interimsummary",
                         "provisionalbill"],
            "policycard": ["laboratory", "transport", "licence", "drive", "manager",
                           "bill", "medicine", "method", "investigationreport"],
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
        }
    elif hosp == "sreegokulammedicalcentre":
        present = {
            "dischargesheet": ["dischargesummary", "category", "adm.date", "disch.date",
                               "presentillness", "adviceondischarge", "dischargemedications"
                                                                      "chiefcomplaints", "pastmedicalhistory",
                               "personalhistory", "labreport",
                               "Haematology", "rftpanel", "lftpanel", "urinerepanel", "miscellaneous",
                               "familyhistory", "investigations", "courseinthehospital"],
            "billsummary": ["consolidatedfinalbill", "billnumber", "summaryoffinalbill", "annexure", ],
            "billdetails": ["services", "description", "qty", "price", "lab",
                            "pharmacy&material", "billdate", "billid", "drugname", "batch"
                                                                                   "exp", "rate", "gst"],
            "cashless": ["requestforcashlesshospitalisationformedicalinsuracepolicy", "claimintimationnumber",
                         "tobefilledbytheinsured", "policynumber",
                         "dateofbirth", "contactnumber", "policyno",
                         "tobefilledbythetreatingdoctor", "nameofthetreatingdoctor", "natureofillness",
                         "relevantclinicalfindings", "durationofpresentailment", "dateoffirstconsultation",
                         "pasthistoryofpresentailment", "proposeddiagnosis",
                         "proposedlineoftrreatment", "surgical", "intensivecare", "nonallopathic",
                         "detailsofpatientadmitted", "duration",
                         "expectedcostforinvestigations", "allinclusivepackagecharges", "professionalfees", "otcharge",
                         "icucharges", "othersifany", "sumtotal",
                         "declaration", "signatureoftreatingdoctorwithhospitalseal"],
            "labreport": ["departmentofradiodiagnosis", "refby", "sex", "obstetricreport",
                          "no of fetuses", "foetalpresentation", "foetalposition", "foetalcardiacactivity",
                          "foetalmovements", "dateandtimeofreporting", "dateandtimeofsamplecollection",
                          "receiptofspecimenatthelab", "sampletestdate", "resultapprovedon", "conditionofthespecimen",
                          "breathingmovements", "placentalsite", "amnioticfluidvolume", "remarks",
                          "covid-19testreport", "typeoftest", "covid-19result"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
        }
        absent = {
            "dischargesheet": ["consolidatedfinalbill", "billnumber", "summaryoffinalbill", "annexure",
                               "pharmacy&material", "billdate", "billid", "drugname", "batch", "outpatientrecord",
                               "price", "amount", "covid-19testreport"],
            "billsummary": ["dischargesummary", "chiefcomplaints", "pastmedicalhistory", "personalhistory", "billid",
                            "drugname",
                            "labreport", "Haematology", "rftpanel", "lftpanel", "urinerepanel", "miscellaneous"],
            "billdetails": ["dischargesummary", "diagnosis", "chiefcompliants", "pastmedicalhistory", "personalhistory",
                            "familyhistory", "billnumber", "consolidatedfinalbill", "reportingdetails",
                            "summaryoffinalbill", "labreport", "Haematology", "rftpanel", "lftpanel", "urinerepanel",
                            "miscellaneous"],
            "cashless": ["consolidatedfinalbill", "billnumber", "summaryoffinalbill", "annexure", "pharmacy&material",
                         "billdate", "billid", "drugname", "batch",
                         "rftpanel", "lftpanel", "urinerepanel", "dischargesummary"],
            "labreport": ["dischargesummary", "consolidatedfinalbill", "billnumber", "summaryoffinalbill",
                          "claimintimationnumber",
                          "tobefilledbytheinsured", "policynumber", "nameofthepatient", "billdate", "billid"],
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno."],
        }
    elif hosp == 'breachcandyhospital':
        present = {
            'billsummary': ["interimbill", "servicetaxcode", "cgst", 'sgst'],
            'billdetails': ["date", "qty", "description", "doctor"],
            "dischargesheet": ["dischargesummary", "admissiondate", "finaldiagnosis",
                               "surgeryperformed", "presentingcomplaints", "pasthistory",
                               "allergies", "currentmedication", "examinationatthetime", "systemicexamination",
                               "localexamination", "surgerydetails", "procedure", "investigation",
                               "courseduringhospitalstay",
                               "treatmentgiven", "advisedondischarge", "followup", "nameoftheconsultant"],
            "authorizationletter": ["queryletterforcashlessauthorization", "claimintimationno", "hospitalname",
                                    "address"],
            # "labreport": ["mriscanreport", "name", "referredby", "age", "sex", "date", "scanno"],
            "cashless": ["policypart", "cashless", "tobefilled", "nameofthetreatingdoctor", "declaration",
                         "qualification",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "policycard": ["customeridno", "policyno", "corporatename",
                           "relationship", "validfrom", "officecode",
                           "emergencyhelplineno"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
        }
        absent = {
            "billsummary": ["qty", "dischargesummary", "admissiondate"],
            "billdetails": ["admissiondate", "dischargesummary"],
            "dischargesheet": [],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'dr.kamakshimemorialhospital':
        present = {
            'billsummary': ["interimbill", "servicetaxcode", "cgst", 'sgst'],
            'billdetails': ["date", "qty", "description", "doctor", "billamount", "claimamount"],
            "dischargesheet": ["dischargesummary", "admissiondate", "finaldiagnosis",
                               "surgeryperformed", "presentingcomplaints", "pasthistory", "treatmentgiven",
                               "conditionatdischarge"
                               "allergies", "currentmedication", "examinationatthetime", "systemicexamination", "tab",
                               "followup", "pleasecallemergency"
                                           "localexamination", "surgerydetails", "procedure", "investigation",
                               "courseduringhospitalstay",
                               "treatmentgiven", "advisedondischarge", "followup", "nameoftheconsultant"],
            "authorizationletter": ["queryletterforcashlessauthorization", "claimintimationno", "hospitalname",
                                    "address"],
            # "labreport": ["mriscanreport", "name", "referredby", "age", "sex", "date", "scanno"],
            "cashless": ["policypart", "cashless", "tobefilled", "nameofthetreatingdoctor", "declaration",
                         "qualification",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "policycard": ["customeridno", "policyno", "corporatename",
                           "relationship", "validfrom", "officecode",
                           "emergencyhelplineno"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
        }
        absent = {
            "billsummary": ["qty", "dischargesummary", "admissiondate"],
            "billdetails": ["admissiondate", "dischargesummary"],
            "dischargesheet": ["finalbill"],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == "bellevueclinic":
        present = {
            'billsummary': ["finalbill", "servicetaxcode", "cgst", 'sgst'],
            'billdetails': ["qty", "description", "code", "charge", "billno", "netamount",
                            "claimamount", "expenses"],
            "dischargesheet": ["dischargesummary", "admissiondate", "finaldiagnosis",
                               "surgeryperformed", "reviewafter", "dischargedate", "presentingcomplaints",
                               "pasthistory", "treatmentgiven",
                               "conditionatdischarge"
                               "allergies", "currentmedication", "examinationatthetime", "systemicexamination", "tab",
                               "followup", "pleasecallemergency"
                                           "localexamination", "surgerydetails", "procedure", "investigation",
                               "courseduringhospitalstay",
                               "treatmentgiven", "advisedondischarge", "followup", "nameoftheconsultant"],
            "authorizationletter": ["queryletterforcashlessauthorization", "claimintimationno",
                                    "documentstobeprovidedbythehospital", "insupportoftheclaim",
                                    "address", "authorizationletter", "approveddate", "initialapproved"],
            # "labreport": ["mriscanreport", "name", "referredby", "age", "sex", "date", "scanno"],
            "cashless": ["policypart", "cashless", "tobefilled", "nameofthetreatingdoctor", "declaration",
                         "qualification",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "policycard": ["customeridno", "policyno", "corporatename",
                           "relationship", "validfrom", "officecode",
                           "emergencyhelplineno"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
        }
        absent = {
            "billsummary": ["qty", "dischargesummary", "admissiondate"],
            "billdetails": ["dischargesummary", "normaldischarge", "adviceondischarge",
                            "courseinhospital", "followup", "reviewafter", "authorizationletter"
                , "alapproveddate", "alnumber"],
            "dischargesheet": ["finalbill"],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == "woodlandhospital":
        present = {
            'billsummary': ["summarisedbill", "description", "actamt", "totalbillforserviceprovided",
                            "netamountinwords", "note:bedchargenotincluded"],
            'billdetails': ["qty", "rate", "quantity", "subtotal", "balance", "servicedetail", "rundate"],
            "dischargesheet": ["dischargesummary", "admissiondate", "finaldiagnosis",
                               "surgeryperformed", "reviewafter", "dischargedate", "presentingcomplaints",
                               "pasthistory", "treatmentgiven", "operativeprogress", "courseoftreatment",
                               "conditionatdischarge"
                               "allergies", "currentmedication", "examinationatthetime", "systemicexamination", "tab",
                               "followup", "pleasecallemergency"
                                           "localexamination", "surgerydetails", "procedure", "investigation",
                               "courseduringhospitalstay",
                               "treatmentgiven", "advisedondischarge", "followup", "nameoftheconsultant"],
            "authorizationletter": ["queryletterforcashlessauthorization", "claimintimationno",
                                    "documentstobeprovidedbythehospital", "insupportoftheclaim",
                                    "address", "authorizationletter", "approveddate", "initialapproved"],
            # "labreport": ["mriscanreport", "name", "referredby", "age", "sex", "date", "scanno"],
            "cashless": ["policypart", "cashless", "tobefilled", "nameofthetreatingdoctor", "declaration",
                         "qualification",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "policycard": ["customeridno", "policyno", "corporatename",
                           "relationship", "validfrom", "officecode",
                           "emergencyhelplineno"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
        }
        absent = {
            "billsummary": ["qty", "dischargesummary", "quantity", "subtotal"],
            "billdetails": ["dischargesummary", "normaldischarge", "adviceondischarge",
                            "courseinhospital", "followup", "reviewafter", "authorizationletter"
                , "alapproveddate", "alnumber"],
            "dischargesheet": ["finalbill"],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == "holyspirithospital":
        present = {
            'billsummary': [],
            'billdetails': ["draftbill", "class", "rate", "amount", "charge", "issueno", "issuedate", "hshis"],
            "dischargesheet": [],
            "authorizationletter": ["queryletterforcashlessauthorization", "claimintimationno",
                                    "documentstobeprovidedbythehospital", "insupportoftheclaim",
                                    "address", "authorizationletter", "approveddate", "initialapproved"],
            # "labreport": ["mriscanreport", "name", "referredby", "age", "sex", "date", "scanno"],
            "cashless": ["policypart", "cashless", "tobefilled", "nameofthetreatingdoctor", "declaration",
                         "qualification",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "policycard": ["customeridno", "policyno", "corporatename",
                           "relationship", "validfrom", "officecode",
                           "emergencyhelplineno"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
        }
        absent = {
            "billsummary": ["qty", "dischargesummary", "quantity", "subtotal"],
            "billdetails": ["dischargesummary", "normaldischarge", "adviceondischarge",
                            "courseinhospital", "followup", "reviewafter", "authorizationletter"
                , "alapproveddate", "alnumber"],
            "dischargesheet": ["finalbill"],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == "metrohospital":
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "hepaticfunction", "attendingpractitioner", "dischargedate",
                               "allergicdrugs",
                               "admissiondate", "followup", "ensuringappointment", "dateofdischarge",
                               "hospitaldeclaration",
                               "dischargediagnosis",
                               "findings", "adviceondischarge", "pendingresult", "conditionatdischarge",
                               "dischargemedication", "dischargerecommendation"],
            "billsummary": ["billsummary", "dischargebill", "qty", "amount", "totalamount",
                            "qty", "item", "netamount"],
            "billdetails": ["billofsupplyinpatientbill", "netbillamount", "payeramount", "paymentmode" "summary",
                            "billdate", "signatureofaccountant", "amountinwords", "billbreakup",
                            "gstin", "subtotal", "admincharges" "procedurecharge", "nursingcarecharge", "expirydate",
                            "qty", "price",
                            "quantity", "batchno",
                            "signatureofcashier", "billdate", "amounttopay", "amountcollected", "investigationcharge",
                            "consultationcharge", "partytotal", "consumable", "unitprice", "mrp"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policy": ["uhid", "policy"],
            "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "cashlessauthorization", "claimform", "declarationbythepatient",
                               "teslamri"],
            "billsummary": ["dischargesummary", "price", "qty"],
            "billdetails": ["dischargesummary", "relation", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", ],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],

        }
    elif hosp == "starhospital":
        present = {
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "dischargesheet": ["dischargesummary", "hepaticfunction", "attendingpractitioner", "dischargedate",
                               "allergicdrugs", "diagnosis", "historyof", "physicalexaminations"
                                                                          "admissiondate", "followup",
                               "ensuringappointment", "dateofdischarge",
                               "hospitaldeclaration", "mrno./ipno", "patientname", "adviseddrug",
                               "dischargediagnosis", "hospitalcourse", "adviseddrug",
                               "findings", "adviceondischarge", "pendingresult", "conditionatdischarge",
                               "dischargemedication", "dischargerecommendation"],
            "billsummary": ["billsummary", "dischargebill", "qty", "amount", "totalamount",
                            "qty", "item", "netamount"],
            "billdetails": ["billofsupplyinpatientbill", "netbillamount", "payeramount", "paymentmode" "summary",
                            "billdate", "signatureofaccountant", "amountinwords",
                            "gstin", "subtotal", "admincharges" "procedurecharge", "nursingcarecharge", "expirydate",
                            "qty", "price", "finalbill",
                            "quantity", "batchno",
                            "signatureofcashier", "billdate", "amounttopay", "amountcollected", "investigationcharge",
                            "consultationcharge", "partytotal", "consumable", "unitprice", "mrp"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policy": ["uhid", "policy"],
            "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "claimnumber", "alapproved", "alrequested"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }

        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "dischargesheet": ["billsummary", "cashlessauthorization", "claimform", "declarationbythepatient",
                               "teslamri", "authorizationlettertothe", "qty", "indentno", "cashlessrequest"],
            "billsummary": ["dischargesummary", "price", "qty"],
            "billdetails": ["dischargesummary", "relation", "mandatorypasthistory", ],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", ],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],

        }
    elif hosp == "globalhospital":
        present = {

            "billsummary": ["finalbill", "interimbill", "admissiondate", "saccode", "discount", "billno",
                            "totalgrossamount"
                            "netamountpayable", "approximatebill"],
            "billdetails": ["encounterno", "totalbill", "drugs&disposables", "issuedate", "itemname", "batchno",
                            "expdate",
                            "qty", "unitprice", "daywisebreakup", "units", "credit", "subtotal", "pharmacytotal",
                            "exclusion",
                            "drugsanddisposables", "pharmacyindentcharges", "wardindentcharges", "ipconsultations",
                            "threewayextension", "examinationdisposable", "medicalequipments", "surgicalpapertape",
                            "steriledisposable", "disposableface", "othbed", "luerlock", "gauzeward"],
            "dischargesheet": ["dischargesummary", "principaldiagnosis", "chiefcomplaints", "historyofpatientillness",
                               "pastsurgicalhistory", "onexamination", "systemicexamination", "localexamination",
                               "hospitalcourse", "operativenotes", "postoperativeperiod", "dischargeinstructions",
                               "allreportsattachedwith", "otherinstruction", "nutritionadvice", "medicaldosage",
                               "dischargecare", "incaseofsevere", "cometoemergency", "pastmedicalhistory", ],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policy": ["uhid", "policy"],
            # "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
            #               "scanno", "report", "radiologist", "mri", "observations",
            #               "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["authorizationletter", "claimnumber", "alapproved", "alrequested"],
            # "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],
            "billsummary": ["encounterno", "drugs&disposables", "expdate", "daywisebreakup", "subtotal",
                            "pharmacytotal",
                            "dischargesummary", "principaldiagnosis", "chiefcomplaints", "pastsurgicalhistory",
                            "onexamination",
                            "systemicexamination", "localexamination", "unitprice"],
            "billdetails": ["finalbill", "interimbill", "netamountpayable", "dischargesummary", "admissiondate"],
            "dischargesheet": ["finalbill", "interimbill", "encounterno", "totalbill", ],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", ],
            # "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
            #               "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "authorizationletter": ["requestforcashless"],
            # "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],
        }
    elif hosp == "wockhardthospital":
        present = {
            "billdetails": ["finalbill", "billtype", "exp.date", "expdate", "ipbill", "(detail)", "(final)", "qty",
                            "batchno"],
            "dischargesheet": ["dischargesummary", "finaldiagnosis", "surgerydone", "chiefcomplaints", "pasthistory",
                               "systemicexamination", "courseinthehospital", "treatmentinthehospital",
                               "conditionatthetimeofdischarge", "treatmentondischarge", "followupadvice",
                               "dischargeaftercare", "treatmentondischarge", "followup", "dischargeaftercare",
                               "instructionsgivenaboutthemedications",
                               "aboutthemedications"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],
        }
        absent = {
            "billdetails": ["dischargesummary", "finaldiagnosis"],

            "dischargesheet": ["finalbill", "billtype", ],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
        }
    elif hosp == 'astercmibangalore':
        present = {
            "dischargesheet": ["dischargesummary", "dateofoperation", "reasonforadmission", "courseinthehospital",
                               "courseinthe",
                               "dietadvice", "whentoobtain", "surgicaloncology", "dischargediagnosis",
                               "leadandsrconsultant",
                               ],
            "billdetails": ["draftpackage", "servicedetails", "patientpackagedetails", "exc.qty", "exp.dt",
                            "packageexcludes",
                            "accountheadservice", "acountheadservicedetails", "headservicedetails", "accounthead",
                            "discount",
                            "draftservicedetails", "hospitalisationcharges", ],
            "labreport": ["diagnosisreport", "haematology", "biologicalreferencerange", "biochemistry",
                          "consultantpathologist",
                          "microbiology", "serology", "covid19test", ],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],

            "authorizationletter": ["authorizationletter", "sanctionedamount", "claimnumber", "agreedtariff",
                                    'initialapproved'],
            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],
            # "progressnotes": ["progressnotes", "medicationorderdoctor", "progressnotesdoctor", "icdcode"]

        }
        absent = {
            "dischargesheet": ["draftpackage", "servicedetails", "patientpackagedetails", "exc.qty", "exp.dt",
                               "packageexcludes",
                               "accountheadservice", "acountheadservicedetails", "headservicedetails", "accounthead",
                               "hospitalisationcharges",
                               "diagnosisreport", "biologicalreferencerange", "progressnotes", "medicationorderdoctor",
                               "progressnotesdoctor"],
            "billdetails": ["dischargesummary", "reasonforadmission", "courseinthehospital", "courseinthe",
                            "dietadvice", "whentoobtain", "dischargediagnosis",
                            "diagnosisreport", "biologicalreferencerange", "progressnotes", "medicationorderdoctor",
                            "progressnotesdoctor"],
            "labreport": ["dischargesummary", "reasonforadmission", "courseinthehospital", "courseinthe",
                          "whentoobtain", "draftpackage", "servicedetails",
                          "patientpackagedetails", "exc.qty", "exp.dt", "packageexcludes", "accountheadservice",
                          "acountheadservicedetails", "headservicedetails",
                          "accounthead", "draftservicedetails", "hospitalisationcharges", "progressnotes",
                          "medicationorderdoctor", "progressnotesdoctor"],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],
            "authorizationletter": [],
            "policyidcard": [],
            # "progressnotes": ["dischargesummary", "draftpackage", "servicedetails", "accountheadservice",
            #                   "acountheadservicedetails", "diagnosisreport", "biologicalreferencerange"],
        }
    elif hosp == 'qrghealthcityhospital':
        present = {
            "authorizationletter": ["authorizationletter", "alapproveddatae", "alrrequesteddate", "alnumber",
                                    "policyrelateddeductions", "proportionatededuction", "theauthorizationisvalidfor",
                                    "intheeventofunauthorizedrecovery", ],
            "billsummary": ["provisionalbillofsupplysummary",
                            "billofsupplysummary", "supplysummary", "finalbill", "billno"],
            "billdetails": ["provisionalbillofsupplydetail", "billofsupplydetail", "supplydetail", "qty",
                            "nonpayablebill",
                            "totalforbedcharges", "totalforadministrationcharges", "totalforcriticalcare", "preparedby",
                            "totalforlaboratory", "totalfor", "ip-nonpayablebill", "disposable"],
            "dischargesheet": ["dischargesummary", "briefhistoryofillness", "hospitalcourse", "operativeprocedure",
                               "operativefindings", "conditionatdischarge", "dischargeadvised", "preventivestrategies",
                               "whentoobtainurgentcare", "dischargedate", "dischargeadvise", "pendingreports",
                               "postdeliveryperiod", "followup", "nextappointment", "investogationsdonewithreports",
                               ],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "tobefilledbytreating", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization", "hospitaldeclaration"
                                                          "natureofillness", "noobjectiontoanyauthorizedtpa",
                         "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],

            "policyidcard": ["customeridentitycard", "customeridno", 'cardno', 'validto'],
        }
        absent = {
            "authorizationletter": ["provisionalbillofsupplysummary", "provisionalbillofsupplydetail",
                                    "briefhistoryofillness", "hospitalcourse", "nextappointment",
                                    "investogationsdonewithreports"],
            "billsummary": ["provisionalbillofsupplydetail", "billofsupplydetail", "supplydetail", "qty",
                            "nonpayablebill",
                            "ip-nonpayablebill""preparedby", "totalforlaboratory", "totalfor"],
            "billdetails": ["provisionalbillofsupplysummary", "billofsupplysummary", "supplysummary", ],
            "dischargesheet": ["authorizationletter", "alapproveddatae", "alrrequesteddate", "alnumber",
                               "provisionalbillofsupplysummary",
                               "billofsupplysummary", "provisionalbillofsupplydetail", "billofsupplydetail",
                               "nonpayablebill", ],
            "aadhar": ['incometax', 'permanentteam'],
            "pan": ['aadhar'],
            "panaadhar": ['amount', 'discharge', 'rate', 'diagnosis'],
            "cashless": ['sanctionedamount'],

            "policyidcard": [],

        }
    elif hosp == 'jaypeehospital':
        present = {
            "billdetails": ["inpatientdetailrunningbill", "inpatientdetail", "inpatientdetailrunning",
                            "detailrunningbill",
                            "billno", "billdate", "batchno", "expirydate", "discount", "episodeno", "provisionalbill",
                            "unitrate", "qty", "finalbill", "refundabletopatient"],
            "dischargesheet": ["dischargesummary", "dateofprocedure", "examinationonadmission", "localexamination",
                               "doctorsteam", "courseinthehospital", "procedurefindings", "medicationsadviced",
                               "medicationsadvicedondischarge", "futuretreatmentplan", "conditionondischarge",
                               "adaypriortoyourvisit",
                               "reasonforadmission", "wasadmitted", "mentionedcomplaints", "investigations", "Reviewin",
                               "incaseyouwanttotakean", "proceduredone", "physicalactivityadvice", "followup",
                               "casesummary", "forappointments&lab", "&labreorts", "forhomesamplecollection"],
            "authorizationletter": ["authorizationletter", "alapproveddatae", "alrrequesteddate", "alnumber",
                                    "policyrelateddeductions", "proportionatededuction", "theauthorizationisvalidfor",
                                    "intheeventofunauthorizedrecovery"],
            "pan": ["incometax", "depart", "permanentaccountnumber"],
            "panaadhar": ["incometax", "depart", "address", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policy": ["uhid", "policy"],
            # "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
            #               "scanno", "report", "radiologist", "mri", "observations",
            #               "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", ],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],

            # "authorizationletter": ["authorizationletter", "claimnumber", "alapproved", "alrequested"],
            # "prescription": ["capsule", "oral", "dose", "prescription", "duration"],
            "policyidcard": ["customeridentitycard", "customeridno"],
        }
        absent = {
            "billdetails": ["dischargesummary", "authorizationletter", "policyrelateddeductions",
                            "proportionatededuction",
                            "theauthorizationisvalidfor", ],
            "dischargesheet": ["inpatientdetailrunningbill", "inpatientdetail", "inpatientdetailrunning",
                               "detailrunningbill", "provisionalbill", "finalbill", "refundabletopatient",
                               "staffisqualified"],
            "authorizationletter": ["casesummary", "examinationonadmission", "inpatientdetailrunningbill",
                                    "inpatientdetail", "inpatientdetailrunning", "provisionalbill",
                                    "requestforcashless",
                                    "unitrate", "qty"],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", ],
            # "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
            #               "billsummary", "tobefilled", "cashless"],
            "cashless": ["claimnumber", "relation", "admissionofliability"],
            "aadhar": ["incometax", "depart", "permanentaccountnumber", ],

            # "prescription": ["nothing", "attendingpractitioner", "claimform"],
            "policyidcard": [],
        }
    else:
        present = {
            "emergencycertificate": ["emergencycertificate", "anemergencycondition"],
            "denguemalariainsurance": ["dengueandmalariainsurance", "icici", "malariarelated",
                                       "onbehalfofalltheinsured"],
            "aadhar": ["youraadhaarno.", "proofofidentity", "enrolmentno",
                       "governmentofindia", "uidai", "uldal", "dob", "aadhaar", "governmentof", "mentofindia",
                       "uniqueidentificationauthorityofindia", "help@uidal.gov.in", "www.vidal.gov.in",
                       "www.uidal.gov.in","uniqueidecation","gov.inm", "rityofindia" ],
            "cancelledcheque": ["paratallbranches", "orbearer", "pay", "payableatallbranches",
                                "payableatparatalbranches", "amount", "cancel",
                                "payableatallourbranches", "payableatparatall", "citycheque",
                                "payablealparthroughclearing",
                                "payableatparthroughclearing", "cancelled", "ororder", "payableat", "non-homebranch"],
            "dischargesheet": ["dischargesummary", "hepaticfunction", "attendingpractitioner", "dischargedate",
                               "allergicdrugs", "courseduringhospitalization", "repeatedinvestigations",
                               "admissiondate", "followup", "ensuringappointment", "dateofdischarge",
                               "hospitaldeclaration", "feverwithchills", "cvsexamination", "homeadvice",
                               "whatcaretotake", "indoorno",
                               "dischargediagnosis", "complaintsonadmission", "abdomenexamination", "restcourse",
                               "findings", "adviceondischarge", "pendingresult", "conditionatdischarge",
                               "dischargemedication", "dischargerecommendation", "treatmentadvice", "followup",
                               "dateofadmission", "operationnote", "treatmentgiven", "semiliquid",
                               "dischargecard", "dischargeticket", "doa", "specialinvestigation", "treatmentgiven",
                               "treatmentadvised", "capidreview", "investigations", "blood", "treatmentised", "dod", "pasthistory"],
            "billsummary": ["billsummary", "dischargebill", "qty", "amount", "totalamount","village", "particular",
                            "qty", "item", "netamount","particulars","investigation/services","usgwholeabdomenfemale"],
            "billdetails": ["billofsupplyinpatientbill", "netbillamount", "payeramount", "paymentmode" "summary",
                            "billdate", "signatureofaccountant", "amountinwords", "detailrunningbill", "quantity",
                            "gstin", "subtotal", "admincharges" "procedurecharge", "nursingcarecharge", "expirydate",
                            "qty", "price", "billno", "particulars", "billcumreceipt", "receipt/regno",
                            "quantity", "batchno","gstinvoice",
                            "signatureofcashier", "billdate", "amounttopay", "amountcollected", "investigationcharge",
                            "consultationcharge", "partytotal", "consumable", "unitprice", "mrp",
                            "registrationcharges","ipfinalbill", "bill-detailed","finalbill","ipfinal.bill","particulars"],
            "admissionnote": ["admissionnote"],
            "pan": ["incometax", "depart", "permanentaccountnumber", "taxdepartment"],
            "panaadhar": ["incometax", "depart", "youraadhaarno.", "proofofidentity", "enrolmentno",
                          "governmentofindia",
                          "uidai", "uldal"],
            "policy": ["uhid", "policy"],
            "labreport": ["report", "departmentof", "laboratorymedicine", "methodused", "testname", "scans&laboratory",
                          "scanno", "report", "radiologist", "mri", "observations","usgabdomen","nosignificantusg",
                          "reportedon", "reportedby", "investigation", "laboratory", "ultrasoundfor", "urine",
                          "testdone","antibiotic","normalrange","specimentype","sampleid","standardoperatorid",
                          "reactiveproteintest", "chestradiograph", "bothlungfields","dopplermeasurements","mitralvalve"
                          "spermatozoa"],
            "cashless": ["cashless", "authorization", "tobefilled", "nameofthetratingdoctor", "declaration",
                         "qualification", "expectedcostofinvestigation", "costofimplants",
                         "expectedcostofhospitalization",
                         "natureofillness", "detailsofpatientadmitted", "mandatorypasthistory",
                         "roomtype"],
            "authorizationletter": ["cashlessauthorizationletter", "claimnumber"],
            "prescription": ["capsule", "oral", "dose", "prescription", "duration", "ciproduc", "soomg", "ceproduc",
                             "histaben", "amypres", "fomili", "ainsweet", "blavani", "cannula", 'washermenpet',
                             "capsule", "oral", "dose", "prescription", "duration", "edervit", "frcp",
                             "medicineorders", "drugsensitivity", "omnacortil", 'ferinject', "bekalin",
                             "sherofmed", "prelumbar", "backino", "pericurial", "culoscess", "penicual", "pugsout",
                             "butdol","pantin","hybocal","sporlalpowder","xone","similac","amokav"
                             "ciproduc", "dompay"],
            "policyidcard": ["customeridentitycard", "customeridno", "validupto", "cardno", "validfrom"],
            "claimform": ["updateonyourclaimstatus", "detailsofamountclaimed", "allclaimsshallbesettled",
                          "enclosurechecklist", "claimform", "insuranceofthisclaimform", "tobefilledbyinsuredperson",
                          "claimdetails", "hospitaldetails", "tobefilledbyinsuredperson", "insuredpersondeclaration",
                          "undertaketorefund", "detailsprovidedbytheclaimant", "insuredpersoninthemandate",
                          "ourclaimpayment",
                          "groupsafeguard", "maternalcomplication", "neftdetails", "inuredperson", "irdaregistration",
                          "sectionsandbenefits", "lossdate",
                          "allclaims", "part-b", "declarationbythehospital", "claimnumber", "empcode", "cardno",
                          "claimfor"],
            "indoorcasepapers": ["progressrecord", "clinicalfindings", "findings&progress", "aspiration", "d.i.c",
                                 "medicine", "specialinstruction", "familycommunication", "personofproviding",
                                 "progress", "treatment", "initialassessmentrecord", "sourceofhistory", "careplanby",
                                 "intake", "nursingassessmentform", "reasonforadmission"],
            "receipt": ["receipt", "reciept", "reg.charges", "receiptno", "advancereceived", "investigation",
                        "thesumofrupees", "recievedwiththanksrs", "referredbydr.", "recievedwiththanksfrommr",
                        "towardsoperation","cashreceipt", "billcollection",
                        "onaccountofconsultation", "receivedwiththanks", "particulars", "towardsmyconsultationfeesrs"],
            "consultationpapers": ["fcough", "sartos", "rugrl", "murovel"],
            "driverslicence": ["drivinglicence", "dateofissue", "form7rule", "mcwg"],
            "queryreply": ["claimno", "weshallproceed"],

            "essentialitycertificate": ["essentialitycertificate", "prescribedbyme"],
            "riskassumption": ["riskassumptionletter", "loantenure", "groupsafeguardinsurance", "insuredeventalongwith",
                               "premiumdetails", "stampduty", "taxcertificate"]
        }

        absent = {
            "emergencycertificate": [],
            "denguemalariainsurance": ["benefitamount"],
            "aadhar": ["incometax", "depart", "permanentaccountnumber", "policy"],
            "cancelledcheque": ["reimbursement", "passbook", "policywording", "qty", "claimform",
                                "guidelinesissuedbytheirdai", 'myopiadone', "billcumreceipt",
                                "riskassumption", "insurance", "payabletoinsured", "hospitaldiscounts", "detailedbill",
                                "doctor","bill"],
            "dischargesheet": ["billsummary", "cashlessauthorization", "claimform", "declarationbythepatient",
                               "teslamri", "advancereceived", "admissioncard", "deposit", "haemogramreport","up-sheet",
                               "staffisqualified", "employeeno", "empcode", "detailedbill", "policynumber",
                               "registrationcharges", "ipfinalbill", "finalbill", "indoorno", "lab.ref.no",
                               "malarialparasite", "smearfindings","inpatientbill","mrfistulogram","studydate"],
            "billsummary": ["dischargesummary", "price", "qty", "quantity", "detailrunningbill",
                            "essentialitycertificate","ipfinalbill","itemname",],
            "billdetails": ["dischargesummary", "mandatorypasthistory", "billsummary", "tobefilled", "hospitalpolicy",
                            "denguens1antigentest","indoorno","oracle","spermatozoa",
                            "testdone","conditionsofreporting","totalamount"],
            "admissionnote": [],
            "pan": ["discharge", "hrctchest", "radiology", "findings", "clinical", "billsummary", "youraadhaarno.",
                    "proofofidentity", "enrolmentno", "governmentofindia", "uidai", "uldal"],
            "panaadhar": ["laboratory", "starhealth", "hospitalisation", "manager", "bill", "medicine", "doctor",
                          "method", "policycertificate"],
            "policy": ["discharge", "authorizationsummary", "totalbillamount", "departmentofradiology", "hrctchest",
                       "invoice", "claimnumber"],
            "labreport": ["admissiondate", "dischargesummary", "conditionatdischarge", "detailsofpatientadmitted",
                          "billsummary", "tobefilled", "cashless", "policy", "dischargecard", "onephotocopy",
                          "courseduring", "dischargecard","pastsurgicalhistory","glucose-random",
                          "undertakingfor", "familycommunication", "continuationsheet", "receiptno",
                          "initialassessment","declarationform","cell/cum","halfhourreading",
                          "billcumreceipt", "claimno", "lossdate", "riskassumption", "statethat", "attendance",
                          "total:", "empcode", "government","terms&conditions","conditionsofreporting"],
            "cashless": ["claimnumber", "relation", "admissionofliability", "declarationbythehospital"],
            "authorizationletter": ["requestforcashless"],
            "prescription": ["nothing", "attendingpractitioner","nothing", "attendingpractitioner", "claimform","riskassumption","hospitaldetails","follow-up-sheet",
                             "aspiration","electoral", ],
            "policyidcard": [],
            "claimform": ["conditionsofreporting"],
            "indoorcasepapers": ["certificate"],
            "receipt": ["allclaims", "claimfor"],
            "consultationpapers": [],
            "driverslicence": [],
            "queryreply": [],

            "essentialitycertificate": [],
            "riskassumption": []

        }

    """classification of doc starts here"""
    count = 0
    document = 'none'
    document_final = 'unknown'

    documents = []
    hospitals = []

    print('98')
    # if txt.lower().replace(" ","").__contains__('nanavati'):
    #     hospital = 'nanavati'
    # elif txt.lower().replace(" ","").__contains__('medanta') or txt.lower().replace(" ","").__contains__('medantha'):
    #     hospital = 'medanta'
    # elif txt.lower().replace(" ","").__contains__('maxcare') or txt.lower().replace(" ","").__contains__('maxsuper'):
    #     hospital = 'max'
    # elif txt.lower().replace(" ","").__contains__('deenanath') or txt.lower().replace(" ","").__contains__('deenanathmangeshkar'):
    #     hospital='deenanath'
    # elif txt.lower().replace(" ","").__contains__('aster') or txt.lower().replace(" ","").__contains__('astermims'):
    #     hospital='aster'
    # elif txt.lower().replace(" ", "").__contains__('blk'):
    #     hospital = 'blk'
    for key in present.keys():
        # print('into the present dictionary')
        count = 0
        for i in present[key]:
            # print('into the keywords of '+key)
            # print(i + '\n')
            if txt.lower().replace(" ", "").__contains__(i):
                count = count + 1
                print(i)
                print('doc: ' + key)
                if count >= c:
                    print('117')
                    document = key
                    print('138 ' + document)
                    print(key)
                    for j in absent[key]:
                        # print('into the absent keywords of '+key)
                        # print('141 ' + key)
                        if txt.lower().replace(" ", "").__contains__(j):
                            count = 0
                            print('Exceptions:')
                            print(j)
                            document = 'none'
                            break
                    if count >= c:
                        break
        if count >= c:
            print('148')
            print(document)
            document_final = document
            # documents.append(document)
            break
    print('list:\n')
    print(document_final)
    return document_final
