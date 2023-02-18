import math,json

#Scoring tra 0 e 5
"dcg = score/log2(pos)"
"idcg = 5/log2(pos)"
"ndcg = dcg/idcg"

def dcg_calculator(values):      
    index=1
    dcg=values[0]
    print("{:<5} {:<5} {:<5} {:<5} {:<5}".format("Score","Gain","DCG","IDCG","NDCG"))
    for value in values:
        if index == 1:
            idcg = 5
            ndcg = float(dcg/idcg)
            print("{:<5} {:<5} {:<5} {:<5} {:<5}".format(value,value,dcg,idcg,ndcg))   
        else:
            gain_value=round(value/(math.log2(index)),2)
            dcg+=gain_value
            idcg += 5/(math.log2(index))
            ndcg = dcg/idcg
            print("{:<5} {:<5} {:<5} {:<5} {:<5}".format(value,gain_value,round(dcg,2),round(idcg,2),round(ndcg,2)))
            
        index += 1

if __name__ == "__main__":
    
    
    with open("static_data/benchmark_query.json","r") as f:
        with open("static_data/queries.txt","w") as queries:
            data = json.load(f)
            for index,item in enumerate(data):
                print("----------------------------\n\n")
                print(f"QUERY {index+1}\n")
                print(item["query"]+"\n")
                queries.write(f"QUERY {index+1}: {item['query']}\n")
                dcg_calculator(item["relevances"])


