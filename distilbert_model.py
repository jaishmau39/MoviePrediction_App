import ktrain

# using CPU for prediction
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1" 

predictor = ktrain.load_predictor('distilbert')


def get_prediction(x):
	sent = predictor.predict([x])
	return sent[0]