# ERLC Server Overlay

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

This is a simple Flask web application that provides a web overlay to display server and player information for an ERLC (Emergency Response: Liberty County) private server. It uses the [policeroleplay.community API](https://apidocs.policeroleplay.community/).

## Features

-   Displays general server information.
-   Shows player counts for each team (Civilian, Police, Sheriff, Fire, DOT).
-   Provides a simple and clean HTML template to visualize the data.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ERLC-Overlay.git
    cd ERLC-Overlay
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your API Key:**
    -   Rename the `.env.example` file to `.env`.
    -   Open the `.env` file and add your API key from the policeroleplay.community website:
        ```
        API_KEY="your_api_key_here"
        ```

4.  **Configure OBS:**
    -   In OBS Studio, add a new "Browser" source.
    -   Set the URL to `http://localhost:8000`.
    -   Adjust the width and height as needed.

## How to Use

To start the overlay, simply run the following command in the project directory:

```bash
python main.py
```

The application will then be accessible at `http://localhost:8000`, and the OBS Browser source will become active.