# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LikealyzerItem(scrapy.Item):
    
    name = scrapy.Field()
    summary = scrapy.Field()
    comments = scrapy.Field()
    coverMetric = scrapy.Field()
    aboutMetric = scrapy.Field()
    activityMetric = scrapy.Field()
    responseMetric = scrapy.Field()
    compromiseMEtric = scrapy.Field()
    userPhotoAvailable = scrapy.Field()
    aboutAvailable = scrapy.Field()
    usernameAvailable = scrapy.Field()
    achievementsQuality = scrapy.Field()
    contactInfoAvailable = scrapy.Field()
    phoneNumberAvailable = scrapy.Field()
    webpageAvailable = scrapy.Field()
    mailAvailable = scrapy.Field()
    locationAvailable = scrapy.Field()
    percentageOfPhotos = scrapy.Field()
    percentageOfNotes = scrapy.Field()
    percentageOfVideos = scrapy.Field()
    dailyMessages = scrapy.Field()
    messageLengthRatio = scrapy.Field()
    likedPages = scrapy.Field()
    originalFBVideos = scrapy.Field()
    usersCanPost = scrapy.Field()
    answerToUsersRatio = scrapy.Field()
    answerToUserResponseTime = scrapy.Field()
    peopleInteracting = scrapy.Field()
    totalLikes = scrapy.Field()
    participationRatio = scrapy.Field()




