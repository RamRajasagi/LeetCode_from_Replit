word=["gin","zen","gig","msg"]
morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
trans=set()
li=[]
for w in word:
  for l in w:
    ind=ord(l)-97
    li.append(morse[ind])
  trans.add(tuple(li))
  li=[]
print(trans)
print(len(trans))
  