from unipath import Path
import sys
import os

PROJECT_DIR = Path(os.path.abspath(__file__)).parent.parent.parent
sys.path.append(PROJECT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seaserpent.settings')

import django
django.setup()

import threading
from crawler import SubmarinoSerpent, AmericanasSerpent, ShoptimeSerpent

class CollectData(threading.Thread):
    
    serpent = None

    def __init__(self, serpent):
        super(CollectData, self).__init__()
        self.serpent = serpent

    def run(self):
        self.serpent.collect_data()

americanas = CollectData(AmericanasSerpent())
submarino = CollectData(SubmarinoSerpent())
shoptime = CollectData(ShoptimeSerpent())

americanas.start()
submarino.start()
shoptime.start()