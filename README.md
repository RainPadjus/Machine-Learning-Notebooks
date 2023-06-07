# Machine-Learning-Notebooks
Bunch of ML/DL notebooks. Code, exercises, testing, etc.


# First Project: TensorForge - Deep Learning Library from Scratch

This project demonstrates the creation of a deep learning library called TensorForge, built from scratch using NumPy. The library features basic tensor operations, layers, and optimization functions, and uses a simple feedforward neural network to classify the MNIST dataset.

The code carries out the following steps:

1. Define the `Tensor` class with basic tensor operations and autograd functionality.
2. Define the `SGD` optimizer class for parameter updates.
3. Define various `Layer` classes, including `Linear`, `Sequential`, `Tanh`, `Sigmoid`, and `MSELoss`.
4. Load and preprocess the MNIST dataset.
5. Create a feedforward neural network model using the TensorForge library.
6. Train the model using the SGD optimizer and MSELoss.
7. Test the trained model on some samples from the MNIST dataset.

The TensorForge library provides an excellent starting point for understanding the inner workings of deep learning libraries and can be extended with additional functionality as needed.

# Second Project:GAN with TensorForge

This project demonstrates the implementation and training of a Generative Adversarial Network (GAN) using the TensorForge library on the MNIST dataset. The GAN consists of two models: a Generator and a Discriminator. The Generator generates realistic images from random noise, while the Discriminator distinguishes between real and generated images.

The code carries out the following steps:

1. Define the Generator and Discriminator using the `Sequential` class with `Linear` layers and `LeakyReLU` activations.
2. Initialize the models, `MSELoss` loss function, and `SGD` optimizers for both models.
3. Load and preprocess the MNIST dataset.
4. Train the GAN using a loop for 20 epochs with a batch size of 100.
5. Print the losses for each epoch and model.

This GAN example provides a practical application of the TensorForge library and helps in understanding GAN training dynamics.


## Third Project: Morse Code Decoder

This project is a Morse code decoder that takes a string of binary-encoded Morse code and decodes it into human-readable text. 
The decoder processes the input bits and uses a clustering algorithm to determine the Morse code's structure.

The code first decodes the binary string into Morse code by identifying the lengths of ones and zeros, representing dots, dashes, and spaces. 
Then, it clusters the lengths to differentiate between dots, dashes, and spaces within characters and words. Finally, it translates the clustered Morse code into human-readable text.

Binary-encoded Morse Code Input ==>> Decode Bits into Morse Code ==>> Cluster Lengths to Differentiate Morse Code Elements ==>>Translate Morse Code to Text ==>> Human-readable Text Output


# Fourth Project: Dog or Not Dog - Webcam Classifier

This project demonstrates the use of a trained classifier to identify whether a webcam feed displays a Samoyed dog or a person. The classifier is trained using images of Samoyed dogs and people obtained through DuckDuckGo searches. 

The project first downloads and processes the images, then trains a ResNet-18 model on the data. After training, the classifier is used in real-time to detect the presence of a Samoyed dog or a person in the webcam feed, and the predictions are displayed on the video feed.

The code carries out the following steps:

1. Search and download images of Samoyed dogs and people.
2. Process and resize images for model training.
3. Train a ResNet-18 model using FastAI.
4. Access the webcam feed and display predictions in real-time.

The classifier can differentiate between Samoyed dogs and people based on the webcam feed, providing a practical example of real-time object recognition using deep learning.


## Awesome Autoencoder

An exciting and educational project implementing an autoencoder, a unique type of neural network used to learn efficient encodings of input data. The autoencoder uses the famous MNIST dataset of handwritten digits.

### Inside the Autoencoder
Our autoencoder comprises an **encoder** and a **decoder**. The encoder compresses input data, while the decoder reconstructs the original data from this compressed form.

### Training and Evaluation
We train the autoencoder using the Adam optimizer and Mean Squared Error (MSE) as the loss function. After training, we evaluate its performance on a test set.

### Visualization
We provide a visualization section that displays test images, their encoded representations, and the reconstructed images.
