## LV-Hackathon-2024 
# Campus Food Recommendations
Campus food recommendations based on chosen dietary restrictions!!

**Authors:** Maisy Earl, Anthony Cutrona, Sam Briggs


## About our Project
A common problem plaguing many college students is finding food that fits with dietary restrictions. Students who must follow vegan, vegetarian, pescetarian, gluten-free,or dairy-free, for any reason, have a much more difficult experience trying to find food on campus. We decided to provide an aid to these students to help them find possible options to eat considering both what they're in the mood for and also their personal dietary needs/restrictions. 

## The Process
We started by developing a recomendation model using AWS Personalize, with S3 storing our datasets used for training. We used a selected menus from hawks nest, common grounds, the grind, and global cafe as the set of foods to train our model. 

## The Product
Our final product is a user interface that allows users to tell the application their dietary restrictions (if any) and the cuisine/food type they're currently in the mood for. Our program will then consider the data we trained it on to determine the best possible option for on-campus dining to satisfy their current needs. 

## Fallbacks
Due to the time restriction, we weren't able to build up our application as much as we had hoped. We limited the options to just a few of the retail options on campus (Hawk's Nest, Common Grounds, The Grind, and Global Cafe). Since we weren't able to incorporate the dining halls, we didn't have any certified options for halal or kosher diets. Further, since we built the data sets ourselves from publicly provided information, we didn't have exact ingredients and methods of preparation, so much of the possible information was missing. In the future, we'd like to cooperate with the dining services at Lehigh to gain a much more comprehensive knowledge of the dining options available. We also weren't able to consider the time of day when the user accesses the application, which would restrict which food locations are currently open and available to the student. 
