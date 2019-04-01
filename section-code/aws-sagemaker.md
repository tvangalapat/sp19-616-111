# AWS SageMaker :o: sp19-616-111 ✋

<p> Amazon SageMaker </p> is a fully managed machine learning service. Using Amazon SageMaker, data scientists and developers can quickly and easily build and train machine learning models, and then directly deploy them into a production-ready hosted environment. 

Amazon SageMaker provides following advantages:

- An integrated Jupyter authoring notebook instance for easy access to your data sources for exploration and analysis, so you don't have to manage servers
- Common machine learning algorithms that are optimized to run efficiently against extremely large data in a distributed environment
- Native support for bring-your-own-algorithms and frameworks, Amazon SageMaker offers flexible distributed training options that adjust to your specific workflows
- Deploy a model into a secure and scalable environment by launching it with a one click from the Amazon SageMaker console. - - Training and hosting are billed by minutes of usage, with no minimum fees and no upfront commitments.

## How Machine Learning with Amazon SageMaker?

In this section, we described a typical machine learning workflow and summarizes how you accomplish those tasks with Amazon SageMaker.

In general, machine learning is all about you "teach" a computer to make predictions, or inferences. As a first step, you use an algorithm and example data to train a model. Then you integrate your model into your application to generate inferences in real time and at scale. In a production environment, a model typically learns from millions of example data items and produces inferences in hundreds to less than 20 milliseconds.

The following diagram illustrates the typical workflow for creating a machine learning model:

![AWS SageMaker](images/machine_learning_workflow.png){#fig:machinelearning-workflow}
