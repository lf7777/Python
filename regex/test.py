import re



if __name__ == '__main__':

    text = 'He was carefully dislyguised but captured quickly by policely.'

    pattern = '(\w*ly)[^a-zA-Z]'

    res = re.findall(pattern,text)

    print(res)
