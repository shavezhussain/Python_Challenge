# PyBank and PyPoll Data Analysis

This repository contains two Python projects: PyBank and PyPoll. Each project analyzes specific datasets and provides insightful information based on the data.

## Project Structure

The repository is organized as follows:

- `PyBank` folder:
  - `resources` sub-folder: Contains the dataset used for financial analysis.
  - `analysis` sub-folder: Contains the output text file of the financial analysis.
  - `main.py`: Python script for analyzing financial data.

- `PyPoll` folder:
  - `resources` sub-folder: Contains the dataset used for election analysis.
  - `analysis` sub-folder: Contains the output text file of the election analysis.
  - `main.py`: Python script for analyzing election data.

## PyBank - Financial Analysis

The `PyBank` project focuses on financial data analysis. It performs the following tasks:

- Calculates the total number of months in the dataset.
- Calculates the net total amount of "Profit/Losses" over the entire period.
- Calculates the changes in "Profit/Losses" over time and calculates the average of those changes.
- Identifies the greatest increase and decrease in profits along with their corresponding dates.

To run the analysis, execute `main.py` in the `PyBank` folder.

## PyPoll - Election Analysis

The `PyPoll` project analyzes election data to provide insights into the election results. It performs the following tasks:

- Calculates the total number of votes cast.
- Lists all candidates who received votes.
- Calculates the total number of votes each candidate won.
- Calculates the percentage of votes each candidate received.
- Identifies the winner of the election based on the popular vote.

To run the analysis, execute `main.py` in the `PyPoll` folder.

## Instructions

1. Clone the repository to your local machine using `git clone <repository-url>`.

2. Navigate to the respective project folder you want to analyze (PyBank or PyPoll).

3. Make sure you have the necessary dependencies installed.
 
4. Run the analysis by executing the `main.py` script. The results will be displayed in the terminal, and an output text file will be generated in the `analysis` sub-folder.

5. View the results in both the terminal and the generated output text file.

