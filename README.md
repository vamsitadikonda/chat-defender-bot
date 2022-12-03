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
[![GitHub Super-Linter](https://github.com/nvuillam/npm-groovy-lint/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

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
3) The current model can be extended to detect spam users
4) Pre-evaluate a message at sender before posting
5) In the curent system, the bot has complete control over identifying profanity. As the model can be wrong at times, moderators can be introduced to check the model performance.
6) Similar to the profanity checker that is being implemented, an apology checker can also be developed to better identify apologies.

## Tech Stack
<img src="https://drive.google.com/uc?export=view&id=1jREu_hnGJ1gxv6hx2KMmM1zzHc8Yhvdh" alt="python" width="20" height="20"/> Python </br>
<img src="https://drive.google.com/uc?export=view&id=1Jnn5fThJOy1WMnlQcDyOHMdt2dB8imws" alt="MySql" width="20" height="20"/> MySql </br>
<img src="https://drive.google.com/uc?export=view&id=17444V8CAig18_kQ9gQHY1ZX1JXObFMoz" alt="Docker" width="20" height="20"/> Docker </br>
<img src="data:image/png;base64,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p" alt="Redis" width="20" height="20"/> Redis </br>

Check out our code documentation [here](https://www.vamsitadikonda.com/chat-defender-bot) 

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

