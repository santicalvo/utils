# -*- coding: utf-8 -*-
import keys
dic={ u"á":u"aCute", u"é":u"eCute", u"í":u"iCute", u"ó":u"oCute", u"ú":u"uCute",
      u"Á":u"ACute", u"É":u"ECute", u"Í":u"ICute", u"Ó":u"OCute", u"Ú":u"UCute",
      u"à":u"aLCute", u"è":u"eLCute", u"ì":u"iLCute", u"ò":u"oLCute", u"ù":u"uLCute",
      u"À":u"ALCute", u"È":u"ELCute", u"Ì":u"ILCute", u"Ò":u"OLCute", u"Ù":u"ULCute",
      u"ñ":u"nTILDE", u"Ñ":u"NTILDE",
      ".": "dDOT",
      ",": "cCOMMA",
      ":": "cCOLON",
      ";": "cSEMICOLON",
      "/": "bSLASH",
      "\\": "bBACKSLASH",
      u"º":u"oDEGREE", " ":"_"}

def replace_spanish_alphabet(str, real=False):
    chars = dict (zip(dic.values(),dic.keys())) if real else dic
    new_str = unicode(str, "utf-8") if not isinstance(str, unicode) else str
    for valueSearch, valueReplace in chars.iteritems():
        new_str = new_str.replace(valueSearch, valueReplace)
    return new_str

if __name__=='__main__':
    reversed = []
    reversed_back = []
    for txt in keys.txts:
        reversed.append(replace_spanish_alphabet(txt))

    for txt in reversed:
        reversed_back.append(replace_spanish_alphabet(txt, True))

    print reversed
    print "------------------------"
    for v in reversed_back:
        print v



