from pandac.libpandaexpressModules import *
import string
import types
try:
    language = getConfigExpress().GetString('language', 'portuguese')
    checkLanguage = getConfigExpress().GetBool('check-language', 0)
except:
    language = simbase.config.GetString('language', 'portuguese')
    checkLanguage = simbase.config.GetBool("check-language", 0)

def getLanguage():
    return language
    
print ('OTPLocalizer: Running in language: %s' % (language)
if language == "english":
    _languageModule = "otp.otpbase.OTPLocalizer" + string.capitalize(language)
else:
    checkLanguage = 1
    _languageModule = "otp.otpbase.OTPLocalizer_" + language
print('from ' + _languageModule + ' import *')
exec('from ' + _languageModule + ' import *')
if checkLanguage:
    l = {}
    g = {}
    englishModule = __import__('otp.otpbase.OTPLocalizer_portuguese', g, l)
    foreignModule = __import__(_languageModule, g, l)
    for key, val in englishModule.__dict__.items():
        if not foreignModule.__dict__.has_key(key):
            print ('WARNING: Foreign module: %s missing key: %s' % (_languageModule, key))
            locals()[key] = val
        else:
            if isinstance(val, types.DictType):
                fval = foreignModule.__dict__.get(key)
                for dkey, dval in val.items():
                    if not fval.has_key(dkey):
                        print ('WARNING: Foreign module: %s missing key: %s.%s' % (_languageModule, key, dkey))
                        fval[dkey] = dval
                      
                for dkey in fval.keys():
                    if not val.has_key(dkey):
                        print ('WARNING: Foreign module: %s extra key: %s.%s' % (_languageModule, key, dkey))
                  
    for key in foreignModule.__dict__.keys():
        if not englishModule.__dict__.has_key(key):
            print ('WARNING: Foreign module: %s extra key: %s' % (_languageModule, key))
