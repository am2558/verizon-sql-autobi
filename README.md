# verizon-sql-autobi

Auto-BI tool to generate SQL queries for Verizon's datasets.

<!--
Project repo instructions
https://lms.ecornell.com/courses/1788003/pages/step-1-ensure-your-project-repo-is-complete-by-dec-8th-team-to-do

Project README instructions
https://lms.ecornell.com/courses/1788003/pages/step-2-ensure-your-project-readme-is-complete-by-dec-8th-team-to-do
-->

## Project Overview



Objective: BI tool for natural language data interaction.
Scope: Supports multiple metadata types and SQL dialects.
NLP Focus: Conversational and keyword query support.
Output: Generate SQL, visualize results, automate insights.

?
Create metadata for Network Performance dataset to help LLM create SQL queries
○ What do the columns mean, intuitively? What is the table about? What kinds of
questions will users ask? All of this is good context for an LLM.
● Develop prompts for LLM to instruct SQL query creation process\
○ Will need to research which LLM will be best for SQL query generation
● Leverage LLM to generate SQL queries related to Network Performance dataset
○ Use similar interactive tool to validate creation of SQL queries and improve
prompting used (e.g. take user feedback and integrate to future prompts as few
shot learning)

## Objectives and Goals

Enhanced Decision-Making: Users access insights and visualizations independently.
Multi-Unit Support: Consistent analysis for Verizon executives, business, and IT teams.
Time & Accuracy: Automates SQL, reduces errors, speeds analysis.
User-Friendly: NLP simplifies data access for non-technical users.

## Methodology

Prompt training: GPT interprets natural language with metadata.
Enhanced capabilities: Image reading and file handling could be added.
Visualization: Direct chart/graph generation from queries could be added.
Pivot decision: Shifted focus to Gemini, simplifying scope.

## Results and Key Findings

GitHub: https://github.com/am2558/verizon-sql-autobi/tree/main

Deployed: https://verizon-sql-autobi.onrender.com/

## Visualizations

## Potential Next Steps

Combining the two projects:
● Integrate RLAIF (Reinforcement Learning with AI Feedback, as opposed to RLHF or
Reinforcement Learning with Human Feedback) into the interactive tool for evaluating
CV model performance.
○ For a given set of images, use autoBI to query the network dataset about network
performance at the location of each image.
○ Use the relative Network Performance at those sites to determine if foliage might
be driving poor performance
■ Will need to think through how to best evaluate this, as many factors
could be at play, team will need to determine which features will
contribute to determining performance issues with foliage as root cause
(maybe images for same site from different times in the year?).
○ Based on the performance evaluation, label images on 1-10 scale for likely
density of tree canopy (1 not at all dense, 10 very dense)
○ Compare human feedback to AI-based feedback
● Final deliverable - report on overarching project and performance of RLAIF vs. RLHF

## Individual Contributions

## Sample Datasets

<!-- Include sample datasets to help users test the project effectively. Ensure that any datasets used are properly licensed and that users understand how to access the data. -->

The dataset we used for testing is [Telco Customer Churn](https://www.kaggle.com/datasets/abdallahwagih/telco-customer-churn?resource=download) by Kaggle. To download this dataset, run the following command in your terminal:

```
curl -L https://www.kaggle.com/api/v1/datasets/download/abdallahwagih/telco-customer-churn -o telco-customer-churn.zip
```

## Colab Notebooks

<!-- Provide example notebooks demonstrating how to implement your project, including any relevant code snippets, visualizations, and explanations of the logic behind your models. -->

## Installation Instructions

<!-- Include step-by-step instructions on how to set up the project locally, install dependencies, train the model, and evaluate its performance. Consider using a requirements.txt file for Python dependencies. -->
