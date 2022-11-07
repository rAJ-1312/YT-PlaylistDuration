# YT-PlaylistDuration


<!-- TABLE OF CONTENTS -->
## Table of Contents
- [YT-PlaylistDuration](#yt-playlistduration)
  - [Table of Contents](#table-of-contents)
  - [## About The Project](#-about-the-project)
  - [Built with](#built-with)
  - [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Get Playlists Duration](#get-playlists-duration)
  - [For Contribution](#for-contribution)
  - [License](#license)


<!-- ABOUT THE PROJECT -->
## About The Project
---
<br>

__Problem__: If you ever wished to watch any youtube-playlist and wondered how long it will take to complete the whole playlist like the total duration of the playlist in that case Youtube doesn't provide any information regarding that.

__Solution__: You can use this script to find the duration of any playlist, not just one but you can find the durations of all the playlists any channel has in just one go. The only thing you will need is the **YT-channel ID**.
<br><br>





## Built with

* [python](https://www.python.org/downloads/release/python-3106/)
* [google-api-client](https://github.com/googleapis/google-api-python-client/)



<!-- GETTING STARTED -->
## Getting Started

Clone the repo to get started with the bot.

## Prerequisites

* Python 3.x
* Channel_ID: To get the channel ID of any Youtube Channel you can visit this [Get Channel ID](https://commentpicker.com/youtube-channel-id.php) and simply paste any of the recent video link of the channel whose ID you want to find.
After getting the channel ID you can proceed with the script to get the duration of all the playlists of that channel.
<br><br>

## Installation
 
1. Clone the repo
```sh
git clone https://github.com/rAJ-1312/YT-PlaylistDuration.git
cd YT-PlaylistDuration
```
2. Installing required pip packages
```sh
pip3 install -r requirements.txt
```
3. Create a .env file in the same directory:
```sh
touch .env
```
4. Now inside that .env file you will have to insert one entry which will be the api key to make api calls. Go through this [Generate API-KEY](https://support.google.com/googleapi/answer/6158862?hl=en) if you face any difficulty in generating API key. After getting the key, put it in the `.env` file in the given format
```sh
API_KEY = *******************************
```

1. Run the script passing the channel id as argument
```sh
python3 main.py *****************
e.g. python3 main.py UCCezIgC97PvUuR4_gbFUs5g
```

<!-- USAGE EXAMPLES -->
## Usage
<br>

### Get Playlists Duration
<br>

<p align="center">
  <img align="center" src="docs.png?raw=true" alt="bot.jpg" width="530">
</p>

<br>

<!-- CONTRIBUTING -->
## For Contribution

“One of the marvelous things about community is that it enables us to welcome and help people in a way we couldn't as individuals.” – *Jean Vanier* 
Any contributions you make are _*most welcomed*_.

Just follow these steps :smile: : 
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/ur_feature`)
3. Commit your Changes (`git commit -m 'feat: Add some features'`)
4. Push to the Branch (`git push origin feature/ur_feature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.

****
