import os
import sys
import re
import math
import json

def create_dic(list_pictures,query_txt): #takes in a list of file names
    #print list_pictures
    all_dict=[]
    dict_idf={}
    words=[]
    num_pic=1000
    iterator=0
   
    for x in range(0, 1000): #goes through each file and takes all the words
        words.append([])
        c = list_pictures[x]
        caption=c["caption"]
        if caption!=None:
            caption = caption.lower()
            words[iterator]=(re.split('[^a-zA-z]*',caption))
        iterator+=1

    for i in range(num_pic): #creates a dictionary and key= word, value=word count
        dict={}
        for x in range(len(words[i])): #creates a dictionary for words that are greater than or equal to 3
            if len(words[i][x])>=3:
                if words[i][x] in dict:
                    dict[words[i][x]]+=1
                else:
                    dict[words[i][x]]=1
                if words[i][x] not in dict_idf:
                    dict_idf[words[i][x]]=0
        all_dict.append(dict)
    all_words=dict_idf.keys()
    dict_idf.clear()
    
    for word in all_words: #finds how many documents each word is in
        numt=0.0
        for i in range(num_pic):
            if word in all_dict[i]:
                numt+=1
        dict_idf[word]=numt
    new_dict_idf={}
    
    for key in dict_idf: #calculate idf
        value=(float(num_pic)/float(dict_idf[key]))
        new_dict_idf[key]=math.log(value,10)
    dict_tfidf=[]
    
    for i in range(len(all_dict)): #calculate tf-idf
        new_dict={}
        for key in all_dict[i]:
            new_dict[key]=1+(math.log(all_dict[i][key],10)*new_dict_idf[key])
        dict_tfidf.append(new_dict)
    length_docs=[]
    query=query_txt
    
    query1=(re.split(r'[^a-zA-z]*\s*',query))
    new_query1=[]
    query_vector={}
    
    for query_word in query1:
        print query_word
        if len(query_word)>=3:
            new_query1.append(query_word)
            query_vector[query_word]=new_dict_idf[query_word]
   
    sum_query=0.0
    for key in query_vector:
        sum_query+= math.pow(query_vector[key],2)
    query_mag=math.sqrt(sum_query)
    
    for i in range(num_pic): #finds magnitude for each document
        sum=0.0
        for key in dict_tfidf[i]:
            sum+= math.pow(dict_tfidf[i][key],2)
        value=math.sqrt(sum)
        length_docs.append(value)
        
    cos_docs={}
    
    for i in range(num_pic): #finds the cosine for each document
        dot_product=0.0
        for word in new_query1:
            if word in dict_tfidf[i]:
                dot_product+=dict_tfidf[i][word]*query_vector[word]
        string=list_pictures[i]["photo_id"]
        if length_docs[i]==0:
            length_docs[i]=1000000000000
        cos_docs[string]=(float(dot_product)/(query_mag*length_docs[i]))
        
    cos_docs_tuples= cos_docs.items()
    sorted_cos_docs=sorted(cos_docs_tuples,key=lambda tuple: tuple[1],reverse=True) #sorts the cosine in revers order
    print "TOP 5 results for query : ", query
    for i in range (5):
        if i<len(sorted_cos_docs):
            print i+1,'.', sorted_cos_docs[i][0], " cos=",sorted_cos_docs[i][1]
    # return dict
    #usage 
def main():

    data = []
    with open('photo_id_to_restuarant_NV.json') as f:
        data = json.load(f)
    create_dic(data,"thai tea")
    
if __name__ == '__main__':
  main()