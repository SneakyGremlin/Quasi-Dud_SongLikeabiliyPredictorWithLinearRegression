import matplotlib.pyplot as plt
import pandas as pd

from preparation import normalise_response
from preparation import normalise_intelligence

# NOTE: the empty values are not filled in yet (no preparation has been done)
# mean and/or (at discretion) median of independent variable group aggregates has >=0.5 effect on response : bearing
# " <0.5 & >0.1 " = minor bearing.
# " <0.1 = no bearing.

originalDataFrame = pd.read_excel("AliasedDataForAlgorithm.xlsx", sheet_name="data")


# to indicate that age has bearing on the Response (>0.5)
def age_demographic_has_bearing_on_response():
    print(originalDataFrame[["Age Demographic"]].value_counts())
    print("\n")
    # We have class imbalance here: there are much more GenZs in comparison to the other designations
    # To work around this problem I randomly choose 11 (the difference b/w GenX and GenY is 2 thus the mean is)
    # GenZ records 10 times, take the average of their Response each time, and then take the average of the three
    # iterations. I then compare this to the average of the Response of GenY and GenX respectively.
    # NOTE: by average I refer to the median whenever appropriate (because outliers in this case will have a significant
    #       effect owing to paucity). The median values are in order X Y Z: 2.5, 3.5, 3.7(3)
    #       I ran this with the means as well and the results are in order X Y Z: 2.8, 3.3, 3.6 which still justifies
    #       the correlation

    mask_gen_z = originalDataFrame["Age Demographic"] == "GenZ"
    gen_z_df = originalDataFrame[mask_gen_z]

    total = 0
    for i in range(10):
        total += gen_z_df.sample(n=11)["Response"].mean()  # non-declarative auto access of "global"

    gen_z_average = total / 10

    gen_y_average = originalDataFrame[originalDataFrame["Age Demographic"] == "GenY"][["Response"]].mean()[0]
    gen_x_average = originalDataFrame[originalDataFrame["Age Demographic"] == "GenX"][["Response"]].mean()[0]

    print("The three averages are (in order X Y Z) " + str(gen_x_average) + " "
          + str(gen_y_average) + " " + str(gen_z_average) + "\n")  # 2.5, 3.5, 4.0

    # we conclude, therefore, that age is indeed a determining feature (insofar as can be determined from the dataset
    # that was used)

    # I now use a comparison visualisation box plot:
    originalDataFrame.pivot(columns="Age Demographic", values="Response").plot(kind="box")
    plt.show()


# to indicate relationship level/perception of the artist (refer to read me) may impact whether a person likes their
# song
# NOTE: this seems an outlandish exploration (I refer to the box plot distribution towards the high relationship
# `     segment) so I will attempt to hypothesise:
#       >>> Since this is a more personal interaction, it may be that those close to me may choose to be as constructive
#           as possible (high volubility (ref "Response" attribute exposition in README.md)). In their good intentions
#           they may have been assigned such a score (I couple this with the fact that I was profoundly adherent when I
#           assigned the scores as outlined in "Response (same reference as aforementioned).
#       >>> This has an important implication: "Relationship Level" and "Artist Perception" may not be directly
#           interchangeable. For artists, their audiences engage in parasocial interactions, and mostly the relationship
#           borders on a "consider them an icon/godhead" type. Thus, criticisms would be majorly withheld though they
#           may offer some insight into preferences if prompted.
#       >>> for the general "inner" distribution, I listen to songs from artists I care not two whits about and even
#           artists that I find distasteful. Perhaps only individuals who consider some artists anathema would
#           actively CHOOSE to "dislike" the song. Also, the participants that constitute this sector were sufficiently
#           terse (one may argue they chose to withheld criticisms but the "inner distribution" includes people, I
#           have a distaste for me.
#       >>> the relationship between low relationship participants and the response was predicable (though maybe
#           I was implicitly weighing their criticism more? Perhaps, but I did devise the number iteratively so this
#           mitigates against that.
def relationship_level_may_have_bearing_on_response():
    # setting up preliminary expectations.
    originalDataFrame.plot(kind="scatter", x="Relationship Level", y="Response")
    plt.show()

    mask_below_three = originalDataFrame["Relationship Level"] < 3
    mask_above_and_including_three = originalDataFrame["Relationship Level"] >= 3
    bt_df = originalDataFrame[mask_below_three]
    at_df = originalDataFrame[mask_above_and_including_three]

    print(bt_df.shape)
    print(at_df.shape)

    # median owing to lass imbalance. ratio is approximately ~1:3; below three: above and equal to three
    print("The difference in medians is " + str(
        abs(bt_df[["Response"]].median() - at_df[["Response"]].median())[0]))  # 0.5

    # will find the mean 10 times of the above and equals 3 dataframe.
    total = 0
    for i in range(10):
        total += at_df.sample(n=26)["Response"].mean()  # 0.5
    total = total / 10

    print("The difference in means is " + str(abs(total - at_df["Response"].mean())) + "\n")  # 0.03, 0.02, 0.01...

    # a composition graph would be misleading (at least for me) owing to the class imbalance

    # a comparison visualisation may be mildly instrumental owing to the class imbalance
    originalDataFrame.pivot(columns="Relationship Level", values="Response").plot(kind="box")
    plt.show()
    # interesting insight: highly below average values and highly above average values have a greater chance of being
    #                      off the mean of the dataset but the primary good responses come from people within 2-5 i.e.
    #                      I am not too liked or too disliked.

    # conclusion: relationship level may have bearing on likability of the song.


# QUALIFIED RELATIONSHIP INFERENCE OWING TO MAJOR CLASS IMBALANCE.
# musical aptitude may have minor bearing on response.
def musical_aptitude_may_have_minor_bearing_on_response():
    print(originalDataFrame["Musical Aptitude"].value_counts())
    # here we have a ginormous class imbalance
    # owing to the class imbalance the method below may be immensely frowned upon but I pursue it nonetheless
    # I divide the dataframe into two parts: a dataframe consisting of Participants with musical aptitude 0, and then
    #    the others.
    mask_zero = originalDataFrame["Musical Aptitude"] == 0
    mask_non_zero = originalDataFrame["Musical Aptitude"] > 0
    df_zero = originalDataFrame[mask_zero]
    df_non_zero = originalDataFrame[mask_non_zero]

    print(df_zero.shape)
    print(df_non_zero.shape)
    # ratio of zero to non-zero is ~ 7:4

    # first I explore the distribution of responses in the zero dataframe
    df_zero["Response"].plot(kind="hist")
    plt.show()
    # discouraging results. Huge spread of values

    # now I explore the distribution in the non-zero df
    df_non_zero["Response"].plot(kind="hist")
    plt.show()
    # midly encouraging, the distribution shifts to the right.

    # I now calculate the mean and median and compare it (I use sampling owing to imbalance)
    total_mean = 0
    total_median = 0
    for i in range(10):
        total_mean += df_zero.sample(n=39)["Response"].mean()
        total_median += df_zero.sample(n=39)["Response"].median()
    zero_mean = total_mean / 10
    zero_median = total_median / 10

    print("\n")
    print("The difference in means is " + str(abs(zero_mean - df_non_zero["Response"].mean())))  # 0.06
    print("The difference in medians is " + str(abs(zero_median - df_non_zero["Response"].median())))  # 0.3
    # hypothesis: yes there is class imbalance BUT it approximates 7:4. It is possible that a positive correlation
    #       exists between Musical Affinity and Response since the medians are marginally distal.


# Musical Affinity may have minor bearing
def musical_affinity_may_have_minor_bearing_on_response():
    print(originalDataFrame["Musical Affinity"].value_counts().sort_values())
    originalDataFrame[["Musical Affinity"]].plot(kind="hist")
    plt.show()
    # from the histogram we can see we have a relatively minor class imbalance (look two on the x-axis)

    mask_below_two = originalDataFrame["Musical Affinity"] < 2
    df_bt = originalDataFrame[mask_below_two]
    mask_above_equal_two = originalDataFrame["Musical Affinity"] >= 2
    df_aet = originalDataFrame[mask_above_equal_two]

    print(df_bt.shape)  # 48
    print(df_aet.shape)  # 65
    # difference of 17/113 = 0.15 which is enough for me to resort to sampling.
    # I use the mean since the data is relatively populous (but the median as well because "relatively")

    total_mean = 0
    total_median = 0
    for i in range(10):
        total_mean += df_aet.sample(n=48)["Response"].mean()
        total_median += df_aet.sample(n=48)["Response"].mean()

    above_equal_two_mean = total_mean / 10
    below_two_mean = df_bt["Response"].mean()
    above_equal_two_median = total_median / 10
    below_two_median = df_bt["Response"].median()

    print(" \nThe difference in their means is " + str(abs(above_equal_two_mean - below_two_mean)) + "\n")  # 0.06, 0.03
    print("The difference in their medians is " + str(abs(above_equal_two_median - below_two_median)) + "\n")  # 0.4

    # for further exploration a box plot
    # all values above and equal to 2 assume 2 as their value, all values below assume 1
    original_data_frame_copy = originalDataFrame.copy(deep=True)

    original_data_frame_copy.loc[mask_below_two, ["Musical Affinity"]] = 1
    original_data_frame_copy.loc[mask_above_equal_two, ["Musical Affinity"]] = 2
    print(original_data_frame_copy["Musical Affinity"].value_counts())

    # now we make the box plot
    original_data_frame_copy.pivot(columns="Musical Affinity", values="Response").plot(kind="box")
    plt.show()

    # INSIGHT: oddly enough people who don't have musical affinities are more prone to give better remarks, maybe
    #          due to lack of experience?


# to illustrate sensibility as I defined it has little bearing on the Response.
# NOTE: This is immensely surprising for me: I would think aesthetes would show greater appreciation. Perhaps
#       it may be they are capable of "seeing" more or feeling more, or perhaps my methodology or definition or both
#       were flawed. (This is surprising since I expected the correlation to be greater).
def sensibilities_has_minor_bearing_on_response():  # both are >0.1 <0.5
    # the following scatter plot is obviously misleading owing to the class imbalance
    plot = originalDataFrame.plot(kind="scatter", x="Sensibilities", y="Response")
    plt.show()

    print(originalDataFrame[["Sensibilities"]].value_counts())
    print()

    # unsurprisingly, I run into the problem of class imbalance once again.
    # to resolve this the following will be done: every record above (and including) 2
    # will be treated the same; likewise will be done for below 2. the ratio imbalance is
    # ~2:1 so sample will be used to mitigate against this.
    mask_upper = originalDataFrame["Sensibilities"] >= 2
    usensible_df = originalDataFrame[mask_upper]
    mask_lower = originalDataFrame["Sensibilities"] < 2
    dsensible_df = originalDataFrame[mask_lower]

    # now if the means are sufficiently close to each other we will disregard sensibilities (we use means because
    # this time the data is relatively large)
    # P.S. the sample() call is to account for the class imbalance, and I do I iterate for the selfsame reason.

    total_mean = 0
    total_median = 0

    for i in range(10):
        total_mean += dsensible_df[["Response"]].sample(n=39).mean()[0]
        total_median += dsensible_df[["Response"]].sample(n=39).median()[0]
    usensible_median = total_median / 10
    usensible_mean = total_mean / 10

    print(" The difference in the mean is: " + str(abs(usensible_df[["Response"]].mean()[0] -
                                                       usensible_mean)))  # 0.2,0.1,0.2

    # but I still use the median
    print(" The difference in the median is: " + str(abs(usensible_df[["Response"]].median()[0] -
                                                         usensible_median)))  # 0.4,0.3

    # we thus conclude sensibilities, as I inferred it, has minor bearing on the Response


# To indicate that intelligence has no bearing on the response variable
def intelligence_has_no_bearing_on_response():
    normalise_response(originalDataFrame)
    normalise_intelligence(originalDataFrame)
    plot_intelligence = originalDataFrame["Intelligence"].plot(kind="hist", bins=10)
    plt.show()
    plot_response = originalDataFrame["Response"].plot(kind="hist", bins=10)
    plt.show()
    # As can be seen the distributions do not match. I was prompted to think a correlation might exist.

    # the following section pertaining to scatter involves a lot of drudgery, skip if you feel like it.
    # We plot a scatter to show a relation.
    print(originalDataFrame.groupby("Intelligence")["Response"].value_counts())  # compare this with the graph
    plot_scatter = originalDataFrame.plot(kind="scatter", x="Intelligence", y="Response")
    plt.show()
    # as one can see from the scatter plot if a line of best fit were drawn its gradient would be > 1
    # BUT that would only be true since due to multiple mapping. There might be greater variance on the north-west
    # side of the graph, THAT may be being reflected.

    # here I show using simple aggregates that Intelligence does not have bearing.
    # I chose the median as the splitting point to approximately equally divide the values (they aren't equally
    # divided on account of the equals in one of the mask).
    mask_under_median = originalDataFrame["Intelligence"] < originalDataFrame["Intelligence"].median()
    mask_above_median = originalDataFrame["Intelligence"] >= originalDataFrame["Intelligence"].median()
    df_below = originalDataFrame[mask_under_median]
    df_above = originalDataFrame[mask_above_median]

    print(df_below.shape)
    print(df_above.shape)
    # minor class imbalance still not ignoring below:above = ~5:6.5

    # calculating median and mode using iteration and sampling
    total_median = 0
    total_mean = 0
    for i in range(10):
        total_mean += df_above.sample(n=48)["Response"].mean()
        total_median += df_above.sample(n=48)["Response"].median()
    above_mean = total_mean / 10
    above_median = total_median / 10

    print("\nThe difference in means is " + str(abs(above_mean - df_below["Response"].mean())))  # 0.015
    print("\nThe difference in medians is " + str(abs(above_median - df_below["Response"].median())))  # 0.003


# QUALIFIED DUE TO CLASS IMBALANCE
# to indicate that gender may have minor bearing on Response.
def sex_may_have_minor_bearing_on_response():
    print(originalDataFrame["Sex"].value_counts(normalize=True))
    print(originalDataFrame["Sex"].value_counts())
    # as we can see ratio of men to women is ~4:1; this is a testament to the fact I got no rizz.
    # finding the median of the women and the men.

    print("\n")

    male_mask = originalDataFrame["Sex"] == "Male"
    df_male = originalDataFrame[male_mask]
    female_mask = originalDataFrame["Sex"] == "Female"
    df_female = originalDataFrame[female_mask]

    # using sampling and iteration
    mean_total = 0
    median_total = 0

    for i in range(25):
        mean_total += df_male.sample(n=23)["Response"].mean()
        median_total += df_male.sample(n=23)["Response"].median()

    print("The difference in their means is " + str(abs(mean_total / 25 - df_female["Response"].mean())))  # 0.02
    print("The difference in their medians is " + str(abs(median_total / 25 - df_female["Response"].median())))  # 0.27$

    # we will now utilise a comparison visualisation i.e. a box plot to show that the difference. This is
    # done in spite of the huge class imbalance only fortifying the point.
    originalDataFrame.pivot(columns="Sex", values="Response").plot(kind="box")
    plt.show()
    # a composition visualisation is not used on account of the class imbalance

    # in sum a minor correlation may exist; the difference between the differences of the means and medians suggests
    # may be due to the class imbalance but the fact that the difference of the means is negligible this is a qualified
    # correlation.


# shows that multiple exposure may have bearing
# NOTE: the probability of a positive response is greatly increased with multiple exposure as the stacked bar chart
#       and the difference b/w the mean and median suggest.
def multiple_exposure_may_have_bearing_on_response():
    # here the scatter plot is only slightly misleading.
    plot = originalDataFrame.plot(kind="scatter", x="Multiple Exposure", y="Response")
    plt.show()

    print(originalDataFrame[["Multiple Exposure"]].value_counts())
    # the difference b/w the two is 25 which is 25/113 ~= 0.22 of the total.
    # this argument is however insufficient by any standard

    # hence a stacked bar chart is made (despite the minor class imbalance)
    originalDataFrame.groupby("Multiple Exposure")["Response"].value_counts().unstack().plot(kind="bar", stacked=True)
    plt.show()
    # note how the compositions suggest multiple exposure means a better response.

    # seeing that that may still be unconvincing, so we use another graph: box
    originalDataFrame.pivot(columns="Multiple Exposure", values="Response").plot(kind="box")
    plt.show()
    # the medians and the quartiles indicate a possible positive correlation.

    # calculating the median and mean (because the outliers are quite out there).
    mask_true = originalDataFrame["Multiple Exposure"] == 1
    true_df = originalDataFrame[mask_true]
    mask_false = originalDataFrame["Multiple Exposure"] == 0
    false_df = originalDataFrame[mask_false]

    print("The difference in their medians is " + str(
        true_df["Response"].median() - (false_df["Response"].median())))  # 0.5
    print(
        "The difference in their means is " + str(true_df["Response"].mean() - (false_df["Response"].mean())))  # 0.132

    # hence, multiple exposure may have a positive correlation with Response (positive as inferred
    # by the expression)


# to show the distribution of the response.
def response_distribution():
    plot = originalDataFrame["Response"].plot(kind="hist")
    plt.show()


# to show the min-max normalisation of the response.
def response_normalised_distribution():
    normalise_response()
    plot = originalDataFrame["Response"].plot(kind="hist")
    plt.show()


# ---------------------------------------------------------------
# For further exploration


def relationship_sensibility_intelligence():
    pass


# ---------------------------------------------------------------


# here we take the user input. and show them a visualisation.
def choose():
    global originalDataFrame
    originalDataFrame = pd.read_excel("AliasedDataForAlgorithm.xlsx", sheet_name="data")
    # this is done since some of the procedures invoke normalising functions.
    print("\n \n")
    global user_input
    print("Greetings, This is the data exploration module. It is intended to be used in the following manner: \n"
          "You will be prompted to enter a selection which will be a number from 0 to 9 inclusive, each of which \n"
          "corresponds to a function inside the .py file. The functions are ordered so locating them should not be \n"
          "a Herculean Labour and it is intended that you follow along the comments inside the function as well. :) \n"
          "Enter -1 to Terminate. \n"
          "NOTE: Please ensure that you are cognisant of the fact that the graphs open in a different window; the "
          "program isn't bottlenecked. \n")
    while user_input != -1:
        print("\n \n---")
        try:
            user_input = int(input("Please enter a selection from the following: \n" +
                                   "0. age_demographic_has_bearing_on_response \n" +
                                   "1. relationship_level_may_have_bearing_on_response \n" +
                                   "2. musical_aptitude_may_have_minor_bearing_on_response \n" +
                                   "3. musical_affinity_may_have_minor_bearing_on_response \n" +
                                   "4. sensibilities_has_minor_bearing_on_response \n" +
                                   "5. intelligence_has_no_bearing_on_response \n" +
                                   "6. sex_may_have_minor_bearing_on_response \n" +
                                   "7. multiple_exposure_may_have_bearing_on_response \n" +
                                   "8. response_distribution \n" +
                                   "9. response_normalised_distribution \n" +
                                   "Selection: "))
            print("---")
        except:
            print("OOPS! Try a valid Integer value from 0-9. Remember: no spaces!")
            continue
        if user_input == 0:
            age_demographic_has_bearing_on_response()
        elif user_input == 1:
            relationship_level_may_have_bearing_on_response()
        elif user_input == 2:
            musical_aptitude_may_have_minor_bearing_on_response()
        elif user_input == 3:
            musical_affinity_may_have_minor_bearing_on_response()
        elif user_input == 4:
            sensibilities_has_minor_bearing_on_response()
        elif user_input == 5:
            intelligence_has_no_bearing_on_response()
        elif user_input == 6:
            sex_may_have_minor_bearing_on_response()
        elif user_input == 7:
            multiple_exposure_may_have_bearing_on_response()
        elif user_input == 8:
            response_distribution()
        elif user_input == 9:
            response_normalised_distribution()
        elif user_input == -1:
            continue
        else:
            print("OOPS! Try a valid Integer value from 0-9. Remember: no spaces!")
    print("Adios! Hopefully this was as illuminating as you are :)")


# ------------------------------------------------------------------

user_input = 777
choose()