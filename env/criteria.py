class Search_Criteria:

    def __init__(self, subject, keywords):
        self.__subject = subject # "genomics"
        self.__keywords = keywords # ["DNA", "genetics", "treatment"]
    
    def add_keyworld(self, new_keyword):
        self.__keywords.append(new_keyword)

    def remove_keyworkd(self, old_keyword):
        self.__keywords.pop(self.__keywords.index(old_keyword))

    @property
    def subject(self):
        return self.__subject
    
    @subject.setter
    def subject(self, new_subject):
        self.__subject = new_subject

    @property
    def keywords(self):
        return self.__keywords