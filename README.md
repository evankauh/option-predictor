# **Option-Predictor**

**Option-Predictor** is a machine learning-based system designed to assist in executing the **wheel strategy** for options trading. The wheel strategy involves selling cash-secured puts and covered calls, and this project uses historical market data, implied volatility, and other market indicators to predict the most profitable option contracts.

The system leverages machine learning models (such as XGBoost) to identify and predict the profitability of option contracts. It continuously learns and adjusts its predictions based on new incoming data, making it a robust and scalable solution for traders seeking to maximize returns through the wheel strategy.

Key Features:
- **Data Collection and Preprocessing**: Collects historical stock and options data from APIs (e.g., Yahoo Finance), calculates option Greeks, and generates features such as moving averages and volatility.
- **Machine Learning Model**: Uses advanced algorithms to predict profitable option contracts based on historical market trends, implied volatility, and other factors.
- **Backtesting Engine**: Simulates the wheel strategy on historical data to evaluate the performance of the predictions.
- **Real-Time Prediction**: Predicts option profitability for live data to assist in real-time trading decisions.
- **Continuous Learning**: Automatically retrains models as new data becomes available, improving accuracy over time.

---

## **Project Structure**

option-predictor/ ├── data/
│ ├── raw/ # Raw market data 
│ ├── processed/ # Cleaned and processed data 
├── models/ # Saved trained machine learning models 
├── notebooks/ # Jupyter notebooks for exploration and prototyping 
├── src/
│ ├── data_processing.py # Data collection and preprocessing 
│ ├── model.py # Model training and evaluation 
│ ├── predict.py # Live prediction 
│ ├── backtesting.py # Backtesting the strategy on historical data 
├── tests/ # Unit tests for the project 
├── config/
│ └── settings.yaml # Project configuration and parameters 
├── README.md # Project documentation 
├── requirements.txt # Python dependencies 
└── run.py # Main script to run the project



---

## **Installation and Setup**

### **1. Clone the Repository**

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/option-predictor.git
cd option-predictor
```

### **2. Set Up a Virtual Environment**

It's recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
Install the required Python packages listed in the `requirements.txt` file:
```bash 
pip install -r requirements.txt
```

### **4. Configure the Project**
You can configure certain parameters (e.g., model hyperparameters, trading rules) by modifying the `config/settings.yaml` file.
