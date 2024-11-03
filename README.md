# Spotify Listening Analysis with Tableau

This project provides Tableau Public dashboards configured to analyze personal Spotify listening history. Personal listening history can be obtained from Spotify via a request process. 

## Data Source
- Personal Spotify account data requested through Spotify's official data download process
- Data includes listening history, duration, geographical locations, and other user activity 

## Features
- Listening duration for songs/artists/albums for a customizable duration 
- Top new albums for a customizable duration
- *TBD*

## Prerequisites
- Tableau Public
- Spotify Account (Paid or Free)

## Installation

1. Request Spotify Listening History (It typically takes ~30 days to receive your full listening history)

- Navigate to your Account Privacy page (https://www.spotify.com/us/account/privacy/)
- Select the 'Select Extended streaming history' checkbox
- Select Request Data 

(This is the process as of Nov 3, 2024)

**Note:** Spotify will first provide you with a preview of your listening history. The dashboard here requires the **full** listening history. 

2. Clone this repository:
   ```
   git clone https://github.com/pjtat/spotify-tableau-data-visualization.git
   ```

3. Download Tableau Public (https://public.tableau.com/app/discover)

4. Open the Tableau Dashboards in this repository

5. Add your Spotify listening history to the project 

**Note:** You may have multiple files to encompass all of your listening history. If so, please combine them as a *Union* in Tableau. (https://help.tableau.com/current/pro/desktop/en-us//joining_tables.htm)