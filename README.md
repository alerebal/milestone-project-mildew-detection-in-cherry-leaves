## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* According to specialist of [Garden Tech webpage](https://www.gardentech.com), powdery mildew is one of the easiest plant diseases to recognize. The first sign of problems is usually white, powdery spots or patches on the top side of leaves or on plant stems. The powdery surface growth gradually spreads to cover the entire leaf, including the undersides, until the plant looks like it's dusted with white powder. Infected leaves turn yellow and twisted.
    * A average image study can help to investigate it


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requierement 1:** Data Visualization
    * We will display the average and variability image for each class(healthy or powdery mildew).
    * We will display the difference between an average healthy leaf and an average powdery mildew leaf.
    * We will display a image montage for each class of leaf, healty or powdery mildew.

* **Business Requirement 2:** Classification
    * We want to predict if a given leaf is healthy or contains powdery mildew.
    * We want to build a binary classifier and generate reports.


## ML Business Case
### PowderyMildewClf
* We want a ML model to predict if a leaf contains powdery mildew, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
* Our outcome is provide the Marianne McGuineys team a faster and reliable diagnostic if a given leaf has powdery spots or patches that can indicate that the cherry tree is not healthy.
* The model success metrics are
    * Accuracy of 65% or above on the test set
* The model output is defined as a flag, indicating if the leaf contains any feature that can show that the tree is infected. The staff of the plantation will take a picture of some leaves of the tree and upload them to the App. The preciction is made on the fly.
* Heuristic: Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.
* The training data to fit the model come from [Kaggle](https://www.kaggle.com/), there is no description available about the dataset, it contains 2104 files of healthy leaves and 2104 files of powdery mildew leaves.
    * Train data - target: leaf infected or not; features: all images


## Dashboard Design
### Page 1: Quick Project Summary
* Quick project summary
    * General information
        * Many different fungal species cause powdery mildew, with each species attacking a different plant or plant family. The widespread disease affects many plant types, from annuals and vegetables to ornamental shrubs.
        * New shoots and buds develop distorted growth. Flowers and fruit are normally spared the white mildew, but infected plants have low yields and poor-quality fruits.
        * Prevention and perseverance are essential in controlling powdery mildew. 
        * The first sign of problems is usually white, powdery spots or patches on the top side of leaves or on plant stems. The powdery surface growth gradually spreads to cover the entire leaf, including the undersides, until the plant looks like it's dusted with white powder. Infected leaves turn yellow and twisted.
    * Project Dataset
        * The available dataset contains 4208 thousand images taken from different leaves, half infected and half healthy.
    * Link to addition information
    * Business Requirements
        * The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
        * The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.
### Page 2: Leaves Visualizer
* It will answer business requirement 1
    * Checkbox 1 - Difference between average and variability image
    * Checkbox 2 - Difference between average healthy and average not healthy leaves
    * Checkbox 3 - Image Montage
### Page 3: Powdery Wildew Detector
* Business requirement 2 information.
* Link to download a set of healthe and not healthy leaves images for live prediction.
* User Interface with a file uploader widget. The user should upload leaf images. It will display the image and a prediction statement, indicating if the leaf is healthy or not.
* Table with image name and prediction results.
* Download button to download table.

** List all dashboard pages and its content, either block of information or widgets, like: buttons, checkbox, image, or any other item that your dashboard library supports.

** Eventually, during the project development, you may revisit your dashboard plan to update a give feature (for example, in the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type).


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.


## Credits 

* In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.
