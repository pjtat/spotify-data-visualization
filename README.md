# Spotify Listening Analysis with Tableau

A data visualization project that transforms your personal Spotify listening history into interactive Tableau dashboards, providing insights into your music listening habits.

## Prerequisites
- Spotify Account (Free or Premium)
- Tableau Public
- Python 

## Features 
- Python script to preprocess Spotify data
- Pre-configured Tableau dashboard with various visualizations such as:
  - Most played songs/artists/albums by year/all time
  - Top new songs/artists/albums of the year
  - Most listened to genres 
  - ...

## Installation & Setup

1. **Request Your Spotify Data**
   - Go to [Spotify Account Privacy Settings](https://www.spotify.com/us/account/privacy/)
   - Check 'Extended streaming history'
   - Click 'Request Data'
   
   *Note: Full data delivery takes approximately 30 days*

2. **Get the Project**
   ```bash
   git clone https://github.com/pjtat/spotify-tableau-data-visualization.git
   cd spotify-tableau-data-visualization
   ```

3. **Data Preparation**
   - Once you receive your Spotify data, extract the files
   - Place your `StreamingHistory*.json` files in the `data/raw` directory
   - Run the preprocessing script:
     ```bash
     python src/main.py
     ```

4. **Tableau Setup**
   - TBD

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.