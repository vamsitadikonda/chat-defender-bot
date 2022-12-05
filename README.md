# Chat-Defender-bot
[![License](https://img.shields.io/badge/License-BSD_2--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Build](https://github.com/vishnuchalla/chat-defender-bot/actions/workflows/python-app.yml/badge.svg)](https://github.com/vishnuchalla/chat-defender-bot/actions)
[![DOI](https://zenodo.org/badge/543915548.svg)](https://zenodo.org/badge/latestdoi/543915548)
[![GitHub Release](https://img.shields.io/github/release/vishnuchalla/chat-defender-bot)](https://github.com/vishnuchalla/chat-defender-bot/releases/)
![Python](https://img.shields.io/badge/python-v3.8+-yellow.svg)
![GitHub issues](https://img.shields.io/github/issues/vishnuchalla/chat-defender-bot)
![GitHub closed issues](https://img.shields.io/github/issues-closed/vishnuchalla/chat-defender-bot)
![Lines of code](https://img.shields.io/tokei/lines/github/vishnuchalla/chat-defender-bot)
[![codecov](https://codecov.io/gh/vishnuchalla/chat-defender-bot/branch/main/graph/badge.svg?token=h4F94IJMzj)](https://codecov.io/gh/vishnuchalla/chat-defender-bot)
[![Repo Size](https://img.shields.io/github/repo-size/vishnuchalla/chat-defender-bot?color=brightgreen)](https://github.com/vishnuchalla/chat-defender-bot.git)
[![contributors](https://img.shields.io/github/contributors/vishnuchalla/chat-defender-bot)](https://github.com/vishnuchalla/chat-defender-bot/graphs/contributors)
[![commit-activity](https://img.shields.io/github/commit-activity/w/vamsitadikonda/chat-defender-bot?color=blue)](https://github.com/vamsitadikonda/chat-defender-bot/graphs/commit-activity)
[![pull-requests-open](https://img.shields.io/github/issues-pr/vamsitadikonda/chat-defender-bot?color=yellow)](https://github.com/vamsitadikonda/chat-defender-bot/pulls)
[![pull-requests-closed](https://img.shields.io/github/issues-pr-closed/vamsitadikonda/chat-defender-bot?color=green)](https://github.com/vamsitadikonda/chat-defender-botpulls?q=is%3Apr+is%3Aclosed)
[![languages](https://img.shields.io/github/languages/count/vamsitadikonda/chat-defender-bot)](https://github.com/vamsitadikonda/chat-defender-bot)
[![forks](https://img.shields.io/github/forks/vamsitadikonda/chat-defender-bot?style=social)](https://github.com/vamsitadikonda/chat-defender-bot/network/members)

## About
Chat-Defender-bot : A Discord Bot to prevent cyberbullying and hate speech in chatrooms.

The chat bot built in this project evaluates the text data whenever a message is sent onto the the discord group. If any offensive behaviour is observed, the user will be warned initially, before they are banned from the chat group. A user who receives a warning can apologize to the others in the group if they do not want to be further penalized later for the offense. Their behaviour data will be updated accordingly in the database. The database keeps updating based on the user inputs on which words should be considered as profanity. This bot can be highly customized according to the needs of the chat group, and has a huge scope of users.


## Implementation Steps
Refer to INSTALL.md for detailed implementation steps
## Video Link
https://drive.google.com/file/d/1LNjVeSV_3JWVeWB_Lr11941LlmDSVAg8/view?usp=sharing
## Future Scope
1) The in-build detoxify() function  being used in this project is highy sensitive, so a model can be developed to adapt better to real world conversations, using desired datasets.
2) The message data that is being evaluated in the current model is text. This can be expanded to detect profanity through other input sources such as image, video, GIF, etc.
3) The current model can be extended to detect spam users.
4) Currently Apology checker is checking the sentiment of the text and looking for apology bag of words this can be improved by using an NLP custom apology model

## Tech Stack
<img src="https://drive.google.com/uc?export=view&id=1jREu_hnGJ1gxv6hx2KMmM1zzHc8Yhvdh" alt="python" width="20" height="20"/> Python </br>
<img src="https://drive.google.com/uc?export=view&id=1Jnn5fThJOy1WMnlQcDyOHMdt2dB8imws" alt="MySql" width="20" height="20"/> MySql </br>
<img src="https://drive.google.com/uc?export=view&id=17444V8CAig18_kQ9gQHY1ZX1JXObFMoz" alt="Docker" width="20" height="20"/> Docker </br>
<img src="https://github.com/Spartee/redis-vector-search/blob/master/app/vecsim_app/data/redis-logo.png?raw=true" alt="Redis" width="20" height="20"> Redis </br>

Check out our code documentation [here](https://sumanthbsundar.github.io/discord_chat_bot_doc/) 

:sparkles: Contributors
---

<table>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/srujanponnur">Srujan Ponnur</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/sumanth-somasundar">Sumanth Somasundar</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/vishnuchalla/">Vishnu Challa</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/svnsairam/">Sairam Sakhamuri</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/kanchan-rawat-793753a2/">Kanchan Rawat</a></td>
  </tr>
</table>

:email: Support
---

For any queries and help, please reach out to us at: vchalla2@ncsu.edu

