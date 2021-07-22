import requests 

# https://your-heroku-app-name.herokuapp.com/predict
# http://localhost:5000/predict
resp = requests.post("https://pytorch-flower-classifier.herokuapp.com/predict", files={'file': open('test_image.jpg', 'rb')})

print(resp.text)