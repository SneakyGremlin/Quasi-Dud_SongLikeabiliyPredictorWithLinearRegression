# Linear Regression to predict Song Viability

This project purports to use a fundamental Linear Regression Algorithm and certain attributes to predict how much an instance (in this case a person)
would like a song of a particular genre of a specific artist (or simply: a song)

Several attributes are used to determine which of them, if any, are correlational with liking the song. 

"Song of a specific genre of a specific artist" is a caveat here. The results here cannot and should be generalised to other music the artist attempts (though I would wager that there would be a positive correlation).
The features used should illustrate why. 

I could not classify the song based on pre-existing genres (except indie/alternate) so I coin the term "Emotionally-Charged-Operatic-Arias": Operatic and Arias since the primary focus is not on the background/complementary music but rather on the vocals of the singer themself.

> Relationship Level can be translated to Sentiment (on the artist); I use "Relationship Level" since the artist is me.

> **I reiterate the song was sung by me**

---

## RoadMap of Project 
There exist three .py files:
1. exploration.py
2. preparation.py
3. main.py

### exploration.py
This comprehensively explores the dataset contained within "AliasedDataForAlgorithm.xlsx". Graphs and aggregates are used 
and justifications are provided. 

There is a rudimentary interface that appears if the file is run. The pre-amble of the interface mentions this, but it is 
intended that the user follows along the method invocation along with the method code and comments. It would be much more 
illuminating for the user.

The purport of the file was to discern which features were of importance and their degrees of importance.

### preparation.py
This file contains a method(s) that normalises the dataset and performs stratified sampling based on age. 

### main.py
This file contains the actual models that were built using the inferences from exploration.py and the methods from preparation.py


## Notes on Data Collection apropos of Ethics: Confidentiality and Consent.

**The data set utilised by the algorithm dissembles the participant's names by simply referring to them as participants i.e. "Participant 1" etc.**

**Consent was provided by all participants. Debriefing was rejected by almost all but when asked for, was provided.**

All data collected is data that is 
1. Publicly available (and consensually used). 
2. Inferrable (barring Gender identification which has been confirmed): these include `Musical Affinity, Sensibilities, Intelligence, Relationship Level` and the dependent class variable, `Liked the song`. (Inferential process was such that it minimised my error (see Arguments section)).
3. Consensually provided by the participant.

> Here I think it is wise to mention the file contained in this package is aliased, there is a different "original" file which
> included much more information that I decided to redact. 

---

## Data Collection Methodology: Exposition, Arguments, and a Justification TODO

### Exposition
All participants are individuals I have had at least 2 hours of interactions with (this is an outlier lower bound, the actual bound is 10 hours on average). 
In essence the following approach was utilised: either the individual was sent a link to the song on *SoundCloud* , or they were sent a recording of the song on either *WhatsApp* or *Gmail* (I do believe the dependent variable would be NOT contingent on this). All communication apropos of the concerned was digital. 
They were advised to provide "feedback": this ambiguous locution was intentionally used since, in my experience, humans are bad at "rating" things in general AND it is also the case that a given ten-point scale would be interpreted differently by different people (e.g. an individual may adore a song and yet give it an 8 since he believes a 10 is perfection and ergo unattainable: in essence, the interpretation of the scale itself is inherently idiosyncratic; this is to mitigate against that). It was from their responses (that varied in verbosity) I made 
the inference for the dependent response variable: `Liked the Song`. (see "Arguments" section below for potential Perverse Incentive effect). 
The primary features of the text feedback I used were volubility (i.e. how much they said: were they taciturn or gushing and semantics (this is inferential in general and touches on the field of linguistics: I do think decades of interacting with people has afforded me the moderate ability to suss out what they *mean* (see "Arguments")).
I then, with intervals of three days each time (for a total of 3 times), and taking the average, translated that into a bounded numerical value:
The scale goes from 1 to 5:
1. 1 It was good but nothing special, non-constructive nitpicking. 
2. 2 Decently impressive, nitpicking but constructive.
3. 3 Impressed but flaws/improvements were indicated. 
4. 4 Infatuated but only one or two "preferences" were indicated
5. 5 Gobsmacked (could be taciturn (this part is a bit iffy in all honesty, maybe they just wish to terminate the interaction?: no way to account for this except gut feeling and three-day method) or gushing).

The interval method was also used for other inferential characteristics (viz. `Musical Affinity, Sensibilities, Intelligence, Relationship Level`)

The participants were aware I was the singer.

The data file is included in the repository, as well. The "exploration.py" file allows you to explore the data visually and numerically.

### Arguments 

These are all the "quibbles" I could think of. 

#### Limits of Inference
I didn't have a choice (well I did: I just liked this one better (other choices being not embarking on this ~~goose chase~~ illuminating endeavour)).

Abductive thinking is useful: I mean we're 8 billion strong; I'm betting inferences played a part. But the rub is that inferences
can be *wildly* wrong: I mitigate against this by enumerating the values multiple times. Even so an error bound remains but given the scales I'm using 
this is likely within acceptable ranges, so I think it is pardonable. 

p.s. this is a rather ludicrous argument but if I am off by 1, 100 percent of time, and have no biases towards over or under-rating, and have a large enough data set, then doesn't everything balance out? :) (this is a joke).

#### People may be influenced by a semi-hawthorne effect.
Preamble: Hawthorne effect refers to the relationship between an individual's behaviour and being observed. I'm tryna sound fancy, people alter their responses when talking *directly* with a person (and this differs even in text and in person). 

Seeing that I was conversing with the individuals I was gleaning data from, they may have been prone to be either more harsh or more lenient in their feedback.
Hopefully, both of these balanced each other out.

> The solution, of course, involved surveys (like the Likert Scale which would have greatly decreased my reliance on inference), however, I do justify my lack of the usage thereof (see "Justification").

#### Perverse Incentive
I expound on the inscrutability and variability of human responses above and justify inference for the dependent variable but it could be the case 
my OWN scale is flawed! What if (the scale goes from 1-5) my scale is logarithmic to the base 1.2? If this is the case then I do not believe it should be 
a problem since the entire model would implicitly take that into account and the results would be interpretable by me and explainable to those who deign to concern themselves herewith.

For variability my argument would really be a regurgitation of "Limits of inference above" (specifically the part pertaining to multiple reckonings of values).

#### independent variables not independent of each other
Well of course this could be an issue! `Sensibility` and `Age Demographic` could be correlated. 

I take this into account (consider how I.Q. tests take into account ages before administration of the test; my method is something along those lines).

But in all honesty, I conjecture the final model won't have to worry about these correlations, confounding variables and the like since I am certain a lot of properties have little bearing (with some caveats of course: I didn't subject an infant to music; how would that even work?).

#### Am I a Narcissist for using my own song? 
No, I merely have modest belief in my skills to be mellifluous. And I also didn't have a choice here, did I? Had I used an *actual* artist's song 
would I have a way of knowing their sentiments thereon (at all/accurately)? At least this way I can factor in biases against me (using inferences of course...).

### Justification 
I'm 21 years of age: who was gonna actually gimme "good data"? (this is a joke of course: the data collection process was immensely arduous, demeaning, painstaking, and painful).

I didn't use surveys because that would have GREATLY diminished my data set (one could argue here that maybe their responses were taking into account my feelings: to this I say please hear the song yourself; there were no "reasons" to render me "upset" apart from the particpant being a spoilsport).

*I write this portion after being done with the project. Should have used surveys. I have no way of knowing if it is the case that the data 
itself is flawed, or there is no linear relation but at least I could have been sure*


### Something I wanna say 
It took me a total of three weeks collecting, collating, organising, and reviewing the data. This is three weeks wherein an average of 
2 hours was spent each day (remember the variables were devised by me as well). I was meticulous with the scores, the deciphering
of responses, the revising, the reckonings and justifications of intelligence scores and what-not. 

It was demeaning, it just ineffably was, and I was emotionally exhausted by the end of it. Next time I'm sticking to data 
already available (well I say this right now but who knows...)


**The following is not intended to offend anyone, I based them on interactions I had and included them for your amusement. I do this because some of the feedback I got was VERY amusing.**
1. How important can ANYONE in my circle be that they can't spare ten minutes of their time for a **pleasant** task.
2. Well I understand you're very busy, but maybe you can do me this small favour since I literally did our entire BIOL course project person xxx.
3. Why does almost every girl think I'm trying to make advances? SHEESH. I know I ain't no Prince Charming but you don't gotta be Cruella. 
4. Oh, I see good sir, thank you very much for informing me how falsettos are supposed to sound; I hadn't learned in the two years I've spent singing them on two octaves. 
5. Wait a second, you won't do me this favour cuz you have put on some muscle, did ya swap your brain matter for it?
6. No no no, this ain't a social call John Doe, I'm still upset for that stink, but do this and we might just be back on speaking terms.
7. "The singer is not singing on his scale": the singer can hit the same notes an octave higher!
8. "There are voice cracks and the voice vibrates": THAT IS A SKILL IT TOOK ME MONTHS TO REFINE. 
9. (this one's a bit esoteric) "This doesn't qualify as Hindi-inspired since there are no Raagas": O musician extraordinaire do you not know that given that there were 200 thaats initally and a gazillion ragas can be made from just one, ALL MUSIC can be said to have flavours of hindi music (this is a qualified statement).
10. Fine read-zone me, I never liked you anyway (as I cry internally).
11. I mean you said you'll do it, so why do I gotta ask you for the tenth time: your hippocampus dislocated? (this person is a close friend, I think you can badger your close friends) 

I've now said it. Thank you Universe :).

---

## Notes on Data Attributes/Features 

> For arguments on inference see above section.


> IMPORTANT: in the dataset, a particular record may have values not enumerated herein. These values are the product of
> the application of division by 2 and my vacillation.

#### \>Participant 
Very simple aliasing for the participants; they are referred to as "1", "2" etc. Confidential (original) data file 
is... somewhere (privacy of participants **will** and **has** been safeguarded).

#### \> Age Demographic
I use the ubiquitous terms (and their meanings' excerpted from Wikipedia... (Only because GREAT pedantry here isn't required of course)):
1. GenX (1965-80): 44 - 59
2. Millennials / GenY (1981-96) 28 - 43 
3. Zoomers / GenZ (1997-2012) 12 - 27
Age is calculated considering this is 2023 and including the birth year e.g. someone born in 2022 would be 2 years old (A minor leeway of 1 was granted at my discretion only because I suspect it shouldn't matter).
> In the `DataFrame` GenX/Y/Z will be used.


#### \> Relationship Level (inference)
Is a bounded attribute: [0, 6] (positivity)

(for the positive numbers goo relations are implied)
1. 0 means active hostility (needless to say very hard to acquire; such a point may not even exist!)
2. 1 means major distaste (avoids conversations, but doesn't snub)
3. 2 means minor distaste (makes small talk but otherwise holds me in little to no regard)
4. 3 means no interactions and neutral (a literal random person whom I've never interacted with (or once/twice) and who *should* harbour neutrality for me).
5. 4 means friendly acquaintance (<5 hours of conversations / could potentially take friendship further)
6. 5 means chummy/close (~10 to <30 hours of interaction; personal details divulged; can make requests)
7. 6 means "best friend" (needless to say this will be very sparse)

n.b. Reflects how I *think* they feel about me (not how I feel about them).
n.b.b. The time period suggests positive interactions; I could have spent days with an individual who is actively hostile towards me (hence the obliques).

#### \> Musical Aptitude 
Bounded (qualifiedly: values that are means are allowed (ref caveat above)) discrete attribute: [0, 3]:
1. 0 means no knowledge about music whatsoever (i.e. the theory behind it)
2. 0.5 is a default value when data is insufficient; justification is hopefully "overlooked" savants are balanced out (pseudo-justification). TODO !!! Replace this value with a 0 
3. 1 means basic knowledge; dilettante guitarists/vocalists etc
4. 2 means sufficient knowledge/skill to be considered good by the uninitiated.
5. 3 means mastery. 

#### \> Musical Affinity (inference)
Bounded (same) discrete attribute: [1, 3]:
1. 1 means little to no interest in music and no active interest in seeking out new songs to hear OR actively (i.e. puts a song on) listens to music <2 hours a week (for the sake of music not as backing tracks for video games etc).
2. 1.5 is a default value when data is insufficient
3. 2 means has interest; may have a favourite artist; would go to a concert; has curated playlists.
4. 3 means devotee: has favourite artists/songs; actively follows artists tours; would purchase and is vocal about support for certain artists.

**No subjects had an aversion for music**

#### \> Sensibilities (inference) 
Refers to a person's ineffable ability to "appreciate" creation. This is enigmatic, I concede.
Bounded (same) discrete attribute: [1, 3]:
1. Little to no interest in the arts / aversive to philosophical discussions, books, arts: borders on philistinism 
2. 1.5 is when I vacillate b/w 1 and 2. Default Value.
3. Shows capacity for reflection on the arts: can be prompted to articulate sapient impressions on "art"
4. Has a distinct weltanschauung; immensely reflective and can be prompted to offer various idiosyncratic and "original" insights on art. <br/>
`4. This is kept separate since no such person I have interacted with hitherto: enlightened. I cannot confirm i such people even exist.`

> Please note that one may like music and have nigh-on no sensibilities: consider an individual who loves disco music but has no propensity for the arts.
> Also note that this property may make me sound pretentious: that is not lost on me. A person who does not desire the arts is not anathema: people hate science (math) whilst being consummate authors/artists too!


#### \> Intelligence (inference) 
Bounded (same) discrete value: [0, 5]
Devised my own scale (pardon the presumptuousness) owing to the controversy surrounding much more orthodox measures (Intelligence Quotient etc.) 
but mainly since there was a snowball's chance in Venus I was getting the participant's IQ scores.

> Since I have devised my own scale it should be made clear this score could not correlate strongly with orthodox measures
> such as IQ etc. (though if they do then we have another penicillin here)

> CAVEAT apropos of Intelligence : The coupling of intelligence and my inferential skills definitely may not reflect the actual intellectual capacities/ or capacities in general  of the participants.
> "Intelligence" in of itself is a heavily convoluted emergenet feature that is manifold: sensibilities, intuitions, implicit memory, spatial and temporal recognition etc. 
> I do not have the **authority** to adjudicate and masquerade as an authority. 

How I devised is simply on the basis of grades (when you interact with individuals for some time GPA inevitably comes up...), Emotional Intelligence (which is quite manifest if one observes), in cases where the participant is an adult, occupation and affluence (at times this is known, others not so much but margin of miscategorisation is very low here) , implicit skills (e.g. skills the the body knows i.e. implicit memory), and interactions in general.
It was a simple aggregate (and I believe a comprehensive overview of points granted is a bit redundant): 
1. Grades/occupation: 1.75 (justification: with all due lack of acerbity grades determine nigh on everything pre-actual-adult life; no comment on grades actually being a measure of intelligence/ for adults their occupation is sufficient though this is a bit iffy: librarians may be looked down upon but may be immensely intelligent)
2. Emotional Intelligence; ability to deal with people; charisma; savoir faire: 1.75
3. Manifested intelligence (this is the knowledge that refers to implicit memory e.g. a master seamstress): 0.5
4. Interactions (consider this cookie points; this is inferential after all ): 1.

> I had intended that a score of 2.5 corresponds to the average IQ (100). The scale unfortunately may become slightly logarithmic (this is propensity of mine and is unintentional) 
> The score defaults to 2,3 or 2.5 on account of the fact all the individuals I'm interacting with are either university students or have sufficient skill to maintain an occupation. This is contingent on information I have on them e.g. it is unlikely someone with musical aptitude is not "intelligent".


#### \> Sex
Unfortunately the individuals I used for this project were "boolean" in nature. So `Sex` is either "Male" or "Female"

#### \> Multiple Exposure
This is a boolean metric: either the participant has been exposed to more music by me or has not (arguably should be a scale but I'm a burgeoning artist: how much exposure could they have had?)

This serves to mitigate against the "exploration" part of music: when you're trying a new genre or an artist you tend have butterflies or excitement.

#### \> (How much they) Liked the song (Dependent Response Variable)
This is a measure of how much they liked the song. The scale used is copied here from the "Exposition" section for convenience: 
1. 1 It was good but nothing special, non-constructive nitpicking. 
2. 2 Decently impressive, nitpicking but constructive.
3. 3 Impressed but flaws/improvements were indicated. 
4. 4 Infatuated but only one or two "preferences" were indicated
5. 4.5 when I vacillate b/w 4 and 5.
6. 5 Gobsmacked (could be taciturn (this part is a bit iffy in all honesty, maybe they just wish to terminate the interaction?: no way to account for this except gut feeling and three-day method) or gushing).

**No participant was absolutely repulsed by the song**. (This may appear narcissistic, so for your own reference I provide a reference to the song used TODO).

**It bears mentioning that though the values in my training and testing dataset are "discrete", regression does not provide discrete outputs. Hence, response instead of class is used.**

> I discuss the problem of class imbalance and outliers below in "Flaws". TODO 

---

## Exposition on Data Exploration TODO

when both mean and median are >=0.5 has bearing 
when one is, may have bearing 
when both >0.1 <5 has minor
when >0.1 <5 even one may have minor 
when both <0.1 none

---

## Exposition on Data Preparation TODO

---

## Exposition on Modelling TODO

---

## Why linear Regression? 
Is not a classification problem; is a regression problem, so it seems fit to use a Regressive model.

Why I chose to use *Linear Regression* specifically, is simple: its the only algorithm I felt conversant in. To this end I 
even based the properties in such a manner so as to have a linear relationship between the feature and the response, even if 
that may not have existed. 


> Reduction of the data attributes:
> It may have been implicit already, but now I make it explicit:
> It had always been my intention to prune (feature selection) certain properties/characteristics of the records. Why I did not do this initially is because
I wished to confirm it via data exploration. The criteria and my method for this is outlined in "Exposition on Data Exploration". 
> The reason for this is simple: the lesser the number of coefficients the better the model i.e. the curse of dimensionality (given that the other coefficients have little to no effect on the response, of course). 

---

## Possible hypotheses/epiphanies to explore 

1. Link between volubility and Intelligence.
2. Direct correlation b/w past exposure to artist/music of artist/genre and JUST genre
3. Sensibility and emotional receptivity with age. 
4. Music is a highly idiosyncratic. Preferences abound but maybe take preferences into account?
5. Correlation b/w my scale of Intelligence and Sensibilities. 

TODO:::: AT THE END OF ALL OF THIS MAKE A LIST OF ALL THE FEEDBACKS RECEIVED AND WORK ON THEM. 



---
 
## Flaws 

1. Class Imbalance (perhaps age has no correlation) Got no rizz :(<br/>
   \> The collation of certain demographics was at my discretion.
2. Data Collection Methodology has a (arguably acceptable margin of error).
3. Should re-run simulations with the same data set by 
   1. !!! removing redundant variables
   2. Using a different machine learning algorithm

class imbalance. resolution thereof and had to drop one entire variabel 
data definition. 

---

## What next
logitic regression 
better data 
unsupervised model

---

## Footnote 
Imagine you're on an island...

---

## Coming Clean :)
genre specialiation, attractiveness, 

Introduction of a new variable: aplomb/attractiveness.

I ain't done python in a long time so no syntactic sugar.

To show prediction of an artist's success is an impossible endevaour 
Time for reflection with everyone and pruning people from my life 

If I stand an actual chance.

It was also to see if what I feel about other people is constant and the effect of ...
So I could truly appreciate the efforts of data collectors and attempt to begin to understand linear regression,




---


!!!!!!!!!!!!!!!!!!!! TODO: is normalisation REQUIRED here? what do the values of the coefficients mean?

!!!!!! Bananas
!!!!!! Normalisation? 

!!! take money from baba 
savoir faire 
au courant 
sensibilities
liberal use of 
onliging.
seamless
refine
chorus 

medley of !!!

TODO: provide an overview of the excel file layout; both of them 



# music 
>>>> sometimes the high pitches when held they crack

god given talen 
