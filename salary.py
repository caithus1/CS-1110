import re
import urllib.request
import ast


def get_info(name):
    result = {}
    name = name.lower()
    if ',' in name:
        l = name.split(', ')
        name = l[1] + '-' + l[0]
    elif ' ' in name:
        name = name.replace(' ', '-')
    try:
        print(name)
        url = 'http://cs1110.cs.virginia.edu/files/uva2015/' + name
        body = urllib.request.urlopen(url).read().decode('utf-8')
    except:
        return {}
    try:
        job_re = re.compile('(?<=<meta property="og:description" content="Job title: ).*?(?=<br \/>)')
        job = job_re.findall(body)[0].replace('&amp;','&')
        result['title'] = job
    except:
        print('no job')
    try:
        comp_re = re.compile('(?<=gross pay: \$).*?(?=" \/>)')
        comp = float(comp_re.findall(body)[0].replace(',', ''))
        result['pay'] = comp
    except:
        print('comp')
    try:
        compUVa_re = re.compile('(?<=<tr><td>University of Virginia rank<\/td><td>).*?(?=<\/td><\/tr>)')
        compUVa = int(compUVa_re.findall(body)[0].split()[0].replace(',',''))
        result['rank'] = compUVa
    except:
        print('no compUVa')

    compdict_pre_re = re.compile('(?<=var pay = \[ ).*?(?= ];)')
    final = {}
    print((compdict_pre_re.findall(body)[0]))
    print(type(compdict_pre_re.findall(body)[0]))
    print('sa')
    try:
        for i in ast.literal_eval(compdict_pre_re.findall(body))[0]:
            final[i['name']] = float(i['amount'])
        result['breakdown'] = final
        #print('no compdict_pre')
        print('wowow')
    except Exception as e:
        try:
            fi_dict = ast.literal_eval(compdict_pre_re.findall(body)[0])
            final[fi_dict['name']] = float(fi_dict['amount'])
            result['breakdown'] = final
            print('ss')
        except Exception as ee:
            print('noo', ee)
        #print('yes',e)
    return result
