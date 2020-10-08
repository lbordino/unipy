scholars = [1, 2, 3, 4, 5, 6, 7, 8000, 8]


def max_age(list_school):
    age_max = list_school[0]
    for i in list_school:
        if age_max < i:
            age_max = i
    return age_max


print(max_age(scholars))

# fatto come dovrebbe essere fatto
print(max(scholars))
