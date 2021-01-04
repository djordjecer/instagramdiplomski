from defines import getCreds, makeApiCall

def getUsersMedia( params ) :

	endpointParams = dict()
	endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username,comments_count,like_count'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['instagram_account_id'] + '/media'

	return makeApiCall( url, endpointParams, params['debug'] )

params = getCreds()
params['debug'] = 'no'
response = getUsersMedia( params )


for post in response['json_data']['data'] :
	print ("\n----- POST ------ \n")
	print ("Link to post:")
	print (post['permalink'])
	print ("\nPost caption:")
	print (post['caption'])
	print ("\nMedia type:")
	print (post['media_type'])
	print ("\nPosted at:")
	print (post['timestamp'])
	print ("\nComment count:")
	print (post['comments_count'])
	print ("\nLike count:")
	print (post['like_count'])


