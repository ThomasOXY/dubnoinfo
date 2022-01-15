readme

proto aby to fungovalo potrebujes samozrejme python a packages, tahle je to asi nejjednodusejsi
pip install bs4 (BeautifulSoup)
pip install requests

mozna "json", a "time"






from bakalariWebDataExtractionWithSoup import main

json = main("název třídy", "zapisovat do dataALL.json? True/False") #název třídy = např. 13 = 3.ZI, priklad.png

>> print json

*dataALL.json








"group": "", pokud je prazndy tak plati pro vsechny
"group": "AT", plati pro danou rozdelenou tridu







\u010cesk\u00fd jazyk a literatura - se musi spravne dekodovat



raw data z timetabelu z webu:
{
    "absencetext": null,
    "changeinfo": "",
    "group": "",
    "homeworks": null,
    "notice": "",
    "room": "206",
    "subjecttext": "\u010cesk\u00fd jazyk a literatura | po 10.1. | 0 (7:10 - 7:55)",
    "teacher": "Mgr. Jana Durajov\u00e1",
    "theme": "\u010cesk\u00e1 literatura konce 20. stolet\u00ed",
    "type": "atom"
},

po úpravě přidáno:
"subjecttext" splitnuty na nameLesson, date, time

prvni cislo v "time": "0 (7:10 - 7:55)", je cislo hodiny
{
    "absencetext": null,
    "changeinfo": "",
    "date": "po 10.1.",
    "group": "",
    "homeworks": null,
    "nameLesson": "\u010cesk\u00fd jazyk a literatura",
    "notice": "",
    "room": "206",
    "subjecttext": "\u010cesk\u00fd jazyk a literatura | po 10.1. | 0 (7:10 - 7:55)",
    "teacher": "Mgr. Jana Durajov\u00e1",
    "theme": "\u010cesk\u00e1 literatura konce 20. stolet\u00ed",
    "time": "0 (7:10 - 7:55)",
    "type": "atom"
},

















