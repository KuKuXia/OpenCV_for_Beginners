# Deep Learning for OpenCV

---

## Keras Workflow

![keras-workflow](https://www.learnopencv.com/wp-content/uploads/2017/09/keras-workflow.jpg)

## Keras Layers

- Dense layers, also called fully connected layer, since, each node in the input is connected to every node in the output,

- Activation layer which includes activation functions like ReLU, tanh, sigmoid among others,

- Dropout layer – used for regularization during training,

- Flatten, Reshape, etc.

- Convolution layers – used for performing convolution,

- Pooling layers – used for down sampling,

- Recurrent layers,

- Locally-connected, normalization, etc.

  ````python
  from keras.layers import Dense, Activation, Conv2D, MaxPooling2D
  ````

## Keras Models

Keras provides two ways to define a model:

- [**Sequential**](https://keras.io/getting-started/sequential-model-guide/), used for stacking up layers – Most commonly used.

- [**Functional API**](https://keras.io/getting-started/functional-api-guide/), used for designing complex model architectures like models with multiple-outputs, shared layers etc.

  ```python
  from keras.models import Sequential
  ```

### Method 1

```python
from keras.models import Sequential
from keras.layers import Dense, Activation
 
model = Sequential([Dense(10, input_shape=(nFeatures,)), 
                    Activation('linear') ])
```

### Method 2

```python
from keras.models import Sequential
from keras.layers import Dense, Activation
 
model = Sequential()
model.add(Dense(10, input_shape=(nFeatures,)))
model.add(Activation('linear'))
```

## Configuring the training process

- Specify an Optimizer which determines how the network weights are updated
- Specify the type of cost function or loss function.
- Specify the metrics you want to evaluate during training and testing.
- Create the model graph using the backend.
- Any other advanced configuration.

```python
model.compile(optimizer='rmsprop', loss='mse', metrics=['mse', 'mae'])
```

#### ## Optimizers

Keras provides a lot of optimizers to choose from, which include

- Stochastic Gradient Descent ( SGD ),
- Adam,
- RMSprop,
- AdaGrad,
- AdaDelta, etc.

## Loss function

- binary-cross-entropy for a binary classification problem,
- categorical-cross-entropy for a multi-class classification problem,
- mean-squared-error for a regression problem and so on.

## Training

```python
model.fit(trainFeatures, trainLabels, batch_size=4, epochs = 100)
```

## Evaluating the model

- model.evaluate() – It finds the loss and metrics specified in the model.compile() step. It takes both the test data and labels as input and gives a quantitative measure of the accuracy. It can also be used to perform cross-validation and further finetune the parameters to get the best model.
- model.predict() – It finds the output for the given test data. It is useful for checking the outputs qualitatively.