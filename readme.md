# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone - HDB Price Prediction


### Problem Statement

To predict the HDB house price by creating models based on the HDB resale transactions dataset

Datasets used 2015 - 2023
To create a  model using the data to train and test towards predicting the price by using the dataset mentioned above.

### Summary

To assist future home buyers to utilise this tool to evaluate the price of a HDB

To serve as a guide whether the price on other websites are inflated on in line with the market value.


### Process

Columns that were dropped were 'lease_commence_date', 'month', 'street_name', 'block' as it's not significant for feature engineering.

Categorical variables were converted to one-hot encoded columns using one-hot encoder to make give it a quantitative value to pushed to the model.

The training data was split using scikit-learn train_test_split and further enhance with hyper-parameters to allow the model to produce a better score.
However more can be done introducing more models to train the data with for compare and contrast.

I tested the models with linear regression and random forest regressor. Random forest regressor gave a better score to proceed to pushing the data to the UI.

The model was then deployed to a UI platform, the platform in use is streamlit for usability.

Model | Test R^2 Score | Test RMSE 
--- |--- | ---
Linear Regression | 0.795 | 72,969.34 
Random Forest Regressor | 0.905 | 45,204.75 


### Conclusion

As mentioned above, certain tweaks and changes will be able to improve the model.
By utilizing a wider dataset for more accurate modelling, as mentioned above to introduced other types of model for compare and comparison also by refining the UI Experience by omitting certain features to improve usability.

