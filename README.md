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
- 
You can read the generated CSV file and perform analyses, with results printed to the console, describing the following metrics:

- **Nombre de paris effectués depuis inscription**: The total number of bets placed since registration.
- **Mise en moyenne**: The average stake per bet.
- **Moyenne gains**: The average gains from the bets.
- **Total argent misé**: The total amount of money wagered.
- **Total argent gagné**: The total amount of money won.
- **Balance gains - mise**: The balance calculated by subtracting the total stakes from the total winnings.

These statistics will provide you with insights into your betting activity and overall performance.

