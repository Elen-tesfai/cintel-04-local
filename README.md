# cintel-04-local

# Elen's Palmer Penguin Dataset Exploration

This is an interactive, reactive web application that visualizes penguin data from a dataset, using Shiny in Python. The app allows users to filter penguins by species and select different columns to display in various charts and grids. The app is hosted for free on GitHub Pages and built entirely in Python.

## Project Overview

The Popper's Penguin Dashboard showcases the use of Shiny for building reactive web apps with Python. The app allows users to interactively explore penguin species data, providing charts and filters to make data exploration fun and insightful.

## Features

- **Interactive Dropdown Menu**: Users can select a column from the dataset to display.
- **Species Filter**: Checkbox group to filter the penguins by species.
- **Reactive Calculations**: The app re-renders charts and tables as filters or selections change.

## How to Run Locally

To run this app on your local machine, follow these steps:

### Prerequisites

Make sure you have Python installed and that you’re familiar with virtual environments. You will also need the required packages listed in the `requirements.txt` file.

### Setup

1. **Clone the Repository**  
   First, clone the repository to your local machine:
   ```bash
   git clone https://github.com/elen-tesfai/cintel-04-local.git

 ### 2. Create a Virtual Environment
It's recommended to use a virtual environment to manage your project's dependencies. To create one, run the following command:
```bash
python -m venv .venv
```
### 3. Activate the Virtual Environment
Once the virtual environment is created, you need to activate it:
```bash
.\.venv\Scripts\activate
```
### 4. Install Dependencies
 After activating the virtual environment, install the necessary Python packages by running:
```bash
pip install -r requirements.txt
```
### 5. Run the App
 Now that everything is set up, you can run the app by using the following command:
 ```bash
shiny run --reload --launch-browser penguins/app.py
```
### Local Path for Screenshot:
```bash
![Penguin Dataset Screenshot](assets/images/Screenshot%202024-11-11%20214616.png)