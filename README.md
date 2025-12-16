<div align="center">
<div style="background-color: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); max-width: 900px; margin: 0 auto;">

# **House Price Prediction Using Artificial Intelligence 🏠🤖**

This project focuses on developing an ML model for predicting house prices, addressing a critical need in the real estate industry for accurate and reliable pricing tools. By leveraging machine learning, particularly *linear regression*, the project estimates **house prices🏠💵** based on key features such as square footage, number of bedrooms, number of bathrooms, year of construction, lot size, garage size, and neighborhood quality.

---

## **Internship Experience**

I developed this project during my internship at **Company name** from *09.12.2024 to 27.12.2024*. During this period, I worked as an **AI Intern** 👩🏽‍💻 focusing on building a predictive web application that integrates artificial intelligence and web technologies. The internship provided valuable hands-on experience in applying machine learning techniques and managing project development.

---

## **Implementation**

### 🔺 **Data Collection and Preprocessing**
- The **House Price Regression Dataset** is used for this project.
  [Kaggle Dataset link: https://www.kaggle.com/datasets/prokshitha/home-value-insights]
- To ensure data quality, preprocessing was performed to handle missing values and clean the dataset.

### 🔺 **Feature Selection**
- The target variable is the "house price". 
- The data was split into features (X) and target (y), then further divided into training and testing sets in *80:20* proportion.

### 🔺 **Model Training**
- A **Linear Regression model** was trained using the training dataset to learn the relationship between house features and their prices.

### 🔺 **Model Saving**
- The trained model was saved to a file (`house_price_model.joblib`) using the **joblib** library for later reuse without retraining.

### 🔺 **Model Evaluation**
- The model's performance was evaluated on the test data using common regression metrics:
  - 🔵 **Mean Absolute Error (MAE)**
  - 🔵 **Mean Squared Error (MSE)**
  - 🔵 **R-squared (R²) score**
- Additionally, a scatter plot was generated comparing actual vs predicted house prices to visually assess the model's accuracy.

### 🔺 **Exploratory Data Analysis (EDA)**
- Correlation between features and target was examined using a correlation matrix and heatmap.
- A scatter plot between square footage and house price was also created to understand feature impact.

### 🔺 **Web Deployment**
The project includes two separate web deployments to demonstrate different application interfaces and user management:

#### 🟡 **Streamlit**
A house prediction application developed using **Streamlit** for an interactive and user-friendly interface, styled with CSS to enhance visual appeal and usability.

#### 🟢 **Flask**
A House Price Prediction System developed using **Flask** as the backend framework, with HTML and CSS for creating an engaging and responsive user interface. Additionally, **XAMPP server** is utilized to manage and store users' login credentials, ensuring seamless functionality and data storage in a *localhost environment*.

</div>
</div>
