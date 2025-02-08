# **Online Retail Sales Data Analyses**

## **Overview**  
This project provides a detailed analysis of online retail transaction data collected over 13 months. The dataset, 
sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail), is analyzed 
to uncover actionable insights for improving customer engagement, understanding purchasing behaviors, and optimizing 
business strategies.  

The aim is to showcase how data analytics can drive decision-making in e-commerce, combining exploratory, predictive, 
and prescriptive analyses.

---

## **Table of Contents**  
1. [Dataset Description](#dataset-description)  
2. [Project Structure](#project-structure)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Project Modules](#project-modules)  
   - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
   - [Customer Lifetime Value (CLV)](#customer-lifetime-value-clv)  
   - [Customer Retention](#customer-retention)  
   - [Customer Patronage Forecast](#customer-patronage-forecast)  
   - [Daily Purchase Trends](#daily-purchase-trends)  
6. [Key Insights and Results](#key-insights-and-results)  
7. [Future Enhancements](#future-enhancements)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Acknowledgments](#acknowledgments)  

---

## **Dataset Description**  

The dataset contains the following fields:  
- **InvoiceNo**: Invoice number (Nominal). A unique 6-digit identifier for each transaction. Codes starting with "C" 
indicate cancellations.  
- **StockCode**: Product/item code (Nominal). A unique 5-digit identifier for each product.  
- **Description**: Product/item name (Nominal).  
- **Quantity**: Number of units sold per transaction (Numeric).  
- **InvoiceDate**: Date and time of the transaction (Datetime).  
- **UnitPrice**: Price per unit in GBP (£) (Numeric).  
- **CustomerID**: Unique identifier for each customer (Nominal).  
- **Country**: Country of residence of the customer (Nominal).  

*This dataset represents real-world e-commerce data, making it ideal for exploratory and advanced analytics. Addressing 
missing data and anomalies like cancellations is critical to ensure analysis accuracy*.

---

## **Project Structure**

The repository is organized as follows:  

```plaintext
Online_Sales_Data_Analysis/
├── data/
│   ├── online-retail.xlsx       # Raw data
│   ├── cleaned-data.csv         # Cleaned and pre-processed data
├── docs/                        # Documentation for various project stages
│   ├── customer-lifetime-value.md
│   ├── customer-retention.md
│   ├── daily-purchase-trend.md
│   ├── customer-patronage-forecast.md
│   ├── data-processing.md
├── figures/                     # Generated visualizations
├── images/                      # Supporting images for documentation
├── scripts/                     # Python scripts for data analysis
│   ├── EDA/
│   ├── customer_lifetime_value.py
│   ├── customer_retention.py
│   ├── daily_purchase_trend.py
│   ├── customer_patronage_forecast.py
├── CODE_OF_CONDUCT.md		 # Code of ethics regarding contribution to the project
├── CONTRIBUTING.md		 # Doc about contributing to the project
├── LICENSE.md
├── README.md
├── requirements.txt             # Required libraries and dependencies
```


## Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/DataAnalyticaLab/online-retail-sales-data-analysis.git
cd online-retail-sales-data-analysis
pip install -r requirements.txt
```


## Usage
Follow these steps to explore and analyze the dataset:

1. **Exploratory Data Analysis (EDA)**: 
     Clean and preprocess the data.
    ```bash
    scripts/EDA/eda_script.py
    ```

2. **Calculate Customer Lifetime Value (CLV)**:
     Analyze customer segments and behavior.
    ```bash
    scripts/customer_lifetime_value.py
    ```

3. **Forecast Customer Patronage**:
     Predict customer behavior trends.
    ```bash
    scripts/customer_patronage_forecast.py
    ```

4. **Customer Retention**: Determine customer retention rates.
    ```bash
    scripts/customer_retention.py
    ```



## Project Modules
### Exploratory Data Analysis (EDA)
- Data cleaning: Handle missing values, duplicates, and cancellations.
- Initial insights: Explore data distributions and relationships.
- Feature engineering: Transform data types and normalize values.

### Customer Lifetime Value (CLV)
- RFM Analysis: Segment customers based on recency, frequency, and monetary value.
- Segmentation: Group customers by purchasing behavior using clustering.
- Model Evaluation: Analyze feature importance and visualize clusters.

### Customer Retention
- Cohort Analysis: Identify customer retention patterns by cohorts.
- Retention Rates: Analyze retention over time and its business implications.

### Customer Patronage Forecast
- Weekly predictions of customer behavior trends.
- Time series modeling with appropriate parameters for accurate forecasting.

### Daily Purchase Trends
- Analyze daily revenue patterns and seasonality.
- Visualize purchasing behavior over time.



## Key Insights and Results
- High-value customers identified using RFM analysis contributed ~60% of revenue.
- Retention patterns revealed a sharp churn within the first 3 months, with actionable insights to improve loyalty.
- Sales spikes observed during holiday seasons, guiding promotional strategies.
	[Visuals of these insights can be found in the figures/directory.]


## Future Enhancements
1. **Frequent Item Analysis**:
   Use Apriori or FP-Growth algorithms to discover frequently purchased item pairs. Hardware limitations will be addressed using cloud solutions.

2. **Deep Learning Integration**:
   Explore advanced models like LSTMs for customer behavior predictions.

3. **Interactive Dashboards**:
   Develop dashboards using Power BI or Tableau for dynamic visualizations.



## Contributing
We welcome contributions! To get started:

1. Fork the repository.
2. Create a feature branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add your commit message here"
    ```
4. Push to the branch
    ```bash
    git push origin feature/your-feature-name
    ```
5. Submit a pull request.
Refer to the [CONTRIBUTING](CONTRIBUTING.md) file for more details.


## License
This project is licensed under the Apache License 2.0. See [LICENSE.md](LICENSE.md) for more details.


## Acknowledgments
- Dataset source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail).
- Visualization inspiration: Kaggle datasets and Medium articles on customer analytics.
- Contributors: Special thanks to all collaborators and contributors to this project.


## Note: 
I did an analysis on _items that are mostly purchased together_; I have the code for it, but it is **NOT TESTED!**.  
My laptop memory (8GiB) cannot handle the (Apriori) algorithm that I used. I will be looking at rectifying this 
challenge. The result of this analysis has the potential to increase business gains.

---

This README.md file provides a clear and organized structure for **Online Sales Data Analysis** project. It includes sections for project 
overview, installation instructions, usage guidelines, and references to each project module.
