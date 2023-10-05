# A Comparative Study of Closed Issues in TensorFlow and PyTorch Frameworks

This repository contains a comparative study of closed issues in the TensorFlow and PyTorch frameworks. The study focuses on five metrics of closed issues: Time To Close, Number of Assignee, Number of Comments, Number of Labels, and Type of Issue. The goal of this study is to gain insights into the behavior and performance of bug fixing process in these two popular deep learning frameworks. 


## Data Collection 

The data for this study was collected from the Github API using the PyGithub library, focusing on closed issues from the last two years. The aim of the data collection process was to gather relevant information about the closed issues in order to conduct a comprehensive analysis. This information included details such as the time to close, number of assignees, number of comments, and type of issue. The data collection process was carefully designed to ensure the accuracy and completeness of the information gathered. The results of this study provide valuable insights into the performance and behavior of the issue tracking systems in the targeted projects.

I conducted a systematic examination of the closed issues reported to the GitHub projects of PyTorch and TensorFlow over the last two years and discovered that the TensorFlow framework had 4,662 closed issues, whereas the PyTorch framework had 4,244 closed issues. This well-balanced dataset is a valuable resource for conducting a comprehensive analysis of the two frameworks and provides a basis for understanding the relative performance of each framework in terms of issue resolution.

<p> <strong>Note that </strong>during the data collection process, I performed feature engineering on the starting and closing dates of the issues. I calculated the difference between these dates in order to obtain a more meaningful representation of the data. This allowed me to gain a deeper understanding of the duration of each issue and to identify trends and patterns related to issue resolution time.</p>

<p>Another <strong>Note</strong> is that I collected the titles of the issues for text mining and topic modeling analysis.</p>


### Justification for the Metrics Choice
* **Time to Close**: This metric represents the elapsed time between the creation and closure of an issue. It provides insight into the efficiency of issue resolution and highlights any delays in addressing certain types of issues.

* **Number of Assignees**: This metric represents the number of individuals assigned to an issue. It provides information on the level of collaboration required to resolve the issue and highlights any differences in the number of people assigned to different types of issues.

* **Number of Comments**: This metric represents the number of comments made on an issue. It provides information on the level of discussion and collaboration required to resolve the issue and highlights any differences in the number of comments for different types of issues.

* **Number of Labels**: This metric represents the number of labels associated with an issue. It provides information on the different aspects of the issue addressed and highlights any differences in the number of labels for different types of issues.

* **Type of Issue**: This metric represents the type of issue, such as bug, feature request, enhancement, etc. It provides information on the nature of the issue and highlights any differences in the types of issues reported.


## Data Preprocessing

Prior to the analysis, the data underwent a preprocessing step to eliminate any irrelevant or incomplete data. The data was transformed into a format that was appropriate for analysis. This involved the following specific actions:
 
* Conducting feature engineering on the Type of Issue attribute in order to categorize it into Type and Priority.
* Encoding the Type and Priority categories into numerical values for visualization purposes.
* Removing instances of ReadMe issues, as they do not provide relevant information about the bug fixing process.
* Conducting text mining on the issue descriptions to gauge the diversity of issues presents in the two Framework.

## Analysis

A comparative analysis was performed on the closed issues of the PyTorch and TensorFlow frameworks. This analysis helps identify the strengths and weaknesses of each framework, as well as potential areas for improvement. For the **additional analysis**, I used Text Mining Text Mining and NLP for Topic Modeling. Details for the analysis are in the "The analysis Notebook.ipynb".

## Results 
### From The 5 Metrics
* TensorFlow seems to have a larger and more established community compared to PyTorch. It has a substantial community of developers who actively contribute to the maintenance and development of the framework. This large developer community is likely to result in a higher number of bugs being reported and subsequently addressed.
* TensorFlow could have an extensive array of tools and libraries.
* PyTorch are more straightforward to understand and resolve, or that the PyTorch community prioritizes brevity in their discussions and solutions.
* The majority of closed issues in PyTorch lack assigned individuals or teams, which could indicate a less organized community, fewer contributors, less complex issues, or an internal handling preference. Without further information, the exact reason is uncertain.
* PyTorch's closed issues with fewer comments are more broadly categorized compared to TensorFlow's closed issues. This is in line with the fact that the majority of PyTorch issues are resolved more quickly, often within a day.
* The correlation between Number of Labels and Time to Close in both datasets is somehow fair. This suggests that issues with more labels might be more complex or have more components to them, leading to a longer resolution time.
* After conducting experiments with varying values of PCA (200, 100, etc.), it was observed that there were distinct clusters present in the issue titles of the PyTorch framework. However, the issue titles in the TensorFlow framework did not show clear separations and appeared to overlap with each other.

### For the additional Analysis: Data Mining and NLP 

* TensorFlow has two clusters in its issues titles. The first cluster focuses on general errors, building issues, and GPU-related issues. The second cluster discusses issues and errors related to the model.
* PyTorch also has two clusters in its issues titles. The first cluster focuses on GPU-related issues, general errors, and building issues. The second cluster deals with issues related to make test and disabling torch dynamo.

## Limitations

* While the **number of reviews** can provide insight into the level of testing, review, and validation of the solution for the bug, it is not available in the data collected through PyGithub as it does not provide information on the number of reviewers of closed issues that are not pull-requests.

* The data utilized in this comparative study is restricted to a two-year time frame, thus the conclusions drawn may not accurately represent the long-term functioning of the issue tracking systems in TensorFlow and PyTorch. Furthermore, the analysis only encompasses closed issues, and as a result, the findings may not provide a comprehensive understanding of the issue tracking systems in these frameworks.

## Further Work 

* It is possible to contribute to adding a feature in pyGithub for the number of reviews. 
* Using Natural Language Processing (NLP), we can scrape the content of the closed issues and the comments. Then, the content of closed issues can shed light on the types of problems that are frequently encountered. This insight can help in identifying areas for improvement in the issue tracking process and overall software development process. Furthermore, the analysis of the content of closed issues and comment content can also provide information on the level of technical support provided to users and the overall user experience.
* Sentiment analysis of issues and comments for that issue: (1) Breakdown of sentiment per user and types of issues (2) Analysis of Issue Titles: Looking to have better descriptive titles.
* We could use Time-Series Analysis. This type of analysis involves analyzing the issues content over time, including the number of new issues reported, the time taken to resolve issues, and the frequency of specific types of issues.
* We could also have User Analysis. This type of analysis involves studying the behavior and characteristics of the users who reported the issues, including their location, device, and language.

 


