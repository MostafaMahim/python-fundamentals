scores = [85, 92, 78, 90, 65, 88]
scores.append(95)

lowest_score = min(scores)
scores.remove(lowest_score)
print(scores)


sorted_scores = sorted(scores,reverse=True)
print(sorted_scores)


total = 0 

for num in scores:
    total = num+total

average = total/len(scores)
print(f"Average: {average:.2f}")