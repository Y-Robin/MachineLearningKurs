"""Einfacher Transformer für Notebook 02b."""
from sklearn.base import BaseEstimator, TransformerMixin


class FlaechenMerkmale(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        # Die feste Rechenregel muss nichts aus Trainingsdaten lernen.
        return self

    def transform(self, X):
        # Kopieren, damit die ursprünglichen Daten unverändert bleiben.
        erweitert = X.copy()
        erweitert["kelch_flaeche"] = X["sepal length (cm)"] * X["sepal width (cm)"]
        erweitert["blueten_flaeche"] = X["petal length (cm)"] * X["petal width (cm)"]
        return erweitert
