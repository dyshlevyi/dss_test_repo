library(dataiku)

# Recipe inputs
round <- dkuReadDataset("round", samplingMethod="head", nbRows=100000)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
R_round <- round # For this sample code, simply copy input to output


# Recipe outputs
dkuWriteDataset(R_round,"R_round")
