# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:54:57 2015
Wrapper around the Hacker News API provided by algolia
the base endpoint is -
http://hn.algolia.com/api/v1/users/pg - For User Information
http://hn.algolia.com/api/v1/search?query=startup - For a given search query
@author: Rupak Chakraborty
"""
import urllib2
import json
import socket

class Post:
    
    link = "http://hn.algolia.com/api/v1/search?query=" 
    created_at = ""
    title = ""
    url = ""
    author = ""
    points = ""
    story_text = ""
    comment_text = ""
    num_comments = ""
    story_id = ""
    story_title = ""
    story_url = ""
    parent_id = ""
    created_at_i = ""
    tags = []
    objectID = ""    
    
    def __init__(self,userQuery):
        self.userQuery = userQuery 
        self.link = self.link + self.userQuery.strip()
        
    def getJSONResponse(self,link):        
        response = urllib2.urlopen(link,timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
        jsonData = json.loads(response.read())
        return jsonData
    
  