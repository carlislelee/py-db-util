#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pymongo

host = ''
port = 27017
user = ''
passwd = ''
replicaset = ''
try:
    c = pymongo.MongoClient(host = host, port = port)
    #c = pymongo.MongoReplicaSetClient('mongodb://%s:%s@%s' % (user, passwd, host), replicaset)
    db
