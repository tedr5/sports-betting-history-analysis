# 📖 Description

A personal project to summarize sports betting history for personal analysis using Python and Selenium. This application automates the process of logging into a sports betting account, retrieves betting data, and summarizes it in a CSV file.

## ⚙️ Technologies

- Programming Language: Python
- Web Automation: Selenium
- Data Manipulation: Pandas

## 🛠️ Installation

Clone the repository:

```bash
  git clone https://github.com/tedr5/sports-betting-history-analysis.git
```

Install the required libraries:
```bash
  pip install selenium pandas
```
## 🚀 Features

- **Automated Login**: Logs into a sports betting account using Selenium.
- **Data Retrieval**: Collects historical betting data, including date, reference, total stake, and returns.
- **CSV Export**: Outputs the collected data into a CSV file for easy analysis.
- **Summary Statistics**: Computes key statistics like average stake, average gains, and overall balance.

## 📊 Data Structures

The project utilizes:

- A CSV file for storing betting data.
- DataFrames from the Pandas library for data manipulation and statistical analysis.

## 📄 Usage

 Run the script to fetch and summarize your betting history. Ensure you fill in your username, password, and date of birth in the script before executing.
```bash
python uniautomata.py
```
After running the script, the output will be saved to `unibet.csv` on your desktop.

## 📈 Analysis

The output CSV file contains the following columns:

- **Date/Time**: The date and time of the bet.
- **Reference**: Unique reference number for the bet.
- **Total Stake**: Amount wagered.
- **Gains**: Total winnings or losses.

Statistics will be printed to the console, summarizing your betting activity.

