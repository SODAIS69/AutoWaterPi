import os
from moisture import GetMoisture
def GenerateGallery():
    message="這是一盆黃金葛"
    basepath=f'{os.path.dirname(os.path.abspath(__file__))}/Captured/'
    pictures=os.listdir(basepath)
    if os.path.exists(f'{basepath}/index.html'):
        pictures.remove('index.html')
    picturesSort=sorted(pictures,reverse=True)
    htmlhead="<html><head><meta http-equiv=\"refresh\" content=\"30\"><meta charset=\"utf-8\"><title>My dear plant</title>\r\n<style>\r\nbody {\r\n    font-family: 微軟正黑體;\r\n    background-color: #f0f2fb;\r\n    margin: 70px;\r\n    margin-top: 50px\r\n}\r\n\r\ndiv.gallery {\r\n    background-color: white;\r\n    margin: 5px;\r\n    border: 1px solid #ccc;\r\n    float: left;\r\n    width: 400px;\r\n}\r\n\r\ndiv.gallery:hover {\r\n    border: 1px solid #777;\r\n}\r\n\r\ndiv.gallery img {\r\n    width: 100%;\r\n    height: auto;\r\n}\r\n\r\ndiv.desc {\r\n    padding: 15px;\r\n    font-size: 28;\r\n    text-align: center;\r\n}\r\n\r\ndiv.panel {\r\n    background-color: white;\r\n    margin: 5px;\r\n    margin-right: 15px;\r\n    border: 1px solid #777;\r\n    float: left;\r\n    width: 500px;\r\n}\r\n\r\ndiv.panel:hover {\r\n    border: 1px solid #df9797;\r\n}</style>\r\n</head>\r\n<body>\r\n"
    
    htmlhead+=f"<h1>୧(๑•̀ᴗ•́๑)୨～～我ㄉ盆栽～～ 🌡️ 濕度: {GetMoisture()}%</h1><marquee scrollamount=\"10\">{message}</marquee>"
    htmlbottom="</body>\r\n\r\n</html>"
    picturesSort.remove("moisture.jpg")
    picturesSort.remove("archive.jpg")

    htmlhead+=f"<div class=\"panel\" >\r\n<a target=\"_blank\" href=\"moisture.jpg\">\r\n<img src=\"moisture.jpg\" alt=\"Cinque Terre\" width=\"100%\">\r\n</a>\r\n<div class=\"desc\">🌡️濕度</div>\r\n</div>"
    for i in picturesSort:
        name=i
        path=i
        if i=="archive":
            name="archive"
            path="archive.jpg"
        htmlhead+=f"<div class=\"gallery\">\r\n<a target=\"_blank\" href=\"{name}\">\r\n<img src=\"{path}\" alt=\"Cinque Terre\" width=\"800\">\r\n</a>\r\n<div class=\"desc\">🌻:&nbsp;{name}</div>\r\n</div>"
    htmlhead+=htmlbottom
    #print(f"{basepath}/index.html")
    f=open(f'{basepath}/index.html',"w")
    f.write(htmlhead)
    f.close()

