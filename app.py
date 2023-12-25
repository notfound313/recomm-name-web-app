from flask import Flask, request, render_template
import pandas as pd
import re
import random
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)

df = pd.read_csv("df_nodc.csv")


@app.route('/')
def index():
    return render_template('index.html', active=0)

@app.route('/predict', methods=['POST'])
def predict():
    
    no, desc = [x for x in request.form.values()]
    desc = desc.lower()

    user_response = pd.DataFrame({ 'nama':['-'],
                                'arti':['-'],
                                'arti_clean':desc})



    dataName = []
    names = []
    arti =[]
    df_fc = pd.concat([user_response, df]).reset_index()
    df_fcp = df_fc.drop("index", axis=1)
    TfidfVec= TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0,)
    tfidf= TfidfVec.fit_transform(df_fcp['arti_clean'])
    con_simls = cosine_similarity(tfidf,tfidf)

    score = pd.Series(con_simls[0]).sort_values(ascending = False)
    top_ = list(score.iloc[1:7].index)
    for i in top_:
        names.append(df_fcp.iloc[i][0])
        arti.append( df_fcp.iloc[i][2])
    #return data
    for x in range(len(names)):
        nm = random.choice(df)
        nm2 = random.choice(df)
        nm3 = random.choice(df)
        if nm != nm2 != nm3:
            dataName.append(nm+" "+nm2+" "+nm3)
    
    
    output = 1

    return render_template('app_recom.html', active=output, lenNama=len(dataName), dataName=dataName, lenTable=len(arti), arti=arti, names=names)


if __name__ == '__main__':
    app.run(debug=True)