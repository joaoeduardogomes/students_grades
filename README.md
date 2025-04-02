# Students grades **🇺🇸**
This project processes a CSV file containing students' scores, calculates their final grades, and indicates their status (passed/failed). It also provides useful information such as the mean grade of the students. Additionally, it displays two types of charts: a pie chart showing the percentage of students who passed or failed, and a histogram illustrating the distribution of grades.

The code was initially [developed in Jupyter Notebook](https://github.com/joaoeduardogomes/students_grades/tree/main/jupyter) to create the logic. Once the functionality was confirmed, I built a [Flask version of the project](https://github.com/joaoeduardogomes/students_grades/tree/main/flask). This version includes the ability to upload a CSV file via the web interface and download a new CSV file with the calculated grades and statuses of the students.

## What problem does it solve?
This project automates grade calculation for a class and provides useful insights into the results. It can be especially helpful for professors who want to streamline the grading process.

## Project Goal
To create a functional application through which I could practice Python and problem-solving skills.

## Tecnologies

**Front-end:** ![HTML](https://img.shields.io/badge/HTML-%20?style=for-the-badge&color=orange) ![Bootstrap](https://img.shields.io/badge/BOOTSTRAP-%20?style=for-the-badge&logo=bootstrap&logoColor=white&color=%236F2CF4)

**Back-end:** ![Python](https://img.shields.io/badge/PYTHON-%20?style=for-the-badge&logo=python&logoColor=white&color=%23356F9F) ![Static Badge](https://img.shields.io/badge/pandas-%231B2154?style=for-the-badge&logo=pandas) ![Static Badge](https://img.shields.io/badge/matplotlib-%231C557C?style=for-the-badge&logo=matplotlib) ![Static Badge](https://img.shields.io/badge/flask-%232A2123?style=for-the-badge&logo=flask)

## Lessons learned & challenges
One of the biggest challenges was displaying the charts on the Flask web page. I solved this by saving the charts as PNG files and embedding them in an <img> tag in the HTML. However, I’m not sure if this is the most efficient approach.

## How to use
The easiest way to test the project is by using [this hosted link on Render](https://students-grades-1imn.onrender.com/). The code is also available here on GitHub for testing and customization to suit your needs.
You can just use the csv file inside the "test csv files" folder if you just want to test this project.

## **License**

![MIT license](https://img.shields.io/badge/License-MIT-%20?link=https%3A%2F%2Fchoosealicense.com%2Flicenses%2Fmit%2F)
