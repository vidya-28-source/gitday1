def timeFunc():
 global time,score,missed,count
 if(count<=10): # If count is less than 10, update the time
  time +=1
  timer.configure(text=time)
  timer.after(1000,timeFunc)
 else: #If count is equal to 10 then show the results, initialize the variables and destroy the other widgets
  #Label to show result after the game ends
  result= Label(wn,text='',font=('arial',25,'italic bold'),fg='grey')
  result.place(x=230,y=250)
  result.configure(text='Time taken = {} \n Score = {} \n Missed = {}'
                     .format(time,score,count-score-1))
  missed=0
  score=0
  time=0
  count=0
  nextWord.destroy()
  userInput.destroy()
  scorelabel.destroy()
  scoreboard.destroy()
  timerlabel.destroy()
  timer.destroy()