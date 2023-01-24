import json

from datetime import datetime

def log_message(message):
    """Print message to the console with the current datetime

    Args:
        message: Message to print to the console
    """

    now = datetime.now()
    dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
    print('[{dt}] {msg}'.format(dt=dt_string, msg=message))

def print_grid_scores(clf, txt_file):
    """Taken from scikit-learn's docs: https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html

    Args:
        clf: Classifier used
        txt_file: Text file where the results should be stored
    """
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print('%0.3f (+/-%0.03f) for %r' % (mean, std * 2, params))
        txt_file.write('%0.3f (+/-%0.03f) for %r\n' % (mean, std * 2, params))

def print_classifier_scores(hp_type, clf, clf_name, runtime=0):
    """Print the best parameter set found and grid scores result for a given classifier

    Args:
        hp_type: Type of hyperparameterization used to identify the file
        clf: Classifier used
        clf_name: Name of the classfier
        runtime: Script runtime
    """

    log_message('Best parameter set found on training set for %s:' % clf_name)
    
    f = open(hp_type + '_parameterization_results.txt', 'a')
    f.write('Best parameter set found on training set for %s: ' % clf_name)
    print(clf.best_params_)
    f.write(json.dumps(clf.best_params_) + '\n')
    
    log_message('Grid scores found on training set for %s:' % clf_name)
    f.write('Grid scores found on training set for %s:\n' % clf_name)
    print_grid_scores(clf, f)
    
    f.write('\n')

    if (runtime != 0):
        f.write('Runtime: %s' % runtime)

    f.close()
    print()

def preprocess_data(x, y):
    """Handle preprocessing tasks such as normalization/standardization 
    and encoding

    Args:
        x: Independent variables
        y: Dependent variables

    Returns:
        x_train: Training portion of the independent variables
        x_test: Testing portion of the independent variables
        x_validation: Validation portion of the independent variables
        y_train: Training portion of the dependent variable
        y_test: Testing portion of the dependent variable
        y_validation: Validation portion of the dependent variable
    """

# def get_1d_ranking_of_features(x_train, y_train)

# def get_2d_ranking_of_features(x_train, y_train)

# def get_feature_correlation(x_train, y_train)

# def get_variance_threshold()