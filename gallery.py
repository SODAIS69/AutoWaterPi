import os
def GenerateGallery():
    basepath=f'{os.path.dirname(os.path.abspath(__file__))}/Captured/'
    pictures=os.listdir(basepath)
    if os.path.exists(f'{basepath}/index.html'):
        pictures.remove('index.html')
    picturesSort=sorted(pictures,reverse=True)
    htmlhead="<html>\r\n<head>\r\n<meta http-equiv=\"refresh\" content=\"3\" ><meta charset=\"utf-8\"><title>My dear plant</title>\r\n<style>\r\nbody {font-family:微軟正黑體;\r\n:background-color: #dae0ff;\r\nmargin: 70px;\r\nmargin-top: 50px}div.gallery {\r\n background-color:white; margin: 5px;\r\nborder: 1px solid #ccc;\r\nfloat: left;\r\nwidth: 400px;\r\n}\r\n\r\ndiv.gallery:hover {\r\nborder: 1px solid #777;\r\n}\r\n\r\ndiv.gallery img {\r\nwidth: 100%;\r\nheight: auto;\r\n}\r\n\r\ndiv.desc {\r\npadding: 15px;\r\nfont-size: 28;\r\ntext-align: center;\r\n}\r\n</style>\r\n</head>\r\n<body>\r\n<h1>～～我ㄉ盆栽～～</h1>"
    htmlbottom="</body>\r\n\r\n</html>"

    for i in picturesSort:
        htmlhead+=f"<div class=\"gallery\">\r\n<a target=\"_blank\" href=\"{i}\">\r\n<img src=\"{i}\" alt=\"Cinque Terre\" width=\"800\">\r\n</a>\r\n<div class=\"desc\">🌻:&nbsp;{i}</div>\r\n</div>"
    htmlhead+=htmlbottom
    #print(f"{basepath}/index.html")
    f=open(f'{basepath}/index.html',"w")
    f.write(htmlhead)
    f.close()

