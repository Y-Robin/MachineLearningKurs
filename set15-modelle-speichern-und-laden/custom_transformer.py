"""Eigener Transformer muss beim Laden unter diesem Modulnamen verfügbar sein."""
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted

class FlaechenMerkmale(TransformerMixin,BaseEstimator):
    def fit(self,X,y=None):
        self.feature_names_in_=X.columns.to_numpy()
        self.n_features_in_=X.shape[1]
        return self
    def transform(self,X):
        check_is_fitted(self,'feature_names_in_')
        if list(X.columns)!=list(self.feature_names_in_):
            raise ValueError('Feature-Reihenfolge stimmt nicht.')
        result=X.copy()
        result['kelch_flaeche']=X['sepal length (cm)']*X['sepal width (cm)']
        result['blueten_flaeche']=X['petal length (cm)']*X['petal width (cm)']
        return result
