import os
basepath=f'{os.path.dirname(os.path.abspath(__file__))}/Captured/'
pictures=os.listdir(basepath)
pictures.remove('index.html')
picturesSort=sorted(pictures,reverse=True)
htmlhead="<html>\r\n<head>\r\n<title>My dear plant</title>\r\n<style>\r\ndiv.gallery {\r\nmargin: 5px;\r\nborder: 1px solid #ccc;\r\nfloat: left;\r\nwidth: 400px;\r\n}\r\n\r\ndiv.gallery:hover {\r\nborder: 1px solid #777;\r\n}\r\n\r\ndiv.gallery img {\r\nwidth: 100%;\r\nheight: auto;\r\n}\r\n\r\ndiv.desc {\r\npadding: 15px;\r\ntext-align: center;\r\n}\r\n</style>\r\n</head>\r\n<body>\r\n"
htmlbottom="</body>\r\n\r\n</html>"

for i in picturesSort:
    htmlhead+=f"<div class=\"gallery\">\r\n<a target=\"_blank\" href=\"{i}\">\r\n<img src=\"{i}\" alt=\"Cinque Terre\" width=\"800\">\r\n</a>\r\n<div class=\"desc\">{i}</div>\r\n</div>"
htmlhead+=htmlbottom

f=open(f'{basepath}/index.html',"w")
f.write(htmlhead)
f.close()

print(pictures)