# 🏡 Boston Housing Price Prediction  

This project demonstrates a **Machine Learning Regression Model** to predict housing prices in Boston.  
It includes both:  
- 📓 A **Jupyter Notebook** for model training & evaluation.  
- 🌐 A **Streamlit Web App** for interactive predictions using user inputs.  

---

## 📂 Project Structure  

```
├── Python_miit_class_12_ML_regression.ipynb   # Notebook with ML training & evaluation
├── boston_housing.pkl                         # Trained ML model (required for Streamlit app)
├── app.py                                     # Streamlit app for predictions
├── requirments.txt                            # Dependencies list
```

---

## ⚙️ Requirements  

Install dependencies with:  

```bash
pip install -r requirments.txt
```

### Dependencies used  
- pandas  
- numpy  
- scikit-learn  
- streamlit  
- matplotlib  
- seaborn  

---

## 🚀 How to Run Locally  

### 1️⃣ Run the Jupyter Notebook  
```bash
jupyter notebook Python_miit_class_12_ML_regression.ipynb
```

### 2️⃣ Run the Streamlit App  
Make sure `boston_housing.pkl` (trained model) is in the same folder.  

```bash
streamlit run app.py
```

---

## 🖥️ Streamlit App Features  

- Interactive **sliders & dropdowns** to enter property details.  
- Real-time **house price predictions**.  
- **Feature importance visualization** (if supported by model).  

---

## 📊 Example  

Sample prediction output (with default inputs):  
```
The Predicted price is $23,450.00
```

---

## 🌐 Deploying on Streamlit Cloud  

You can deploy this app online for free using **Streamlit Cloud**.  

### Steps:  
1. Push your project to **GitHub** with these files:  
   - `app.py`  
   - `boston_housing.pkl`  
   - `requirments.txt`  
   - (optional) `Python_miit_class_12_ML_regression.ipynb`  

2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and log in with GitHub.  

3. Click **“New app”** → Select your repository.  

4. Set:  
   - **Main file path** = `app.py`  
   - **Python version** = 3.9+  

5. Click **Deploy** 🚀  

Your app will be live at:  
```
https://<your-username>-<repo-name>.streamlit.app
```

---

## 🧑‍💻 Author  

**Henish Modi**  
📍 Brampton, ON, Canada  
🔗 [LinkedIn](https://www.linkedin.com/in/henishmodi24)  
