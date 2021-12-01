# Netflix_Team_1 

Google Slides Presentation: https://docs.google.com/presentation/d/1fv0OF2bgY7Or7vcxAlTc8aO8qdhZG9EgHe21lIacDxk/edit?usp=sharing
Tableau Dashboard: https://public.tableau.com/app/profile/melisa.vacca/viz/Netflix_16382377392490/Story1?publish=yes

## Deliverable 1

### Topic: Netflix TV Shows and Movies
Our team has decided to focus on Netflix TV Shows and movies, specfically, how different variables affect ratings.  We have all really enjoyed the new shows Netflix has recently put out along with past TV shows and movies we can now watch through the application.  Since there are so many options to choose from, we were curious what factors make a TV show or movie reach high ratings and scores.  

### Data
We are starting off with two different datasets downloaded from Kaggle.com that include both common and uncommon columns.  Some columns that appear on both datasets include: Title, Type (TV Show/Movie), Release Year, Cast, and Country Origin.  Netflix Data #1 has some columns that are not included in Netflix Data #2 which include: Popular Rank and Genres.  Netflix Data #2 has some columns that are not included in Netflix Data #1 which include: Director and Show ID.  One interesting column header found in both datasets is "Rating."  However, in dataset #1 this is referring to its score out of 10, while it is referring to parental guidance ratings (such as PG13) in dataset #2.  

See  original ERD image below:

![image](https://user-images.githubusercontent.com/64279232/140628398-59b659df-ba62-499c-9745-ba3b532f7f9f.png)

Preview of original Netflix dataset #1 below:
![image](https://user-images.githubusercontent.com/64279232/140628580-d81c9e31-1353-455f-b672-c49be421b366.png)

Preview of original Netflix dataset #2 below:
![image](https://user-images.githubusercontent.com/64279232/140628670-22d7736a-491c-4e4b-80e4-9672009c5220.png)


### Questions We Hope to Answer
We will primarily be focusing on how (and if) different factors affect how a Netflix TV show or movie's individual rating. To start, we are most interested in the following:
- What tv show genres overall have the best ratings?  What movie genres overall have the best ratings?
- Are movies or tv shows more successful on Netflix?
- Is there a correlation with tv show and movie duration and its likeability factor? 
- How well are documentaries rated compared to other shows?

### Machine Learning Model
 
We have decided to use supervised learning due to our labeled datasets and knowledge of our inputs and outputs.  The data is split into 75% training and 25% testing.  From there, we are going to be working with the random forest classifier since it is an ensemble learning model that combines multiple smaller models into a more robust and accurate model. Randrom forest models are beneficial because they are easy to work with our given CSV files and the dataframes that we are cleaning. This model does limit us as we continue working with it since it is hard to improve and optimize the model unless you change the data input.  During the preliminary data process, we were able to bin movie rating and type of show, and we also added dummy variables for three different genre columns allowing for the random forest algorithm to accurately predict the target column. 

![image](https://user-images.githubusercontent.com/64279232/143799144-6e6a64d1-232d-4a28-abfc-9f53a6a17f07.png)

## Deliverable 2

### Data Exploration

As a team, we were able to go through and clean up each dataset before merging them together.  The "type" column in the first dataframe included many different categories such as "video", "tvEpisode", and "tvSeries" that we were able to classify as either tvShow or movie. See below:

![image](https://user-images.githubusercontent.com/64279232/142741814-5ab5bff8-fb9a-4db6-853d-6574b3f9eef9.png)

In the second dataframe, we dropped columns that were insignificant to our analysis such as director, cast, and show_id.  Similar to the process we used for "type" in the first dataframe, we looked further at all the movie ratings listed such as "TV-MA", "TV-Y7", and "PG-13" and classified each as either children, teen, or adult. See below:

![image](https://user-images.githubusercontent.com/64279232/142741836-dcc4d37e-843c-443a-86b3-6d6df1110d04.png)

After further analyzing the duration column in the second dataframe, we came to the decision to drop it due to the high variety of data esepecially when comparing tv shows and movies.  See below:

![image](https://user-images.githubusercontent.com/64279232/142741856-7e80c022-e222-4675-8492-6b9ebfcfd7ed.png)

There are many other steps we took during this ETL process that led us to two clean dataframes that we were able to join on the "title" and "type" columns.  See new ERD below:

![image](https://user-images.githubusercontent.com/64279232/142741912-bcd9687b-c879-4f6f-be1c-720c1063c7de.png)

We were able to join these two dataframes through Python code in Pandas as well as by database language and PG Admin.  See merged dataframe in Pandas below:

![image](https://user-images.githubusercontent.com/64279232/142741974-6949dd22-ae8a-4d87-9e1c-ef9cbb1bab4a.png)

Below is the code used in PG Admin to create a table merging the two dataframes and the result:

![image](https://user-images.githubusercontent.com/64279232/142741992-dc63ea0f-7c3a-42fb-b835-618b5cec3733.png)
![image](https://user-images.githubusercontent.com/64279232/142742001-5f0908ab-ce88-4526-b163-4c751dcb3ce1.png)

These new merged dataframes used two different methods to create the same result.  


## Deliverable 3

### Genres
In order to utilize the genre columns in the most efficient way, we used a lambda function to make each genre its own column for the machine learning.  The column received a "1" for genres it was listed as, and a "0" for genres it was not.  See below:

![image](https://user-images.githubusercontent.com/64279232/143794591-b16396db-09e6-4cb2-bfb1-7f999a422097.png)

Based on the image above, we can see that Lucifer is a fantasy, and it is not listed as a mystery, romance, or music.  If a specific tv show/movie is listed with multiple genres, each genre will be identified. 


### Analysis

We were able to determine that there is a correlation between number of votes and rating.  The main takeaway from this analysis is tv shows/movies with the highest number of votes also show high ratings.  There were no examples of tv shows/movies that had more than 400,000 votes and a score lower than 7/10.  See this scatterplot below:

![image](https://user-images.githubusercontent.com/64279232/143794901-3b55e605-1b0f-4252-af26-0e28b2d5df3a.png)

We were also able to determine that overall, tv shows are rated slightly higher than movies.  See chart below:

![image](https://user-images.githubusercontent.com/64279232/143799561-d7eece0e-f1c6-4808-b835-6e8d0c45364b.png)

Next, we were able to observe how countries' ratings compare with a visual and interative map of the world. We also were able to identify the top 15 rated countries and lowest 15 rated countries.  Through both the map and bar graph, we can see that Vietnam has the highest average rating and Bulgaria has the lowest average rating. See below:

![image](https://user-images.githubusercontent.com/64279232/143795718-89e7a878-3573-49c3-94cb-40cf6ffed6c1.png)
![image](https://user-images.githubusercontent.com/64279232/143795786-a078ec5d-34ac-4ec0-a467-4d1f7d063401.png)
![image](https://user-images.githubusercontent.com/64279232/143795832-60abb799-f570-4163-8d8a-ee8609dbf515.png)

The bubble chart below dives deep into analyzing genres.  Because some tv shows/movies are categorized under one single genre and others two, or three, it is difficult to graph these results cohesively.  We also didn't want to focus on genres with very little data that may skew the results.  This bubble chart does a great job of showing genres that have high/low ratings, but also how often they are represented in the dataset.  For example, tv shows in the drama/horror/thriller category are very popular and have an average rating of 8.067, which is quite high.  This bubble chart is interactive and can be swtiched between tv shows and movies, or both combined. See below:

![image](https://user-images.githubusercontent.com/64279232/143797188-4b444069-a52d-4a67-ac3b-22cc6a10169e.png)

Since documentaries have become more common on Netflix over the past few years, we wanted to see how their ratings compared to other highly watched genres.  We compared the average ratings of documentaries to action, comedy, and crime, and we found that documentaries have the highest average rating of these categories.  See below:

![image](https://user-images.githubusercontent.com/64279232/143798363-809b7afe-f476-40cb-a73f-4be8b17062ab.png)



