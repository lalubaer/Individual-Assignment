# Individual-Assignment
library('tidyverse')
library('ggplot2')
library('lubridate')

#making data variable and backup variable
data=read.csv('preprocessed_data.csv')
data_=data

#selecting my 3 samples
high_income = data%>%filter(Country %in% c("United States of America"))
intermediate_income= data%>%filter(Country %in% c("Brazil"))
low_income = data%>%filter(Country %in% c("Burundi"))

#trimming them to only non-active years
high_income = high_income%>%filter(Active %in% c("False"))
middle_income= data%>%filter(Active %in% c("False"))
low_income = data%>%filter(Active %in% c("False"))

#counting events
count(low_income)
count(high_income)
count(middle_income)

