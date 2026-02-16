from githubactivity.data.repository import fetch_user_activity


def sort_events(username: str) -> dict[str, dict[str, int]]:
    """
    Sorts the events given by the github API.

    Args:
        username (str): GitHub username.
    
    Returns:
        dict[str, dict[str, int]]: A dict of events, in which each event contains
                                 its own dictionary of repos in which the said 
                                 event occurred at least 1 time.
    """

    raw_events = fetch_user_activity(username)

    if not raw_events:
        return {}

    event_types = {}

    for i in raw_events:

        event_type = i["type"]
        repo = i["repo"]["name"]

        if  event_type not in event_types:
            event_types[event_type] = {repo : 1}
        else:
            if repo in event_types[event_type]:
                event_types[event_type][repo] += 1
            else:
                event_types[event_type][repo] = 1

    return event_types




        


        


