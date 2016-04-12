import os
import sys
import re
import math
import json
import FP_user

def create_dic(list_pictures,query_txt): #takes in a list of file names
    #print list_pictures
    all_dict=[]
    dict_idf={}
    words=[]
    num_pic=1000 #only searches through first 1000
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
    return cos_docs

    # return dict
    #usage


def pic_food_algorithm(user, query):
    user.print_food_ratings()
    with open('photo_id_to_restuarant_NV.json') as f:
        data = json.load(f)
    all_cos = []
    food_ratings = user.user_food_ratings()
    print food_ratings
    for food in food_ratings:
        all_cos.append(create_dic(data, food))
    orig_cos = create_dic(data, query)
    total_cos = {}
    for i in range(1000):
        total_cos[data[i]["photo_id"]] = orig_cos[data[i]["photo_id"]]/len(food_ratings)
        for cos in all_cos:
            total_cos[data[i]["photo_id"]] += cos[data[i]["photo_id"]]

    cos_docs_tuples = total_cos.items()
    sorted_cos_docs = sorted(cos_docs_tuples, key=lambda tuple: tuple[1],
                             reverse=True)  # sorts the cosine in revers order
    print "TOP 5 results for query : ", query
    for i in range(5):
        if i < len(sorted_cos_docs):
            print i + 1, '.', sorted_cos_docs[i][0], " cos=", sorted_cos_docs[i][1]
    thousand_photos = open('test_photos.txt', 'w')
    for i in range(1000):
        thousand_photos.write(data[i]["photo_id"]+"\n")
    thousand_photos.close()


def pf_user():
    # print "Enter Username or 0 for new user: "
    username = raw_input("username:")
    password = raw_input("password:")
    user = FP_user.PFUser(username, password)
    return user


def user_rating(user):
    food_ratings = {}
    print "Please enter a type of food you like: "
    answer = raw_input()
    print "Please enter a rating for " + answer + " from 1 to 10: "
    rating = int(input())
    food_ratings[answer] = rating
    for food in food_ratings:
        user.add_ratings(food, food_ratings[food])


def main():
    user = pf_user()
    user_rating(user)
    user.print_food_ratings()
    pic_food_algorithm(user, "pizza")


if __name__ == '__main__':
    main()