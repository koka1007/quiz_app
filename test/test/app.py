from flask import Flask,request,render_template, jsonify,g
import numpy as np
import random
import time
import check_table


app = Flask(__name__)
 
# list1 = np.arange(125).reshape(25,5)
list1 = check_table.check()


# kotae = []
# list1=[]
# for i in range(0,10):
#     sublist=[]
#     for j in range(0,5):
#         sublist.append(j+i)
#         if(j == 4):
#             kotae.append(j)
#     list1.append(sublist)
# answer =list(range(10))
answer=[]
kotae=[]


# for a in range(0,11):
#     answer.append(0)

lastans=False
gronum = 0
user_name = ""


@app.template_filter('judge')
def judge_filter(total,idx=0): # idxの位置だけ大文字にして、それ以外はそのまま返す
    if((total/idx)*100 > 60 ):
        return "合格です"
    else:
        return "不合格です"
    
@app.route('/')
def top():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def main2():
    global user_name
    global gronum
    global kotae
    global answer

    answer = []
    random.seed(0)
    random.shuffle(list1)
    for i in list1:
        kotae.append(i[2])
    name = request.form.get('name')
    user_name = name 
    
    list2=list1[gronum]
    length=len(list2)
    mondai="問題"
    sentaku="選択"
    return render_template("main.html",mondai=mondai,sentaku=sentaku,list1=list2,flag=lastans,len=length,num=gronum)

@app.route('/main', methods=['POST'])
def main1():
    global gronum
    global lastans

    chk = request.form.getlist('chk',type=int)
    print(chk)
    ans = request.form.get('anse',type=int)
    if(ans is None):
        ans = np.sum(chk)
    print(ans)
    # answer[gronum]=ans

    answer.append(ans)
    gronum += 1
    if(gronum == (len(list1)-1)):
        lastans = True
    list2=list1[gronum]
    length=len(list2)
    mondai="問題"
    sentaku="選択"
    return render_template("main.html",mondai=mondai,sentaku=sentaku,list1=list2,flag=lastans,len=length,num=gronum)

@app.route('/timeup')
def timeup():
    global answer 
    global list1
    global lastans
    global gronum

    remain = len(list1)-gronum
    print(remain)
    for a in range(remain):
        answer.append(0)
    lastans = False
    gronum = 0
    point = [x - y for (x,y) in zip(answer,kotae) ]

    total = point.count(0)
    
    return render_template("result.html",mondai=user_name,answer=answer,list1=list1 ,point=point,total=total)




@app.route('/result',methods=['POST'])
def result():

    global lastans
    global answer
    global kotae
    global gronum

    ans = request.form.get('anse',type=int)
    if(ans is None):
        ans = -1 
    answer.append(ans)
    leng = len(answer)
    lastans = False
    gronum = 0
    point = [x - y for (x,y) in zip(answer,kotae) ]

    total = point.count(0)




    return render_template("result.html",mondai=user_name,answer=answer,list1=list1 ,point=point,total=total,leng=leng)








if __name__ == "__main__":
    app.run(port=8000, debug=True)