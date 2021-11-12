import gcld3  # For this, you must also install protobuf compiler - https://grpc.io/docs/protoc-installation/
from pycountry import languages

# Create our Language Detector object.

detector = gcld3.NNetLanguageIdentifier(
    min_num_bytes=3, # Filters out empty strings 
    max_num_bytes=1000
)

def languageDetector(text="Hello World!"):
    '''This function detects the most probable language from a given string and returns a comprehensive dictionary of what and why.'''

    result = detector.FindLanguage(text=text)  # Here, we detect our language.
    
    if result.language != 'und':  # If the result is undefined, we cannot define a country for it.
        result.language = languages.get(alpha_2=result.language).name  # Here, we replace the language shorthand name with it's full name.
    else:
        result.language = 'Undefined'

    return {
        "Language": result.language,
        "Is Reliable?": result.is_reliable,
        "Proportion of Text with this Language": result.proportion,
        "Probability": result.probability,
    }
