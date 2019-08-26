
library(dplyr )
library(ggplot2)
library(tidyr)
library(purrr)
library(ggrepel)

setwd('/Users/kahaanshah/Desktop/Summer Research/urban-isochrones')
cities <- read.csv(file="car_data_30_5pm.csv", header=TRUE, sep=",")
cities_off <- read.csv(file="car_data_30_2.csv", header=TRUE, sep=",")
cities_new <- read.csv(file = 'contain_data_30_4pm.csv', header= TRUE, sep=",")
cities_10 <- read.csv(file = 'contain_data_0_10_4pm.csv', header=TRUE, sep=',')
cities_20 <- read.csv(file = 'contain_data_10_20_4pm.csv', header=TRUE, sep=',')
cities_urban_10 <- read.csv(file = 'urban_data_0_10.csv', header = TRUE, sep=',')
cities_urban_20 <- read.csv(file = 'urban_data_10_20.csv', header = TRUE, sep=',')

ggplot(cities_urban_20)+
  #Times <= 100)) +
  geom_line(aes(x = Times,
                y = Fitness, 
                color = NAME)) +
  theme_minimal() +
  theme(legend.position = 'bottom') +
  guides(color=guide_legend(nrow=5,byrow=TRUE))

cities_viz_new <- cities_20 %>%
  mutate(Fitness = Intersection/Isoline_Area) %>%
  arrange(NAME, Times)

IOU <- cities_new %>%
  filter(IOU_Largest == 1)

ggplot(IOU, aes(x = Times, y = IOU)) + geom_point() + geom_text_repel(aes(label=NAME), size=3)

ggplot(cities_viz_new)+
  #Times <= 100)) +
  geom_line(aes(x = Times,
                y = Fitness, 
                color = NAME)) +
  theme_minimal() +
  theme(legend.position = 'bottom') +
  guides(color=guide_legend(nrow=5,byrow=TRUE))


spain_cities <- read.csv(file='spain_data.csv', header=TRUE, sep = ",")

spain_cities_viz <- spain_cities %>%
  group_by(NAME) %>%
  mutate(Population.Share = Cumulative_Population/max(Cumulative_Population)) %>%
  ungroup()

ggplot(spain_cities_viz) +
  geom_line(aes(x = Times,
                y = Population.Share, 
                color = NAME)) +
  theme_minimal() +
  theme(legend.position = 'bottom') +
  guides(color=guide_legend(nrow=5,byrow=TRUE))

spain_optima <- spain_cities_viz %>%
  filter(Maxima == 1)

ggplot(spain_optima, aes(x = Times, y = Population.Share)) + geom_point() + geom_text_repel(aes(label=NAME), size=3)



cities_viz_off <- cities_off %>%
  group_by(NAME) %>%
  mutate(Total.Population = sum(Marginal.Population)) %>%
  mutate(Cum.Pop = cumsum(Marginal.Population)) %>%
  ungroup() %>%
  arrange(NAME, Times) %>%
  mutate(Population.Share = Cum.Pop/Total.Population)

cities_list_off <- cities_viz_off %>%
  group_by(CBSAFP, NAME) %>%
  summarise(total = sum( Marginal.Population)) %>%
  ungroup() %>%
  mutate(rank_pop = row_number(desc(total))) %>%
  filter(rank_pop <= 10) 



cities_list_off <- unique(cities_list_off$NAME)

ggplot(cities_viz_off %>% 
         filter(NAME %in% cities_list_off))+
  #Times <= 100)) +
  geom_line(aes(x = Times,
                y = Population.Share, 
                color = NAME)) +
  theme_minimal() +
  theme(legend.position = 'bottom') +
  guides(color=guide_legend(nrow=5,byrow=TRUE))

cities_viz <- cities %>%
  group_by(NAME) %>%
  mutate(Total.Population = sum(Marginal_Population)) %>%
  mutate(Cum.Pop = cumsum(Marginal_Population)) %>%
  ungroup() %>%
  arrange(NAME, Times) %>%
  mutate(Population.Share = Cum.Pop/Total.Population)

cities_list <- cities_viz %>%
  group_by(CBSAFP, NAME) %>%
  summarise(total = sum( Marginal_Population)) %>%
  ungroup() %>%
  mutate(rank_pop = row_number(desc(total))) %>%
  filter(rank_pop <= 10) 

IOU <- cities %>%
  filter(IOU_Largest == 1)

ggplot(IOU, aes(x = Times, y = IoU)) + geom_point() + geom_text_repel(aes(label=NAME), size=3)
  
first_optima <- cities_viz %>%
  filter(Optima == 1) %>%
  group_by(NAME) %>%
  filter(row_number()==1) %>%
  ungroup()

second_optima <- cities_viz %>%
  filter(Optima == 1) %>%
  group_by(NAME) %>%
  filter(row_number()==2) %>%
  ungroup()

ggplot(first_optima, aes(x = Times, y = Population.Share)) + geom_point()
ggplot(first_optima, aes(x = Times, y = Population.Share)) + geom_point() +
  geom_text_repel(aes(label=NAME), size=3)
ggplot(second_optima, aes(x = Times, y = Population.Share, )) + geom_point() + 
  geom_text_repel(aes(label=NAME), size=3)

?geom_point
  

cities_list <- unique(cities_list$NAME)

ggplot(cities_viz %>% 
         filter(NAME %in% cities_list))+
                #Times <= 100)) +
  geom_line(aes(x = Times,
                y = Population.Share, 
                color = NAME)) +
  theme_minimal() +
  theme(legend.position = 'bottom') +
  guides(color=guide_legend(nrow=5,byrow=TRUE))



