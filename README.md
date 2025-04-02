# Student Performance Indicator

## Project Overview
This project analyzes how students' performance (test scores) is influenced by various factors such as gender, ethnicity, parental level of education, lunch type, and test preparation course completion. By understanding these relationships, we can gain insights into key determinants of academic success.

## Dataset
- **Source:** [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)
- **Description:** This dataset consists of student test scores in math, reading, and writing, along with demographic and socio-economic attributes.
- **Columns:**
  - `gender`: Male or Female
  - `race/ethnicity`: Student's ethnic background (Group A, B, C, D, or E)
  - `parental level of education`: Highest education level attained by a student's parents
  - `lunch`: Standard or free/reduced-price lunch
  - `test preparation course`: Completed or not completed
  - `math score`: Math test score (0-100)
  - `reading score`: Reading test score (0-100)
  - `writing score`: Writing test score (0-100)

## Objectives
- Perform exploratory data analysis (EDA) to understand the dataset.
- Identify correlations between different factors and student performance.
- Develop a predictive model to estimate test scores based on input features.
- Interpret findings to derive meaningful insights.

## Technologies Used
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Tools:** Jupyter Notebook / Google Colab

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/student-performance.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Load the dataset and run the analysis:
   ```python
   import pandas as pd
   df = pd.read_csv('StudentsPerformance.csv')
   ```

## Exploratory Data Analysis (EDA)
- Data Cleaning and Handling Missing Values
- Data Visualization using Seaborn and Matplotlib
- Correlation Analysis

## Machine Learning Approach
- Preprocessing: Encoding categorical variables, handling missing data
- Model Selection: Linear Regression, Decision Trees, Random Forest
- Model Evaluation: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), R² Score

## Expected Outcomes
- Understanding how different factors impact student test scores.
- A trained model that predicts student performance based on given inputs.
- Data-driven recommendations for educators and policymakers.

## Contribution
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is open-source and available under the MIT License.

---

For any questions, feel free to reach out!