# sudo python3 -m pip install --upgrade --force pip
# pip3 install --upgrade ibm-watson
# pip3 install ibm-cloud-sdk-core
# pylint: disable=unused-import,line-too-long,bare-except,import-error,invalid-name,missing-final-newline

"""This is a translator module"""

import ibm_watson

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

url_lt='https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/1beb677f-25e9-46e2-820a-2f9df6fef8e3'
apikey_lt='WgPhFyYQymJ-sqZfdNf3YGMxMm2Qv8QKKBtYKb6NA-kv'
version_lt='2023-04-23'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(
    version=version_lt,
    authenticator=authenticator
)

language_translator.set_service_url(url_lt)

def englishtofrench(word):
    """This class does english to french translation"""
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-fr").get_result()
    if word == " ":
        print("Please enter a word")
    else:
        pass

    return translation['translations'][0]['translation']

def frenchtoenglish(word):
    """This class does french to english translation"""
    lt = language_translator
    translation = lt.translate(text=word, model_id="fr-en").get_result()

    return translation['translations'][0]['translation']

def englishtogerman(word):
    """This class does english to german translation"""
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-de").get_result()
    return translation['translations'][0]['translation']