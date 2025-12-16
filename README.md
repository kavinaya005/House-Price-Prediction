**House Price Prediction Using Artificial Intelligence 🏠🤖 project** focuses on developing an ML model for predicting house prices, addressing a critical need in the real estate industry for accurate and reliable pricing tools. By leveraging machine learning, particularly *linear regression*, the project estimates **house prices🏠💵** based on key features such as square footage, number of bedrooms, number of bathrooms, year of construction, lot size, garage size, and neighborhood quality.

I developed this project during my internship at **Elysium Technologies Private Limited, Madurai, Tamil Nadu** from *09.12.2024 to 27.12.2024*. During this period, I worked as an **AI Intern** focusing on building a predictive web application that integrates artificial intelligence and web technologies. The internship provided valuable hands-on experience in applying machine learning techniques and managing project development.

**Implementation:**

🔺Data collection and Preprocessing:
 
The **House Price Regression Dataset** is used for this project. [Kaggle Dataset link: https://www.kaggle.com/datasets/prokshitha/home-value-insights]

<img width="610" height="273" alt="image" src="https://github.com/user-attachments/assets/958d2f32-3993-4254-b8d1-6f1b471fa75b" />


To ensure the data quality, preprocessing was performed to handle missing values and clean the dataset.

<img width="546" height="319" alt="image" src="https://github.com/user-attachments/assets/fbede9a2-9875-47c6-ad2e-21c8dc17ad52" />


🔺Feature selection:

The target variable is the *"house price"*. The data was split into features (X) and target (y), then further divided into training and testing sets in *80:20* proportion.

🔺Model Training:

A "Linear Regression model" was trained using the training dataset to learn the relationship between house features and their prices.

🔺Model Saving:
	
The trained model was saved to a file (house_price_model.joblib) using the "joblib" library for later reuse without retraining.

🔺Model Evaluation

The model’s performance was evaluated on the test data using common regression metrics:

🔵Mean Absolute Error (MAE)
🔵Mean Squared Error (MSE)
🔵R-squared (R²) score

<img width="426" height="125" alt="image" src="https://github.com/user-attachments/assets/0cb63a3e-b387-4914-be38-a0fcfcc4bf4e" />


Additionally, a scatter plot was generated comparing actual vs predicted house prices to visually assess the model’s accuracy.

<img width="492" height="330" alt="image" src="https://github.com/user-attachments/assets/72a3a3a4-792f-4c3d-bccf-87b214121870" />


🔺Exploratory Data Analysis (EDA)

Correlation between features and target was examined using a correlation matrix and heatmap.

<img width="1037" height="822" alt="image" src="https://github.com/user-attachments/assets/d5f9d482-fc72-4a05-8172-4a963706e0da" />

	
A scatter plot between square footage and house price was also created to understand feature impact.

<img width="538" height="375" alt="image" src="https://github.com/user-attachments/assets/2a366161-21f8-40c5-83e0-8b3ebbdcb1d3" />


🔺Web Deployment:

The project includes two separate web deployments to demonstrate different application interfaces and user management:

🟡Streamlit: A house prediction application is developed using "Streamlit" for an interactive and user-friendly interface, styled with CSS to enhance visual appeal and usability.

<img width="789" height="448" alt="image" src="https://github.com/user-attachments/assets/48d0d139-87a4-4bad-9693-7a8983e92395" />
<img width="849" height="383" alt="image" src="https://github.com/user-attachments/assets/528bfd1f-a50f-4249-8d3b-74c08f43a3ce" />


🟢Flask: Similarly like in Streamlit, a House Price Prediction System is developed using "Flask" as the backend framework, with HTML and CSS for creating an engaging and responsive user interface. Additionally, "XAMPP server" is utilized to manage and store users' login credentials, ensuring seamless functionality and data storage in a *localhost environment*.

<img width="747" height="326" alt="image" src="https://github.com/user-attachments/assets/4c068341-0f7f-4afd-a383-a0268979e413" />
<img width="739" height="315" alt="image" src="https://github.com/user-attachments/assets/845e286d-bc9b-48a4-85a6-49837f29986e" />
<img width="748" height="315" alt="image" src="https://github.com/user-attachments/assets/61d48987-af76-4f47-8f2f-d814df693254" />
<img width="750" height="315" alt="image" src="https://github.com/user-attachments/assets/aaf12bb2-0b19-4738-b738-1a377ba88eb4" />
<img width="750" height="315" alt="Screenshot 2025-01-03 192931" src="https://github.com/user-attachments/assets/a41c3959-a9f2-4cc7-a0c3-0afffeacab14" />









	
