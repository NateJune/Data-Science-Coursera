import kaggle
import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

author_and_dataset = 'victorsoeiro/netflix-tv-shows-and-movies'

api.dataset_download_files(author_and_dataset, path="./")

with zipfile.ZipFile('c:/users/natha/desktop/cenith_python_project/netflix-tv-shows-and-movies.zip', "r") as zipref:
    zipref.extractall("c:/users/natha/desktop/cenith_python_project")

api.dataset_download_files('piterfm/2022-ukraine-russian-war', path="./")

with zipfile.ZipFile('c:/users/natha/desktop/cenith_python_project/2022-ukraine-russian-war.zip', "r") as zipref:
    zipref.extractall("c:/users/natha/desktop/cenith_python_project")