# This script is used to provision text translation offline.
# Written by Josh Higginson, 12th November 2021.

from argostranslate import package, translate
import os

# Use OS.path to make operating system friendly.
DEFAULT_LANGUAGE_MODEL_PATH = os.path.abspath(os.path.join('.', 'language_models'))

def get_files_for_installation(path_to_language_models=DEFAULT_LANGUAGE_MODEL_PATH):
   '''This function walks through our language_model directory and returns a list of files that end in .argos or .argosmodel'''
   
   # Initialise List.
   list_of_models = []
   
   # Use os.walk to get files in folder. 
   for root, _, files in os.walk(path_to_language_models, topdown=False):
      for name in files:
         if '.argos' in name:

            # Append our file to list_of_models if name contains .argos.
            list_of_models.append(os.path.join(root, name))

   return list_of_models


def install_languages(path_to_language_models=DEFAULT_LANGUAGE_MODEL_PATH):
   '''This function installs our language models from language_models folder.'''

   # Loop through list of .argos files in our language_model folder and install them.
   for package_path in get_files_for_installation(path_to_language_models):
      package.install_from_path(package_path)
