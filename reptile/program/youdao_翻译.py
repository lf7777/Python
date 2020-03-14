import requests,json,time,random
import hashlib

def translate(key): 
    ts = int(time.time()*1000)
    salt = str(ts+random.randint(0,10))
    sign = 'new-fanyiweb'+key+salt+"ydsecret://newfanyiweb.doctran/sign/0j9n2{3mLSN-$Lg]K4o0N2}"
    lmd5 = hashlib.md5()
    lmd5.update(sign.encode('utf-8'))
    sign_md5 = lmd5.hexdigest()

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    headers = {
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=788442849@10.108.160.19; JSESSIONID=aaaYA2s5IkJ7Y_RKC7tdx; OUTFOX_SEARCH_USER_ID_NCOO=889010775.8694379; ___rl__test__cookies=1584106271634'
    }

    form={
    'i': key,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign_md5,
    'ts': ts,
    'bv': '5dfabd970ef44d778884b2781249f18c',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'}

    response = requests.post(url,data=form,headers=headers)

    res_dict = json.loads(response.text)

    print(res_dict['translateResult'][0][0]['tgt'])

if __name__ =='__main__':
    while True:
        key = input('请输入要翻译的内容:\n')
        if key == 'q':
            break
        translate(key)
