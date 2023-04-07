from json import load as _json_load
import os as _os
from typing import Dict as _Dict



PWD = _os.getcwd()
if '/src' in PWD:
    PWD = f'{PWD}\\pss_data\\'
else:
    PWD = f'{PWD}\\pss_data\\'

ID_NAMES_FILEPATH = _os.path.join('pss_data', 'id_names.json')

ID_NAMES_INFO: _Dict[str, str]

with open(ID_NAMES_FILEPATH) as fp:
    ID_NAMES_INFO = _json_load(fp)