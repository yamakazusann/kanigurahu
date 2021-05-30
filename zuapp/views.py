from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
from .models import *
from django.shortcuts import redirect
import matplotlib
import pandas as pd
matplotlib.use('Agg')
import japanize_matplotlib
import matplotlib.pyplot as plt
import io
import seaborn as sns
sns.set(font='IPAexGothic')
import numpy as np
from matplotlib.pyplot import figure
import matplotlib.cm as cm
from django.contrib.auth.decorators import login_required

@login_required
def zentai(request):
    params={
        'title':'簡単グラフ作成',
    }

            
    return render(request,'zuapp/zentai.html',params)







@login_required
def paretozu_index(request):
    data=paretozu.objects.all()
    params={
        'title':'パレート図簡単作成',
        'message':'グラフパラメーターを入力してグラフを作成を押してください',
        'data':data,
    }
    
    return render(request,'zuapp/paretozu_index.html',params)

@login_required
def paretozu_edit(request,num):
    obj=paretozu.objects.get(id=num)
    if(request.method=='POST'):
        kaku=paretozuForm(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/gurahu/paretozu_index')
    params={
        'title':'パレート図パラメーター',
        'id':num,
        'form':paretozuForm(instance=obj),
    }
    return render(request,'zuapp/paretozu_edit.html',params)

@login_required
def oresen_index(request):
    data=oresenzu.objects.all()
    params={
        'title':'折れ線グラフ簡単作成',
        'message':'グラフパラメーターを入力してグラフを作成を押してください',
        'data':data,
    }
    
    return render(request,'zuapp/oresen_index.html',params)

@login_required
def oresen_edit(request,num):
    obj=oresenzu.objects.get(id=num)
    if(request.method=='POST'):
        kaku=oresenzuForm(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/gurahu/oresen_index')
    params={
        'title':'折れ線グラフパラメーター',
        'id':num,
        'form':oresenzuForm(instance=obj),
    }
    return render(request,'zuapp/oresen_edit.html',params)

@login_required
def bougurahu_index(request):
    data=bougurahu.objects.all()
    params={
        'title':'棒グラフ簡単作成',
        'message':'グラフパラメーターを入力してグラフを作成を押してください',
        'data':data,
    }
    
    return render(request,'zuapp/bougurahu_index.html',params)

@login_required
def bougurahu_edit(request,num):
    obj=bougurahu.objects.get(id=num)
    if(request.method=='POST'):
        kaku=bougurahuForm(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/gurahu/bougurahu_index')
    params={
        'title':'棒グラフパラメーター',
        'id':num,
        'form':bougurahuForm(instance=obj),
    }
    return render(request,'zuapp/bougurahu_edit.html',params)

@login_required
def engurahu_index(request):
    data=engurahu.objects.all()
    params={
        'title':'円グラフ簡単作成',
        'message':'グラフパラメーターを入力して作成を押してください',
        'data':data,
    }
    
    return render(request,'zuapp/engurahu_index.html',params)

@login_required
def engurahu_edit(request,num):
    obj=engurahu.objects.get(id=num)
    if(request.method=='POST'):
        kaku=engurahuForm(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/gurahu/engurahu_index')
    params={
        'title':'円グラフパラメーター',
        'id':num,
        'form':engurahuForm(instance=obj),
    }
    return render(request,'zuapp/engurahu_edit.html',params)






















def setplt_z():



    data=paretozu.objects.all().values('グラフタイトル','グラフ要素_空白くぎりで記入してください','グラフ要素の数値_空白区切りで記入してください','横軸の名称','縦軸の名称')
    data_1=data[0]
    d1=data_1['グラフタイトル']
    d2=data_1['グラフ要素_空白くぎりで記入してください']
    d3=data_1['グラフ要素の数値_空白区切りで記入してください']
    d4=data_1['横軸の名称']
    d5=data_1['縦軸の名称']

    d2=d2.split()
    d3=d3.split()
    d3=list(map(str.lower,d3))
    d3=list(map(int,d3))






    labels=d2
    values=d3
    x=(d4)
    y=(d5)
    title=(d1)




    df=pd.DataFrame({'label':labels,'value':values},columns=['label','value'])
    df=df.sort_values(by='value',ascending=False)
    df['accum']=np.cumsum(df['value'])
    df['accum_percent']=df['accum']/sum(df['value'])*100
    
    
    
    fig=plt.figure()
    ax=fig.add_subplot(111)
    
    data_num=len(df)
    fig,ax=plt.subplots(figsize=(16,9))
    ax.bar(range(data_num),df['value'])
    ax.set_xticks(range(data_num))
    ax.set_xticklabels(df['label'].tolist())
    ax.set_xlabel(x,fontsize=23)
    ax.set_ylabel(y,fontsize=23)
    ax_add = ax.twinx()
    ax_add.plot(range(data_num),df['accum_percent'],c='r',marker='o')
    ax_add.set_ylim([0,120])
    ax_add.set_ylabel('(累積比率)')
    
    plt.title(title,fontsize=50)
    
    
    

def plt2svg_z():
    buf=io.BytesIO()
    plt.savefig(buf,format='png',dpi=200)
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_z(request):
    setplt_z()
    svg=plt2svg_z()
    plt.cla()
    response=HttpResponse(svg,content_type='image/png')
    return response


def setplt_o():
#年グラフにする
    data=oresenzu.objects.all().values('グラフタイトル','グラフの凡例','数字を入力してください_4月','数字を入力してください_5月','数字を入力してください_6月','数字を入力してください_7月','数字を入力してください_8月','数字を入力してください_9月','数字を入力してください_10月','数字を入力してください_11月','数字を入力してください_12月','数字を入力してください_1月','数字を入力してください_2月','数字を入力してください_3月','横軸の名称','縦軸の名称')
    data_1=data[0]
    d1=data_1['グラフタイトル']
    d4=data_1['横軸の名称']
    d5=data_1['縦軸の名称']
    a_1=data_1['数字を入力してください_4月']
    a_2=data_1['数字を入力してください_5月']
    a_3=data_1['数字を入力してください_6月']
    a_4=data_1['数字を入力してください_7月']
    a_5=data_1['数字を入力してください_8月']
    a_6=data_1['数字を入力してください_9月']
    a_7=data_1['数字を入力してください_10月']
    a_8=data_1['数字を入力してください_11月']
    a_9=data_1['数字を入力してください_12月']
    a_10=data_1['数字を入力してください_1月']
    a_11=data_1['数字を入力してください_2月']
    a_12=data_1['数字を入力してください_3月']

    
    

    aa='4月'
    bb='5月'
    cc='6月'
    dd='7月'
    ee='8月'
    ff='9月'
    gg='10月'
    hh='11月'
    ii='12月'
    jj='1月'
    kk='2月'
    ll='3月'

    a_a=data_1['グラフの凡例']

    

    columns=[a_a]
    index=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll]
    df_a=pd.DataFrame([a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9,a_10,a_11,a_12],index=index,columns=columns)
    figure(num=None, figsize=(16, 9))
    plt.title(d1,fontsize=30)
    plt.xlabel(d4,fontsize=25)
    plt.ylabel(d5,fontsize=25)
    plt.plot(list(df_a.index),df_a[a_a],marker='o',label=a_a)
    plt.legend()




def plt2svg_o():
    buf=io.BytesIO()
    plt.savefig(buf,format='png',dpi=200)
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_o(request):
    setplt_o()
    svg=plt2svg_o()
    plt.cla()
    response=HttpResponse(svg,content_type='image/png')
    return response




def setplt_b():

    data=bougurahu.objects.all().values('グラフタイトル','グラフ要素_空白くぎりで記入してください','グラフ要素の数値_空白区切りで記入してください','横軸の名称','縦軸の名称')
    data_1=data[0]
    d1=data_1['グラフタイトル']
    d2=data_1['グラフ要素_空白くぎりで記入してください']
    d3=data_1['グラフ要素の数値_空白区切りで記入してください']
    d4=data_1['横軸の名称']
    d5=data_1['縦軸の名称']




    d2=d2.split()
    d3=d3.split()
    d3=list(map(str.lower,d3))
    d3=list(map(int,d3))






    labels=d2
    values=d3
    x_l=(d4)
    y_l=(d5)
    title=(d1)

    x_n=labels
    y_n=values
   

    
    

    x = np.array(x_n)
    y = np.array(y_n)
   
   
    x_position = np.arange(len(x))
    fig = plt.figure()
    fig,ax=plt.subplots(figsize=(16,9))
    
    ax.bar(x_position, y, tick_label=x)
    
    plt.title(title,fontsize=50)
    plt.xlabel(x_l,fontsize=23)
    plt.ylabel(y_l,fontsize=23)
    fig.show()


def plt2svg_b():
    buf=io.BytesIO()
    plt.savefig(buf,format='png',dpi=200)
    s=buf.getvalue()
    buf.close()
    return s


@login_required
def get_svg_b(request):
    setplt_b()
    svg=plt2svg_b()
    plt.cla()
    response=HttpResponse(svg,content_type='image/png')
    return response



def setplt_e():


    data=engurahu.objects.all().values('グラフタイトル','グラフ要素_空白くぎりで記入してください','グラフ要素の数値_空白区切りで記入してください')
    data_1=data[0]
    d1=data_1['グラフタイトル']
    d2=data_1['グラフ要素_空白くぎりで記入してください']
    d3=data_1['グラフ要素の数値_空白区切りで記入してください']
    



    d2=d2.split()
    d3=d3.split()
    d3=list(map(str.lower,d3))
    d3=list(map(int,d3))






    label=d2
    data=d3
    
    title=(d1)

    data=data
    label=label


    plt.style.use('ggplot')
    plt.rcParams.update({'font.size':25})

    size=(20,17)
    col=cm.Spectral(np.arange(len(data))/float(len(data)))

    plt.figure(figsize=size,dpi=100)
    plt.pie(data,colors=col,counterclock=False,startangle=90,autopct=lambda p:'{:.1f}%'.format(p) if p>=5 else'')
    plt.subplots_adjust(left=0,right=0.7)
    plt.legend(label,fancybox=True,loc='center left',bbox_to_anchor=(0.9,0.5))
    #plt.savefig('figre.png',bbox_inches='tight',pad_inches=0.05)



    
    plt.title(title,fontsize=50)
    


def plt2svg_e():
    buf=io.BytesIO()
    plt.savefig(buf,format='png',dpi=200)
    s=buf.getvalue()
    buf.close()
    return s


@login_required
def get_svg_e(request):
    setplt_e()
    svg=plt2svg_e()
    plt.cla()
    response=HttpResponse(svg,content_type='image/png')
    return response
