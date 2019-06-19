import requests 
import uuid
import json 
import datetime
import os 


def requestData(retryLimit=60):

	url = "https://api.bird.co/user/login"
	device_id = str(uuid.uuid4())
	data = {'email': 'birdview@mailinator.com'}
	headers = {'User-Agent': 'Nintendo 64','Device-id': device_id, 'Platform': 'ios','App-Version': '3.0.5','Content-type':'application/json'}

	r = requests.post(url=url, json=data, headers=headers, timeout=60)


	if r.status_code != 200 and retryLimit > 0:
		retry = retryLimit - 1
		requestData(retry)
	else:
		#403 http status call this again so a try: except to catch 403 code 

		current_datetime = datetime.datetime.now() # retrieve current date and time 
		location_url = "https://api.bird.co/bird/nearby?latitude=34.024212&longitude=-118.496475&radius=10000"
		bird_location_headers = {'Authorization':'Bird eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBVVRIIiwidXNlcl9pZCI6ImMzZDQ5MmNmLThhMzctNDI1MC1hNTE4LTE2YTJiZTAzMGM3YiIsImRldmljZV9pZCI6ImJiMDljNTAwLTllNTUtNGZkMC05ZjU3LTZmMTRjMDNlMjVhZSIsImV4cCI6MTU5MTgxODY5OH0.FYQGvlDRhtUM7Izh43FP3Ud-Tb84JPWLjWZ8JTU7Cbg','Device-id':device_id, 'App-Version': '3.0.5','Location': json.dumps({"latitude":34.024212,"longitude":-118.496475})}
		birds = requests.get(url=location_url, headers=bird_location_headers)

		if birds.status_code == 200: # good response 
			json_response_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "responses",current_datetime.strftime("%d-%b-%Y %H:%M:%S.%f") +".json"), 'w')
			birds_json = birds.json()
			result  = {'timestamp': current_datetime.strftime("%d-%b-%Y %H:%M:%S.%f"), 'data': birds_json}
			json_response_file.write(json.dumps(result))
			json_response_file.close()

requestData()
