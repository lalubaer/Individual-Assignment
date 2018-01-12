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
middle_income= data%>%filter(country %in% c("Guatemala") & active %in% c("False"))
low_income = data%>%filter(country %in% c("Ethiopia") & active %in% c("False"))

#filtering and making a new column income with value "low", "middle", high"
high_income = data%>%filter(country %in% c("United States of America")) %>% droplevels() %>% filter(active %in% c("False")) %>% mutate(income="high")
middle_income= data%>%filter(country %in% c("Guatemala") & active %in% c("False")) %>% mutate(income="middle") %>% droplevels()
low_income = data%>%filter(country %in% c("Ethiopia") & active %in% c("False")) %>% mutate(income="low") %>% droplevels()

#binding the three frames, keeping in mind that it should count the entries grouped per income value. The counts are put into a table called pop.income.counts
pop.income.counts <- rbind(low_income, middle_income, high_income) %>%
  group_by(income) %>%
  summarize(n())

# This solution comes because the high income turns up empty, so we just forced in a value 0, otherwise it wouldn't show
pop.income.counts <- rbind(pop.income.counts, c("high", 0))

#renames the columns
names(pop.income.counts) <- c("income", "counts") 

#converting the numbers from strings to numerics
pop.income.counts$counts <- as.numeric(pop.income.counts$counts)

#make bar plot
ggplot(data=pop.income.counts) +
  geom_bar(mapping=aes(x=income, y=counts), stat="identity")
# stat="identity": It wants to compute stuff, so you need to tell it to just plot the value (identity)


#in case I still get to turn the number of events into a ration of events/population
#making population data variable and backup
pop_data=read.csv('useful_pop_data.csv')
pop_data_=pop_data

#Selecting my samples
select_pop=pop_data%>%filter(country %in% c("United States of America", "Guatemala", "Ethiopia"))


