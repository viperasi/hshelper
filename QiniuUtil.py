# -*- coding: utf-8 -*-
__author__ = 'arthurtsu'

import qiniu.conf
import qiniu.rs
import qiniu.io
from StringIO import StringIO

#qiniu sdk config
qiniu.conf.ACCESS_KEY = ""
qiniu.conf.SECRET_KEY = ""

bucket_name = "hshelper"

policy = qiniu.rs.PutPolicy(bucket_name)
uptoken = policy.token()

def uploadQiniu(filename):
    fileHandle = open(filename)
    data = StringIO(fileHandle.read())
    ret, err = qiniu.io.put(uptoken, None, data)
    print ret
    if err is not None:
        print('error : %s' % err)
    fileHandle.close()
    return ret['key']

