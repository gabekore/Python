#! /usr/bin/env python3


# 抽象クラス
from abc import ABCMeta, abstractmethod


class JTCode(metaclass=ABCMeta):
  
  def run(self):
    return self

  @abstractmethod
  def add(self, code):
    raise ("このオブジェクトに演算子'+'は使えません。")

  @abstractmethod
  def sub(self, code):
    raise ("このオブジェクトに演算子'-'は使えません。")

  @abstractmethod
  def multiply(self, code):
    raise ("このオブジェクトに演算子'*'は使えません。")

  @abstractmethod
  def devid(self, code):
    raise ("このオブジェクトに演算子'/'は使えません。")

