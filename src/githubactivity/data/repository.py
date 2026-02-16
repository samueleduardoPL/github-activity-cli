import json
import urllib.request
from urllib.error import HTTPError, URLError




def fetch_user_activity(username: str) -> list[dict]:

    """
    Retrieves a list of events from the GitHub API for a given username.

    Args: 
        username (str): GitHub username.

    Returns:
        list[dict]: A list of events structured as dictionaries 
                    returned by the GitHub API.

    """

    url = f"https://api.github.com/users/{username}/events"
    

    try: 
        with urllib.request.urlopen(url) as response:
            raw_data = response.read()  
            text_data = raw_data.decode("utf-8")
            data = json.loads(text_data)
            return data
    
    except HTTPError as e:
        if e.code == 404:
            print(f"User: '{username}' not found.")
        elif e.code == 403:
            print(f"Rate limit exceeded. Try again later.")
        else:
            print(f"HTTP Error {e.code} for {username}")
        
        return []
    
    except URLError as e:
        print(f"URL Error: {e.reason} for {username}")
        return []
    




