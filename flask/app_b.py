from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
import torchvision
import torchvision.models as models
import torchvision.transforms as transforms
import torch.nn as nn
import io

app = Flask(__name__)
CORS(app)

EPOCHS = 200
BATCH_SIZE = 32
IMG_SIZE = 224
PATCH_SIZE = 16
IN_CHANNELS = 3  # Still 3 channels since we convert back to RGB-like tensors
NUM_CLASSES = 6

EPOCHS = 200
BATCH_SIZE = 32  # Reduced from 64 for better gradient updates
IMG_SIZE = 224
PATCH_SIZE = 16
IN_CHANNELS = 3
EMBED_DIM = 256
NUM_PATCHES = (IMG_SIZE // PATCH_SIZE) ** 2
NUM_HEADS = 8
NUM_ENCODERS = 6
NUM_CLASSES = 6
LEARNING_RATE = 1e-4  # Reduced from 3e-4
DROPOUT = 0.1
ACTIVATION = 'gelu'
WARMUP_EPOCHS = 5  # For learning rate warmup

prediction_classes = ["Bacteria", "Fungi", "Healthy", "Pest", "Phytopthora", "Virus"]

class PatchEmbedding(nn.Module):
    def __init__(self, in_channels, patch_size, embed_dim, num_patches, dropout):
        super(PatchEmbedding, self).__init__()
        self.patcher = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=embed_dim,
                      kernel_size=patch_size, stride=patch_size),
            nn.Flatten(2)
        )
        self.cls_token = nn.Parameter(torch.zeros(1, 1, embed_dim))
        self.pos_embed = nn.Parameter(torch.zeros(1, num_patches + 1, embed_dim))
        self.dropout = nn.Dropout(dropout)

        # Initialize weights properly
        nn.init.trunc_normal_(self.cls_token, std=.02)
        nn.init.trunc_normal_(self.pos_embed, std=.02)

    def forward(self, x):
        x = self.patcher(x).permute(0, 2, 1)
        cls_tokens = self.cls_token.expand(x.size(0), -1, -1)
        x = torch.cat((cls_tokens, x), dim=1)
        x = x + self.pos_embed
        return self.dropout(x)

class ViT(nn.Module):
    def __init__(self):
        super(ViT, self).__init__()
        self.patch_embed = PatchEmbedding(IN_CHANNELS, PATCH_SIZE, EMBED_DIM, NUM_PATCHES, DROPOUT)
        self.norm = nn.LayerNorm(EMBED_DIM)  # Additional layer norm
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=EMBED_DIM,
            nhead=NUM_HEADS,
            activation=ACTIVATION,
            dropout=DROPOUT,
            batch_first=True  # Use batch_first for better compatibility
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=NUM_ENCODERS)
        self.mlp_head = nn.Sequential(
            nn.LayerNorm(EMBED_DIM),
            nn.Linear(EMBED_DIM, EMBED_DIM//2),  # Narrower
            nn.GELU(),
            nn.Dropout(0.3),
            nn.Linear(EMBED_DIM//2, EMBED_DIM//4),
            nn.GELU(),
            nn.Dropout(0.2),
            nn.Linear(EMBED_DIM//4, NUM_CLASSES)
        )
    def forward(self, x):
        x = self.patch_embed(x)
        x = self.norm(x)  # Additional normalization
        x = self.transformer(x)
        return self.mlp_head(x[:, 0])  # Class token

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = ViT().to(device)
model.load_state_dict(torch.load('model_b.pt', map_location=device))
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
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(input_tensor)
        predicted_class = output.argmax(dim=1).item()
    return jsonify({'prediction': prediction_classes[predicted_class] + " (" + str(predicted_class) + ")"})

if __name__ == '__main__':
    app.run(port=5000)
