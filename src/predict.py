import os
import pandas as pd


def predict(src_filename):
    """

    :param src_filename: Data of a new patient
    :return: Returns the probability of Exitus - Death for this new patient given the data provided
    """
    new_patient_data = pd.read_csv(src_filename)

    # Put your code here... (pending to do)

    return 0.5


if __name__ == '__main__':

    print(predict(os.path.join('..', 'data', 'test-coding-a-data-predict.csv')))
