# Github Wrapper API

## Overview
We want to have an app that utilizes the GitHub API and creates a wrapper library around it that has it’s own custom end-points (REST API format)

## TO-DO
- Utilise the Github API to create a wrapper REST-API that can return the following responses in JSON:
- Return the most popular repositories based on a filter like Open Pull Requests, Number of commits and
number of contributors. Once filtered the following 3 information NEEDS to be there, number of stars,
number of contributors and primary programming language used by the repo. There should be an option to
go to the Github link of the repo.
- Return popular repositories for different languages. Feel free to choose any 3 programming languages.
The choice Need NOT be configurable, just choose any 3 languages and implement based on your static
choice
- Return top 5 contributors for any repo.


## Criteria
- Ease of Usability of the app
- Is the app live and hosted on a cloud server (Heroku, AWS etc.)
- Readability and modularity of code
- Appropriate git use
- programming guidelines like PEP-8 (or if you chose something else please specify)
- A clear README.md to setup the project with dependencies mentioned with version no. of the library used.

## Bonus
- A frontend to test the REST-API which shows formatted JSON response in an easy-to-read format
- You containerize the app using Docker.