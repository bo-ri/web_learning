import numpy as np

class Perceptron(object):
  def __init__(self, eta=0.01, n_iter=50, random_state=1):
    self.eta = eta
    self.n_iter = n_iter
    self.random_state = random_state
  
  # トレーニングデータに適合させる処理
  def fit(self, X, Y):
    # '''
    #   X : トレーニングデータ
    #       shspe = [サンプルの個数(n_samples), 特徴量の個数(n_features)]
    #   Y : 目的変数
    #       shape = [サンプルの個数(n_samples)]
    # '''
    rgen = np.random.RandomState(self.random_state)
    self.w = rgen.normal(loc+0.0, scale=0.01, size=1+X.shape[1])
    self.errors_ = []

    for _ in range(self.n_iter):  # ここでトレーニング回数分ループ
      errors = 0
      for xi, target in zip(X, Y):  # 各サンプルで重みを更新
        update = self.eta * (target - self.predict(xi))
        self.w_[1:] += update * xi
        self.w_[0] += update
        errors += int(update != 0.0)
      self.errors_.append(errors)
    return self
  
  def net_input(self, X):
    return np.dot(X, self.w_[1:]) + self.w_[0]
  
  def predict(self, X):
    return np.where(self.net_input(X) >= 0.0, 1, -1)

