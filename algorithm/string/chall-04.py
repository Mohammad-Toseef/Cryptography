S = "http://something.com and http://xyz.com we can say https://abc.dom "


http = [x for x in range(len(S)) if S.startswith('http://',x)]
for index in http:
    print(S[index:S.index(' ', index)])
https = [x for x in range(len(S)) if S.startswith('https://',x)]
for index in https:
    print(S[index:S.index(' ', index)])
