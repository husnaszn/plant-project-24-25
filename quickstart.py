import os
import requests
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete the file token.json.
# SCOPES = [
#     'https://www.googleapis.com/auth/photos.upload',
#     'https://www.googleapis.com/auth/photoslibrary'
# ]
SCOPES = [
    'https://www.googleapis.com/auth/photoslibrary',
    'https://www.googleapis.com/auth/photoslibrary.sharing',
    'https://www.googleapis.com/auth/photos.upload'
]



"""
def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
"""
def authenticate():
    creds = None
    # Check if token.json exists
    if os.path.exists('token.json'):
        try:
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        except Exception as e:
            print(f"Failed to load credentials: {e}")

    # Check if credentials are valid
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
                print("Token refreshed successfully.")
            except Exception as e:
                print(f"Failed to refresh token: {e}")
                creds = None
        else:
            # Start the OAuth flow
            try:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                print("User authenticated successfully.")
            except Exception as e:
                print(f"Failed to authenticate user: {e}")
                return None

        # Save the credentials for the next run
        if creds:
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
            print("Credentials saved to token.json.")

    return creds


def upload_photo(creds, photo_path, album_id=None):
    url = 'https://photoslibrary.googleapis.com/v1/uploads'
    
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type': 'application/octet-stream',
        'X-Goog-Upload-File-Name': os.path.basename(photo_path),
        'X-Goog-Upload-Protocol': 'raw'
    }

    # Upload the photo
    with open(photo_path, 'rb') as photo_file:
        response = requests.post(url, headers=headers, data=photo_file)

    if response.status_code == 200:
        upload_token = response.text
        print('Upload successful! Upload token:', upload_token)
        
        # Create a media item
        create_body = {
            "newMediaItems": [
                {
                    "description": "Uploaded via API",
                    "simpleMediaItem": {
                        "uploadToken": upload_token
                    }
                }
            ]
        }

        # If you have an album ID, add the media item to it
        if album_id:
            create_body["albumId"] = album_id

        # Call the batchCreate endpoint
        create_url = 'https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate'
        create_response = requests.post(create_url, headers={'Authorization': f'Bearer {creds.token}'}, json=create_body)

        if create_response.status_code == 200:
            print('Media item created successfully:', create_response.json())
        else:
            print('Failed to create media item:', create_response.json())
    else:
        print('Upload failed:', response.content)

def list_albums(creds):
    url = 'https://photoslibrary.googleapis.com/v1/albums'
    headers = {
        'Authorization': f'Bearer {creds.token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        albums = response.json().get('albums', [])
        if not albums:
            print("No albums found.")
        else:
            print("Albums:")
            for album in albums:
                print(f"Title: {album['title']}, ID: {album['id']}")
    else:
        print('Failed to retrieve albums:', response.content)

def main():
    creds = authenticate()
    photo_path = '/home/picuteness/Bookshelf/pls/photo_2024-09-$d_12-09-52.jpg'  # Update with your photo path
    album_id = "AEgp6Z_hoDbDJ8mEDdt3lCFye8Wq7D6CnuyrAQRQwH9mJDDu1hSWnmbeoNJXr2Lxe7JsdSvwUUG-" # Optionally, specify an album ID to upload to
    upload_photo(creds, photo_path, album_id)
    list_albums(creds)

if __name__ == '__main__':
    main()