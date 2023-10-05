import csv 
from github import Github
from github import RateLimitExceededException
from github.GithubException import GithubException
import time
import calendar
import logging



def writing_in_file(issues, file_name):
    """ًWriting the Label issues in a file_name
    Args:
        issues (list): List of issues.
        file_name    : (str): Name of the CSV file.
    Returns:
        None
    """
    states = set()

    for issue in issues:
        for label in issue.labels:
            states.add(label.name)
    
    with open(file_name, 'w') as f:
        for item in states:
            f.write("%s " % item)
    
    return states



def set_labels(issue):
    """Set labels of an issue.
    Args:
        issue (Issue): Issue object.
    Returns:
        list: List of labels.
    """
    # label Classifications are ["Bug", "Critical", "Question", "Documentation", "critical", "enhancement", "Minor", "Other"]
    labels = []
    label_mapper = {"bug":"Bug",
                    "critical":"Critical",
                    "documentation":"Documentation",
                    "enhancement":"enhancement",
                    "feature": "enhancement",
                    "enhanc": "enhancement",
                    "question": "Question",
                    "high priority": "Critical",
                    "high-priority": "Critical",
                    "vulnerab": "Critical",
                    "low priority": "Minor",
                    "low-priority": "Minor",
                    "minor": "Minor",
                    "segfault": "Bug",
                    "error": "Bug",
                    "crash": "Critical",
                    }
    
    for label in issue.labels:
        for key in label_mapper:
            if key in label.name.lower() or key in issue.title.lower():
                #Check if the label is already in the list
                if label_mapper[key] not in labels:
                    labels.append(label_mapper[key])
    return labels



def get_issues(g, repo_name, state='closed', since=None):
    """Get issues of a repository.
    Args:
        repo_name (str): Name of the repository.
        state (str): State of the issues. Can be 'open', 'closed' or 'all'.
        since (datetime): Only issues updated at or after this time are returned.
    Returns:
        list: List of issues.
    """
    while True: 
        try:
            repo = g.get_repo(repo_name)
            issues = repo.get_issues(state=state, since=since)
            break

        #Handle if we exceed the rate limit
        except RateLimitExceededException as e:
            search_rate_limit = g.get_rate_limit().search
            logging.info('search remaining: {}'.format(search_rate_limit.remaining))
            reset_timestamp = calendar.timegm(search_rate_limit.reset.timetuple())
            # add 10 seconds to be sure the rate limit has been reset
            sleep_time = reset_timestamp - calendar.timegm(time.gmtime()) + 10
            print("Rate Limit Exceeded", sleep_time)
            time.sleep(sleep_time)
            continue 
        
    return issues


def write_issues_to_csv(g, issues, filename, fieldnames):
    """Write issues to a CSV file.
    Args:
        issues (list): List of issues.
        filename (str): Name of the CSV file.
        fieldnames (list): List of field names.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # iterate over issues
        iter_obj = iter(issues)
        while True: # To wait if we exceed the rate limit
            try:
                issue = next(iter_obj)
                isPullRequest = False
                while True: #To wait if any problem happened in pull request and exceeded time-out
                    try:
                        if issue.pull_request:
                            isPullRequest = True
                            break
                        else:
                            break
                    except GithubException as e:
                        print(e)
                        continue
                if isPullRequest:
                    continue

                issue_type = set_labels(issue)
                writer.writerow({'Issue Number': issue.number,
                                'Issue Title': issue.title,
                                'Time to Close': (issue.closed_at-issue.created_at).days,
                                'Number of Assignees': len(issue.assignees),
                                'Number of Comments': issue.comments,
                                'Number of Labels': len(issue.labels),
                                'Type of Issue': issue_type if len(issue_type) > 0 else ['Other']
                                })
            
            except StopIteration:
                break
            
            #Handle if we exceed the rate limit
            except RateLimitExceededException: 
                search_rate_limit = g.get_rate_limit().search
                logging.info('search remaining: {}'.format(search_rate_limit.remaining))
                reset_timestamp = calendar.timegm(search_rate_limit.reset.timetuple())
                # add 10 seconds to be sure the rate limit has been reset
                sleep_time = reset_timestamp - calendar.timegm(time.gmtime()) + 10
                print("Rate Limit Exceeded", sleep_time)
                time.sleep(sleep_time)
                continue 
    
