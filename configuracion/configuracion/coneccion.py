import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# mysqlclient

MYSQL_LOCAL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd_prefectura',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',

    }
}

MYSQL_REMOTO = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'byolhvawacj64ejwvwrt',
        'USER': 'ulhh4fuf1ivkutre',
        'PASSWORD': '6o05NMS0fhln1KSlKai',
        'HOST': 'byolhvawacj64ejwvwrt-mysql.services.clever-cloud.com',
        'PORT': '21070'

    }

}