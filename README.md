 GraphGuard
A deep dive into the intricacies of review networks using various algorithms and methods to understand and predict user behaviors.

Description
This project aims to analyze review networks and predict user behavior based on historical data. It delves deep into the structure and behavior patterns within review networks. The project uses the REV2 algorithm for fairness and goodness calculation, applies Machine Learning techniques like Random Forest for predictions, and evaluates the results using precision, recall, and other metrics.
Clone the repository:
git clone [https://github.com/JAANVI999/GraphGuard]
Running REV2 Algorithm:
sh run-rev2-all-params.sh
Evaluating the Results:
Use the ei_2.py and ec_2.py scripts for evaluation purposes. These scripts compute precision, recall, and other metrics based on the results of the REV2 algorithm.

Supervised Learning with Random Forest:
Run the supervised_2.py script to use the Random Forest classifier on the data. This script uses the features extracted from the review network and predicts user behaviors.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
