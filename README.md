# NFL Combine & Career Score Analysis
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Jupyter_Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)]()
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=NumPy&logoColor=white)]()
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)]()
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)]()

## 🏈 Project Summary
<p align="center">
  <img src="./nfl-cartoon.gif" width="1000" height="450">
</p>

Our project analyzed the effectiveness of the NFL combine in predicting the career readiness of offensive players in the NFL. Specifically, we focused on the offensive players who participated in the combine in 2018 and examined their first-year success in the league. By examining the correlation between combine performance and NFL career success, we aimed to provide insights to improve how NFL teams evaluate players and guide athletes in their preparation for their professional careers.

The NFL combine holds significant weight in an NFL hopeful's draft stock, often influencing team decisions and players' training priorities. However, there have been notable cases, such as Tom Brady, where poor combine performance did not hinder an athlete's remarkable success in the league. Therefore, we aimed to determine if the combine accurately identified NFL-ready players across different positions or if its importance should be reassessed.

We hypothesized that the degree to which combine performance predicted NFL readiness would vary by position. For example, we expected that positions requiring more skill, like quarterbacks, may not be as reliant on combine scores as other positions like linebackers. Furthermore, we anticipated that even in positions where combine performance was a strong predictor of NFL success, there would be exceptions—athletes with exceptional combine performances who did not excel in the league.

Ultimately, our analysis shed light on the benefits and limitations of the NFL combine, helping teams make more informed decisions when evaluating players and aiding athletes in understanding the most effective areas to focus their training efforts. By evaluating the relationship between combine performance and NFL career success, we contributed to the improvement of player analysis and preparation strategies in the NFL.

## 🗂️ Dataset 1: NFL Raw Downloadable Data
The NFL Raw Data dataset was downloaded from the <a href="https://www.advancedsportsanalytics.com/nfl-raw-data">Advanced Sports Analytics website</a>. It is a CSV file containing player fantasy football data and game information for each game from 2019 to 2023. The dataset had 26,600 rows and 68 columns, with a file size of approximately 6.7 MB. The structure of the dataset consisted of multiple rows per game, with each row corresponding to a player's performance in that game. The columns of interest were "winning_team," "vis_team," and "home_team." These columns were used to determine the winning team for each game. This dataset was used to calculate the win/loss percentage of each player's team in their first year and make adjustments to their career success scores based on this ratio.

## 🗂️ Dataset 2: NFL Combine Webscraped Data
The NFL Combine Data was obtained by web scraping from the <a href="https://nflcombineresults.com/nflcombinedata.php?year=2018&pos=QB&college=">NFL Combine Results website</a>. The data was retrieved for the year 2018 and specifically for quarterbacks. The data was organized in an HTML table format. The structure of the dataset included rows corresponding to players, with columns representing different combine metrics such as "Name," "40 Yard Dash," "Vertical Leap," "Broad Jump," "Shuttle," and "3Cone." These metrics were used to calculate the combine score for each player. The dataset provided insights into the combine performance of players, which was then combined with other data to analyze the correlation between combine performance and NFL career success.

## 🗂️ Dataset 3: ESPN Sport Core API Data
The ESPN Sport Core API Data was used to retrieve <a href="https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes?limit=1000&active=true">NFL player information</a>, including career statistic and college career data. The data was obtained by making API requests to the ESPN API. The structure of the dataset was in JSON format and contained nested dictionaries. Each player's data was stored under the "athlete" key, with nested dictionaries representing different seasons of their career. This dataset provided comprehensive information about player performance across their entire NFL career. It was used to calculate career success scores and gain insights into the relationship between player performance and career success. The data from this dataset was combined with other datasets, such as combine scores, to draw meaningful conclusions.

## 🤝 Contacts
- [Dylan Both (Data Analyst)](https://www.linkedin.com/in/dylan-both-31a17b216/)
- [Rian Rahman (Data Analyst)](https://github.com/RiRah123)


