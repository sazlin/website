Title: Visualizing Twitter data in near real time
Date: 2014-07-14
Slug: project-rhetoracle
Author: Sean Azlin
Category: Programming
Tags: Python, CodeFellows, Business Intelligence
Summary: How rheTOracle collects, analyzes, and visualizes Twitter data  

##Visualizing Twitter data with rheTOracle
###What is rheTOracle?
For our first group project at Code Fellows, I set out with two others (John Shiver and Muazzez Mira) to create a service that could collect, analyze, and visualize Twitter data in near real time. We dubbed this service [rheTOracle](http://ec2-54-213-173-105.us-west-2.compute.amazonaws.com/). With rheTOracle, we decided to target data that helped us answer a couple specific questions that we were all interested in answering:

* Which programming language is the most discussed on Twitter?
* For each programming language, which @user talks about that language the most?

We later tacked on a few smaller questions because it was fun visualizing the answers:

* What was the last Tweet mentioning a programming language?
* Where was the last Tweet mentioning a programming language Tweeted from?

So, what is rheTOracle? rheTOracle is a service that collects, aggregates, processes, and visualizes Twitter data in near-real time in an effort to help answer a set of specific questions. It's essentially a rich, living dashboard that grows and evolves right in front of you.

###What makes rheTOracle special?
* rheTOracle provides quantitative insight about specific topics using Twitter data in a way that is really hard to do otherwise.
* rheTOracle just works for everyone. There is no sign-up or sign-in to fuss with.
* rheTOracle updates in near-real time automagically. No refreshing necessary.
* It's free! You're welcome, Internet :)

###How is it built?
rheTOracle's architecture is comprised of multiple independent services deployed across several AWS nodes. Each indepedent service performs a core function for the overall experience:

* **Filter Map**: Basically a Python dictionary that captures both a whitelist and a blacklist of relevant #hashtags, @users, and keywords and relates those to a specific topic.
* **Twitter Worker**: A Python script that collects and processes Twitter stream data according to the criteria defined by our Filter Map.
* **PostgreSQL DB**: A PostgreSQL DB instance on AWS stores the Twitter data that the Twitter Worker collects.
* **Redis**: A Redis server is used to cache SQL query results and insulate the PostgreSQL DB from an overwhelming # of SQL requests from clients.
* **Flask service**: A Python service, built using the Flask microframework, that services requests from clients that are monitoring rheTOracle's data. The Flask service pulls results from the Redis server as needed, which in turn pulls data from our SQL DB periodically.
* **Frontend**: HTML/CSS/Javascript that renders data provided by the Flask service using AJAX, Google Visualizations, and Ammchart (a JS charting library). rheTOracle's front end pulls data from the Flask service every 3 seconds and updates the page's charts as you watch - no reloading of the overall page is required.

Want to know more? Check out our source on GitHub.

###Plans for the Future?
We have a second project week coming up and we all intend to continue working on rheTOracle with the goal of shipping a solid beta in August. Two big ideas we have for the future:

* Crowd-source weekly questions that we can tackle with our service and build-up a library of questions & answers over time.
* Build out a sentiment analysis service using a composite of multiple machine learning algorithms and run that service against our database of collected tweets. 

