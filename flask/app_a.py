from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
import torchvision
import torchvision.transforms as transforms
import io

app = Flask(__name__)
CORS(app)

model = torchvision.models.resnet18(pretrained=False)
torch.save(model.state_dict(), 'model_a.pt')
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_bytes = request.files['image'].read()
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)
        predicted_class = output.argmax(dim=1).item()
    return jsonify({'prediction': predicted_class})



if __name__ == '__main__':
    app.run(port=5000)
