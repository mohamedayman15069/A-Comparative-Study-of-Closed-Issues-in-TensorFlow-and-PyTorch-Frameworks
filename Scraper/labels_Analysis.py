from github import Github
from datetime import datetime, timedelta
from utils import get_issues, writing_in_file



def __main__(): 
    g = Github("ADD YOUR TOKEN HERE")
    # set the date two years ago
    two_years_ago = datetime.now() - timedelta(days=365*2)
    PyT_issues = get_issues(g, 'pytorch/pytorch', state='closed', since=two_years_ago)
    TF_issues = get_issues(g, 'tensorflow/tensorflow', state='closed', since=two_years_ago)

    pt_states = writing_in_file(PyT_issues, 'pt_states.txt')
    tf_states = writing_in_file(TF_issues, 'tf_states.txt')

    #compare the two sets
    print(pt_states.difference(tf_states))

    #How much difference between them?
    print(len(pt_states.difference(tf_states)))


if __name__ == "__main__":
    __main__()