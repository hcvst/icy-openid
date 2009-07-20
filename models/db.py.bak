# -*- coding: utf-8 -*-
#########################################################################
try:
    from gluon.contrib.gql import *  # if running on Google App Engine
except:
    db = SQLDB('sqlite://storage.db')  # if not, use SQLite or other DB
else:
    db = GQLDB()  # connect to Google BigTable
    session.connect(request, response, db=db)  # and store sessions there
    # or use the following lines to store sessions in Memcache
    #from gluon.contrib.memdb import MEMDB
    #from google.appengine.api.memcache import Client
    #session.connect(request, response, db=MEMDB(Client()))

# OID Config Parameters
SSL = False
DEFAULT_COUNTRY = 'ZA'
DEFAULT_LANG = 'en'
DEFAULT_TIMEZONE = 'Africa/Johannesburg'

# you do not have to edit the following paramters
if SSL: 
    PROTO='https' 
else: 
    PROTO='http'
APP_BASE = "%s/%s" % (request.env.http_host, request.application)
OID_SERVER =  PROTO + "://%s/server" % APP_BASE
OID_DELEGATION_BASE = PROTO + "://%s/identity/profile/" % APP_BASE
OID_XRDS_BASE = PROTO + "://%s/identity/xrds/" % APP_BASE
OID_XRDS = """
<xrds:XRDS
  xmlns:xrds="xri://$xrds"
  xmlns:openid="http://openid.net/xmlns/1.0"
  xmlns="xri://$xrd*($v*2.0)">
  <XRD>
    <Service priority="1">
      <Type>http://openid.net/signon/1.0</Type>
      <URI>%s</URI>
      <openid:Delegate>%s</openid:Delegate>
    </Service>
  </XRD>
</xrds:XRDS>"""

COUNTRYCODES = {"AF":"Afghanistan", "AX":"Åland Islands", "AL":"Albania", "DZ":"Algeria", "AS":"American Samoa", "AD":"Andorra", "AO":"Angola", "AI":"Anguilla", "AQ":"Antarctica", "AG":"Antigua And Barbuda", "AR":"Argentina", "AM":"Armenia", "AW":"Aruba", "AU":"Australia", "AT":"Austria", "AZ":"Azerbaijan", "BS":"Bahamas", "BH":"Bahrain", "BD":"Bangladesh", "BB":"Barbados", "BY":"Belarus", "BE":"Belgium", "BZ":"Belize", "BJ":"Benin", "BM":"Bermuda", "BT":"Bhutan", "BO":"Bolivia, Plurinational State Of", "BA":"Bosnia And Herzegovina", "BW":"Botswana", "BV":"Bouvet Island", "BR":"Brazil", "IO":"British Indian Ocean Territory", "BN":"Brunei Darussalam", "BG":"Bulgaria", "BF":"Burkina Faso", "BI":"Burundi", "KH":"Cambodia", "CM":"Cameroon", "CA":"Canada", "CV":"Cape Verde", "KY":"Cayman Islands", "CF":"Central African Republic", "TD":"Chad", "CL":"Chile", "CN":"China", "CX":"Christmas Island", "CC":"Cocos (Keeling) Islands", "CO":"Colombia", "KM":"Comoros", "CG":"Congo", "CD":"Congo, The Democratic Republic Of The", "CK":"Cook Islands", "CR":"Costa Rica", "CI":"Côte d'Ivoire", "HR":"Croatia", "CU":"Cuba", "CY":"Cyprus", "CZ":"Czech Republic", "DK":"Denmark", "DJ":"Djibouti", "DM":"Dominica", "DO":"Dominican Republic", "EC":"Ecuador", "EG":"Egypt", "SV":"El Salvador", "GQ":"Equatorial Guinea", "ER":"Eritrea", "EE":"Estonia", "ET":"Ethiopia", "FK":"Falkland Islands (Malvinas)", "FO":"Faroe Islands", "FJ":"Fiji", "FI":"Finland", "FR":"France", "GF":"French Guiana", "PF":"French Polynesia", "TF":"French Southern Territories", "GA":"Gabon", "GM":"Gambia", "GE":"Georgia", "DE":"Germany", "GH":"Ghana", "GI":"Gibraltar", "GR":"Greece", "GL":"Greenland", "GD":"Grenada", "GP":"Guadeloupe", "GU":"Guam", "GT":"Guatemala", "GG":"Guernsey", "GN":"Guinea", "GW":"Guinea-Bissau", "GY":"Guyana", "HT":"Haiti", "HM":"Heard Island And Mcdonald Islands", "VA":"Holy See (Vatican City State)", "HN":"Honduras", "HK":"Hong Kong", "HU":"Hungary", "IS":"Iceland", "IN":"India", "ID":"Indonesia", "IR":"Iran, Islamic Republic Of", "IQ":"Iraq", "IE":"Ireland", "IM":"Isle Of Man", "IL":"Israel", "IT":"Italy", "JM":"Jamaica", "JP":"Japan", "JE":"Jersey", "JO":"Jordan", "KZ":"Kazakhstan", "KE":"Kenya", "KI":"Kiribati", "KP":"Korea, Democratic People's Republic Of", "KR":"Korea, Republic Of", "KW":"Kuwait", "KG":"Kyrgyzstan", "LA":"Lao People's Democratic Republic", "LV":"Latvia", "LB":"Lebanon", "LS":"Lesotho", "LR":"Liberia", "LY":"Libyan Arab Jamahiriya", "LI":"Liechtenstein", "LT":"Lithuania", "LU":"Luxembourg", "MO":"Macao", "MK":"Macedonia, The Former Yugoslav Republic Of", "MG":"Madagascar", "MW":"Malawi", "MY":"Malaysia", "MV":"Maldives", "ML":"Mali", "MT":"Malta", "MH":"Marshall Islands", "MQ":"Martinique", "MR":"Mauritania", "MU":"Mauritius", "YT":"Mayotte", "MX":"Mexico", "FM":"Micronesia, Federated States Of", "MD":"Moldova, Republic Of", "MC":"Monaco", "MN":"Mongolia", "ME":"Montenegro", "MS":"Montserrat", "MA":"Morocco", "MZ":"Mozambique", "MM":"Myanmar", "NA":"Namibia", "NR":"Nauru", "NP":"Nepal", "NL":"Netherlands", "AN":"Netherlands Antilles", "NC":"New Caledonia", "NZ":"New Zealand", "NI":"Nicaragua", "NE":"Niger", "NG":"Nigeria", "NU":"Niue", "NF":"Norfolk Island", "MP":"Northern Mariana Islands", "NO":"Norway", "OM":"Oman", "PK":"Pakistan", "PW":"Palau", "PS":"Palestinian Territory, Occupied", "PA":"Panama", "PG":"Papua New Guinea", "PY":"Paraguay", "PE":"Peru", "PH":"Philippines", "PN":"Pitcairn", "PL":"Poland", "PT":"Portugal", "PR":"Puerto Rico", "QA":"Qatar", "RE":"Réunion", "RO":"Romania", "RU":"Russian Federation", "RW":"Rwanda", "BL":"Saint Barthélemy", "SH":"Saint Helena", "KN":"Saint Kitts And Nevis", "LC":"Saint Lucia", "MF":"Saint Martin", "PM":"Saint Pierre And Miquelon", "VC":"Saint Vincent And The Grenadines", "WS":"Samoa", "SM":"San Marino", "ST":"Sao Tome And Principe", "SA":"Saudi Arabia", "SN":"Senegal", "RS":"Serbia", "SC":"Seychelles", "SL":"Sierra Leone", "SG":"Singapore", "SK":"Slovakia", "SI":"Slovenia", "SB":"Solomon Islands", "SO":"Somalia", "ZA":"South Africa", "GS":"South Georgia And The South Sandwich Islands", "ES":"Spain", "LK":"Sri Lanka", "SD":"Sudan", "SR":"Suriname", "SJ":"Svalbard And Jan Mayen", "SZ":"Swaziland", "SE":"Sweden", "CH":"Switzerland", "SY":"Syrian Arab Republic", "TW":"Taiwan, Province Of China", "TJ":"Tajikistan", "TZ":"Tanzania, United Republic Of", "TH":"Thailand", "TL":"Timor-Leste", "TG":"Togo", "TK":"Tokelau", "TO":"Tonga", "TT":"Trinidad And Tobago", "TN":"Tunisia", "TR":"Turkey", "TM":"Turkmenistan", "TC":"Turks And Caicos Islands", "TV":"Tuvalu", "UG":"Uganda", "UA":"Ukraine", "AE":"United Arab Emirates", "GB":"United Kingdom", "US":"United States", "UM":"United States Minor Outlying Islands", "UY":"Uruguay", "UZ":"Uzbekistan", "VU":"Vanuatu", "VE":"Venezuela, Bolivarian Republic Of", "VN":"Viet Nam", "VG":"Virgin Islands, British", "VI":"Virgin Islands, U.S.", "WF":"Wallis And Futuna", "EH":"Western Sahara", "YE":"Yemen", "ZM":"Zambia", "ZW":"Zimbabw"}
LANGCODES = {"aa":"Afar", "ab":"Abkhazian", "ae":"Avestan", "af":"Afrikaans", "ak":"Akan", "am":"Amharic", "an":"Aragonese", "ar":"Arabic", "as":"Assamese", "av":"Avaric", "ay":"Aymara", "az":"Azerbaijani", "ba":"Bashkir", "be":"Belarusian", "bg":"Bulgarian", "bh":"Bihari", "bi":"Bislama", "bm":"Bambara", "bn":"Bengali", "bo":"Tibetan", "br":"Breton", "bs":"Bosnian", "ca":"Catalan", "ce":"Chechen", "ch":"Chamorro", "co":"Corsican", "cr":"Cree", "cs":"Czech", "cu":"Church Slavic", "cv":"Chuvash", "cy":"Welsh", "da":"Danish", "de":"German", "dv":"Divehi", "dz":"Dzongkha", "ee":"Ewe", "el":"Greek", "en":"English", "eo":"Esperanto", "es":"Spanish", "et":"Estonian", "eu":"Basque", "fa":"Persian", "ff":"Fulah", "fi":"Finnish", "fj":"Fijian", "fo":"Faroese", "fr":"French", "fy":"Western Frisian", "ga":"Irish", "gd":"Scottish Gaelic", "gl":"Galician", "gn":"Guaraní", "gu":"Gujarati", "gv":"Manx", "ha":"Hausa", "he":"Hebrew", "hi":"Hindi", "ho":"Hiri Motu", "hr":"Croatian", "ht":"Haitian", "hu":"Hungarian", "hy":"Armenian", "hz":"Herero", "ia":"Interlingu", "id":"Indonesian", "ie":"Interlingue", "ig":"Igbo", "ii":"Sichuan Yi", "ik":"Inupiaq", "io":"Ido", "is":"Icelandic", "it":"Italian", "iu":"Inuktitut", "ja":"Japanese", "jv":"Javanese", "ka":"Georgian", "kg":"Kongo", "ki":"Kikuyu", "kj":"Kwanyama", "kk":"Kazakh", "kl":"Kalaallisut", "km":"Khmer", "kn":"Kannada", "ko":"Korean", "kr":"Kanuri", "ks":"Kashmiri", "ku":"Kurdish", "kv":"Komi", "kw":"Cornish", "ky":"Kirghiz", "la":"Latin", "lb":"Luxembourgish", "lg":"Ganda", "li":"Limburgish", "ln":"Lingala", "lo":"Lao", "lt":"Lithuanian", "lu":"Luba-Katanga", "lv":"Latvian", "mg":"Malagasy", "mh":"Marshallese", "mi":"Māori", "mk":"Macedonian", "ml":"Malayalam", "mn":"Mongolian", "mr":"Marathi", "ms":"Malay", "mt":"Maltese", "my":"Burmese", "na":"Nauru", "nb":"Norwegian Bokmål", "nd":"North Ndebele", "ne":"Nepali", "ng":"Ndonga", "nl":"Dutch", "nn":"Norwegian Nynorsk", "no":"Norwegian", "nr":"South Ndebele", "nv":"Navajo", "ny":"Chichewa", "oc":"Occitan", "oj":"Ojibwa", "om":"Oromo", "or":"Oriya", "os":"Ossetian", "pa":"Panjabi", "pi":"Pāli", "pl":"Polish", "ps":"Pashto", "pt":"Portuguese", "qu":"Quechua", "rm":"Raeto-Romance", "rn":"Kirundi", "ro":"Romanian", "ru":"Russian", "rw":"Kinyarwanda", "sa":"Sanskrit", "sc":"Sardinian", "sd":"Sindhi", "se":"Northern Sami", "sg":"Sango", "si":"Sinhala", "sk":"Slovak", "sl":"Slovenian", "sm":"Samoan", "sn":"Shona", "so":"Somali", "sq":"Albanian", "sr":"Serbian", "ss":"Swati", "st":"Southern Sotho", "su":"Sundanese", "sv":"Swedish", "sw":"Swahili", "ta":"Tamil", "te":"Telugu", "tg":"Tajik", "th":"Thai", "ti":"Tigrinya", "tk":"Turkmen", "tl":"Tagalog", "tn":"Tswana", "to":"Tonga", "tr":"Turkish", "ts":"Tsonga", "tt":"Tatar", "tw":"Twi", "ty":"Tahitian", "ug":"Uighur", "uk":"Ukrainian", "ur":"Urdu", "uz":"Uzbek", "ve":"Venda", "vi":"Vietnamese", "vo":"Volapük", "wa":"Walloon", "wo":"Wolof", "xh":"Xhosa", "yi":"Yiddish", "yo":"Yoruba", "za":"Zhuang", "zh":"Chinese", "zu":"Zulu"}
TIMEZONES = ["Africa/Abidjan", "Africa/Accra", "Africa/Addis_Ababa", "Africa/Algiers", "Africa/Asmara", "Africa/Bamako", "Africa/Bangui", "Africa/Banjul", "Africa/Bissau", "Africa/Blantyre", "Africa/Brazzaville", "Africa/Bujumbura", "Africa/Cairo", "Africa/Casablanca", "Africa/Ceuta", "Africa/Conakry", "Africa/Dakar", "Africa/Dar_es_Salaam", "Africa/Djibouti", "Africa/Douala", "Africa/El_Aaiun", "Africa/Freetown", "Africa/Gaborone", "Africa/Harare", "Africa/Johannesburg", "Africa/Kampala", "Africa/Khartoum", "Africa/Kigali", "Africa/Kinshasa", "Africa/Lagos", "Africa/Libreville", "Africa/Lome", "Africa/Luanda", "Africa/Lubumbashi", "Africa/Lusaka", "Africa/Malabo", "Africa/Maputo", "Africa/Maseru", "Africa/Mbabane", "Africa/Mogadishu", "Africa/Monrovia", "Africa/Nairobi", "Africa/Ndjamena", "Africa/Niamey", "Africa/Nouakchott", "Africa/Ouagadougou", "Africa/Porto-Novo", "Africa/Sao_Tome", "Africa/Tripoli", "Africa/Tunis", "Africa/Windhoek", "America/Adak", "America/Anchorage", "America/Anguilla", "America/Antigua", "America/Araguaina", "America/Argentina/Buenos_Aires", "America/Argentina/Catamarca", "America/Argentina/Cordoba", "America/Argentina/Jujuy", "America/Argentina/La_Rioja", "America/Argentina/Mendoza", "America/Argentina/Rio_Gallegos", "America/Argentina/Salta", "America/Argentina/San_Juan", "America/Argentina/San_Luis", "America/Argentina/Tucuman", "America/Argentina/Ushuaia", "America/Aruba", "America/Asuncion", "America/Atikokan", "America/Bahia", "America/Barbados", "America/Belem", "America/Belize", "America/Blanc-Sablon", "America/Boa_Vista", "America/Bogota", "America/Boise ", "America/Cambridge_Bay", "America/Campo_Grande", "America/Cancun", "America/Caracas", "America/Cayenne", "America/Cayman", "America/Chicago", "America/Chihuahua", "America/Costa_Rica", "America/Cuiaba", "America/Curacao", "America/Danmarkshavn", "America/Dawson", "America/Dawson_Creek", "America/Denver", "America/Detroit", "America/Dominica", "America/Edmonton", "America/Eirunepe", "America/El_Salvador", "America/Fortaleza", "America/Glace_Bay", "America/Godthab", "America/Goose_Bay", "America/Grand_Turk", "America/Grenada", "America/Guadeloupe", "America/Guatemala", "America/Guayaquil", "America/Guyana", "America/Halifax", "America/Havana", "America/Hermosillo", "America/Indiana/Indianapolis", "America/Indiana/Knox", "America/Indiana/Marengo", "America/Indiana/Petersburg", "America/Indiana/Tell_City", "America/Indiana/Vevay", "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Inuvik", "America/Iqaluit", "America/Jamaica", "America/Juneau", "America/Kentucky/Louisville", "America/Kentucky/Monticello", "America/La_Paz", "America/Lima", "America/Los_Angeles", "America/Maceio", "America/Managua", "America/Manaus", "America/Marigot", "America/Martinique", "America/Mazatlan", "America/Menominee", "America/Merida", "America/Mexico_City", "America/Miquelon", "America/Moncton", "America/Monterrey", "America/Montevideo", "America/Montreal", "America/Montserrat", "America/Nassau", "America/New_York", "America/Nipigon", "America/Nome", "America/Noronha", "America/North_Dakota/Center", "America/North_Dakota/New_Salem", "America/Panama", "America/Pangnirtung", "America/Paramaribo", "America/Phoenix", "America/Port-au-Prince", "America/Port_of_Spain", "America/Porto_Velho", "America/Puerto_Rico", "America/Rainy_River", "America/Rankin_Inlet", "America/Recife", "America/Regina", "America/Resolute", "America/Rio_Branco", "America/Santarem", "America/Santiago", "America/Santo_Domingo", "America/Sao_Paulo", "America/Scoresbysund", "America/Shiprock", "America/St_Barthelemy", "America/St_Johns", "America/St_Kitts", "America/St_Lucia", "America/St_Thomas", "America/St_Vincent", "America/Swift_Current", "America/Tegucigalpa", "America/Thule", "America/Thunder_Bay", "America/Tijuana", "America/Toronto", "America/Tortola", "America/Vancouver", "America/Whitehorse", "America/Winnipeg", "America/Yakutatk", "America/Yellowknife", "Antarctica/Casey", "Antarctica/Davis", "Antarctica/DumontDUrville", "Antarctica/Mawson", "Antarctica/McMurdo", "Antarctica/Palmer", "Antarctica/Rothera", "Antarctica/South_Pole", "Antarctica/Syowa", "Antarctica/Vostok", "Arctic/Longyearbyen", "Asia/Aden", "Asia/Almaty", "Asia/Amman", "Asia/Anadyr", "Asia/Aqtau", "Asia/Aqtobe", "Asia/Ashgabat", "Asia/Baghdad", "Asia/Bahrain", "Asia/Baku", "Asia/Bangkok", "Asia/Beirut", "Asia/Bishkek", "Asia/Brunei", "Asia/Choibalsan", "Asia/Chongqing", "Asia/Colombo", "Asia/Damascus", "Asia/Dhaka", "Asia/Dili", "Asia/Dubai", "Asia/Dushanbe", "Asia/Gaza", "Asia/Harbin", "Asia/Ho_Chi_Minh", "Asia/Hong_Kong", "Asia/Hovd", "Asia/Irkutsk", "Asia/Jakarta", "Asia/Jayapura", "Asia/Jerusalem", "Asia/Kabul", "Asia/Kamchatka", "Asia/Karachi", "Asia/Kashgar", "Asia/Kathmandu", "Asia/Kolkata", "Asia/Krasnoyarsk", "Asia/Kuala_Lumpur", "Asia/Kuching", "Asia/Kuwait", "Asia/Macau", "Asia/Magadan", "Asia/Makassar", "Asia/Manila", "Asia/Muscat", "Asia/Nicosia", "Asia/Novosibirsk", "Asia/Omsk", "Asia/Oral", "Asia/Phnom_Penh", "Asia/Pontianak", "Asia/Pyongyang", "Asia/Qatar", "Asia/Qyzylorda", "Asia/Rangoon", "Asia/Riyadh", "Asia/Sakhalin", "Asia/Samarkand", "Asia/Seoul", "Asia/Shanghai", "Asia/Singapore", "Asia/Taipei", "Asia/Tashkent", "Asia/Tbilisi", "Asia/Tehran", "Asia/Thimphu", "Asia/Tokyo", "Asia/Ulaanbaatar", "Asia/Urumqi", "Asia/Vientiane", "Asia/Vladivostok", "Asia/Yakutsk", "Asia/Yekaterinburg", "Asia/Yerevan", "Atlantic/Azores", "Atlantic/Bermuda", "Atlantic/Canary", "Atlantic/Cape_Verde", "Atlantic/Faroe", "Atlantic/Madeira", "Atlantic/Reykjavik", "Atlantic/South_Georgia", "Atlantic/St_Helena", "Atlantic/Stanley", "Australia/Adelaide", "Australia/Brisbane", "Australia/Broken_Hill", "Australia/Currie", "Australia/Darwin", "Australia/Eucla", "Australia/Hobart", "Australia/Lindeman", "Australia/Lord_Howe", "Australia/Melbourne", "Australia/Perth", "Australia/Sydney", "Europe/Amsterdam", "Europe/Andorra", "Europe/Athens", "Europe/Belgrade", "Europe/Berlin", "Europe/Bratislava", "Europe/Brussels", "Europe/Bucharest", "Europe/Budapest", "Europe/Chisinau", "Europe/Copenhagen", "Europe/Dublin", "Europe/Gibraltar", "Europe/Guernsey", "Europe/Helsinki", "Europe/Isle_of_Man", "Europe/Istanbul", "Europe/Jersey", "Europe/Kaliningrad", "Europe/Kiev", "Europe/Lisbon", "Europe/Ljubljana", "Europe/London", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta", "Europe/Mariehamn", "Europe/Minsk", "Europe/Monaco", "Europe/Moscow", "Europe/Oslo", "Europe/Paris", "Europe/Podgorica", "Europe/Prague", "Europe/Riga", "Europe/Rome", "Europe/Samara", "Europe/San_Marino", "Europe/Sarajevo", "Europe/Simferopol", "Europe/Skopje", "Europe/Sofia", "Europe/Stockholm", "Europe/Tallinn", "Europe/Tirane", "Europe/Uzhgorod", "Europe/Vaduz", "Europe/Vatican", "Europe/Vienna", "Europe/Vilnius", "Europe/Volgograd", "Europe/Warsaw", "Europe/Zagreb", "Europe/Zaporozhye", "Europe/Zurich", "Indian/Antananarivo", "Indian/Chagos", "Indian/Christmas", "Indian/Cocos", "Indian/Comoro", "Indian/Kerguelen", "Indian/Mahe", "Indian/Maldives", "Indian/Mauritius", "Indian/Mayotte", "Indian/Reunion", "Pacific/Apia", "Pacific/Auckland", "Pacific/Chatham", "Pacific/Easter", "Pacific/Efate", "Pacific/Enderbury", "Pacific/Fakaofo", "Pacific/Fiji", "Pacific/Funafuti", "Pacific/Galapagos", "Pacific/Gambier", "Pacific/Guadalcanal", "Pacific/Guam", "Pacific/Honolulu", "Pacific/Johnston", "Pacific/Kiritimati", "Pacific/Kosrae", "Pacific/Kwajalein", "Pacific/Majuro", "Pacific/Marquesas", "Pacific/Midway", "Pacific/Nauru", "Pacific/Niue", "Pacific/Norfolk", "Pacific/Noumea", "Pacific/Pago_Pago", "Pacific/Palau", "Pacific/Pitcairn", "Pacific/Ponape", "Pacific/Port_Moresby", "Pacific/Rarotonga", "Pacific/Saipan", "Pacific/Tahiti", "Pacific/Tarawa", "Pacific/Tongatapu", "Pacific/Truk", "Pacific/Wake", "Pacific/Wallis"]

# OpenID tables
db.define_table('oid_associations', 
                SQLField('server_url', 'string', length=2047, required=True),
                SQLField('handle', 'string', length=255, required=True),
                SQLField('secret', 'blob', required=True),
                SQLField('issued', 'integer', required=True),
                SQLField('lifetime', 'integer', required=True),
                SQLField('assoc_type', 'string', length=64, required=True)
               )
                                    
db.define_table('oid_nonces', 
                SQLField('server_url', 'string', length=2047, required=True),
                SQLField('timestamp', 'integer', required=True),
                SQLField('salt', 'string', length=40, required=True)
               )
                             
db.define_table('oid_users',
                SQLField('nickname', label='Username', unique=True,
                         requires=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'oid_users.nickname', error_message='This name is already taken.'), 
                         IS_MATCH(r'^[a-z0-9]+$', error_message='Usernames have to be alphanumeric and lowercase')]),
                SQLField('oid_name', readable=False, writable=False, unique=True),
                SQLField('first_name', required=True, length=128, default='',  requires=IS_NOT_EMPTY()),
                SQLField('last_name', required=True, length=128, default='', requires=IS_NOT_EMPTY()),
                SQLField('email', length=128, default='', requires=[IS_EMAIL(), IS_NOT_IN_DB(db, 'oid_users.email')]),
                SQLField('password', 'password', default='', readable=False, requires=[CRYPT(), IS_NOT_EMPTY()]),
                SQLField('registration_key', length=128, writable=False, readable=False, default=''),
                SQLField('dob', 'date', label='Date of birth', required=False, default='', requires=None, comment='optional ex: 1975-09-20'),
                SQLField('gender',requires=IS_IN_SET(['', 'M', 'F']), comment='optional'),
                SQLField('postcode', comment='optional'),
                SQLField('country', default=DEFAULT_COUNTRY, requires=IS_IN_DB(db,'oid_country_codes.code','oid_country_codes.country')),
                SQLField('language', default=DEFAULT_LANG, requires=IS_IN_DB(db,'oid_lang_codes.code','oid_lang_codes.language')),
                SQLField('timezone', default=DEFAULT_TIMEZONE, requires=IS_IN_DB(db,'oid_timezones.timezone'))
               ) 
               
db.define_table('oid_trust',
                SQLField('auth_user', db.oid_users),
                SQLField('trust_root', 'string', length=2047)
               )
                           
db.define_table('oid_country_codes', SQLField('code', length=2, unique=True), SQLField('country'))
db.define_table('oid_lang_codes', SQLField('code', length=2, unique=True), SQLField('language'))
db.define_table('oid_timezones', SQLField('timezone'))

def db_init():
    db.oid_country_codes.truncate()
    db.oid_lang_codes.truncate()
    db.oid_timezones.truncate()
    for k,v in COUNTRYCODES.iteritems(): db.oid_country_codes.insert(code=k,country=v)
    for k,v in LANGCODES.iteritems(): db.oid_lang_codes.insert(code=k,language=v)
    for t in TIMEZONES: db.oid_timezones.insert(timezone=t)
    return True
    
cache.ram('db_init', lambda:db_init(), time_expire=123456789) #run db_init only once


#########################################################################
## uncomment the following line if you do not want sessions
#session.forget()
#########################################################################

#########################################################################
## Define your tables below, for example
##
## >>> db.define_table('mytable',SQLField('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','booelan'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytbale.myfield=='value).select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################


                
#########################################################################
## Here is sample code if you need:
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - crud actions
## uncomment as needed
#########################################################################

def assignOidname():
    """The nickname/username the user chooses at registration is copied
       to the db field oid_name. The oid_name is the name used in the openid
       and cannot, unlike the nickname, be changed later on."""
       
    query = (db.oid_users.nickname == request.vars.nickname)
    db(query).update(oid_name=request.vars.nickname.lower())


    


from gluon.tools import Mail, Auth, Crud     # new in web2py 1.56
#mail=Mail()                                  # mailer
#mail.settings.server='smtp.gmail.com:587'    # your SMTP server
#mail.settings.sender='you@gmail.com'         # your email
#mail.settings.login='username:password'      # your credentials
auth=Auth(globals(),db)                      # authentication/authorization
auth.settings.table_user = db.oid_users
auth.settings.register_onaccept = lambda _:assignOidname() 
#auth.settings.mailer=mail                    # for user email verification
auth.define_tables()                         # creates all needed tables
if session.oid_url:
    auth.settings.login_next = session.oid_url
#crud=Crud(globals(),db)                      # for CRUD helpers using auth
#crud.settings.auth=auth                      # (optional) enforces authorization on crud

#########################################################################
## then, to expose authentication
## http://..../[app]/default/user/login
## http://..../[app]/default/user/logout
## http://..../[app]/default/user/register
## http://..../[app]/default/user/profile
## http://..../[app]/default/user/retrieve_password
## http://..../[app]/default/user/change_password
## use the following action in controller default.py
##
##     def user(): return dict(form=auth())
##
## read docs for howto create roles/groups, assign memberships and permissions
##
## to expose CRUD
## http://..../[app]/default/data/tables
## http://..../[app]/default/data/select/[table]
## http://..../[app]/default/data/create/[table]
## http://..../[app]/default/data/read/[table]/[id]
## http://..../[app]/default/data/update/[table]/[id]
## http://..../[app]/default/data/delete/[table]/[id]
## use the following action in controller default.py
##
##     def data(): return dict(form=crud())
##
## to allow automatic download of all uploaded files and enforce authorization
## use the following action in controller default.py
##
##     def download(): return response.download(request,db)
