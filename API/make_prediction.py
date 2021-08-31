import pickle
import pandas as pd



class Predictor:
    with open('../saved_models/lr2.pckl', 'rb') as fp:
      model = pickle.load(fp)

    labels = pd.read_csv('../data/lang_codes.txt', encoding='utf-8', sep='	',
                     names=['iso1', 'iso2', 'English', 'French', 'German'])

    def get_pred_label(self, pred):
        """
        :param pred:
        Take models prediction as input
        :return:
        Return English name of language
        """
        if pred[0] in Predictor.labels.iso1.to_list():
            x = Predictor.labels.English.where(Predictor.labels.iso1 == pred[0]).dropna().tolist()
            return x[0]
        elif pred[0] in Predictor.labels.iso2.to_list():
            x = Predictor.labels.English.where(Predictor.labels.iso2 == pred[0]).dropna().tolist()
            return x[0]
        else:
            return pred[0]

    def make_prediction(self, text):
        if type(text) is str:
            text_input = [text]
        elif type(text) is list:
            text_input = text

        pred = Predictor.model.predict(text_input)
        pred = self.get_pred_label(pred)
        return pred
