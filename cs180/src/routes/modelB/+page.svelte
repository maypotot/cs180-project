<div class="flex justify-center p-12 space-y-4 max-w-10xl">
    <div class="flex-col w-10/12 max-w-5xl text-center bg-gray-100 rounded-lg shadow-lg p-8">
        <h1 class="text-7xl font-bold mb-12">Model B</h1>
        <p class="font-mono text-5xl font-bold py-2 px-4">Description</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">This is the second model of the project, which is a deep learning model that employs a transfomer architecture that will be trained to classify the diseases or lack of in images of potato plants. </p>
        <p class="font-mono text-5xl font-bold py-2 px-4">Methodology</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 1. Preprocessing the Images</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">Cleaning the dataset by resizing the images to 224 x 224 pixels and normalizing it to the Image.net values for normalization. For the Train Data, we used random Crop, random horizontalflip, random verticalflip, random rotation, color jitte, and gaussian blur to avoid overfitting and make the model memorize the data. For the validation data, no augmentations will be done. We used an 80 - 20 split for the train - validation, from the dataset, as the the test data will come at a later stage of this project.</p>
        
        <p class="font-mono text-4xl font-bold py-2 px-4">Step 2. Building the Model</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">Our model follows the traditional ViT model from the lessons, we build it from scratch. The model consists of a patch embedding layer instead of convolutional layer, where its purpose is to split the image into patches. We also have class token and position embedding which retain spatial information and handles the patch sequence. Next is the transformer layer which processes and learns the image. Lastly, the mlp Classification head handles the classification. The last two layers contain dropouts to handle overfitting and uses GELU.</p>
        <img src="/vit.png" alt="ViT Model" class="w-full h-auto my-4 rounded-lg shadow-lg">

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 3. Training the Model</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">Training the model, we used 200 epochs since training ViT models from scratch needs alot of epochs to learn. ViT also needs alot of dataset, but currently we have very little which is why the 200 epoch and patience will be high. Per epoch, validity accuracy and loss, as well as train accuracy and loss is printed to check for overfitting and plateus for manual stopping.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 4. Evaluating the Model</p>        
        <p class="font-mono text-lg py-2 px-4 text-justify">Evaluatiung the model through accuracy, F1 scores, stabiility, recall and specificity per class is printed at the end of this notebook. With this evaluation we are able to evaluate the performance of the model per class, knowing which class has a harder time to recognize by the model. Evaluating also includes the graph for the Train vs Validity values aswell as the confusion matrices, which finds overfitting and find the models confusion between classes.</p>
        
        <p class="font-mono text-4xl font-bold py-2 px-4">Step 5. Preditcion</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">After, using the test dataset, the model is used to predict this dataset, which is saved at the deeplearning_vit_predictions.csv file, with also evaluation on how it accuractely classifies potato diseases</p>
    </div>
</div>