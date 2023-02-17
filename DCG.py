import math

def dcg_calculator(values):      
    index=1
    DCG=values[0]
    print("{:<5} {:<5} {:<}".format("Score","Gain","DCG"))
    for value in values:
        if index == 1:
            print("{:<5} {:<5} {:<}".format(value,value,DCG))   
        else:
            gain_value=round(value/(math.log2(index)),2)
            DCG+=gain_value
            print("{:<5} {:<5} {:<}".format(value,gain_value,round(DCG,2)))
            
        index += 1

if __name__ == "__main__":
        
    with open("valori.txt","r") as f:
        num_of_entrys = 10
        values = []
        for line in f.readlines():
            
            values_str = line.split(" ")
            values = [int(v) for v in values_str]
            print("----------------------------\n\n")
            dcg_calculator(values)


