from django import forms
from .models import *

class pareForm(forms.ModelForm):
    class Meta:
        model=pare
        fields=['グラフタイトル入力','要素名入力は要素ごとに空白を入れてください','要素数値入力は要素ごとに空白を入れてください','x軸ラベル入力','y軸ラベル入力']


class paretozuForm(forms.ModelForm):
    class Meta:
        model=paretozu
        fields=['グラフタイトル','グラフ要素_空白くぎりで記入してください','グラフ要素の数値_空白区切りで記入してください','横軸の名称','縦軸の名称']



class oresenForm(forms.ModelForm):
    class Meta:
        model=oresen
        fields=['グラフタイトル','グラフ要素_空白くぎりで記入してください','グラフ要素の数値_空白区切りで記入してください','横軸の名称','縦軸の名称']

class oresenzuForm(forms.ModelForm):
    class Meta:
        model=oresenzu
        fields=['グラフタイトル','グラフの凡例','数字を入力してください_4月','数字を入力してください_5月','数字を入力してください_6月','数字を入力してください_7月','数字を入力してください_8月','数字を入力してください_9月','数字を入力してください_10月','数字を入力してください_11月','数字を入力してください_12月','数字を入力してください_1月','数字を入力してください_2月','数字を入力してください_3月','横軸の名称','縦軸の名称']


class bougurahuForm(forms.ModelForm):
    class Meta:
        model=bougurahu
        fields=['グラフタイトル','グラフ要素_空白くぎりで記入してください','グラフ要素の数値_空白区切りで記入してください','横軸の名称','縦軸の名称']

class engurahuForm(forms.ModelForm):
    class Meta:
        model=engurahu
        fields=['グラフタイトル','グラフ要素_空白くぎりで記入してください','グラフ要素の数値_空白区切りで記入してください']