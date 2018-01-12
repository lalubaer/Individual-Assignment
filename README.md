# Individual-Assignment
library('tidyverse')
library('ggplot2')
library('lubridate')
install.packages('data.table')
library('data.table')

#making data variable and backup variable
data=read.csv('useful_data.csv')
data_=data

#selecting my 3 samples & trimming them to only non-active years
high_income = data%>%filter(country %in% c("United States of America") & active %in% c("False"))
middle_income= data%>%filter(country %in% c("Brazil") & active %in% c("False"))
low_income = data%>%filter(country %in% c("Burundi") & active %in% c("False"))

#counting events
count(low_income)
count(high_income)
count(middle_income)

#plotting
Burundi=count(low_income)
USA=count(high_income)
Brazil=count(middle_income)

table=data.table(Burundi, Brazil, USA)
setnames(table, c("Burundi", "Brazil", "USA"))

#making population data variable and backup
pop_data=read.csv('useful_pop_data.csv')
pop_data_=pop_data
