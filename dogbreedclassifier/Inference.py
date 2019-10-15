import torch,json,io,logging
import torch.nn as nn
from torchvision import transforms,models
from PIL import Image
logger = logging.getLogger(__name__)

class Inference:

    def __init__(self,model_file):
        self.image_tensor = None
        self.cnn_model = models.resnet152(pretrained=True)
        self.training_device = torch.device("cpu")
        self.fully_connected_layer = nn.Sequential(
                                       nn.Linear(2048,800),
                           nn.ReLU(),
                           nn.Dropout(p=0.35),
                           nn.Linear(800,120),
                           nn.ReLU(),
                           nn.LogSoftmax(dim=1))
        self.load_cnn_model(model_file)

    def load_cnn_model(self,model_file):
        self.cnn_model.fc = self.fully_connected_layer
        self.cnn_model.load_state_dict(torch.load(model_file,map_location="cpu"))

    def transform_image(self,image_bytes):
        my_transforms = transforms.Compose([transforms.Resize(255),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize(
                                        [0.485, 0.456, 0.406],[0.229, 0.224, 0.225])])
        image = Image.open(io.BytesIO(image_bytes))
        return my_transforms(image).unsqueeze(0)

    def set_image_tensor(self,image_file):
        transformed_image = self.transform_image(image_bytes=image_file)
        self.image_tensor = transformed_image

    def get_image_prediction(self,image_bytes):
        logger.info("Starting Image prediction")
        self.image_tensor = self.transform_image(image_bytes=image_bytes)
        logger.info("Setting Model to evaluation mode")
        self.cnn_model.eval()
        logger.info("Making prediction")
        outputs = self.cnn_model.forward(self.image_tensor)
        logger.info("Prediction finished")
        _, label = outputs.max(1)
        inference_result = {
            "prediction":label.item(),
            "results":outputs.tolist()
        }
        logger.info("Prediction results")
        logger.info(inference_result)
        return inference_result



