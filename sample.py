# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:24:39 2015
Sample use cases of the HackerNews API
@author: Rupak Chakraborty
"""
import HackerNewsUser as HNUser
import HackerNews as HN

def sample():
    
    user = HNUser.User("pg")
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

def sampleQuery():
    
    query = HN.QueryResult("internet")
    query.postProcessingPipeline()
    for post in query.postList:
        
        print "------------------------------------------------------"
        print "Post Created : ", post.created_at
        print "Post Title : ", post.title 
        print "Post Url : ", post.url 
        print "Post Author : ", post.author 
        print "Post Points : ", post.points 
        print "Story Text : ", post.story_text 
        print "Comment Text : ", post.comment_text 
        print "Number of Comments : ", post.num_comments 
        print "Story Id : ", post.story_id 
        print "Story Title : ", post.story_title 
        print "Story Url : ", post.story_url 
        print "Parent Id : ", post.parent_id 
        print "Created At i : ", post.created_at_i 
        print "Tags : ", post.tags 
        print "ObjectID : ", post.objectID 
        print "------------------------------------------------------"

sample()
sampleQuery()