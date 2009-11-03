# coding=utf-8

from urlparse import urlparse
from cgi import parse_qs
import urllib

try:
    import json
except ImportError:
    import simplejson as json

import re
POSTCODE_RE = re.compile(r'\b[A-PR-UWYZ][A-HK-Y0-9][A-HJKSTUW0-9]?[ABEHMNPRVWXY0-9]? {0,2}[0-9][ABD-HJLN-UW-Z]{2}\b',re.I)


def addToQueryString(orig, extra_data):
    scheme, netloc, path, params, query, fragment = urlparse(orig)
    query_data = parse_qs(query)
    for k, v in extra_data.items():
        if not v:
            del(extra_data[k])
    query_data.update(extra_data)
    query = urllib.urlencode(query_data, True)
    base_url = ""
    if scheme and netloc:
        base_url += "%s://%s" % (scheme, netloc)
    if path:
        base_url += "%s" % path
    if params:
        base_url += ";%s" % params
    if query:
        base_url += "?%s" % query
    if fragment:
        base_url += "#%s" % fragment
    return base_url


map_id_to_const_name = {'seat-1':'Aberavon',
                        'seat-7':'Aldershot',
                        'seat-8':'Aldridge-Brownhills',
                        'seat-9':'Altrincham & Sale West',
                        'seat-10':'Alyn & Deeside',
                        'seat-11':'Amber Valley',
                        'seat-17':'Arundel & South Downs',
                        'seat-18':'Ashfield',
                        'seat-19':'Ashford',
                        'seat-20':'Ashton-under-Lyne',
                        'seat-21':'Aylesbury',
                        'seat-23':'Banbury',
                        'seat-25':'Barking',
                        'seat-26':'Barnsley Central',
                                                'seat-27':'Barnsley East & Mexborough',
                        'seat-28':'Barnsley West & Penistone',
                        'seat-29':'Barrow & Furness',
                        'seat-30':'Basildon',
                        'seat-31':'Basingstoke',
                        'seat-32':'Bassetlaw',
                        'seat-33':'Bath',
                        'seat-34':'Batley & Spen',
                        'seat-35':'Battersea',
                        'seat-36':'Beaconsfield',
                        'seat-37':'Beckenham',
                        'seat-38':'Bedford',
                        'seat-42':'Belfast East',
                        'seat-43':'Belfast North',
                        'seat-44':'Belfast South',
                        'seat-45':'Belfast West',
                        'seat-46':'Berwick-upon-Tweed',
                        'seat-47':'Bethnal Green & Bow',
                        'seat-48':'Beverley & Holderness',
                        'seat-49':'Bexhill & Battle',
                        'seat-50':'Bexleyheath & Crayford',
                        'seat-51':'Billericay',
                        'seat-52':'Birkenhead',
                        'seat-53':'Birmingham, Edgbaston',
                        'seat-54':'Birmingham, Erdington',
                        'seat-55':'Birmingham, Hall Green',
                        'seat-56':'Birmingham, Hodge Hill',
                        'seat-57':'Birmingham, Ladywood',
                        'seat-58':'Birmingham, Northfield',
                        'seat-59':'Birmingham, Perry Barr',
                        'seat-60':'Birmingham, Selly Oak',
                        'seat-61':'Birmingham, Sparkbrook & Small Heath',
                        'seat-62':'Birmingham, Yardley',
                        'seat-63':'Bishop Auckland',
                        'seat-64':'Blaby',
                        'seat-65':'Blackburn',
                        'seat-66':'Blackpool North & Fleetwood',
                        'seat-67':'Blackpool South',
                        'seat-68':'Blaenau Gwent',
                        'seat-69':'Blaydon',
                        'seat-70':'Blyth Valley',
                        'seat-71':'Bognor Regis & Littlehampton',
                        'seat-72':'Bolsover',
                        'seat-73':'Bolton North East',
                        'seat-74':'Bolton South East',
                        'seat-75':'Bolton West',
                        'seat-76':'Bootle',
                        'seat-77':'Boston & Skegness',
                        'seat-78':'Bosworth',
                        'seat-79':'Bournemouth East',
                        'seat-80':'Bournemouth West',
                        'seat-81':'Bracknell',
                        'seat-82':'Bradford North',
                        'seat-83':'Bradford South',
                        'seat-84':'Bradford West',
                        'seat-85':'Braintree',
                        'seat-86':'Brecon & Radnorshire',
                        'seat-87':'Brent East',
                        'seat-88':'Brent North',
                        'seat-89':'Brent South',
                        'seat-90':'Brentford & Isleworth',
                        'seat-91':'Brentwood & Ongar',
                        'seat-92':'Bridgend',
                        'seat-93':'Bridgwater',
                        'seat-94':'Brigg & Goole',
                        'seat-95':'Brighton, Kemptown',
                        'seat-96':'Brighton, Pavilion',
                        'seat-97':'Bristol East',
                        'seat-98':'Bristol North West',
                        'seat-99':'Bristol South',
                        'seat-100':'Bristol West',
                        'seat-101':'Bromley & Chislehurst',
                        'seat-102':'Bromsgrove',
                        'seat-103':'Broxbourne',
                        'seat-104':'Broxtowe',
                        'seat-105':'Buckingham',
                        'seat-106':'Burnley',
                        'seat-107':'Burton',
                        'seat-108':'Bury North',
                        'seat-109':'Bury South',
                        'seat-110':'Bury St Edmunds',
                        'seat-111':'Caernarfon',
                        'seat-112':'Caerphilly',
                        'seat-114':'Calder Valley',
                        'seat-115':'Camberwell & Peckham',
                        'seat-116':'Cambridge',
                        'seat-121':'Cannock Chase',
                        'seat-122':'Canterbury',
                        'seat-123':'Cardiff Central',
                        'seat-124':'Cardiff North',
                        'seat-125':'Cardiff South & Penarth',
                        'seat-126':'Cardiff West',
                        'seat-127':'Carlisle',
                        'seat-128':'Carmarthen East & Dinefwr',
                        'seat-129':'Carmarthen West & South Pembrokeshire',
                        'seat-131':'Carshalton & Wallington',
                        'seat-132':'Castle Point',
                        'seat-553':'Central Suffolk & North Ipswich',
                        'seat-133':'Ceredigion',
                        'seat-134':'Charnwood',
                        'seat-135':'Chatham & Aylesford',
                        'seat-136':'Cheadle',
                        'seat-138':'Cheltenham',
                        'seat-139':'Chesham & Amersham',
                        'seat-140':'Chester, City of',
                        'seat-141':'Chesterfield',
                        'seat-142':'Chichester',
                        'seat-143':'Chingford & Woodford Green',
                        'seat-144':'Chipping Barnet',
                        'seat-145':'Chorley',
                        'seat-146':'Christchurch',
                        'seat-147':'Cities of London & Westminster',
                        'seat-148':'Cleethorpes',
                        'seat-149':'Clwyd South',
                        'seat-150':'Clwyd West',
                        'seat-154':'Colchester',
                        'seat-155':'Colne Valley',
                        'seat-156':'Congleton',
                        'seat-157':'Conwy',
                        'seat-158':'Copeland',
                        'seat-159':'Corby',
                        'seat-162':'Cotswold',
                        'seat-163':'Coventry North East',
                        'seat-164':'Coventry North West',
                        'seat-165':'Coventry South',
                        'seat-166':'Crawley',
                        'seat-167':'Crewe & Nantwich',
                        'seat-168':'Crosby',
                        'seat-169':'Croydon Central',
                        'seat-170':'Croydon North',
                        'seat-171':'Croydon South',
                        'seat-175':'Cynon Valley',
                        'seat-176':'Dagenham',
                        'seat-177':'Darlington',
                        'seat-178':'Dartford',
                        'seat-179':'Daventry',
                        'seat-180':'Delyn',
                        'seat-181':'Denton & Reddish',
                        'seat-182':'Derby North',
                        'seat-183':'Derby South',
                        'seat-187':'Devizes',
                        'seat-192':'Dewsbury',
                        'seat-193':'Don Valley',
                        'seat-194':'Doncaster Central',
                        'seat-195':'Doncaster North',
                        'seat-200':'Dover',
                        'seat-203':'Dudley North',
                        'seat-204':'Dudley South',
                        'seat-205':'Dulwich & West Norwood',
                        'seat-214':'Durham, City of',
                        'seat-216':'Ealing North',
                        'seat-215':'Ealing, Acton & Shepherd\'s Bush',
                        'seat-217':'Ealing, Southall',
                        'seat-218':'Easington',
                        'seat-13':'East Antrim',
                        'seat-188':'East Devon',
                        'seat-219':'East Ham',
                        'seat-295':'East Hampshire',
                        'seat-382':'East Londonderry',
                        'seat-559':'East Surrey',
                        'seat-649':'East Worthing & Shoreham',
                        'seat-659':'East Yorkshire',
                        'seat-222':'Eastbourne',
                        'seat-223':'Eastleigh',
                        'seat-725':'Renfrewshire East',
                        'seat-225':'Eccles',
                        'seat-226':'Eddisbury',
                        'seat-233':'Edmonton',
                        'seat-234':'Ellesmere Port & Neston',
                        'seat-235':'Elmet',
                        'seat-236':'Eltham',
                        'seat-237':'Enfield North',
                        'seat-238':'Enfield, Southgate',
                        'seat-239':'Epping Forest',
                        'seat-240':'Epsom & Ewell',
                        'seat-241':'Erewash',
                        'seat-242':'Erith & Thamesmead',
                        'seat-243':'Esher & Walton',
                        'seat-245':'Exeter',
                        'seat-248':'Falmouth & Camborne',
                        'seat-249':'Fareham',
                        'seat-250':'Faversham & Mid Kent',
                        'seat-251':'Feltham & Heston',
                        'seat-252':'Fermanagh & South Tyrone',
                        'seat-255':'Finchley & Golders Green',
                        'seat-256':'Folkestone & Hythe',
                        'seat-257':'Forest of Dean',
                        'seat-258':'Foyle',
                        'seat-259':'Fylde',
                        'seat-260':'Gainsborough',
                        'seat-262':'Gateshead East & Washington West',
                        'seat-263':'Gedling',
                        'seat-264':'Gillingham',
                        'seat-275':'Gloucester',
                        'seat-277':'Gosport',
                        'seat-278':'Gower',
                        'seat-279':'Grantham & Stamford',
                        'seat-280':'Gravesham',
                        'seat-281':'Great Grimsby',
                        'seat-282':'Great Yarmouth',
                        'seat-284':'Greenwich & Woolwich',
                        'seat-285':'Guildford',
                        'seat-286':'Hackney North & Stoke Newington',
                        'seat-287':'Hackney South & Shoreditch',
                        'seat-288':'Halesowen & Rowley Regis',
                        'seat-289':'Halifax',
                        'seat-290':'Haltemprice & Howden',
                        'seat-291':'Halton',
                        'seat-294':'Hammersmith & Fulham',
                        'seat-298':'Hampstead & Highgate',
                        'seat-299':'Harborough',
                        'seat-300':'Harlow',
                        'seat-301':'Harrogate & Knaresborough',
                        'seat-302':'Harrow East',
                        'seat-303':'Harrow West',
                        'seat-304':'Hartlepool',
                        'seat-305':'Harwich',
                        'seat-306':'Hastings & Rye',
                        'seat-307':'Havant',
                        'seat-308':'Hayes & Harlington',
                        'seat-309':'Hazel Grove',
                        'seat-310':'Hemel Hempstead',
                        'seat-311':'Hemsworth',
                        'seat-312':'Hendon',
                        'seat-313':'Henley',
                        'seat-314':'Hereford',
                        'seat-315':'Hertford & Stortford',
                        'seat-318':'Hertsmere',
                        'seat-319':'Hexham',
                        'seat-320':'Heywood & Middleton',
                        'seat-321':'High Peak',
                        'seat-322':'Hitchin & Harpenden',
                        'seat-323':'Holborn & St Pancras',
                        'seat-324':'Hornchurch',
                        'seat-325':'Hornsey & Wood Green',
                        'seat-326':'Horsham',
                        'seat-327':'Houghton & Washington East',
                        'seat-328':'Hove',
                        'seat-329':'Huddersfield',
                        'seat-333':'Huntingdon',
                        'seat-334':'Hyndburn',
                        'seat-335':'Ilford North',
                        'seat-336':'Ilford South',
                        'seat-338':'Ipswich',
                        'seat-339':'Isle of Wight',
                        'seat-340':'Islington North',
                        'seat-341':'Islington South & Finsbury',
                        'seat-342':'Islwyn',
                        'seat-343':'Jarrow',
                        'seat-344':'Keighley',
                        'seat-345':'Kensington & Chelsea',
                        'seat-346':'Kettering',
                        'seat-348':'Kingston & Surbiton',
                        'seat-330':'Kingston upon Hull East',
                        'seat-331':'Kingston upon Hull North',
                        'seat-332':'Kingston upon Hull West & Hessle',
                        'seat-349':'Kingswood',
                        'seat-351':'Knowsley North & Sefton East',
                        'seat-352':'Knowsley South',
                        'seat-353':'Lagan Valley',
                        'seat-355':'Lancaster & Wyre',
                        'seat-356':'Leeds Central',
                        'seat-357':'Leeds East',
                        'seat-358':'Leeds North East',
                        'seat-359':'Leeds North West',
                        'seat-360':'Leeds West',
                        'seat-361':'Leicester East',
                        'seat-362':'Leicester South',
                        'seat-363':'Leicester West',
                        'seat-365':'Leigh',
                        'seat-366':'Leominster',
                        'seat-367':'Lewes',
                        'seat-369':'Lewisham East',
                        'seat-370':'Lewisham West',
                        'seat-368':'Lewisham, Deptford',
                        'seat-371':'Leyton & Wanstead',
                        'seat-372':'Lichfield',
                        'seat-373':'Lincoln',
                        'seat-375':'Liverpool, Garston',
                        'seat-376':'Liverpool, Riverside',
                        'seat-377':'Liverpool, Walton',
                        'seat-378':'Liverpool, Wavertree',
                        'seat-379':'Liverpool, West Derby',
                        'seat-381':'Llanelli',
                        'seat-383':'Loughborough',
                        'seat-384':'Louth & Horncastle',
                        'seat-385':'Ludlow',
                        'seat-386':'Luton North',
                        'seat-387':'Luton South',
                        'seat-388':'Macclesfield',
                        'seat-389':'Maidenhead',
                        'seat-390':'Maidstone & The Weald',
                        'seat-391':'Makerfield',
                        'seat-392':'Maldon & East Chelmsford',
                        'seat-394':'Manchester Central',
                        'seat-393':'Manchester, Blackley',
                        'seat-395':'Manchester, Gorton',
                        'seat-396':'Manchester, Withington',
                        'seat-397':'Mansfield',
                        'seat-398':'Medway',
                        'seat-399':'Meirionnydd Nant Conwy',
                        'seat-400':'Meriden',
                        'seat-401':'Merthyr Tydfil & Rhymney',
                        'seat-39':'Mid Bedfordshire',
                        'seat-196':'Mid Dorset & North Poole',
                        'seat-427':'Mid Norfolk',
                        'seat-562':'Mid Sussex',
                        'seat-594':'Mid Ulster',
                        'seat-645':'Mid Worcestershire',
                        'seat-402':'Middlesbrough',
                        'seat-403':'Middlesbrough South & East Cleveland',
                        'seat-406':'Milton Keynes South West',
                        'seat-407':'Mitcham & Morden',
                        'seat-408':'Mole Valley',
                        'seat-409':'Monmouth',
                        'seat-410':'Montgomeryshire',
                        'seat-412':'Morecambe & Lunesdale',
                        'seat-413':'Morley & Rothwell',
                        'seat-415':'Neath',
                        'seat-416':'New Forest East',
                        'seat-417':'New Forest West',
                        'seat-418':'Newark',
                        'seat-419':'Newbury',
                        'seat-421':'Newcastle upon Tyne Central',
                        'seat-422':'Newcastle upon Tyne East & Wallsend',
                        'seat-423':'Newcastle upon Tyne North',
                        'seat-420':'Newcastle-under-Lyme',
                        'seat-424':'Newport East',
                        'seat-425':'Newport West',
                        'seat-426':'Newry & Armagh',
                        'seat-432':'Normanton',
                        'seat-14':'North Antrim',
                        'seat-160':'North Cornwall',
                        'seat-189':'North Devon',
                        'seat-197':'North Dorset',
                        'seat-201':'North Down',
                        'seat-212':'North Durham',
                        'seat-40':'North East Bedfordshire',
                        'seat-117':'North East Cambridgeshire',
                        'seat-184':'North East Derbyshire',
                        'seat-296':'North East Hampshire',
                        'seat-316':'North East Hertfordshire',
                        'seat-405':'North East Milton Keynes',
                        'seat-244':'North Essex',
                        'seat-428':'North Norfolk',
                        'seat-518':'North Shropshire',
                        'seat-531':'North Southwark & Bermondsey',
                        'seat-567':'North Swindon',
                        'seat-576':'North Thanet',
                        'seat-592':'North Tyneside',
                        'seat-614':'North Warwickshire',
                        'seat-118':'North West Cambridgeshire',
                        'seat-213':'North West Durham',
                        'seat-297':'North West Hampshire',
                        'seat-364':'North West Leicestershire',
                        'seat-429':'North West Norfolk',
                        'seat-631':'North Wiltshire',
                        'seat-433':'Northampton North',
                        'seat-434':'Northampton South',
                        'seat-435':'Northavon',
                        'seat-436':'Norwich North',
                        'seat-437':'Norwich South',
                        'seat-438':'Nottingham East',
                        'seat-439':'Nottingham North',
                        'seat-440':'Nottingham South',
                        'seat-441':'Nuneaton',
                        'seat-443':'Ogmore',
                        'seat-444':'Old Bexley & Sidcup',
                        'seat-445':'Oldham East & Saddleworth',
                        'seat-446':'Oldham West & Royton',
                        'seat-721':'Orkney & Shetland',
                        'seat-448':'Orpington',
                        'seat-449':'Oxford East',
                        'seat-450':'Oxford West & Abingdon',
                        'seat-453':'Pendle',
                        'seat-454':'Penrith & The Border',
                        'seat-456':'Peterborough',
                        'seat-457':'Plymouth, Devonport',
                        'seat-458':'Plymouth, Sutton',
                        'seat-459':'Pontefract & Castleford',
                        'seat-460':'Pontypridd',
                        'seat-461':'Poole',
                        'seat-462':'Poplar & Canning Town',
                        'seat-463':'Portsmouth North',
                        'seat-464':'Portsmouth South',
                        'seat-465':'Preseli Pembrokeshire',
                        'seat-466':'Preston',
                        'seat-467':'Pudsey',
                        'seat-468':'Putney',
                        'seat-483':'Rayleigh',
                        'seat-470':'Reading East',
                        'seat-471':'Reading West',
                        'seat-472':'Redcar',
                        'seat-473':'Redditch',
                        'seat-474':'Regent\'s Park & Kensington North',
                        'seat-475':'Reigate',
                        'seat-477':'Rhondda',
                        'seat-479':'Ribble Valley',
                        'seat-480':'Richmond (Yorks)',
                        'seat-481':'Richmond Park',
                        'seat-482':'Rochdale',
                        'seat-469':'Rochford & Southend East',
                        'seat-484':'Romford',
                        'seat-485':'Romsey',
                        'seat-487':'Rossendale & Darwen',
                        'seat-488':'Rother Valley',
                        'seat-489':'Rotherham',
                        'seat-491':'Rugby & Kenilworth',
                        'seat-492':'Ruislip - Northwood',
                        'seat-493':'Runnymede & Weybridge',
                        'seat-494':'Rushcliffe',
                        'seat-495':'Rutland & Melton',
                        'seat-496':'Ryedale',
                        'seat-497':'Saffron Walden',
                        'seat-502':'Salford',
                        'seat-503':'Salisbury',
                        'seat-504':'Scarborough & Whitby',
                        'seat-505':'Scunthorpe',
                        'seat-506':'Sedgefield',
                        'seat-507':'Selby',
                        'seat-508':'Sevenoaks',
                        'seat-511':'Sheffield Central',
                        'seat-509':'Sheffield, Attercliffe',
                        'seat-510':'Sheffield, Brightside',
                        'seat-512':'Sheffield, Hallam',
                        'seat-513':'Sheffield, Heeley',
                        'seat-514':'Sheffield, Hillsborough',
                        'seat-515':'Sherwood',
                        'seat-516':'Shipley',
                        'seat-517':'Shrewsbury & Atcham',
                        'seat-519':'Sittingbourne & Sheppey',
                        'seat-520':'Skipton & Ripon',
                        'seat-521':'Sleaford & North Hykeham',
                        'seat-522':'Slough',
                        'seat-523':'Solihull',
                        'seat-524':'Somerton & Frome',
                        'seat-15':'South Antrim',
                        'seat-119':'South Cambridgeshire',
                        'seat-185':'South Derbyshire',
                        'seat-198':'South Dorset',
                        'seat-202':'South Down',
                        'seat-120':'South East Cambridgeshire',
                        'seat-161':'South East Cornwall',
                        'seat-525':'South Holland & The Deepings',
                        'seat-430':'South Norfolk',
                        'seat-478':'South Ribble',
                        'seat-526':'South Shields',
                        'seat-535':'South Staffordshire',
                        'seat-555':'South Suffolk',
                        'seat-568':'South Swindon',
                        'seat-577':'South Thanet',
                        'seat-41':'South West Bedfordshire',
                        'seat-191':'South West Devon',
                        'seat-317':'South West Hertfordshire',
                        'seat-431':'South West Norfolk',
                        'seat-561':'South West Surrey',
                        'seat-527':'Southampton, Itchen',
                        'seat-528':'Southampton, Test',
                        'seat-529':'Southend West',
                        'seat-530':'Southport',
                        'seat-532':'Spelthorne',
                        'seat-498':'St Albans',
                        'seat-499':'St Helens North',
                        'seat-500':'St Helens South',
                        'seat-501':'St Ives',
                        'seat-533':'Stafford',
                        'seat-534':'Staffordshire Moorlands',
                        'seat-536':'Stalybridge & Hyde',
                        'seat-537':'Stevenage',
                        'seat-539':'Stockport',
                        'seat-540':'Stockton North',
                        'seat-541':'Stockton South',
                        'seat-542':'Stoke-on-Trent Central',
                        'seat-543':'Stoke-on-Trent North',
                        'seat-544':'Stoke-on-Trent South',
                        'seat-545':'Stone',
                        'seat-546':'Stourbridge',
                        'seat-547':'Strangford',
                        'seat-548':'Stratford-on-Avon',
                        'seat-550':'Streatham',
                        'seat-551':'Stretford & Urmston',
                        'seat-552':'Stroud',
                        'seat-554':'Suffolk Coastal',
                        'seat-557':'Sunderland North',
                        'seat-558':'Sunderland South',
                        'seat-560':'Surrey Heath',
                        'seat-563':'Sutton & Cheam',
                        'seat-564':'Sutton Coldfield',
                        'seat-565':'Swansea East',
                        'seat-566':'Swansea West',
                        'seat-569':'Tamworth',
                        'seat-570':'Tatton',
                        'seat-571':'Taunton',
                        'seat-573':'Teignbridge',
                        'seat-574':'Telford',
                        'seat-575':'Tewkesbury',
                        'seat-578':'Thurrock',
                        'seat-579':'Tiverton & Honiton',
                        'seat-580':'Tonbridge & Malling',
                        'seat-581':'Tooting',
                        'seat-582':'Torbay',
                        'seat-583':'Torfaen',
                        'seat-190':'Torridge & West Devon',
                        'seat-584':'Totnes',
                        'seat-585':'Tottenham',
                        'seat-586':'Truro & St Austell',
                        'seat-587':'Tunbridge Wells',
                        'seat-589':'Twickenham',
                        'seat-590':'Tyne Bridge',
                        'seat-591':'Tynemouth',
                        'seat-595':'Upminster',
                        'seat-596':'Upper Bann',
                        'seat-597':'Uxbridge',
                        'seat-598':'Vale of Clwyd',
                        'seat-599':'Vale of Glamorgan',
                        'seat-600':'Vale of York',
                        'seat-601':'Vauxhall',
                        'seat-602':'Wakefield',
                        'seat-603':'Wallasey',
                        'seat-604':'Walsall North',
                        'seat-605':'Walsall South',
                        'seat-606':'Walthamstow',
                        'seat-607':'Wansbeck',
                        'seat-608':'Wansdyke',
                        'seat-609':'Wantage',
                        'seat-610':'Warley',
                        'seat-611':'Warrington North',
                        'seat-612':'Warrington South',
                        'seat-613':'Warwick & Leamington',
                        'seat-615':'Watford',
                        'seat-616':'Waveney',
                        'seat-617':'Wealden',
                        'seat-618':'Weaver Vale',
                        'seat-619':'Wellingborough',
                        'seat-620':'Wells',
                        'seat-621':'Welwyn Hatfield',
                        'seat-622':'Wentworth',
                        'seat-623':'West Bromwich East',
                        'seat-624':'West Bromwich West',
                        'seat-137':'West Chelmsford',
                        'seat-186':'West Derbyshire',
                        'seat-199':'West Dorset',
                        'seat-625':'West Ham',
                        'seat-354':'West Lancashire',
                        'seat-556':'West Suffolk',
                        'seat-593':'West Tyrone',
                        'seat-646':'West Worcestershire',
                        'seat-626':'Westbury',
                        'seat-719':'Na h-Eileanan an Iar',
                        'seat-628':'Westmorland & Lonsdale',
                        'seat-629':'Weston-Super-Mare',
                        'seat-630':'Wigan',
                        'seat-632':'Wimbledon',
                        'seat-633':'Winchester',
                        'seat-634':'Windsor',
                        'seat-635':'Wirral South',
                        'seat-636':'Wirral West',
                        'seat-637':'Witney',
                        'seat-638':'Woking',
                        'seat-639':'Wokingham',
                        'seat-640':'Wolverhampton North East',
                        'seat-641':'Wolverhampton South East',
                        'seat-642':'Wolverhampton South West',
                        'seat-643':'Woodspring',
                        'seat-644':'Worcester',
                        'seat-647':'Workington',
                        'seat-648':'Worsley',
                        'seat-650':'Worthing West',
                        'seat-651':'Wrekin, The',
                        'seat-652':'Wrexham',
                        'seat-653':'Wycombe',
                        'seat-654':'Wyre Forest',
                        'seat-655':'Wythenshawe & Sale East',
                        'seat-656':'Yeovil',
                        'seat-657':'Ynys Môn',
                        'seat-658':'York, City of',
                        'seat-670':'Aberdeen North',
                        'seat-671':'Aberdeen South',
                        'seat-672':'Aberdeenshire West & Kincardine',
                        'seat-673':'Airdrie & Shotts',
                        'seat-674':'Angus',
                        'seat-675':'Argyll & Bute',
                        'seat-676':'Ayr, Carrick & Cumnock',
                        'seat-677':'Ayrshire Central',
                        'seat-678':'Ayrshire North & Arran',
                        'seat-679':'Banff & Buchan',
                        'seat-680':'Berwickshire, Roxburgh & Selkirk',
                        'seat-681':'Caithness, Sutherland & Easter Ross',
                        'seat-682':'Coatbridge, Chryston & Bellshill',
                        'seat-683':'Cumbernauld, Kilsyth & Kirkintilloch East',
                        'seat-684':'Dumfries & Galloway',
                        'seat-685':'Dumfriesshire, Clydesdale & Tweeddale',
                        'seat-686':'East Dunbartonshire',
                        'seat-687':'West Dunbartonshire',
                        'seat-688':'Dundee East',
                        'seat-689':'Dundee West',
                        'seat-690':'Dunfermline & Fife West',
                        'seat-691':'East Kilbride, Strathaven & Lesmahagow',
                        'seat-692':'East Lothian',
                        'seat-693':'Edinburgh East',
                        'seat-694':'Edinburgh North & Leith',
                        'seat-695':'Edinburgh South',
                        'seat-696':'Edinburgh South West',
                        'seat-697':'Edinburgh West',
                        'seat-698':'Falkirk',
                        'seat-699':'Fife North East',
                        'seat-700':'Glasgow Central',
                        'seat-701':'Glasgow East',
                        'seat-702':'Glasgow North',
                        'seat-703':'Glasgow North East',
                        'seat-704':'Glasgow North West',
                        'seat-705':'Glasgow South',
                        'seat-706':'Glasgow South West',
                        'seat-707':'Glenrothes',
                        'seat-708':'Gordon',
                        'seat-709':'Inverclyde',
                        'seat-710':'Inverness, Nairn, Badenoch & Strathspey',
                        'seat-711':'Kilmarnock & Loudoun',
                        'seat-712':'Kirkcaldy & Cowdenbeath',
                        'seat-713':'Lanark & Hamilton East',
                        'seat-714':'Linlithgow & Falkirk East',
                        'seat-715':'Livingston',
                        'seat-716':'Midlothian',
                        'seat-717':'Moray',
                        'seat-718':'Motherwell & Wishaw',
                        'seat-720':'Ochil & Perthshire South',
                        'seat-722':'Paisley & Renfrewshire North',
                        'seat-723':'Paisley & Renfrewshire South',
                        'seat-724':'Perth & Perthshire North',
                        'seat-726':'Ross, Skye & Lochaber',
                        'seat-727':'Rutherglen & Hamilton West',
                        'seat-728':'Stirling',}
                        
