# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:54:57 2015
Wrapper around the Hacker News API provided by algolia
the base endpoint is -
http://hn.algolia.com/api/v1/search?query=startup - For a given search query
@author: Rupak Chakraborty
"""
import urllib2
import json
import socket

"""
Defines the class for the Highlighted Result field of the response
"""
class HighlightResult:
    
    def __init__(self):
        self.title = ""
        self.url = ""
        self.author = ""
        self.story_text = "" 
"""
Defines the value stored in the highlighted result field
"""
class HighlightResultValue:
    
    def __init__(self):
        self.value = ""
        self.matchLevel = ""
        self.matchedWords = [] 
"""
Defines the Post class containing the relevant information of a given post
"""
class Post:
    
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
    
    def __init__(self):
        self.highlightResult = HighlightResult()
"""
Main class to query the HackerNews API and parse the response
"""
class QueryResult: 
    
    link = "http://hn.algolia.com/api/v1/search?query=" 
    linkTag = "http://hn.algolia.com/api/v1/search?tags="
    nbHits = ""
    page = ""
    nbPages = ""
    hitsPerPage = ""
    query = ""
    params = ""
    processingTimeMS = ""
    postList = []
    tagName = ""
    tagParam = "&tags="
    searchbyTag = False
    paginateFlag = False
    pageParam = "&page="
    paginateList = []
    
    """
    Sets the tag name for a given endpoint
    """
    def setTagName(self,tag):
        self.tagName = tag 
    """
    Sets the pagination flag for a given query
    """
    def setPagination(self,pageFlag):
        self.paginateFlag = pageFlag
    """
    Uses the tag endpoint to search
    """
    def setSearchByTagName(self,boolValue,tagName):
        self.searchbyTag = boolValue
        self.tagName = tagName
        
    def __init__(self,userQuery): 
        
        self.userQuery = userQuery 
        self.userQuery = userQuery.replace(" ","%20")
        
    """
    Generates specific urls for the required endpoints
    """
    def linkGen(self): 
        
        if self.tagName != "":
            self.link = self.link + self.userQuery.strip() + self.tagParam + self.tagName
        elif self.searchbyTag:
            self.link = self.linkTag + self.tagParam + self.tagName
        else:
            self.link = self.link + self.userQuery.strip()
            
        return self.link
        
    """
    Given a URL returns the JSON response of it
    """
    def getJSONResponse(self,link):        
        
        response = urllib2.urlopen(link,timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
        if response.getcode() != 200:
            jsonData = "failure"
        else:
            jsonData = json.loads(response.read()) 
        
        return jsonData
    """
    Populates the values in a highlighted JSON field
    """
    def populateHighLightedResultValue(self,result):
        
        high = HighlightResultValue()
        
        if "value" in result:
            high.value = result["value"]
        if "matchLevel" in result:
            high.matchLevel = result["matchLevel"]
        if "matchedWords" in result:
            high.matchedWords = result["matchedWords"]
        
        return high
        
    """
    Function to parse the highlighted fields of a given response
    """
    def populateHighLightedResult(self,highlightedResult):
        
        highlight = HighlightResult()
        
        if "title" in highlightedResult: 
            highlight.title = self.populateHighLightedResultValue(highlightedResult["title"])
        if "url" in highlightedResult:
             highlight.url = self.populateHighLightedResultValue(highlightedResult["url"])
        if "author" in highlightedResult: 
             highlight.author = self.populateHighLightedResultValue(highlightedResult["author"])
        if "story_text" in highlightedResult: 
             highlight.story_text = self.populateHighLightedResultValue(highlightedResult["story_text"]) 
             
        return highlight;
        
    """
    Populates the JSON fields of a given JSON response
    """       
    def populateJSONFields(self,jsonData):
        
        self.nbHits = jsonData["nbHits"]
        self.page = jsonData["page"]
        self.nbPages = jsonData["nbPages"]
        self.hitsPerPage = jsonData["hitsPerPage"]
        self.query = jsonData["query"]
        self.params = jsonData["params"]
        self.processingTimeMS = jsonData["processingTimeMS"]
        
        if "hits" in jsonData: 
            
            hitArray = jsonData["hits"] 
            
            for hit in hitArray: 
                
                post = Post()
                post.created_at = hit["created_at"]
                post.title = hit["title"]
                post.url = hit["url"]
                post.author = hit["author"]
                post.points = hit["points"]
                post.story_text = hit["story_text"]
                post.comment_text = hit["comment_text"]
                post.num_comments = hit["num_comments"]
                post.story_id = hit["story_id"]
                post.story_title = hit["story_title"]
                post.story_url = hit["story_url"]
                post.parent_id = hit["parent_id"]
                post.created_at_i = hit["created_at_i"]
                post.tags = hit["_tags"]
                post.objectID = hit["objectID"]
                
                if "_highlightResult" in hit:
                    post.highlightResult = self.populateHighLightedResult(hit["_highlightResult"])
                    
                self.postList.append(post)
                
        return self.postList
        
    """
    Defines the processing pipeline for the entire post
    """    
    def postProcessingPipeline(self):
        
        if self.paginateFlag: 
            
            link = self.linkGen()
            originalLink = self.linkGen()
            link = link + self.pageParam + str(0)
            jsonResponse = self.getJSONResponse(link)
            self.paginateList.append(self.populateJSONFields(jsonResponse)) 
            self.page = self.page + 1 
            
            while self.page < self.nbPages:
                
                link = originalLink + self.pageParam + str(self.page)
                print link
                print str(self.page)
                jsonResponse = self.getJSONResponse(link)
                self.paginateList.append(self.populateJSONFields(jsonResponse))
                self.page = self.page + 1
        else:
            
            link = self.linkGen()
            jsonResponse = self.getJSONResponse(link)
            self.populateJSONFields(jsonResponse)
        
