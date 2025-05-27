<div class="flex justify-center p-12 space-y-4 max-w-10xl">
    <div class="flex-col w-10/12 max-w-5xl text-center bg-gray-100 rounded-lg shadow-lg p-8">
        <h1 class="text-7xl font-bold mb-12">Model A</h1>
        <p class="font-mono text-5xl font-bold py-2 px-4">Description</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">This is the first model of the project, which is a CNN that is based off the Resnet architecture that will be trained to classify the diseases or lack of in images of potato plants. </p>
        <p class="font-mono text-5xl font-bold py-2 px-4">Methodology</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 1. Setting up the seed and the CPU/GPU dependencies</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">For reproducibility and make the GPU work for training</p>
        
        <p class="font-mono text-4xl font-bold py-2 px-4">Step 2. Extracting and Preprocessing Images</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">From the zip file, the dataset is extracted and cleaned based on the correct filetype, also deleting corruptfiles. The images are resized to 224 x 224 pixels and normalizing them to the image.net values. The Train Data was augmented to have verticalflip, horizontalflip, random rotation, color jitter, and gaussian blur to aviod overfitting and make the model not memorize the data. The validation dataset would not have an augmentation. We also used an 80-20 split train-validation dataset since test data set will be given later.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 3. Building the Model</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">Our model uses the Resnet CNN model with pretrained = false for no weights will be used from online source, which is we will have a scratch resnet model. We replaced the head of the resnet to have a drop out of 50% to avoid overfitting. We also used AdamW optimizers, a scheduler that will reduce Learning rates on plateu and an criterion with entrophyloss.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 4. Training the Model</p>        
        <p class="font-mono text-lg py-2 px-4 text-justify">Our model trains for 50 epochs with a patience of 5 if there is no improvement from the validation accuracy. Also the train accuracy and validation accuracy is printed to check for overfitting and plateu for manual stopping</p>
        
        <p class="font-mono text-4xl font-bold py-2 px-4">Step 5. Evaluating the Model</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">Evaluating the Model through the precision, f1 scores, stability, recall, accuracy and specificity is printed at the end. Evaluation per class, we can see which classes this model classifies the best and which are not. We also have graph for the train vs validity values aswell as the confusion matrices, these finds whether there is overfitting and find the confusion between classes</p>
        
        <p class="font-mono text-4xl font-bold py-2 px-4">Step 6. Predition</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">ALthough not included in this file, the demo_deeplearning_cnn has the notebook code to run and use the model to predict the test dataset given and gives a csv of the predictions per image..</p>
    </div>
</div>