from github import Github
from datetime import datetime, timedelta
from utils import get_issues, write_issues_to_csv



def __main__():
    # authenticate with the token
    ACCESS_TOKEN = ""
    g = Github(ACCESS_TOKEN)
    # set the date two years ago
    two_years_ago = datetime.now() - timedelta(days=365*2)

    #Pytorch
    issues = get_issues(g, 'pytorch/pytorch', state='closed', since=two_years_ago)
    # write issues to a CSV file
    write_issues_to_csv(g, issues, 'PyTorch_issues.csv', ['Issue Number', 'Issue Title', 'Time to Close', 'Number of Assignees','Number of Comments', 'Number of Labels', 'Type of Issue'])

    #Tensorflow
    issues = get_issues(g, 'tensorflow/tensorflow', state='closed', since=two_years_ago)
    # write issues to a CSV file
    write_issues_to_csv(g,issues, 'Tensorflow_issues.csv', ['Issue Number', 'Issue Title', 'Time to Close', 'Number of Assignees', 'Number of Comments', 'Number of Labels', 'Type of Issue'])


if __name__ == "__main__":
    __main__()