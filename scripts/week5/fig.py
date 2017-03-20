from PIL import Image
from io import BytesIO
import requests
import warnings
warnings.filterwarnings("ignore")

r = requests.get('http://docs.python-requests.org/en/master/_static/requests-sidebar.png')
i = Image.open(BytesIO(r.content))
i.show()