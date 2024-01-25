import csv

mn = set()
spk = [0]*5
sps = [0]*5
with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)

    for id, name, title, clas, score in answer:
        if "Хадаров Владимир" in name:
            print("Ты получил:", score, ", за проект -", title)
        if score != 'None' and clas == "8х":
            mn.add("8х")
            spk[0] += 1
            sps[0] += int(score)
        if score != 'None' and clas == "9т":
            mn.add("9т")
            spk[1] += 1
            sps[1] += int(score)
        if score != 'None' and clas == "11в":
            mn.add("11в")
            spk[2] += 1
            sps[2] += int(score)
        if score != 'None' and clas == "9г":
            mn.add("9г")
            spk[3] += 1
            sps[3] += int(score)
        if score != 'None' and clas == "11и":
            mn.add("11и")
            spk[4] += 1
            sps[4] += int(score)
for i in range(0, 5):
    print("оценка:", (sps[i] / spk[i]))

with open("student_new.csv", "w", newLine="") as file2:
    writer = csv.writer(file2)
    for id, name, title, clas, score in answer:
        if score == 'None':
            i = sp.index(clas)
            score = str(sps[i] / spk[i])
        writer.writerow([id, name, title, clas, score])








    

