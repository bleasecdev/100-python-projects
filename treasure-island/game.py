print('''
                        8o88o          __
                      o88o           o688o)
'-,    .``'.          _o8o    .-.'-.(6886898o
   \,'`   . \.  .----| |-.  ,'     o688868698o)
  .'  /   :   '/          \'  \  (68968886)6/88o
 /   '    '   /____________\   '.  866\88|889)
/    .    \   | ___   __   | .'  `   (969/9\
`           _ ||_|_| /  \  |______     \//  \
'.`"'.`,`'./_\||_|_| | .|  |______\.`.`||,`,'
`'^,_`'. ,"|O||______|  |__|======|,.',|| ,..
.'`. "\'^,`.,'.`'``.'/==\.,.'`,.' `,' .||.,.`
`',`' `,'.^ '. ,.'`,/====\,' `,. ^, `.-',, `,
.,`^  `. `,`  ,  ,`/======\,  ,'  `'.,"  
''')

print("Can you sell a house?")
conference_room = input("Your client has arrived at your office, do you want to meet in conference room A or B?\n")
if conference_room == 'A':
    print("That conference room smells bad and it turned your client off. They have decided to work with another agent GAME OVER")
print("Excellent, you have successfully went over the next steps it's time to show homes.")
street = input("Do you want to show the house on Park Ave or Biddle St?\n")
if street == "Biddle St":
    print("You took your client to the hood, while you were showing the house their car was stolen.  You were fired Game Over.")
else:
    print("You took your client to the home of their dreams they signed a contract immediately. Congratulations you win!")
