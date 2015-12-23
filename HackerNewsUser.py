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

class User:
    
    Id = ""
    created_at_i = ""
    submission_count = ""
    username = ""
    submitted = ""
    about = ""
    karma = ""
    comment_count = ""
    created_at = ""
    avg = ""
    delay = ""
    updated_at = ""
    objectId = ""
    link = "http://hn.algolia.com/api/v1/users/"
    
    def __init__(self,userQuery):
        self.userQuery = userQuery 
        self.link = self.link + self.userQuery.strip()
        
    def getJSONResponse(self,link):        
        response = urllib2.urlopen(link,timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
        jsonData = json.loads(response.read())
        return jsonData
    
    def populateUserFields(self,jsonData):
        
        self.Id = jsonData["id"]
        self.created_at_i = jsonData["created_at_i"]
        self.submission_count = jsonData["submission_count"]
        self.username = jsonData["username"]
        self.submitted = jsonData["submitted"]
        self.about = jsonData["about"]
        self.karma = jsonData["karma"]
        self.comment_count = jsonData["comment_count"]
        self.created_at = jsonData["created_at"]
        self.avg = jsonData["avg"]
        self.delay = jsonData["delay"]
        self.updated_at = jsonData["updated_at"]
        self.objectId = jsonData["objectID"]
    
    def userProcessingPipeline(self):
        
        jsonResponse = self.getJSONResponse(self.link)
        self.populateUserFields(jsonResponse)

def sample():
    
    user = User("pg")
    user.userProcessingPipeline()
    print "User Id : ",user.Id
    print "Creation Time : ", user.created_at_i
    print "Submission Count : ", user.submission_count
    print "Username : ", user.username
    print "Submitted : ", user.submitted
    print "About : ", user.about
    print "Karma : ", user.karma
    print "Comment Count : ", user.comment_count
    print "Created At : ", user.created_at
    print "Avg Rating : ", user.avg
    print "Delay : ", user.delay
    print "Updated At : ", user.updated_at
    print "Object ID : ", user.objectId

sample()
