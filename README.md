# *Sentiment Analysis*
Sentiment analysis is defined as the computational process of determining the type of opinion expressed in a piece of text (whether the opinion is negative, positive, or neutral). 

It is widely used in industry today -- ranging from social media to hospitality. The use of sentiment analysis can greatly improve a business's customer service by isolating negative feedback for later improvement. 

## The Project
In regards to software development, the process of creating and developing software is one run by humans and thus vulnerable to the emotions experienced by the developers. By using sentiment analysis to extract the sentiment of commit messages pushed by developers and extracting the success of Travis CI builds then modeling the data in a calendar, CEOs of large companies can determine whether the emotions of their software developers are impacting the progress of their product. 

## Brief Summary and Progress
In this project, I will be using TextBlob (a python library) to determine the sentiment of commit messages pushed by developers in one GitHub repository. The sentiment will be returned as a value between -1 and +1. 

To change the repository used, switch the url to the API of the GitHub repository you're targeting. 

For this step, reference commitsentiment.py. Later on, this will also be integrated into the code for extracting the build status of the commit messages in buildstatus.py. 

To extract the build status of the commit messages, alter the target url according to each individual commit hash (like I have done in buildstatus.py). 

Once the build status, sentiment, and date of the commit messages have been extracted, store the information in a list and convert to a dictionary. The dictionary can then be converted to a JSON file that can be loaded into our calendar. 

For the calendar, I used a [template](https://www.formget.com/bootstrap-calendar/) from FormGet and altered the calendar to fit the extracted data. 

In this project, I altered the background colour of the calendar cells to represent the build status and I added emojis to represent the sentiment of the commit messages pushed. The calendar can then be easily examined for any relationship between the emotions of software developers and the progress of product development. 

## Other Notes
This project was done as a part of the High School Internship Program (HIP) at the University of Alberta during July-August 2018. 
