# Google Calendar Authentication

This module provides authentication functionality for the Google Calendar API.

## Setup Instructions

1. Create a Google Cloud Project:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google Calendar API for your project

2. Create OAuth 2.0 Credentials:
   - In the Google Cloud Console, go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" and select "OAuth client ID"
   - Choose "Desktop app" as the application type
   - Download the client configuration file (it will be named something like `client_secret_XXXXX.json`)

3. Set up the environment:
   - Create a `.env` file in your project root and add:
     ```
     GOOGLE_CREDENTIALS_PATH=/path/to/your/client_secret_XXXXX.json
     ```
   Replace the path with the actual path to your downloaded credentials file.

## Usage

The authentication module provides a `get_calendar_credentials()` function that handles the OAuth2 flow. On first run, it will open a browser window for you to authorize the application. After authorization, the credentials will be saved in a `token.pickle` file for future use.

Example usage:

```python
from googleapiclient.discovery import build
from agentic_workspace.tools.google_calendar.auth import get_calendar_credentials

# Get credentials
creds = get_calendar_credentials()

# Build the Google Calendar API service
service = build('calendar', 'v3', credentials=creds)

# Now you can use the service to interact with Google Calendar
```

See `notebooks\calendar_event_example.ipynb` for a complete example of how to use the authentication to list upcoming calendar events.

## Security Notes

- Keep your client secrets file secure and never commit it to version control
- The `token.pickle` file contains your access tokens - keep it secure
- If you modify the SCOPES, delete the `token.pickle` file to force a new authorization 
