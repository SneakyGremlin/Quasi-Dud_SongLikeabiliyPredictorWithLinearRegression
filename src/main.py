import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

from preparation import prep_data

pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)

originalDataFrameNormalised, predictors_train, predictors_test, response_train, response_test = prep_data()


# main method where the linear regression model resides. data has been explored and
#       prepared prior to this
def main():
    pass
    # this has been left empty on account of there being no viable model.


# This Linear Regression model uses ALL the features that preparation indicates (the "classes"
# are outlined in the README.md) !!!
def model_all_except_participant():
    relevant = ['Age Demographic', 'Relationship Level',
                'Musical Aptitude', 'Musical Affinity', 'Sensibilities', 'Intelligence',
                'Sex', 'Multiple Exposure']
    global predictors_test, predictors_train, response_train, response_test

    predictors_test = predictors_test[relevant]
    predictors_train = predictors_train[relevant]
    model = LinearRegression().fit(predictors_train, response_train)
    print(model.intercept_)  # 0.31816437
    print(model.coef_)
    # when all attributes (except Participant) were fed:
    # [0.24147986,  0.36759859,  0.17661723, -0.13100849, -0.01691545, -0.07490876
    # -0.02632066, 0.01708307]
    # ['Age Demographic', 'Relationship Level',
    #        'Musical Aptitude', 'Musical Affinity', 'Sensibilities', 'Intelligence',
    #        'Sex', 'Multiple Exposure']

    print(model.score(predictors_test, response_test))
    # the score with ALL the independent variables is 0.08512774609131568

    response_predict = model.predict(predictors_test)
    print(mean_absolute_error(response_test, response_predict))
    # 0.17401486061394217

    # FAIL


# This model removes all the variables that have no bearing (as outlined in "Exploration" TODO)
# alternatively it includes all the variables that have any bearing.
def model_a():
    relevant = ['Age Demographic', 'Relationship Level',
                'Musical Aptitude', 'Musical Affinity', 'Sensibilities',
                'Sex', 'Multiple Exposure']
    global predictors_test, predictors_train, response_train, response_test

    predictors_test = predictors_test[relevant]
    predictors_train = predictors_train[relevant]

    model = LinearRegression().fit(predictors_train, response_train)

    print(model.score(predictors_test, response_test))
    #  is 0.057290956406963134

    response_predict = model.predict(predictors_test)
    print(mean_absolute_error(response_test, response_predict))
    # 0.19

    # FAIL


# includes only the features that "have bearing or have minor bearing")
def model_b():
    relevant = ['Age Demographic', 'Sensibilities']  # seems ridiculous tbh

    global predictors_test, predictors_train, response_train, response_test

    predictors_test = predictors_test[relevant]
    predictors_train = predictors_train[relevant]

    model = LinearRegression().fit(predictors_train, response_train)

    print(model.score(predictors_test, response_test))
    # 0.060382639984997155

    response_predict = model.predict(predictors_test)
    print(mean_absolute_error(response_test, response_predict))
    # 0.17

    # FAIL


#  A little early to have a haphazard approach but... gonna listen to my gut
def model_c():
    relevant = ['Relationship Level',
                'Multiple Exposure']
    global predictors_test, predictors_train, response_train, response_test

    predictors_test = predictors_test[relevant]
    predictors_train = predictors_train[relevant]

    model = LinearRegression().fit(predictors_train, response_train)

    print(model.score(predictors_test, response_test))
    print(model.coef_)
    # -0.021446832171691632
    # [[ 0.35225778 -0.01829234]]

    response_predict = model.predict(predictors_test)
    print(mean_absolute_error(response_test, response_predict))
    # 0.2

    # FAIL


# ordered chaos
def model_d():
    relevant = ['Relationship Level',
                'Musical Affinity',
                'Musical Aptitude']
    global predictors_test, predictors_train, response_train, response_test

    predictors_test = predictors_test[relevant]
    predictors_train = predictors_train[relevant]

    model = LinearRegression().fit(predictors_train, response_train)

    print(model.score(predictors_test, response_test))
    print(model.coef_)

    # -0.021446832171691632
    # [[ 0.35225778 -0.01829234]]

    response_predict = model.predict(predictors_test)
    print(mean_absolute_error(response_test, response_predict))
    # +- 0.2

    # FAIL


# does linearity even exist for even one of the attributes?
def model_e():
    relevant = ['Relationship Level']

    global predictors_test, predictors_train, response_train, response_test

    predictors_test = predictors_test[relevant]
    predictors_train = predictors_train[relevant]

    model = LinearRegression().fit(predictors_train, response_train)

    print(model.score(predictors_test, response_test))
    print(model.coef_)


    response_predict = model.predict(predictors_test)
    print(mean_absolute_error(response_test, response_predict))

    # FAIL

# This was excerpted from the preparation module to aid in the model making process.

# "0. age_demographic_has_bearing_on_response \n" +
# "1. relationship_level_may_have_bearing_on_response \n" +
# "2. musical_aptitude_may_have_minor_bearing_on_response \n" +
# "3. musical_affinity_may_have_minor_bearing_on_response \n" +
# "4. sensibilities_has_minor_bearing_on_response \n" +
# "5. intelligence_has_no_bearing_on_response \n" +
# "6. sex_may_have_minor_bearing_on_response \n" +
# "7. multiple_exposure_may_have_bearing_on_response \n" +
# "8. response_distribution \n" +
# "9. response_normalised_distribution \n"
