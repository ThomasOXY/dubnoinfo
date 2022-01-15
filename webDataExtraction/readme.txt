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




























Pokud byly nějaké hodiny vyjmuty z rozvrhu jako školní akce, tak to ukaze pouze jednu hodinu nekdy:
"FRI": {
    "7": "Vyjmuto skol akce"
},

pokud tam jsou hodiny normalni a skolni akce: (skolni akce je od 0 do 5)
"THU": {
    "6": "MAT",
    "7": "PPV",
    "8": "Vyjmuto skol akce"
},


nejlepsi reseni, pokud se objevi "skol. akce" oznacit cely den jako skolni akci, az na vyjimky pokud nejaky jsou


bordel v tom je
kdyz je neco vyjmuto z rozvrhu tak se to prohodi A a B 

nejde pouzit pravidlo na radky, kdyz jsou praxe/normalni tak to neni dobre