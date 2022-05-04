from pprint import pprint
import csv
import re


def regular_expressions_phones():
    with open("phonebook_raw.csv", encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    for name in contacts_list[1::]:
        text = ' '.join(name[0:3]).split(' ')
        name[0], name[1], name[2] = text[0], text[1], text[2]
    contacts_list.append(name)
    del contacts_list[-1]

    contacts_list_new = []
    keys = set()
    for index, cont_list in enumerate(contacts_list):
        for index2 in range(index + 1, len(contacts_list)):
            new = contacts_list[index2]
            if new[0] == cont_list[0] and new[1] == cont_list[1]:
                contacts_list_new.append([f if f else s for s, f in zip(cont_list, new)])
                keys.add(cont_list[0])
        if cont_list[0] not in keys:
            contacts_list_new.append(cont_list)

    for phones_old in contacts_list_new[1::]:
        text = []
        text.append(phones_old[5])
        text2 = ' '.join(text)
        pattern = r"(\+7|8)\s*\(?(\d{3})\)?-?\s*(\d{3})(-|\s)*(\d{2})(-|\s)?(\d{2})\s*\(?(д?о?б?\.?)\s{1}(\d{4})?\)?"
        pattern_c = re.compile(pattern)
        result = pattern_c.sub(r"=+7(\2)\3-\5-\7 \8\9", text2)
        phones = list(filter(None, result.split('=')))
        for p in phones:
            phones_old[5] = p

    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(contacts_list_new)

    pprint(contacts_list_new)

regular_expressions_phones()