scores = []
print('Enter the scores for the test. Use -1 if you want to finish')

score = float(input('score: '))  # priming read
while score != -1:
    scores.append(score)
    score = float(input('score: '))  # modifying read

scores.sort()
print('The scores (ordered): ', scores)
print('The average of these', len(scores), 'scores =', sum(scores)/len(scores))  #use the build-in functions of lists
