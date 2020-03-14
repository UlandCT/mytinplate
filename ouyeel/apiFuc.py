from .setting import *
import datetime as dt
from django.db.models import Q
from django.template import loader
from ouyeel.models import *


def generate_detail(res, temp, path):
    try:
        html = loader.get_template(temp)
        html = html.render({"goodsInfo": res})
        with open(path, 'wt', encoding="utf8") as f:
            f.write(html)
    except Exception as e:
        print(e)


def getCode(param):
    if "sourceCode" in param:
        if isinstance(param["sourceCode"], int):
            param["sourceCode"] = str(param["sourceCode"])
        if param["sourceCode"] == '2':
            modelName = oy
        elif param["sourceCode"] == '1':
                modelName = mt
        elif param["sourceCode"] == '3':
            modelName = ot
        else:
            modelName = None
    else:
        modelName = None
    if "productCode" in param:
        if isinstance(param["productCode"], int):
            param["productCode"] = str(param["productCode"])
        if param["productCode"] == '0':
            productCode = "ALL"
        elif param["productCode"] == '1':
            productCode = duxi
        elif param["productCode"] == '2':
            productCode = duge
        elif param["productCode"] == '3':
            productCode = dugefumo
        else:
            productCode = None
    else:
        productCode = None
    if "page" in param:
        page = int(param["page"])
    else:
        page = 1
    return modelName, productCode, page


def query_single_record(param):
    modelName, productCode, page = getCode(param)
    if modelName != None and "packCode" in param:
        try:
            res = eval(modelName).objects.get(packCode=param["packCode"])
            return res
        except Exception as e:
            print("no packCode : ",param["packCode"])


def queryResult(param):
    modelName, productCode, page = getCode(param)
    timeStamp = dt.datetime.now().strftime("%y-%m-%d")
    if modelName != None and productCode != None:
        if productCode != "ALL":
            res = eval(modelName).objects.filter(~Q(qualityGrade__startswith="B"), businessTimes=timeStamp, productCode=productCode, onBusiness="1", )
            if not res:
                timeStamp = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%y-%m-%d")
                res = eval(modelName).objects.filter(~Q(qualityGrade__startswith="B"), businessTimes=timeStamp, productCode=productCode, onBusiness="1", )
        else:
            res = eval(modelName).objects.filter(~Q(qualityGrade__startswith="B"), businessTimes=timeStamp, onBusiness="1", )
            if not res:
                timeStamp = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%y-%m-%d")
                res = eval(modelName).objects.filter(~Q(qualityGrade__startswith="B"), businessTimes=timeStamp, onBusiness="1", )
        if not res:
            return "", 0
        begin = 0 + (page - 1) * MOUNTS
        end = page * MOUNTS
        if len(res) <= begin:
            if len(res) >= 20:
                end = len(res)
                begin = end - 20
            else:
                end = len(res)
                begin = 0
        elif begin < len(res) <= end:
            end = len(res)
        return res.order_by("basicPrice")[begin:end], len(res)


def updateProduct(obj, i, updateNum):
    num = 0
    if obj.publishDate != i["publishDate"]:
        obj.publishDate = i["publishDate"]
        num += 1
    if int(obj.publishPrice) != i["publishPrice"]:
        obj.publishPrice = i["publishPrice"]
        num += 1
    if int(obj.basicPrice) != i["basicPrice"]:
        obj.basicPrice = i["basicPrice"]
        num += 1
    if int(obj.basicPrice) != i["basicPrice"]:
        obj.basicPrice = i["basicPrice"]
        num += 1
    if obj.hasShop != i["hasShop"]:  # 是否竞拍
        obj.hasShop = i["hasShop"]
        num += 1
    if int(obj.onBusiness) != i["onBusiness"]:  # 是否正在营业
        obj.onBusiness = i["onBusiness"]
        num += 1
    if obj.bidBeginDate != i["bidBeginDate"]:
        obj.bidBeginDate = i["bidBeginDate"]
        num += 1
    if obj.bidEndDate != i["bidEndDate"]:
        obj.bidEndDate = i["bidEndDate"]
        num += 1
    if obj.warehouseName != i["warehouseName"]:
        obj.warehouseName = i["warehouseName"]
        num += 1
    if obj.storeCityName != i["storeCityName"]:
        obj.storeCityName = i["storeCityName"]
        num += 1
    timeStamp = dt.datetime.now().strftime("%y-%m-%d")
    if obj.businessTimes != timeStamp:
        obj.businessTimes = timeStamp
        num += 1
    obj.save()
    if num > 0:
        updateNum += 1
    return updateNum


def getContentType(ext):
    content_types = {
        "aiff": "audio/aiff",
        "anv": "application/x-anv",
        "asa": "text/asa",
        "asf": "video/x-ms-asf",
        "asp": "text/asp",
        "asx": "video/x-ms-asf",
        "au": "audio/basic",
        "avi": "video/avi",
        "awf": "application/vnd.adobe.workflow",
        "biz": "text/xml",
        "bmp": "application/x-bmp",
        "bot": "application/x-bot",
        "c4t": "application/x-c4t",
        "c90": "application/x-c90",
        "cal": "application/x-cals",
        "cat": "application/vnd.ms-pki.seccat",
        "cdf": "application/x-netcdf",
        "cdr": "application/x-cdr",
        "cel": "application/x-cel",
        "cer": "application/x-x509-ca-cert",
        "cg4": "application/x-g4",
        "cgm": "application/x-cgm",
        "cit": "application/x-cit",
        "class": "java/*",
        "cml": "text/xml:客户端浏览器按XML格式进行解析文档",
        "cmp": "application/x-cmp",
        "cmx": "application/x-cmx",
        "cot": "application/x-cot",
        "crl": "application/pkix-crl",
        "crt": "application/x-x509-ca-cert",
        "csi": "application/x-csi",
        "css": "text/css:客户端浏览器按CSS格式进行解析文档",
        "cut": "application/x-cut",
        "dbf": "application/x-dbf",
        "dbm": "application/x-dbm",
        "dbx": "application/x-dbx",
        "dcd": "text/xml:客户端浏览器按XML格式进行解析文档",
        "dcx": "application/x-dcx",
        "der": "application/x-x509-ca-cert",
        "dgn": "application/x-dgn",
        "dib": "application/x-dib",
        "dll": "application/x-msdownload",
        "doc": "application/msword",
        "dot": "application/msword",
        "drw": "application/x-drw",
        "dtd": "text/xml:客户端浏览器按XML格式进行解析文档",
        "dwf": "application/x-dwf",
        "dwg": "application/x-dwg",
        "dxb": "application/x-dxb",
        "dxf": "application/x-dxf",
        "edn": "application/vnd.adobe.edn",
        "emf": "application/x-emf",
        "eml": "message/rfc822",
        "ent": "text/xml:客户端浏览器按XML格式进行解析文档",
        "epi": "application/x-epi",
        "eps": "application/postscript",
        "etd": "application/x-ebx",
        "exe": "application/x-msdownload",
        "fax": "image/fax",
        "fdf": "application/vnd.fdf",
        "fif": "application/fractals",
        "fo": "text/xml:客户端浏览器按XML格式进行解析文档",
        "frm": "application/x-frm",
        "g4": "application/x-g4",
        "gbr": "application/x-gbr",
        "gcd": "application/x-gcd",
        "gif": "image/gif",
        "gl2": "application/x-gl2",
        "gp4": "application/x-gp4",
        "hgl": "application/x-hgl",
        "hmr": "application/x-hmr",
        "hpg": "application/x-hpgl",
        "hpl": "application/x-hpl",
        "hqx": "application/mac-binhex40",
        "hrf": "application/x-hrf",
        "hta": "application/hta",
        "htc": "text/x-component",
        "htm": "text/html:客户端浏览器按超文本格式进行解析文档",
        "html": "text/html:客户端浏览器按超文本格式进行解析文档",
        "htt": "text/webviewhtml",
        "htx": "text/html:客户端浏览器按超文本格式进行解析文档",
        "icb": "application/x-icb",
        "ico": "image/x-icon",
        "iff": "application/x-iff",
        "ig4": "application/x-g4",
        "igs": "application/x-igs",
        "iii": "application/x-iphone",
        "img": "application/x-img",
        "ins": "application/x-internet-signup",
        "isp": "application/x-internet-signup",
        "IVF": "video/x-ivf",
        "java": "java/*",
        "jfif": "image/jpeg",
        "jpe": "image/jpeg",
        "jpeg": "image/jpeg",
        "jpg": "image/jpeg",
        "js": "application/x-javascript",
        "jsp": "text/html:客户端浏览器按超文本格式进行解析文档",
        "la1": "audio/x-liquid-file",
        "lar": "application/x-laplayer-reg",
        "latex": "application/x-latex",
        "lavs": "audio/x-liquid-secure",
        "lbm": "application/x-lbm",
        "lmsff": "audio/x-la-lms",
        "ls": "application/x-javascript",
        "ltr": "application/x-ltr",
        "m1v": "video/x-mpeg",
        "m2v": "video/x-mpeg",
        "m3u": "audio/mpegurl",
        "m4e": "video/mpeg4",
        "mac": "application/x-mac",
        "man": "application/x-troff-man",
        "math": "text/xml",
        "mdb": "application/x-mdb",
        "mfp": "application/x-shockwave-flash",
        "mht": "message/rfc822",
        "mhtml": "message/rfc822",
        "mi": "application/x-mi",
        "mid": "audio/mid",
        "midi": "audio/mid",
        "mil": "application/x-mil",
        "mml": "text/xml",
        "mnd": "audio/x-musicnet-download",
        "mns": "audio/x-musicnet-stream",
        "mocha": "application/x-javascript",
        "movie": "video/x-sgi-movie",
        "mp1": "audio/mp1",
        "mp2": "audio/mp2",
        "mp2v": "video/mpeg",
        "mp3": "audio/mp3",
        "mp4": "video/mpeg4",
        "mpa": "video/x-mpg",
        "mpd": "application/vnd.ms-project",
        "mpe": "video/x-mpeg",
        "mpeg": "video/mpg",
        "mpg": "video/mpg",
        "mpga": "audio/rn-mpeg",
        "mpp": "application/vnd.ms-project",
        "mps": "video/x-mpeg",
        "mpt": "application/vnd.ms-project",
        "mpv": "video/mpg",
        "mpv2": "video/mpeg",
        "mpw": "application/vnd.ms-project",
        "mpx": "application/vnd.ms-project",
        "mtx": "text/xml",
        "mxp": "application/x-mmxp",
        "net": "image/pnetvue",
        "nrf": "application/x-nrf",
        "nws": "message/rfc822",
        "odc": "text/x-ms-odc",
        "out": "application/x-out",
        "p10": "application/pkcs10",
        "p12": "application/x-pkcs12",
        "p7b": "application/x-pkcs7-certificates",
        "p7c": "application/pkcs7-mime",
        "p7m": "application/pkcs7-mime",
        "p7r": "application/x-pkcs7-certreqresp",
        "p7s": "application/pkcs7-signature",
        "pc5": "application/x-pc5",
        "pci": "application/x-pci",
        "pcl": "application/x-pcl",
        "pcx": "application/x-pcx",
        "pdf": "application/pdf",
        "pdx": "application/vnd.adobe.pdx",
        "pfx": "application/x-pkcs12",
        "pgl": "application/x-pgl",
        "pic": "application/x-pic",
        "pko": "application/vnd.ms-pki.pko",
        "pl": "application/x-perl",
        "plg": "text/html",
        "pls": "audio/scpls",
        "plt": "application/x-plt",
        "png": "image/png",
        "pot": "application/vnd.ms-powerpoint",
        "ppa": "application/vnd.ms-powerpoint",
        "ppm": "application/x-ppm",
        "pps": "application/vnd.ms-powerpoint",
        "ppt": "application/x-ppt",
        "pr": "application/x-pr",
        "prf": "application/pics-rules",
        "prn": "application/x-prn",
        "prt": "application/x-prt",
        "ps": "application/x-ps",
        "ptn": "application/x-ptn",
        "pwz": "application/vnd.ms-powerpoint",
        "r3t": "text/vnd.rn-realtext3d",
        "ra": "audio/vnd.rn-realaudio",
        "ram": "audio/x-pn-realaudio",
        "ras": "application/x-ras",
        "rat": "application/rat-file",
        "rdf": "text/xml",
        "rec": "application/vnd.rn-recording",
        "red": "application/x-red",
        "rgb": "application/x-rgb",
        "rjs": "application/vnd.rn-realsystem-rjs",
        "rjt": "application/vnd.rn-realsystem-rjt",
        "rlc": "application/x-rlc",
        "rle": "application/x-rle",
        "rm": "application/vnd.rn-realmedia",
        "rmf": "application/vnd.adobe.rmf",
        "rmi": "audio/mid",
        "rmj": "application/vnd.rn-realsystem-rmj",
        "rmm": "audio/x-pn-realaudio",
        "rmp": "application/vnd.rn-rn_music_package",
        "rms": "application/vnd.rn-realmedia-secure",
        "rmvb": "application/vnd.rn-realmedia-vbr",
        "rmx": "application/vnd.rn-realsystem-rmx",
        "rnx": "application/vnd.rn-realplayer",
        "rp": "image/vnd.rn-realpix",
        "rpm": "audio/x-pn-realaudio-plugin",
        "rsml": "application/vnd.rn-rsml",
        "rt": "text/vnd.rn-realtext",
        "rtf": "application/x-rtf",
        "rv": "video/vnd.rn-realvideo",
        "sam": "application/x-sam",
        "sat": "application/x-sat",
        "sdp": "application/sdp",
        "sdw": "application/x-sdw",
        "sit": "application/x-stuffit",
        "slb": "application/x-slb",
        "sld": "application/x-sld",
        "slk": "drawing/x-slk",
        "smi": "application/smil",
        "smil": "application/smil",
        "smk": "application/x-smk",
        "snd": "audio/basic",
        "sol": "text/plain",
        "sor": "text/plain",
        "spc": "application/x-pkcs7-certificates",
        "spl": "application/futuresplash",
        "spp": "text/xml",
        "ssm": "application/streamingmedia",
        "sst": "application/vnd.ms-pki.certstore",
        "stl": "application/vnd.ms-pki.stl",
        "stm": "text/html",
        "sty": "application/x-sty",
        "svg": "text/xml",
        "swf": "application/x-shockwave-flash:客户端浏览器按Flash格式进行解析文档",
        "tdf": "application/x-tdf",
        "tg4": "application/x-tg4",
        "tga": "application/x-tga",
        "tif": "image/tiff",
        "tiff": "image/tiff",
        "tld": "text/xml",
        "top": "drawing/x-top",
        "torrent": "application/x-bittorrent",
        "tsd": "text/xml",
        "txt": "text/plain:客户端浏览器按纯文本格式进行解析文档",
        "uin": "application/x-icq",
        "uls": "text/iuls",
        "vcf": "text/x-vcard",
        "vda": "application/x-vda",
        "vdx": "application/vnd.visio",
        "vml": "text/xml",
        "vpg": "application/x-vpeg005",
        "vsd": "application/x-vsd",
        "vss": "application/vnd.visio",
        "vst": "application/x-vst",
        "vsw": "application/vnd.visio",
        "vsx": "application/vnd.visio",
        "vtx": "application/vnd.visio",
        "vxml": "text/xml",
        "wav": "audio/wav",
        "wax": "audio/x-ms-wax",
        "wb1": "application/x-wb1",
        "wb2": "application/x-wb2",
        "wb3": "application/x-wb3",
        "wbmp": "image/vnd.wap.wbmp",
        "wiz": "application/msword",
        "wk3": "application/x-wk3",
        "wk4": "application/x-wk4",
        "wkq": "application/x-wkq",
        "wks": "application/x-wks",
        "wm": "video/x-ms-wm",
        "wma": "audio/x-ms-wma",
        "wmd": "application/x-ms-wmd",
        "wmf": "application/x-wmf",
        "wml": "text/vnd.wap.wml",
        "wmv": "video/x-ms-wmv",
        "wmx": "video/x-ms-wmx",
        "wmz": "application/x-ms-wmz",
        "wp6": "application/x-wp6",
        "wpd": "application/x-wpd",
        "wpg": "application/x-wpg",
        "wpl": "application/vnd.ms-wpl",
        "wq1": "application/x-wq1",
        "wr1": "application/x-wr1",
        "wri": "application/x-wri",
        "wrk": "application/x-wrk",
        "ws": "application/x-ws",
        "ws2": "application/x-ws",
        "wsc": "text/scriptlet",
        "wsdl": "text/xml",
        "wvx": "video/x-ms-wvx",
        "xdp": "application/vnd.adobe.xdp",
        "xdr": "text/xml",
        "xfd": "application/vnd.adobe.xfd",
        "xfdf": "application/vnd.adobe.xfdf",
        "xhtml": "text/html",
        "xls": "application/x-xls",
        "xlw": "application/x-xlw",
        "xml": "text/xml",
        "xpl": "audio/scpls",
        "xq": "text/xml",
        "xql": "text/xml",
        "xquery": "text/xml",
        "xsd": "text/xml",
        "xsl": "text/xml",
        "xslt": "text/xml",
        "xwd": "application/x-xwd",
        "x_b": "application/x-x_b",
        "x_t": "application/x-x_t",
        "default": "application/octet-stream",

    }
    if ext in content_types:
        return content_types[ext]
    return content_types["default"]
