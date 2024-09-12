from datetime import datetime


class Person:
  birth = ''

  def birthday(self):
    date_birth = datetime.strptime(self.birth, '%d/%m/%Y')
    date_current = datetime.now()
    if (date_birth.strftime("%d")
        == date_current.strftime("%d")) and (date_birth.strftime("%m")
                                             == date_current.strftime("%m")):
      print("Yes")
    else:
      print("No")
