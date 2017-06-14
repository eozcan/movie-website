#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:13:59 2017

@author: ezgi
"""


import media
import fresh_tomatoes

mrNobody=media.Movie("Mr Nobody", "A boy stands on a station platform as a train is about to leave. Should he go with his mother or stay with his father? Infinite possibilities arise from this decision. As long as he doesn't choose, anything is possible",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4ODkzMDQ3Nl5BMl5BanBnXkFtZTgwNTEwMTkxMDE@._V1_SY1000_CR0,0,675,1000_AL_.jpg","https://www.youtube.com/watch?v=iJAP8q_iPOw")

francesHa=media.Movie("Frances Ha","A story that follows a New York woman (who doesn't really have an apartment), apprentices for a dance company (though she's not really a dancer), and throws herself headlong into her dreams, even as their possibility dwindles.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BOTY0NDQ2NzQ2N15BMl5BanBnXkFtZTcwMTU0OTkwOQ@@._V1_SY1000_CR0,0,637,1000_AL_.jpg", "https://www.youtube.com/watch?v=YBn5dgXFMis")

bigFish=media.Movie("Big Fish", "A frustrated son tries to determine the fact from fiction in his dying father's life.","https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyMzM3MzgyNV5BMl5BanBnXkFtZTcwMTI4MzUyMQ@@._V1_.jpg",
                    "https://www.youtube.com/watch?v=M3YVTgTl-F0")


midnightParis=media.Movie("Midnight in Paris", "While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.","https://images-na.ssl-images-amazon.com/images/M/MV5BMTM4NjY1MDQwMl5BMl5BanBnXkFtZTcwNTI3Njg3NA@@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=FAfR8omt-CY")

gardenState=media.Movie("Garden State","A quietly troubled young man returns home for his mother's funeral after being estranged from his family for a decade.","https://images-na.ssl-images-amazon.com/images/M/MV5BMjc5MDE0NjkxOF5BMl5BanBnXkFtZTcwNzA0NTkyMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg", 
                        "https://www.youtube.com/watch?v=Tej9r6mAcU4")

americanBeauty=media.Movie("A sexually frustrated suburban father has a mid-life crisis after becoming infatuated with his daughter's best friend.", "A sexually frustrated suburban father has a mid-life crisis after becoming infatuated with his daughter's best friend.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM4NTI5NzYyNV5BMl5BanBnXkFtZTgwNTkxNTYxMTE@._V1_SY1000_CR0,0,675,1000_AL_.jpg","https://www.youtube.com/watch?v=FfWnZthD9Tw")

movies=[mrNobody, francesHa, bigFish, midnightParis, gardenState, americanBeauty ]
fresh_tomatoes.open_movies_page(movies)