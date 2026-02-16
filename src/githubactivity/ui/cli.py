from githubactivity.domain.services import sort_events
import argparse


def run_cli() -> None:

    """
    Parses command-line arguments and executes the application logic.

    Handles user input and displays results or error messages.
    
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("username", type=str)

    args = parser.parse_args()

    event_types = sort_events(args.username)

    if not event_types:
        print("No events to print")
        return 

    for event_type, repos in event_types.items():
        for repo, count in repos.items():
            print(render_event(event_type, count, repo))

    


EVENT_TEMPLATES = {
  
    "CommitCommentEvent":
        "Commented on a commit in {repo} ({count} time/s).",

    "CreateEvent":
        "Created {count} branch/es or tag/s in {repo}.",

    "DeleteEvent":
        "Deleted {count} branch/es or tag/s in {repo}.",

    "DiscussionEvent":
        "Started or updated {count} discussion/s in {repo}.",

    "ForkEvent":
        "Forked {repo} ({count} time/s).",

    "GollumEvent":
        "Updated {count} wiki page/s in {repo}.",

    "IssueCommentEvent":
        "Commented on {count} issue/s in {repo}.",

    "IssuesEvent":
        "Opened or closed {count} issue/s in {repo}.",

    "MemberEvent":
        "Added or removed {count} collaborator/s in {repo}.",

    "PublicEvent":
        "Made {repo} public ({count} time/s).",

    "PullRequestEvent":
        "Opened, closed, or merged {count} pull request/s in {repo}.",

    "PullRequestReviewEvent":
        "Reviewed {count} pull request/s in {repo}.",

    "PullRequestReviewCommentEvent":
        "Commented on {count} pull request review/s in {repo}.",

    "PushEvent":
        "Pushed {count} commit event/s into {repo}.",

    "ReleaseEvent":
        "Published {count} release/s in {repo}.",

    "WatchEvent":
        "Starred {repo} ({count} time/s).",
}

        

def render_event(event_type : str, count : int, repo : str) -> str:

    """
    Formats a GitHub event into a human-readable sentence.

    Args:
        event_type (str): Type of event eg.: "PushEvent"
        count (int): The amount of times this event happened in the repository
        repo (str): GitHub repository in which the event occurred

    Returns:
        str: A formatted string describing the event.
    """
    template = EVENT_TEMPLATES.get(event_type, "Unspecified event '{event_type}' occurred {count} time/s in {repo}.")

    sentence = template.format(event_type=event_type, count=count, repo=repo)

    return sentence


        
    
    
