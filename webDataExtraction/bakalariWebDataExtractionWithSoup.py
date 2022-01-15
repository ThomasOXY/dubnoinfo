
def main(webWhatClass, write):
    from bs4 import BeautifulSoup
    import requests
    import time
    import json


    res = requests.get('https://bakalari.dubno.cz/bakaweb/Timetable/Public/Actual/Class/'+str(webWhatClass))

    if res.status_code != 200:
        print('!!!!', 'status code:', res.status_code, '!!!!')
        time.sleep(3)
    else:
        soup = BeautifulSoup(res.content.decode('utf-8','ignore'), 'lxml')

        allDays = soup.find_all("div", {"class": "bk-cell-wrapper"})
        print(len(allDays), 'dní načteno')

        dataALL = {}
        dataALL['ALL'] = []

        for index, i in enumerate(allDays):
            dayItem = i.find_all("div", {"class": "day-item"})
            # dayItem2 = i.find_all("div", {"class": "bk-timetable-cell"})

            for index, o in enumerate(dayItem):
                classInfoJson = o.find_all("div", {"class": "day-item-hover"})[0]['data-detail']
                dataALL['ALL'].append(json.loads(classInfoJson))

    for i in dataALL['ALL']:

        i['nameLesson'] = str(i['subjecttext'].split(' | ')[0])
        i['date'] = str(i['subjecttext'].split(' | ')[1])
        i['time'] = str(i['subjecttext'].split(' | ')[2])
        i.pop('subjecttext', None)

    if write:
        # open('dataALL.json', 'w').close()
        with open('dataALL.json', 'w', encoding='utf-8') as f:
            json.dump(dataALL, f, indent=4, sort_keys=True, ensure_ascii=False)
    return dataALL

# main('1C', True)


