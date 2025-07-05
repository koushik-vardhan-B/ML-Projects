# Student Performance Prediction

This project is an end-to-end Machine Learning pipeline to predict student performance based on demographic and academic features. It covers data ingestion, transformation, model training, evaluation, and provides a Flask web application for real-time predictions. The project is containerized using Docker for easy deployment.

---

## Problem Statement

Educational institutions often seek to identify students who may need additional support to improve their academic performance. By analyzing various features such as gender, ethnicity, parental education, lunch type, test preparation, and previous scores, we aim to predict a student's performance (e.g., exam scores). This helps in early intervention and personalized learning strategies.

---

## Implementation

### 1. Data Ingestion
- Reads raw data from CSV files.
- Splits data into training and testing sets.
- Stores processed data in the `artifacts/` directory.

### 2. Data Transformation
- Handles missing values and categorical encoding.
- Scales numerical features.
- Saves the preprocessor object for future use.

### 3. Model Training
- Trains multiple regression models:
  - Random Forest, Decision Tree, Gradient Boosting, Linear Regression, K-Neighbors, XGBoost, CatBoost, AdaBoost
- Performs hyperparameter tuning using GridSearchCV.
- Selects the best model based on R² score.
- Saves the trained model to `artifacts/model.pkl`.

### 4. Prediction API (Flask App)
- Accepts user input via a web form.
- Uses the trained model and preprocessor to predict student performance.
- Displays the predicted score on the web page.

### 5. Logging & Exception Handling
- All logs are saved in the `logs/` directory.
- Custom exceptions are handled and logged for easier debugging.

### 6. Docker Support
- Dockerfile provided for containerized deployment.

---

## Output

- **Best Model Selection:** The pipeline automatically selects and saves the best-performing regression model based on test R² score.
- **Web Interface:** Users can input student data and receive predicted scores instantly.
- **Logs:** All steps and errors are logged for transparency and debugging.
- **Artifacts:** Trained model, preprocessor, and processed datasets are saved for reproducibility.

Example output from the web app:
```
Predicted Student Score: 78.5
```

---

## Project Structure

```
├── app.py
├── Dockerfile
├── requirements.txt
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   ├── raw.csv
├── logs/
│   └── *.log
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/studentperformance-app.git
cd studentperformance-app
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv myven
source myven/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The app will be available at [http://localhost:5000](http://localhost:5000).

### 5. Build and Run with Docker (Optional)

```bash
docker build -t koushikvardhan/studentperformance-app .
docker run -p 5000:5000 koushikvardhan/studentperformance-app
```

---

## Technologies Used

- Python 3.8
- Flask
- scikit-learn
- pandas, numpy
- xgboost, catboost
- Docker

---

## Author

Koushik Vardhan

---

**Note:**  
- Update paths and URLs as per your setup.
- For any issues, please open an issue on the repository.
