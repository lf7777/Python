import re



if __name__ == '__main__':

    text = 'He was carefully dislyguised but captured quickly by policely.'

    pattern = '(\w*ly)[^a-zA-Z]'

    res = re.finditer(pattern,text)

    for item in res:

        print(item.group(1))



