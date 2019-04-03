# AWS SageMaker :o: sp19-616-111 ✋

Amazon SageMaker is a fully managed machine learning service. Using Amazon SageMaker, data scientists and developers can quickly and easily build and train machine learning models, and then directly deploy them into a production-ready hosted environment. 

Amazon SageMaker provides following advantages:

- An integrated Jupyter authoring notebook instance for easy access to your data sources 
  for exploration and analysis, so you do not have to manage servers
- Common machine learning algorithms that are optimized to run efficiently against 
  extremely large data in a distributed environment
- Native support for bring-your-own-algorithms and frameworks, Amazon SageMaker 
  offers flexible distributed training options that adjust to your specific workflows
- Deploy a model into a secure and scalable environment by launching it with a one 
  click from the Amazon SageMaker console
- Training and hosting are billed by minutes of usage, with 
  no minimum fees and no upfront commitments.

## Machine Learning with Amazon SageMaker

We explained a typical machine learning workflow and summarizes how you accomplish those tasks with Amazon SageMaker.

In general, machine learning is all about you *teach* a computer to make predictions, or inferences. As a first step, you use an algorithm and example data to train a model. Then you integrate your model into your application to generate inferences in real time and at scale. In a production environment, a model typically learns from millions of example data items and produces inferences in hundreds to less than 20 milliseconds.

The following :o: use proper image notation with caption and citation as discussed in notation.md 
diagram illustrates the typical workflow for creating a machine learning model:

![AWS SageMaker](images/machine_learning_workflow.png)

As the above diagram illustrates, you typically perform the following activities:

Generate example data—To train a model, you need example data. The type of data that you need depends on the business problem that you want the model to solve (the inferences that you want the model to generate). For example, suppose that you want to create a model to predict a number given an input image of a handwritten digit. To train such a model, you need example images of handwritten numbers.

Data scientists: often spend a lot of time exploring and preprocessing, or "wrangling," example data before using it for model training. To preprocess data, you typically do the following:

- Fetch the data: You might have in-house example data repositories, or you might use datasets that are publicly available. Typically, you pull the dataset or datasets into a single repository.

- Clean: the data—To improve model training, inspect the data and clean it up as needed. For example, if your data has a country name attribute with values United States and US, you might want to edit the data to be consistent.

- Prepare or transform: the data—To improve performance, you might perform additional data transformations. For example, you might choose to combine attributes. If your model predicts the conditions that require de-icing an aircraft instead of using temperature and humidity attributes separately, you might combine those attributes into a new attribute to get a better model.

In Amazon SageMaker, you preprocess example data in a Jupyter notebook on your notebook instance. You use your notebook to fetch your dataset, explore it and prepare it for model training. 

Train a model—Model training includes both training and evaluating the model, as follows:

- Training the model: To train a model, you need an algorithm. The algorithm you choose depends on a number of factors. For a quick, out-of-the-box solution, you might be able to use one of the algorithms that Amazon SageMaker provides.


You also need compute resources for training. Depending on the size of your training dataset and how quickly you need the results, you can use resources ranging from a single, small general-purpose instance to a distributed cluster of GPU instances. For more information, refer the sub-section Train a Model with Amazon SageMaker.

 
Evaluating the model—After you've trained your model, you evaluate it to determine whether the accuracy of the inferences is acceptable. In Amazon SageMaker, you use either the AWS SDK for Python (Boto) or the high-level Python library that Amazon SageMaker provides to send requests to the model for inferences.

You use a Jupyter notebook in your Amazon SageMaker notebook instance to train and evaluate your model.

- Deploy the model: You traditionally re-engineer a model before you integrate it with your application and deploy it. With Amazon SageMaker hosting services, you can deploy your model independently, decoupling it from your application code. For more information, see Deploy a Model on Amazon SageMaker Hosting Services.

Machine learning is a continuous cycle. After deploying a model, you monitor the inferences, then collect "ground truth," and evaluate the model to identify drift. You then increase the accuracy of your inferences by updating your training data to include the newly collected ground truth, by retraining the model with the new dataset. As more and more example data becomes available, you continue retraining your model to increase accuracy.


## Get Start with SageMaker

In this section, we will explain on how you create your first Amazon SageMaker notebook instance, and train a model. You train the model using an algorithm provided by Amazon SageMaker, deploy it, and validate it by sending inference requests to the model's endpoint.

You use this notebook instance for all kind of machine learning models that are available as part of AWS SageMaker notebook instance or customer machine learning libraries.

### Train a Model with Amazon SageMaker

To train a model in Amazon SageMakar, you can Download the MNIST dataset to your Amazon SageMaker notebook instance, then review the data and preprocess it. For efficient training, you convert the dataset from the numpy.array format to the RecordIO protobuf format. A numpy.array is an n-dimensional array object that the NumPy scientific computing library uses. RecordIO protobuf is a binary data format that the Amazon SageMaker K-Means algorithm expects as input.

- Start an Amazon SageMaker training job.

- Deploy the model in Amazon SageMaker.

- Validate the model by sending inference requests to the model's endpoint. You send images of handwritten, single-digit numbers. The model returns the number of the cluster (0 through 9) that the images belong to.

Important to note that, for model training, deployment, and validation, you can use either of the following:

- The high-level Python library provided by Amazon SageMaker

- The AWS SDK for Python (Boto)

The high-level library abstracts several implementation details, and is easy to use. This exercise provides separate code examples using both libraries. If you're a first-time Amazon SageMaker user, we recommend that you use the high-level Python library.

Basically, there are two ways to practice this exercise:

Follow the steps to create, deploy, and validate the model. You create a Jupyter notebook in your Amazon SageMaker notebook instance, and copy code, paste it into the notebook, and run it.

If you're familiar with using sample notebooks, open and run the following example notebooks that Amazon SageMaker provides in the SageMaker Python SDK section of the SageMaker Examples tab of your notebook instance:

1. kmeans_mnist.ipynb

2. kmeans_mnist_lowlevel.ipynb
