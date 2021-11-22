# Netflix_Team_1 

Link to Google Slides Presentation: https://docs.google.com/presentation/d/1fv0OF2bgY7Or7vcxAlTc8aO8qdhZG9EgHe21lIacDxk/edit?usp=sharing

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

### Machnie Learning Model
 
We have decided to use supervised learning due to our labeled dataets and knowledge of our inputs and outputs.  The data is split into 75% training and 25% testing.  From there, we are going to be working with the random forest classifier since it is an ensemble learning model that combines multiple smaller models into a more robust and accurate model. Randrom forest models are beneficial because they are easy to work with our given CSV files and the dataframes that we are cleaning. This model does limit us as we continue working with it since it is hard to improve and optimize the model unless you change the data input.  During the preliminary data process, we were able to bin movie rating and type of show, and we also added dummy variables for three different genre columns allowing for the random forest algorithm to accurately predict the target column. 


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

