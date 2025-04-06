import os
import pickle
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_credentials():
    """Gets valid user credentials from storage.

    Returns:
        Credentials, the obtained credential.
    
    Raises:
        ValueError: If GOOGLE_CREDENTIALS_PATH environment variable is not set
        FileNotFoundError: If the credentials file doesn't exist
    """
    credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH')

    if not credentials_path:
        raise ValueError(
            "GOOGLE_CREDENTIALS_PATH environment variable is not set. "
            "Please set it in your .env file."
        )

    if not os.path.exists(credentials_path):
        raise FileNotFoundError(
            f"Credentials file not found at {credentials_path}. "
            "Please ensure the file exists and the path is correct in your .env file."
        )

    # Store token.pickle in the same directory as credentials file
    secrets_dir = os.path.dirname(credentials_path)
    token_path = os.path.join(secrets_dir, 'token.pickle')
    
    creds = None
    # Load existing token if it exists
    if os.path.exists(token_path):
        try:
            with open(token_path, 'rb') as token:
                creds = pickle.load(token)
        except (EOFError, pickle.UnpicklingError):
            # If token file is corrupted, we'll create a new one
            creds = None

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Save the credentials for the next run
        os.makedirs(secrets_dir, exist_ok=True)  # Ensure directory exists
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds 
