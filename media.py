#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:59:27 2017

@author: ezgi
"""
import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        