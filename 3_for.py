from random import randint
from warnings import filterwarnings
"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    
    def filler(number, letter):      
        class_score ={}
        scores = []
        class_score["school_class"] = f"{number}{letter}"        
        for i in range(5):
            scores.append(randint(1,5))
        class_score["scores"] = scores
        return(class_score)           
        
    all_class_score = []
    for number in range (1,12):
        all_class_score.append(filler (number,'a'))   
    for number in range (1,12):
        all_class_score.append(filler (number,'b'))    
    for number in range (1,12):
        all_class_score.append(filler (number,'c'))

    full_average_score = 0 
    for a in range(len(all_class_score)):    
        average_score = sum(all_class_score[a]["scores"])/len(all_class_score[a]["scores"])
        full_average_score += average_score        
        print(f'Средняя оценка класса {all_class_score[a]["school_class"]}: {average_score}')        
    print(f'Cредняя оценка по всей школе: {full_average_score/len(all_class_score)}')    

    
if __name__ == "__main__":
    main()