# *Sentiment Analysis*
Sentiment analysis is defined as the computational process of determining the type of opinion expressed in a piece of text (whether the opinion is negative, positive, or neutral). 

It is widely used in industry today -- ranging from social media to hospitality. The use of sentiment analysis can greatly improve a business's customer service by isolating negative feedback for later improvement. 

## The Project
For large software development companies, it is sometimes difficult to gauge how their employees may feel or how fast their project is progressing. By creating a tool that extracts the sentiment of the developers' commit messages and comments and compares it to the state of their Travis CI builds, executives of large companies can decide on the best course of action to take -- whether they need to motivate their employees or let them be. 

## Brief Summary and Progress
In this project, I will be using TextBlob (a python library) to determine the sentiment of commit messages and comments in one GitHub repository. The sentiment will be returned as a value between -1 and +1. 

To change the repository used, switch the url to the API of the GitHub repository you're targeting. 

To extract the build status of the commit messages, alter the target url according to each individual commit hash. 

Once the build status, sentiment, and date have been extracted, store the information in a list and convert to a dictionary. The dictionary can then be converted to a JSON file that can be loaded into our calendar. 

For the calendar, I used a [template](https://www.formget.com/bootstrap-calendar/) from FormGet and altered the calendar to fit the extracted data. 

In this project, I altered the background colour of the calendar cells to represent the build status and I added emojis to represent the sentiment of the commit messages/comments. The calendar then easily visualizes the emotions of the software developers and the success of their Travis CI builds. 

## Other Notes
This project was done as a part of the High School Internship Program (HIP) at the University of Alberta during July-August 2018. 
