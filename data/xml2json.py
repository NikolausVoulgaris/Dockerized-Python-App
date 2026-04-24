import xmltodict
import json


def xml2json(first, per_page, src='202511'):
    filepath = 'data/TOP500_' + src + '_all.xml'

    with open(filepath) as xml_file:
        raw_dict = xmltodict.parse(xml_file.read())

    trans_dict = {}
    for i in range(first, (first + per_page)):
        raw_item = raw_dict['top500:list']['top500:site'][i-1]
        trans_dict[i] = {
            'sytem-name': raw_item['top500:system-name'],
            'description': raw_item['top500:computer'],
            'r-max/PF': float(raw_item['top500:r-max'])/1e6,
            'r-peak/PF': float(raw_item['top500:r-peak'])/1e6,
            'power/kW': raw_item['top500:power'],
            'n-max': raw_item['top500:n-max'],
            'processing cores': raw_item['top500:number-of-processors'],
            'country': raw_item['top500:country'],
            'year': raw_item['top500:year'],
            'area': raw_item['top500:area-of-installation'],
        }

    return json.dumps(trans_dict, indent=4)
