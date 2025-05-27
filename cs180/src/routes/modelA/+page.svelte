<div class="flex justify-center p-12 space-y-4 max-w-10xl">
    <div class="flex flex-col w-10/12 justify-center items-center max-w-5xl text-center bg-gray-100 rounded-lg shadow-lg p-8">
        <h1 class="text-7xl font-bold mb-12">Model A</h1>
        <p class="font-mono text-5xl font-bold py-2 px-4">Description</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">This is the first model of the project, which is a CNN that is based off the Resnet architecture that will be trained to classify the diseases or lack of in images of potato plants. </p>
        <p class="font-mono text-5xl font-bold py-2 px-4">Methodology</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 1. ZIP File extraction</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">Note that the ZIP file to be used must have the same level in the notebook's directory to ensure that this notebook runs smoothly. Otherwise, you may opt to download the zipfile from the Cloud and store it in the same folder as the notebook by uncommenting the GDrive commands in the succeeding code block below. ZIP File extraction is a must to extract the actual potato leaf disease development set.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 2. Import essential libraries and filter corrupted images</p>
        <img src="/pytorch.png" alt="pytorch" class="w-1/2 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">This model implementation relies on pytorch. As such, most imports were garnered from the said library. Without proper imports, the model will be unable to run properly. Apart from import, filtering invalid files will also ensure that the training and, effectively, the model will be produced as intended.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 3. Set up the random seed</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">For this model, we set the random seed to 42 for reproducibility. Nevertheless, you may opt to configure the seed to a different value. Rest assured that the latter results, accuracy, and loss would still produce a model that is shielded against overfitting.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 4. Set up proper CPU/GPU dependencies</p>
        <img src="/gpu.png" alt="gpu" class="w-1/2 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">After numerous configurations on the model, training our model could breeze through a CPU dependency. Nevertheless, to ensure hardware safety, it would be best to use GPU (cuda) to safekeep hardware specs, and to enhance performance and training time.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 5. Data augmentation, preprocessing, and data split</p>
        <img src="/images_a.png" alt="images_a" class="w-1/2 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">To permit the images to properly react and classify images that are either distorted, illuminated, etc., data augmentation and preprocessing was applied before sending the blobs of images through training. The images are resized to 224x224 pixels and normalizing them to the image.net values. The train_data was augmented to have verticalflip, horizontalflip, random rotation, color jitter, and gaussian blur to avoid overfitting and make the model not memorize the data. The validation dataset would not have an augmentation. We also used an 80-20 split train-validation dataset since test data set will be given in succession.</p>
        
        <p class="font-mono text-4xl font-bold py-2 px-4">Step 6. Building the Model</p>
        <img src="/resnet.png" alt="resnet" class="w-3/4 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">Our model is built on a modified ResNet CNN model with pretrained set to false to ensure that the model will only be trained on the development set provided. This essentially sets the retrieved ResNet model to scratch or null. We replaced the head of the ResNet model to have a dropout of 50% (i.e., 0.5) to minimize overfitting. We also used Adam as the optimizer and a scheduler that will effectively reduce learning rates when accuracy begins to plateau. Learning rate reduction and losses are based on a criterion set with CrossEntropyLoss.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 7. Training the Model</p>
        <img src="/graph_a.png" alt="graph_a" class="w-3/4 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">Our model trains for 50 epochs with a patience of 5 if there is no improvement from the validation accuracy. By setting the ResNet-based CNN to train, as epochs go by, we clear optimized parameters, compute loss, perform backpropagation, and update model parameters using computed gradients on the optimizer's algorithm (Adam).</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 8. Fine-tuning the model</p>        
        <p class="font-mono text-lg py-2 px-4 text-justify">Fine-tuning the model uses different parameters in the optimizers. More specifically, with the Adam optimizer (initialized to "optimizer"), it gives different learning rates to the different layers of the model. This, in turn, allows the model to be fine-tuned with novel learnings (due to adjusted parameters) and gain an inccreased accuracy. This is achieved all while preventing overfitting, showing at least a 2% increase in accuracy (after fine-tuning).</p>
        
        <p class="font-mono text-4xl font-bold py-2 px-4">Step 9. Evaluating the Model</p>
        <img src="/table_a.png" alt="table_a" class="w-3/4 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">To sum it all up, apart from the traing loss, validation loss, validation accuracy, and training accuracy, the model is evaluated through precision, f1 scores, stability, recall, accuracy and specificity metrics. Evaluations were done per class and from the produced results, we can see which classes this model classifies the best and which are not. A unifying graph for the train vs validation loss, train vs validatoin accuracy, classification report, and confusion matrix were revealed to show the wins and limitations that the model achieved after rigorous training.</p>
        
        <p class="font-mono text-4xl font-bold py-2 px-4">Step 10. Conclusion </p>
        <img src="/confusion_a.png" alt="confusion_a" class="w-3/4 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">Overall, our developed model for a deeplearning-based approach without the employment of transformer architectures was able to provide competitive and ample image classification to properly classify if potato leaves are diseased or not, based on the six delineated classes. More so, the produced model is able to generalize across different potato leaf disease outputs as revealed in the .csv file produced in the group9_demo1.ipynb demo notebook file. Despite the limited dataset, our model was able to get a satisfactory performance, showing a validation accuracy, precision, recall, f1-score, and specificity metric across all classes that lie at 62% as its base. From the evaluated confusion matrix, we could conclude that our model classifies Bacteria most confidently, but struggles the most with classifying Pest-ridden potato leaves. To sum it all up, by utilizing proper data augmentation, cleaning extraneous features, leveraging ResNet50's base model, and optimizing the ResNet CNN with head layer modifications, we were able to produce a competitive deeplearning-based model without transformer architecture employment, outside sources, or any pretrained model in a creative fashion.</p>
    </div>
</div>