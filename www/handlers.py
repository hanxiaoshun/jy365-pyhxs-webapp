# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'
' url handlers '

# -*- coding: utf-8 -*-
#
# __author__ = 'Michael Liao'
#
# ' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post
from pmModels import HisAddress, HisHeight, HisMobile, HisName
# from models import User, Comment, Blog, next_id


@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # blogs = [
    #     Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
    #     Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
    #     Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    # ]
    return {
        '__template__': 'blogs.html',
        # 'blogs': blogs
    }

@get('/responsive')
def responsive(request):
    # summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # blogs = [
    #     Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
    #     Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
    #     Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    # ]
    return {
        '__template__': 'responsive.html'
        # 'blogs': responsive
    }


@get('/base')
def base(request):
    # summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # blogs = [
    #     Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
    #     Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
    #     Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    # ]
    return {
        '__template__': 'base.html'
        # 'blogs': responsive
    }


@get('/suggest')
def suggest(request):
    # summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # blogs = [
    #     Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
    #     Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
    #     Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    # ]
    return {
        '__template__': 'suggest.html'
        # 'blogs': responsive
    }
#
# @get('/favicon.ico')
# def favicon(request):
#     # summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
#     # blogs = [
#     #     Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
#     #     Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
#     #     Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
#     # ]
#     return {
#         '__template__': 'favicon.ico'
#         # 'blogs': responsive
#     }

@get('/urls')
def urls(request):
    # summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # blogs = [
    #     Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
    #     Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
    #     Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    # ]
    return {
        '__template__': 'urls.html'
        # 'blogs': urls
    }
import pymysql
connection = pymysql.connect(host='60.205.228.47',
                             user='root',
                             password='123456',
                             db='personmanage',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
@get('/hisAddress')
def hisAddress(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # try:
    #     # with connection.cursor() as cursor:
    #     #     # Read a single record
    #     #     # sql = "SELECT `user_id`, `password` FROM `his_address` WHERE `username`=%s"
    #     #     sql = "SELECT * FROM `his_address`"
    #     #     cursor.execute(sql, ())
    #     #     result = cursor.fetchall()
    #     #     # result = cursor.fetchone()
    #     #     print(result)
    #
    # except:
    #     print('no data for this request')
    hisAddresss = yield from HisAddress.findAll()
    print(HisAddress.findAll())
    return {
        '__template__': 'hisAddress.html',
        'hisAddresss': hisAddresss
    }
@get('/toAddhisAddress')
def toAddhisAddress(*, id):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            # sql = "SELECT `user_id`, `password` FROM `his_address` WHERE `username`=%s"
            sql = "SELECT * FROM `his_address`  WHERE `id`=%s"
            result = cursor.execute(sql, (id))
            # result = cursor.fetchone()
            print(result[0])
    except:
        print('no data for this request')
    return {
        '__template__': 'hisAddress.html',
        'result': result[0]
    }
# @post('/addHisAddress')
# def addHisAddress(*, addressType, address,userid):

