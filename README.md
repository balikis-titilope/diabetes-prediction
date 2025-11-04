# Diabetes Prediction using SVM

This project uses **Support Vector Machine (SVM)** to predict the likelihood of diabetes based on diagnostic measurements.  
It is built using the **PIMA Indians Diabetes Dataset**.

## Dataset Description

The dataset contains medical predictor variables and one target variable `Outcome` (1 = diabetic, 0 = non-diabetic).

**Features:**
- **Pregnancies:** Number of times pregnant  
- **Glucose:** Plasma glucose concentration  
- **BloodPressure:** Diastolic blood pressure (mm Hg)  
- **SkinThickness:** Triceps skin fold thickness (mm)  
- **Insulin:** 2-Hour serum insulin (mu U/ml)  
- **BMI:** Body mass index (weight in kg/(height in m)^2)  
- **DiabetesPedigreeFunction:** Likelihood of diabetes based on family history  
- **Age:** Age of the patient (years)  
- **Outcome:** Class variable (0 = Non-diabetic, 1 = Diabetic)

## Data Preprocessing

- Zero values in `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, and `BMI` were replaced as they are **not physiologically possible**.  
- Imputation strategy based on feature distribution:
  - `Glucose`: mean  
  - `BloodPressure`: mean  
  - `SkinThickness`: median  
  - `Insulin`: median  
  - `BMI`: mean  

## Model Training

- Two SVM kernels were tested:
  - **Linear Kernel**
  - **RBF Kernel (with class_weight='balanced')**

- The RBF kernel produced better performance.


## Model Evaluation

**Final Metrics:**
- accuracy of 77%
- recall of 65%
- precision of 0.75

## Insights
- The model performs well with an overall accuracy of ~77%.  
- Good precision indicates fewer false positives.  
- Some trade-off exists between recall and precision, typical in medical prediction models.  


## Tech Stack
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  


## Future Improvements
- Hyperparameter tuning using GridSearchCV  
- Model comparison with Logistic Regression or Random Forest  
- Handling outliers for Insulin and BMI  


## Author
- **name** - Titilope Balikis
- **email** - titilopebalikis806@gmail.com
- **linkedin** - https://www.linkedin.com/in/titilope-balikis
- Data Science & Machine Learning Enthusiast  
