import sys
import os
base_dir = os.path.dirname(os.path.realpath('__file__'))
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import GasTemplatesMatching as GM
from PIL import Image
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello !'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)


