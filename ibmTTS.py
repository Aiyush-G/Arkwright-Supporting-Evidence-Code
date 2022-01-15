from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('lmdgQT1vHGmBpOZSrsHM_HaeAaAieNO7uC2NLBHMlcVl')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/326d3ba3-d11d-4851-897b-ce33846e5388')


try:
	with open('hello_world.wav', 'wb') as audio_file:
	    audio_file.write(
	        text_to_speech.synthesize(
	            '<prosody rate="slow" pitch="medium"> Mayek has many friends. Go to the website google.com for more, plants grow from 15-60 centimetres in the summer. </prosody>',
	            voice='en-GB_JamesV3Voice',
	            accept='audio/mp3'        
	        ).get_result().content)

except ApiException as ex::
	print("Method failed with status code " + str(ex.code) + ": " + ex.message)