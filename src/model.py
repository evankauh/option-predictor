from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(data):
    """Train model to predict best option contracts."""
    X = data.drop(["target"], axis=1)
    y = data["target"]
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, "model.pkl")
    return model

def load_model():
    """Load saved model."""
    return joblib.load("model.pkl")
