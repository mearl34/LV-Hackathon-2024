## LV-Hackathon-2024 
# Dining Hall Diets
Campus food recommendations based on chosen dietary restrictions!!

**Authors:** Maisy Earl, Anthony Cutrona, Sam Briggs


## About our Project
A common problem plaguing many college students is finding food that fits with dietary restrictions. Students who must follow vegan, vegetarian, pescetarian, gluten-free,or dairy-free, for any reason, have a much more difficult experience trying to find food on campus. We decided to provide an aid to these students to help them find possible options to eat based on their personal dietary needs/restrictions and where they could find it. 

## The Process
We started by developing a reccomendation model using AWS Personalize, with S3 storing our datasets used for training. We used a selection of menus from hawks nest, common grounds, the grind, and global cafe as the set of foods to create a dataset, featuring each food, if they can be consumed with certain dietary restrictions in mind, and where the food is from.We also made a dataset featuring representative "customers" and the food they would "purchase", with each customer representing a certain set of dietary restrictions, or none. Finally, we used an html based front-end to gather user input, and display the model's choices for the user. 

## The Product
Our final product is a user interface that allows users to tell the application their dietary restriction(s) (if any). Our program will then consider the data we trained it on to determine the best possible options for on-campus dining to satisfy their current needs. 

## Fallbacks
Due to the time restriction, we weren't able to build up our application as much as we had hoped. We limited the options to just a few of the retail options on campus (Hawk's Nest, Common Grounds, The Grind, and Global Cafe). Since we weren't able to incorporate the dining halls, we didn't have any certified options for halal or kosher diets. Further, since we built the data sets ourselves from publicly provided information, we didn't have exact ingredients and methods of preparation, so much of the possible information was missing. We wished to have a bigger dataset as well, but due to the time to create one, and the increased training time, we could not. Another large issue was the implementation of AWS Personalize into the python program, as many aspects we struggled with, due to limited instructions found online. This resulted in many work around solutions, which could be improved, resulting in better choices by the model.

# Built With
==HTML==
