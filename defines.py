import requests
import json

def getCreds() :
	creds = dict()
	creds['access_token'] = 'EAASs5UU0kyQBALLrIBIa0rtZCuEahnXkeAJQv4ZBSZC8a55y6WNRfieImV5gru5ND0XxZCfcq2m3IJDMwlES9L61S5nz9khWalymLcuY60ZCsBrRQsU80NRJ2umj1ZAp2OKmDXf82TZAoiLceVLY9fwiup5ZBKXtMELzKdAjLTa5vNXFVZBYSfdcM'
	creds['client_id'] = '1316000615404324'
	creds['client_secret'] = '86d845743bd6e4bdadb11a113c39945a'
	creds['graph_domain'] = 'https://graph.facebook.com/'
	creds['graph_version'] = 'v8.0'
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
	creds['debug'] = 'no'
	creds['page_id'] = '109132834256558'
	creds['instagram_account_id'] = '17841440981037920'
	creds['ig_username'] = 'coolerbranko'

	return creds

def makeApiCall( url, endpointParams, debug = 'no' ) : 
	data = requests.get( url, endpointParams )

	response = dict()
	response['url'] = url
	response['endpoint_params'] = endpointParams
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4)
	response['json_data'] = json.loads( data.content )
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 )

	if('yes' == debug) :
		displayApiCallData( response )

	return response


def displayApiCallData( response ) :
	print ("\nURL: ")
	print (response['url'])
	print ("\nEndpoint Params: ")
	print (response['endpoint_params_pretty'])
	print ("\nResponse: ")
	print (response['json_data_pretty'])



