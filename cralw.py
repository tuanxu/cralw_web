import pymysql.cursors

import datetime
import time
import numpy as np
import os.path
import hashlib
import sys
import os
import json
from pprint import pprint

from bs4 import BeautifulSoup
import requests
import re
import urllib

now = datetime.datetime.now()
date = ("%d-%.2d-%.2d %.2d:%.2d:%.2d" % (now.year, now.month, now.day, now.hour, now.minute, now.second))

isUsingPHP = True

def CreateConnectionLocalhost():
    return pymysql.connect(host='127.0.0.1',
                                     port=3306,
                                     user='root',
                                     password='',
                                     db='wordpress',
                                     #charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)


def CreateConnection():

    return pymysql.connect(host='databases.000webhost.com',
                                     port=3306,
                                     user='id16977318_wp_ec276a981c7da1c7842dde3f1b061177',
                                     password='Thbttpbk1*',
                                     db='id16977318_wp_ec276a981c7da1c7842dde3f1b061177',
                                     #charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

def CloseConnection(conn):
   conn.close()
   #print('conn.close')

def getMaxId(conn):
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT max(ID) FROM `wp_posts`"
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        if(result['max(ID)'] != None):
            return result['max(ID)']
    return 0

def SQL_CheckSourceLink(conn,source_link):
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT count(0) FROM `wp_posts` where source_link = \'%s\'"%source_link
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result['count(0)']
    return 0
def InsertPostToDatabase(conn,id,post_title,date_time,post_content,source_link):
    post_date = post_date_gmt = post_modified = post_modified_gmt = date_time
    #add data here
    ID='NULL'
    post_author='1'
    post_content='<!-- wp:paragraph -->\r\n%s\r\n<!-- /wp:paragraph -->'%post_content
    post_excerpt=''
    post_status='publish'
    comment_status='open'
    ping_status='open'
    post_password=''
    post_name='post-%d'%id
    to_ping=''
    pinged=''
    post_content_filtered=''
    post_parent='0'
    guid= 'http://localhost/wp/?p=%d'%id
    menu_order='0'
    post_type='post'
    post_mime_type=''
    comment_count='0'
    #source_link='0'
    sql = ""
    try:
        print('Insert ' + post_title)
        with conn.cursor() as cursor:
            # Create a new record
            sql = """INSERT INTO `wp_posts` (
                `ID`
                , `post_author`
                , `post_date`
                , `post_date_gmt`
                , `post_content`
                , `post_title`
                , `post_excerpt`
                , `post_status`
                , `comment_status`
                , `ping_status`
                , `post_password`
                , `post_name`
                , `to_ping`
                , `pinged`
                , `post_modified`
                , `post_modified_gmt`
                , `post_content_filtered`
                , `post_parent`
                , `guid`
                , `menu_order`
                , `post_type`
                , `post_mime_type`
                , `comment_count`
                , `source_link`
            ) 
            VALUES (
                %s 
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
            )
            """%(
                 ID,
                post_author,
                post_date,
                post_date_gmt,
                post_content,
                post_title,
                post_excerpt,
                post_status,
                comment_status,
                ping_status,
                post_password,
                post_name,
                to_ping,
                pinged,
                post_modified,
                post_modified_gmt,
                post_content_filtered,
                post_parent,
                guid,
                menu_order,
                post_type,
                post_mime_type,
                comment_count,
                source_link
                 )
            print(sql)

            if(isUsingPHP ==True):
                userdata = {"firstname": "John", "lastname": "Doe", "insertsql": "sql"}
                resp = requests.post('https://baotuanxu.000webhostapp.com/insert_wp.php', proxies=urllib.request.getproxies(),params=userdata)

            else:
                result = cursor.execute(sql)
                conn.commit()
            #print(result)
    except Exception as e:
        #print(sql)
        #print(e)
        print('Insert ' + post_title + ' ===============> Fail!')
        return None
    finally:
        print('Done')

def InsertPostToPHP(conn,id,post_title,date_time,post_content,source_link):
    post_date = post_date_gmt = post_modified = post_modified_gmt = date_time
    #add data here
    IDREPLACEID='IDREPLACEID'
    post_author='1'
    post_content='<!-- wp:paragraph -->\r\n%s\r\n<!-- /wp:paragraph -->'%post_content
    post_excerpt=''
    post_status='publish'
    comment_status='open'
    ping_status='open'
    post_password=''
    post_name='post-%s'%IDREPLACEID
    to_ping=''
    pinged=''
    post_content_filtered=''
    post_parent='0'
    guid= 'http://localhost/wp/?p=%s'%IDREPLACEID
    menu_order='0'
    post_type='post'
    post_mime_type=''
    comment_count='0'
    #source_link='0'
    sql = ""
    try:
        print('Insert ' + post_title)
        with conn.cursor() as cursor:
            # Create a new record
            sql = """INSERT INTO `wp_posts` (
                `ID`
                , `post_author`
                , `post_date`
                , `post_date_gmt`
                , `post_content`
                , `post_title`
                , `post_excerpt`
                , `post_status`
                , `comment_status`
                , `ping_status`
                , `post_password`
                , `post_name`
                , `to_ping`
                , `pinged`
                , `post_modified`
                , `post_modified_gmt`
                , `post_content_filtered`
                , `post_parent`
                , `guid`
                , `menu_order`
                , `post_type`
                , `post_mime_type`
                , `comment_count`
                , `source_link`
            ) 
            VALUES (
                %s 
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
            )
            """%(
                 'NULL',
                post_author,
                post_date,
                post_date_gmt,
                post_content,
                post_title,
                post_excerpt,
                post_status,
                comment_status,
                ping_status,
                post_password,
                post_name,
                to_ping,
                pinged,
                post_modified,
                post_modified_gmt,
                post_content_filtered,
                post_parent,
                guid,
                menu_order,
                post_type,
                post_mime_type,
                comment_count,
                source_link
                 )
            #print(sql)

            if(isUsingPHP ==True):
                userdata = {"source_link": source_link, "lastname": "Doe", "insertsql": sql}
                resp = requests.post('https://baotuanxu.000webhostapp.com/insert_wp.php', proxies=urllib.request.getproxies(),data=userdata)
                #print(resp.text)
            else:
                result = cursor.execute(sql)
                conn.commit()
            #print(result)
    except Exception as e:
        #print(sql)
        #print(e)
        print('Insert ' + post_title + ' ===============> Fail!')
        return None
    finally:
        print('Done')


def requestVNExpress():
    res = requests.get('https://vnexpress.net/')
    #print(res)
    #print(res.text.encode("utf-8"))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    match =soup.find(class_="title-news")
    #print (match)
    print (match.a['href'])
    print (match.a['title'])


def crawNewsData(conn,baseUrl, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup.text)
    titles = soup.findAll('h3', class_='title-news')
    links = [link.find('a').attrs["href"] for link in titles]
    data = []
    for link in links:
      fullLink = baseUrl + link
      if(SQL_CheckSourceLink(conn,fullLink) > 0):
        continue

      #hardcode link  here
      #link = '/huong-duong-nguoc-nang-le-the-lai-con-quang-cao-tho-vai-chuong-20210420124052235.htm'
      try:
        news = requests.get(fullLink)
        soup = BeautifulSoup(news.content, "html.parser")
        title = soup.find("h1", class_="article-title").text
        date_time = soup.find("div", class_="date-time").text
        abstract = soup.find("h2", class_="sapo").text
        body = soup.find("div", id="main-detail-body")

        

        content = ""
        #try:
        #    contents = body.findChildren("p", recursive=False)
        #    for c in contents:
        #      content = content + "<p>" +  c.text
        #    
        #except:
        #    content = ""

        
        try:
            blocks = body.findChildren(recursive=False)
            for block in blocks:

              RelatedOneNews = block.find("div", class_="VCSortableInPreviewMode active")
              if(RelatedOneNews != None): #this block is RelatedOneNews
                      #print(block.attrs['data-src'])
                continue

            #process image
              image = block.find("img")
              if(image != None): #this block is image
                  if(block.attrs['type'] != 'RelatedOneNews'): #do not process the note
                    content = content + "<p><img  src=\"" + image.attrs["src"] + "\" ></p>"
                  continue

              video = block.find("div", class_="VideoCMS_Caption")
              if(video != None): #this block is video
                  video_url = re.search(r'poster=(.*?)&_info', block.attrs['data-src']).group(1)
                  #print(video_url)
                  content = content + "<p><img  src=\"" + video_url + "\" ></p>"
                  continue

              #print(block.text) #this block is paragrap text
              content = content + "<p>" + block.text
           
        except e:
            print("exception e = " + e)

        #image = body.find("img").attrs["src"]
        data.append({
            "title": title,
            "abstract": abstract,
            "date_time": date_time,
            "content": content,
            "source_link": fullLink,
            #"image": image,
        })
        print("craw " + title)
        #print("abstract " + abstract)
        #print("content " + content)
        #print("image " + image)
        #return data #tuan.dm cheat return here
      except:
        continue
    return data

def Preprocess_data(data):
    for index, item in enumerate(data):

        item["title"] = item["title"].replace("'", "\\'")
        item["abstract"] = item["abstract"].replace("'", "\\'")
        item["content"] = item["content"].replace("'", "\\'")
        new_date_str = item["date_time"][0:-6]
        datetime_object = datetime.datetime.strptime(new_date_str, '%d/%m/%Y %H:%M')

        item["date_time"] = ("%d-%.2d-%.2d %.2d:%.2d:%.2d" % (datetime_object.year, datetime_object.month, datetime_object.day, datetime_object.hour, datetime_object.minute, datetime_object.second))

    return data
def makeFastNews(conn,data):
    

    for index, item in enumerate(data):

        body =  "<h3>" +  item["abstract"] + "</h3>" +item["content"]
        id_to_insert = getMaxId(conn) + 1
        InsertPostToPHP(
            conn
            ,id_to_insert
            ,item["title"]
            ,item["date_time"]
            ,body
            ,item["source_link"]
            )


        

dt = 60

if __name__ == "__main__":
    count = 0
    
    #test connection online
    #conn = CreateConnection()
    #id_to_insert = getMaxId(conn) + 1

    while True:
    
        try:

            print ("start count = %d"%count)
            conn = CreateConnectionLocalhost()
            #conn = CreateConnection()
            data = crawNewsData(conn,"https://tuoitre.vn", "https://tuoitre.vn/tin-moi-nhat.htm")
            if(len(data)>0):
                data = Preprocess_data(data)
                makeFastNews(conn,data)

            CloseConnection(conn)

            time.sleep(dt)
            count = count +1
            

        except Exception as e:
            print("Whoops, something went wrong when connecting to the servers: %s" % (e))
            print("Oops!  There was an unexpected error.  Try again... in 10 minutes....")
            time.sleep(dt * 10)
            pass   