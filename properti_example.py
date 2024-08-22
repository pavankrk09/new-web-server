class person:
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,user_name):
        if type(user_name)==str and len(user_name) >=3 and len(user_name) <=10 :
           print(f"Name is {user_name}")
        else:
            print("check the charactors in the name")
        

def main():
    person1=person()
    person1.name=""


if __name__ == '__main__':
    main()
        
