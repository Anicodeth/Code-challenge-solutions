def gradingStudents(grades):
    newgrade=[]
    for i in range(0,len(grades)):
        if grades[i]<38:
            newgrade.append(grades[i])
        elif grades[i]%5==3:
            newgrade.append(grades[i]+2)
        elif  grades[i]%5==4:
            newgrade.append(grades[i]+1)
        else:
            newgrade.append(grades[i])
    return newgrade
