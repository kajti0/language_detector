from ViewHelper import ViewHelper
from LangPredict import LangPredict

if __name__ == '__main__':
    # lang = LangPredict()
    # lang.preprocess_data("../polish_raw.txt", "../polish_processed.txt")
    # lang.preprocess_data("../english_raw.txt", "../english_processed.txt", "__label__eng")
    # lang.merge_files("../polish_processed.txt", "../english_processed.txt", "../train_data.txt")
    # lang.train("../train_data.txt", "../model")
    view = ViewHelper()
    view.view()
