# TPM34A - Machine learning for socio technical system (Q2 - 2022)

This is the official repo for the TPM34A - Machine learning for socio-technical systems course. In this ReadMe file, you will find all the information and instructions for this course. This repo is mainly developed for Parts 1 and 2 of the course. But, we will update it with all course material. Please read the information below carefully.

**Before you start** If you are not familiar with Python, **you a strongly advised to do** [Python lab session 0](https://github.com/TPM34A/Q2_2022/blob/main/Lab_sessions/lab_session_00/lab_session_00.ipynb). Lab session 0 provides a crash course Python basics. These basics you will need to succesfully do lab sessions 1 to 3 as well as the assignments. It touches upon topics like, data structures, using external libraries, data exploration, visualization, etc. Also, it will help you set up and familiarise yourself with the coding environment (see [this](#instructions-to-set-up-your-workspace) to prepare your environment)

## Contents
1. [Description](#1-description) 
    - [Pre-requisites knowledge](#11-pre-requisites-knowledge)
2. [Notes](#2-notes)
3. [Calendar](#3-calendar)
4. [Q&A Forum](#4-qa-forum)
5. [Instructions to set-up your workspace](#5-instructions-to-set-up-your-workspace)
    - [Google Colab](#option-1-google-colab-recommended)
    - [Local environment](#option-2-local-environment-not-recommended---limited-support)

## 1. Description

Machine Learning (ML) is increasingly seen as a crucial part of the puzzle to solving the socio-technical challenges of today’s networked, urbanised, knowledge societies. Successful adoption of ML does, however, not only requires skilled computer scientists that do the hard-core programming. Also, professionals are needed that have both domain knowledge of socio-technical systems and sufficient understanding of ML.

This course aims to provide students in the socio-technical domain with a profound understanding of ML. It prepares students for the challenges and questions ML will pose to them in their later careers. To this end, the course consists of three parts:

- **Part 1:** Fundamentals of ML
- **Part 2:** Explainability of ML
- **Part 3:** Applications of ML for socio-technical challenges

In part 1, students learn about ML fundamentals and models. These weeks a critical technical foundation is laid for grasping the strength and weaknesses of ML for the analysis and design of socio-technical systems.

Part 2 is devoted to the explainability of ML. For public decision-making as well as for decision-making in high-stake contexts, such as e.g. autonomous vehicles, legal systems’ transparency and explainability of the models are of critical importance. Students learn several popular explainability techniques and discuss their value for application in socio-technical systems.

In Part 3, a rotating group of TPM scholars provides exemplar applications of ML in socio-tech systems. This serves two purposes: (1) to show where and how ML is applied for analysis and application in socio-technical systems, and (2) to deepen reflection on the impact of ML-based solutions and interventions on individuals, organisations, and society. Consecutively, students work in a group on a group project, building forth on one of the presented applications. This project brings together the three parts of this course. Students will need to apply ML models and techniques to real-world data in a notebook, interpret, and communicate their results, taking into account the socio-technical setting through a presentation.

The course consists of oral lectures, lab sessions, and assignments. The aim of the lab sessions is to show and reinforce how the ML models, explainable ML techniques and ML ideas presented in the oral lectures are put to practice. Also, they help students gather hands-on machine learning skills. The lab sessions involve a series of exercises in the form of Jupyter notebooks.

The course consists of 2 oral lectures and 1 lab session per week. Attendance of the lectures and lab sessions is highly recommended to keep up with the course, but not mandatory.

### 1.1. Prerequisite knowledge
We expect students have taken undergraduate courses on the following topics before coming to this course.
    – Statistics & Data analyses (e.g. hypothesis testing, correlation, etc.)
    – Python programming (basic level)

## 2. Notes
- This repo provides all the coding and lecture materials to develop your coding task during the course. It means you will primarily use this repo for Parts 1 and 3 of the course.
- We highly encourage to use **Google Colab**. However, if you insist to run the notebooks in your local environment (i.e. locally on your laptop), you can do so. Please find the instruction for doing so [here](#option-2-local-environment-not-recommended---limited-support))
- Make sure you use Python 3.7 or above
- The *requirements.txt* file contains all the Python dependencies needed to run the codes used in this course. In each notebook file, we provide two ways to set up your environments: (1) Google Colab and (2) Local ([see here](#5-instructions-to-set-up-your-workspace)). Note that this file may be updated during the course to include more dependencies.

## 3. Calendar

| Course Week | Lecture no |   Weekday |       Date |          Time | Teacher | Lecture type | Materials |
|:-----------:|:----------:|----------:|-----------:|--------------:|--------:|-------------:|----------:|
|      0      |      0     |           |            |               |  Sander |  Lab session | [Lab session 0](https://github.com/TPM34A/Q2_2022/blob/main/Lab_sessions/lab_session_00/lab_session_00.ipynb) |
|      1      |      1     |    Monday | 14-11-2022 | 13:45 - 15:45 |  Sander |      Opening |           |
|      1      |      2     | Wednesday | 16-11-2022 | 13:45 - 15:45 |  Sander | Oral lecture |           |
|      1      |      3     |  Thursday | 17-11-2022 | 13:45 - 15:45 |  Sander |  Lab session | [Lab session 1](https://github.com/TPM34A/Q2_2022/blob/main/Lab_sessions/lab_session_01/lab_session_01.ipynb) |
|      2      |      4     |    Monday | 21-11-2022 | 13:45 - 15:45 |  Sander | Oral lecture |           |
|      2      |      5     | Wednesday | 23-11-2022 | 13:45 - 15:45 |  Sander | Oral lecture |           |
|      2      |      6     |  Thursday | 24-11-2022 | 13:45 - 15:45 |  Sander |  Lab session |           |
|      3      |      7     |    Monday | 28-11-2022 | 13:45 - 15:45 |  Sander | Oral lecture |           |
|      3      |      8     | Wednesday | 30-11-2022 | 13:45 - 15:45 |  Sander | Oral lecture |           |
|      3      |      9     |  Thursday | 1-12-2022  | 13:45 - 15:45 |  Sander |  Lab session |           |
|      4      |     10     |    Monday | 5-12-2022  | 13:45 - 15:45 |   Nadia | Oral lecture |           |
|      4      |     11     | Wednesday | 7-12-2022  | 13:45 - 15:45 |   Nadia | Lab session  |           |
|      5      |     12     |    Monday | 12-12-2022 | 13:45 - 15:45 |   Nadia | Oral lecture |           |
|      5      |     13     | Wednesday | 14-12-2022 | 13:45 - 15:45 |   Nadia | Lab session  |           |
|      5      |     14     |  Thursday | 15-12-2022 | 13:45 - 15:45 |    Amir | Oral lecture |           |
|      6      |     15     |    Monday | 19-12-2022 | 13:45 - 15:45 |    Amir | Mini project |           |
|      6      |     16     | Wednesday | 21-12-2022 | 13:45 - 15:45 |    Amir | Mini project |           |
|      6      |     17     |  Thursday | 22-12-2022 | 13:45 - 15:45 |    Amir | Mini project |           |
|      7      |     18     | Wednesday | 11-1-2023  | 13:45 - 15:45 |    Amir | Mini project |           |
|      7      |     19     |  Thursday | 12-1-2023  | 13:45 - 15:45 |    Amir | Oral lecture |           |

## 4. Q&A Forum

We will use the [Issues section](https://github.com/TPM34A/Q2_2022/issues) of this repo as the official forum for reporting issues. In the Issues section you can ask various types of questions, including: content-related questions, specific questions about the assignments and lab sessions, and technical problems with Python. Before creating a new issue, please make sure the issue has not been raised before by one of your classmates. Besides asking questions, you can also comment on the earlier issues e.g. to continue the discussion. As an example, we have already created the first issue, see [Issues](https://github.com/TPM34A/Q2_2022/issues) and check it out.

To create a new issue, follow these steps:

- Go to the [Issues section](https://github.com/TPM34A/Q2_2022/issues) of the course repo
- Click on **new issue** in the green button located at the upper right of your screen
- Add a informative title to your question/problem/issue (e.g. "Train method of sk-learn does not import in my notebook")
- Describe your question/problem clearly and concisely. Make sure that you do not provide answers here for the graded assignments.
- Add a topic label from the right-hand side. Click on the gear next to "Labels" and add the label based on the topic of your question. For instance, we added the label "Technical" label in the first issue created
- Click on **Submit new issue** in the green button below the text description

After that, one instructor or teacher assistants will reply to your question. **Also, you are allowed (even encouraged) to help others, if you can! If you know how to help your fellow student with an issue, share your thoughts and answers.**

## 5. Instructions to set-up your workspace

In this course, you will work with Python notebooks (Jupyter Notebooks). Python notebooks can be opened in a local environment on your laptop with specific installations of the list of dependend packages, or through using the *Google Colab*. **Using Google Cloab is recommended**. However, if you insist to work in your local environment (i.e. on your laptop) this is possible. But, we will not provide support for installing the python dependencies on personal computers. Below you can find instructions for setting up your notebooks in Google Colab and in a local environment.

## Option 1: Google Colab (recommended)

**Minimal requirements:**
- A Google account
- Google Chrome web browser
- Internet connection

### Steps
- **Step 1:** Download this repo to your computer. On the top of this site, click on (1)**<>Code** tab, then in the green button (2)**Code** and then (3) **Download ZIP** (See numbers 1, 2,a dn 3 on the following image). Unzip this file in a working folder of your own choice.
<p align="center">
  <img width="800" src="https://github.com/FGarridoV/resources/blob/main/step1%20-%20instructions.png?raw=true">
</p>

- **Step 2:** Go to [http://colab.research.google.com](http://colab.research.google.com)
- **Step 3:** Sign in with your Google account (if you are already signed in, skip this step). If you do not have a Google account, you must (temporarily) create one.
- **Step 4:** Upload the Python notebook you want to work on to Colab. Click on the "Upload" tab and then on the "Choose file" tab, see numbers 1 and 2 on the figure below. Then, navigate to your working folder (**Step 1**) and select the Python notebook (.ipynb) you want to work on (e.g. lab_session_00.ipynb).
<p align="center">
  <img width="500" src="https://github.com/FGarridoV/resources/blob/main/Opening%20ipynb.png?raw=true">
</p>

- **Step 5:** Once open, click on "View" >> "Expand sections" on menu bar.

- **Step 6:** **Importantly**, Each notebook has a cell to prepare the data and enviroment in Google Colab. **Uncomment** (i.e. remove the '#') the lines related to Colab set-up in your notebook, see the figure below. Run this cell and wait until finish.
<p align="center">
  <img width="800" src="https://github.com/FGarridoV/resources/blob/main/removinghash.png?raw=true">
</p>

- **Step 7:** You are all set! You can work on your notebook.

**Notes:**
- The uploaded notebook file will be stored on your Google Drive in the folder My Drive \Colab Notebooks\
- If you close the session and want to get started again, then: Go to [Colab](http://colab.research.google.com), open the uploaded notebook from your Google Drive, and re-do Step 5 and 6.


## Option 2: Local environment (not recommended - limited support)

**Minimal requirements:**
- A Python version installed (3.7 or newer)
- An IPython (notebook) enviroment installed on your computer (Jupyter, VSCode or alternatives)
- Basic skills in virtual enviroments (if you don't what to mix your current dependencies)

### Steps
- **Step 1:** Clone or download this repo to your computer (see **Step 1** on Colab section).
- **Step 2:** Two options: (a) Install dependecies separate from your current Python version; (b) Install dependencies for this notebook in your Python version  (easy way):
  - **Step 2.a (you need some knowledge on venvs):**
    - Create a new virtual environment (venv) and install the `requirements_local.txt` file. (see [venv](https://realpython.com/lessons/creating-virtual-environment/) and [install requirements](https://note.nkmk.me/en/python-pip-install-requirements/))
    - Open the notebook you want to work on (**Step 1**) and run the notebook in the newly created venv.
  - **Step 2.b (easy way):** 
    - Open the Python notebook you want to work on (**Step 1**)
    - Uncomment the line related to using a local set-up and run it (see the figure below).
    - Re-comment the lines to avoid re-installing the dependencies every time you run the notebook.
  <p align="center">
  <img width="800" src="https://github.com/FGarridoV/resources/blob/main/removing%20hash%20local.png?raw=true">
</p>

