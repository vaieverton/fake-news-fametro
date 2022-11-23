import cv2
import random

names = []
verbs = []

def read_names_and_verbs():
    with open('./names.txt') as f:
        names = f.readlines()

    with open('./verbs.txt') as f:
        verbs = f.readlines()

    word1 = names[random.randrange(0,13)].replace('\n', '')
    word2 = verbs[random.randrange(0,12)].replace('\n', '')
    word3 = names[random.randrange(0,13)].replace('\n', '')

    text = word1 + ' ' + word2 + ' ' + word3
    return text

im = cv2.imread('template.jpg', 1)

font = cv2.FONT_HERSHEY_SIMPLEX


while(1):
    cv2.imshow('fake',im)

    k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    else:
        print (k) # else print its value
        cv2.rectangle(im ,(5,280),(480,308),(255,255,255), -1)
        cv2.putText(im, read_names_and_verbs(), (10, 302), font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)


cv2.waitKey(0)
cv2.destroyAllWindows()