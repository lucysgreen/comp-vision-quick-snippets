# This script is used to provision text translation offline.
# Written by Josh Higginson, 12th November 2021.

from argostranslate import package, translate
import gcld3  # For this, you must also install protobuf compiler - https://grpc.io/docs/protoc-installation/
from pycountry import languages
import os

# Use OS.path to make operating system friendly.
DEFAULT_LANGUAGE_MODEL_PATH = os.path.abspath(os.path.join('.', 'language_models'))

# Create our Language Detector object.
detector = gcld3.NNetLanguageIdentifier(
    min_num_bytes=3, # Filters out empty strings.
    max_num_bytes=5000  # Maximum for AWS Translate.
)

def get_files_for_argos_installation(path_to_language_models=DEFAULT_LANGUAGE_MODEL_PATH):
   '''This function walks through our language_models folder and returns a list of files that end in .argos or .argosmodel'''
   
   # Initialise List.
   list_of_models = []
   
   # Use os.walk to get files in folder. 
   for root, _, files in os.walk(path_to_language_models, topdown=False):
      for name in files:
         if '.argos' in name:

            # Append our file to list_of_models if name contains .argos.
            list_of_models.append(os.path.join(root, name))

   return list_of_models


def install_argos_languages(path_to_language_models=DEFAULT_LANGUAGE_MODEL_PATH):
   '''This function installs our argos language models from language_models folder.'''

   # Loop through list of .argos files in our language_model folder and install them.
   for package_path in get_files_for_argos_installation(path_to_language_models):
      package.install_from_path(package_path)


def return_installed_argos_languages():
   '''This function returns a list of every installed language.'''

   return [str(lang) for lang in translate.get_installed_languages()]


def glcd3_language_detector(text="Hello World!"):
   '''This function detects the most probable language from a given string and returns a comprehensive dictionary of what and why using GLCD3.'''

   result = detector.FindLanguage(text=text)  # Here, we detect our language.

   print(result.language)
    
   if result.language != 'und':  # If the result is undefined, we cannot define a country for it.
      languagecode = result.language

      if languages.get(alpha_2=result.language):
         result.language = languages.get(alpha_2=result.language).name  # Here, we replace the language shorthand name with it's full name.
   
      else:
         result.language = "Unknown ISO Code"
   else:
      languagecode = 'und'
      result.language = 'Undefined'

   return {
      "Text": text,
      "LanguageName": result.language,
      "LanguageCode": languagecode,
      "IsReliable": result.is_reliable,
      "ProportionTextWithLanguage": result.proportion,
      "Probability": result.probability
   }

def argos_translate_to_english(translation_dictionary):
   '''
   This function gets the argos language model in order for our translation to take place, and then returns the correct model + translation.
   Return formated structured like Amazon Translate for easy interoperability.

   Example Usage:
   translate_to_english({
      "Text": "что слишком сознавать — это болезнь, настоящая, полная болезнь.",
      "SourceLanguageCode": "auto",
      "TargetLanguageCode": "en"
   })
   '''

   # If source language is 'auto', then we try to identify the language with GLCD3.
   if translation_dictionary["SourceLanguageCode"] == "auto":
      translation_dictionary["SourceLanguageCode"] = glcd3_language_detector(text=translation_dictionary["Text"])["LanguageCode"]
   
   # Get the full language's name from the source language code.
   source_language_name = languages.get(alpha_2=translation_dictionary["SourceLanguageCode"]).name

   # Get our source and target language models.
   lang = f'{source_language_name} -> English'
   source_lang = [model for model in translate.get_installed_languages() if lang in map(repr, model.translations_from)]
   target_lang = [model for model in translate.get_installed_languages() if lang in map(repr, model.translations_to)]

   return {
      "TranslatedText": source_lang[0].get_translation(target_lang[0]).translate(translation_dictionary["Text"]),
      "SourceLanguageCode": translation_dictionary["SourceLanguageCode"],
      "TargetLanguageCode": "en"
   }