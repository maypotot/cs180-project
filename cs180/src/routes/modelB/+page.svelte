<div class="flex justify-center p-12 space-y-4 max-w-10xl">
    <div class="flex flex-col w-10/12 justify-center items-center max-w-5xl text-center bg-gray-100 rounded-lg shadow-lg p-8">
        <h1 class="text-7xl font-bold mb-12">Model B</h1>
        <p class="font-mono text-5xl font-bold py-2 px-4">Description</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">This is the second model of the project, which is a deep learning model that employs a transfomer architecture that will be trained to classify the diseases or lack of in images of potato plants. </p>
        <p class="font-mono text-5xl font-bold py-2 px-4">Methodology</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 1. Setup the Random Seed</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">We set the random seed to 42, which is for reproducibility. The values could be edited to a different value which would not affect the performance of the model and would not cause overfitting</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 2. Set up proper CPU/GPU dependencies</p>
        <img src="/gpu.png" alt="gpu" class="w-1/2 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">Using GPU is much better in terms of performance, training time, and it would safekeep hardware, while using CPU will be much more slower and also might fry your CPU, thus the need for GPU to be used</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 3. Preprocessing the Images</p>
        <p class="font-mono text-lg py-2 px-4 text-justify">Cleaning the dataset by resizing the images to 288 x 288 pixels and normalizing it to the Image.net values for normalization. For the Train Data, we used random Crop, random horizontalflip, random verticalflip, random rotation, color jitter, and gaussian blur to avoid overfitting and make the model not memorize the data. For the validation data, no augmentations will be done.
We used an 80 - 20 split for the train - validation, from the dataset, as the the test data will come at a later stage of this project.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 4. Building the Model</p>
        <img src="/vit.png" alt="healthy" class="w-3/4 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">Our model follows the traditional ViT model from the lessons, we build it from scratch. The model consists of a patch embedding layer instead of convolutional layer, where its purpose is to split the image into patches. We also have class token and position embedding which retain spatial information and handles the patch sequence. Next is the transformer layer which processes and learns the image. Lastly, the mlp Classification head handles the classification. The last two layers contain dropouts to handle overfitting and uses GELU</p>


        <p class="font-mono text-4xl font-bold py-2 px-4">Step 5. Training the Model</p>
        <img src="/training_b.png" alt="training_b" class="w-3/4 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">Training the model, we used 200 epochs since training ViT models from scratch needs alot of epochs to learn. ViT also needs alot of dataset, but currently we have very little which is why the 200 epoch and patience will be high. Per epoch, validity accuracy and loss, as well as train accuracy and loss is printed to check for overfitting and plateus for manual stopping</p>
        
        <p class="font-mono text-4xl font-bold py-2 px-4">Step 6. Evaluating the Model</p>
        <img src="/table_b.png" alt="training_b" class="w-3/4 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">Evaluatiung the model through accuracy, F1 scores, stability, recall and specificity per class is printed at the end of this notebook. With this evaluation we are able to evaluate the performance of the model per class, knowing which class has a harder time to recognize by the model. Evaluating also includes the graph for the Train vs Validity values aswell as the confusion matrices, which finds overfitting and find the models confusion between classes.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 7. Prediction using Test Dataset</p>
        <img src="/csv.png" alt="csv" class="w-1/4 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">After, using the test dataset, the model is used to predict this dataset, which is saved at the deeplearning_vit_predictions.csv file, with also evaluation on how it accuractely classifies potato diseases.</p>

        <p class="font-mono text-4xl font-bold py-2 px-4">Step 8. Conclusion </p>
        <img src="/confusion_b.png" alt="confusion_b" class="w-3/4 h-auto my-4 rounded-lg shadow-lg">
        <p class="font-mono text-lg py-2 px-4 text-justify">Overall, our developed deeplearning-based approach using the Vision Transformer was able to also provide an competitive image classification model for classifying potato diseases with a validation accuracy of 61%, which also generalizes majority of potato leaf diseases. With using patching layer to patch the images and train them per patch and learning that with our ViT model, following the architechture of the traditional ViT helped us create this model achieving satisfactory results. As read from sources, ViT requires lots of datasets with 10k above as its minimum, having 4k datasets is a huge blow to the performance of our model as it reaches a stagnant accuracy at epoch 80s above. Also ViT requires lots of epochs, but with the lack of datasets it plateu at 80 epoch in which the normal ViT with 10k images reaaches to 200 and more. With our model achieving 62% accuracy from the testing, in the Classification Matrix, the precision has a 67%, and a 67% F1-Score, with that this model have achieved a satisfactory model for classifying Potato Disease from its leaves. The confusion matrix shows that the model is having troubled differentiating pest and fungi, and having the best in classifying fungi. One thing that we can improve here is in our model is maybe finding another way to get a lot of datasets to feed in our ViT, also we havent explored much using pretrained models to be added or finetuned in this model. This is our creative model especially with guide from the ViT architecture, and tweaking the layers, we are able to create this satisfactory model.</p>
    </div>
</div>