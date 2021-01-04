from defines import getCreds, makeApiCall

def getUserMedia ( params ) :

	endpointParams = dict()
	endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['instagram_account_id'] + '/media'

	return makeApiCall( url, endpointParams, params['debug'] )


def getMediaInsights( params ) :

	endpointParams = dict()
	endpointParams['metric'] = params['metric']
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['latest_media_id'] + '/insights'

	return makeApiCall( url, endpointParams, params['debug'] )


def getUserInsights( params ) :

	endpointParams = dict()
	endpointParams['metric'] = 'follower_count,impressions,profile_views,reach'
	endpointParams['period'] = 'day'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['instagram_account_id'] + '/insights'

	return makeApiCall( url, endpointParams, params['debug'] )



params = getCreds()
response = getUserMedia( params )


print ('\n--- LATEST POST ---\n')
print ('\tLink to post: ')
print ('\t' + response['json_data']['data'][0]['permalink'])
print ('\n\tPost caption: ')
print ('\t' + response['json_data']['data'][0]['caption'])
print ('\n\tMedia type: ')
print ('\t' + response['json_data']['data'][0]['media_type'])
print ('\n\tPosted at: ')
print ('\t' + response['json_data']['data'][0]['timestamp'])


params['latest_media_id'] = response['json_data']['data'][0]['id']

if 'VIDEO' == response['json_data']['data'][0]['media_type'] :
	params['metric'] = 'engagement,impressions,reach,saved,video_views' 
else :
	params['metric'] = 'engagement,impressions,reach,saved'

response = getMediaInsights( params )

print ('\n--- LATEST POST INSIGHTS ---\n')

for insight in response['json_data']['data'] :
	print (( insight['name'] + ' ('+ insight['period'] +'): ' + str( insight['values'][0]['value'] )).encode('utf-8'))


response = getUserInsights( params )

print ('\n--- DAILY USER ACCOUNT INSIGHTS ---\n')

for insight in response['json_data']['data'] :
	print (( insight['name'] + ' ('+ insight['period'] +'): ' + str( insight['values'][0]['value'] )).encode('utf-8'))

	for value in insight['values'] :
		print ("\t\t" + value['end_time'] + ": " + str( value['value'] ))


