from django.db import models

# Create your models here.
class pare(models.Model):
    グラフタイトル入力=models.CharField(max_length=1000,blank=True)
    要素名入力は要素ごとに空白を入れてください=models.CharField(max_length=1000,blank=True)
    要素数値入力は要素ごとに空白を入れてください=models.CharField(max_length=1000,blank=None)
    x軸ラベル入力=models.CharField(max_length=1000,blank=True)
    y軸ラベル入力=models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return str(self.id)

class paretozu(models.Model):
    グラフ名=models.CharField(max_length=1000,blank=True)
    グラフタイトル=models.CharField(max_length=1000,blank=True)
    グラフ要素_空白くぎりで記入してください=models.TextField(max_length=1000,blank=True)
    グラフ要素の数値_空白区切りで記入してください=models.TextField(max_length=1000,blank=True)
    横軸の名称=models.CharField(max_length=1000,blank=True)
    縦軸の名称=models.CharField(max_length=1000,blank=True)

class oresen(models.Model):
    グラフ名=models.CharField(max_length=1000,blank=True)
    グラフタイトル=models.CharField(max_length=1000,blank=True)
    グラフ要素_空白くぎりで記入してください=models.TextField(max_length=1000,blank=True)
    グラフ要素の数値_空白区切りで記入してください=models.TextField(max_length=1000,blank=True)
    横軸の名称=models.CharField(max_length=1000,blank=True)
    縦軸の名称=models.CharField(max_length=1000,blank=True)

class oresenzu(models.Model):
    グラフ名=models.CharField(max_length=1000,blank=True)
    グラフタイトル=models.CharField(max_length=1000,blank=True)
    グラフの凡例=models.CharField(max_length=1000,blank=True)
    数字を入力してください_4月=models.IntegerField(default=0)
    数字を入力してください_5月=models.IntegerField(default=0)
    数字を入力してください_6月=models.IntegerField(default=0)
    数字を入力してください_7月=models.IntegerField(default=0)
    数字を入力してください_8月=models.IntegerField(default=0)
    数字を入力してください_9月=models.IntegerField(default=0)
    数字を入力してください_10月=models.IntegerField(default=0)
    数字を入力してください_11月=models.IntegerField(default=0)
    数字を入力してください_12月=models.IntegerField(default=0)
    数字を入力してください_1月=models.IntegerField(default=0)
    数字を入力してください_2月=models.IntegerField(default=0)
    数字を入力してください_3月=models.IntegerField(default=0)
    横軸の名称=models.CharField(max_length=1000,blank=True)
    縦軸の名称=models.CharField(max_length=1000,blank=True)

class bougurahu(models.Model):
    グラフ名=models.CharField(max_length=1000,blank=True)
    グラフタイトル=models.CharField(max_length=1000,blank=True)
    グラフ要素_空白くぎりで記入してください=models.TextField(max_length=1000,blank=True)
    グラフ要素の数値_空白区切りで記入してください=models.TextField(max_length=1000,blank=True)
    横軸の名称=models.CharField(max_length=1000,blank=True)
    縦軸の名称=models.CharField(max_length=1000,blank=True)

class engurahu(models.Model):
    グラフ名=models.CharField(max_length=1000,blank=True)
    グラフタイトル=models.CharField(max_length=1000,blank=True)
    グラフ要素_空白くぎりで記入してください=models.TextField(max_length=1000,blank=True)
    グラフ要素の数値_空白区切りで記入してください=models.TextField(max_length=1000,blank=True)